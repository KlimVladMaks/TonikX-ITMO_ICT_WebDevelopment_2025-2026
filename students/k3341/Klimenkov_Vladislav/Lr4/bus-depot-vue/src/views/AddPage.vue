<script>
import Header from '@/components/Header.vue';
import { fields, foreignKeys2, namingFunctions, choices } from '@/assets/types.js';

export default {
    name: "AddPage",
    props: {
        type: {
            type: String,
            required: true
        }
    },
    components: {
        Header
    },
    data() {
        return {
            formData: {},
            foreignKeyOptions: {},
        }
    },
    computed: {
        fieldsForType() {
            return fields[this.type] || [];
        },
        apiBaseUrl() {
            return 'http://127.0.0.1:8000/bus-depot';
        },
        foreignKeysForType() {
            return foreignKeys2[this.type] || {};
        },
    },
    methods: {
        isForeignKey(field) {
            return field in this.foreignKeysForType;
        },
        isChoiceField(field) {
            return field in choices;
        },
        getOptionsForField(field) {
            return this.foreignKeyOptions[field] || [];
        },
        getChoicesForField(field) {
            return choices[field] || [];
        },
        async loadForeignKeyOptions() {
            const promises = Object.entries(this.foreignKeysForType).map(async ([field, targetType]) => {
                const token = localStorage.getItem('auth_token');
                const response = await fetch(`${this.apiBaseUrl}/${targetType.replaceAll('_', '-')}/`, {
                    headers: {
                        'Authorization': `Token ${token}`
                    }
                });
                const items = await response.json();
                const optionPromises = items.map(async (item) => {
                    const namingFunc = namingFunctions[targetType.replaceAll('_', '-')];
                    let name = '';
                    name = await namingFunc(item);
                    return {
                        id: item.id,
                        name: name
                    };
                });
                const options = await Promise.all(optionPromises);
                this.foreignKeyOptions[field] = options;
            });
            await Promise.all(promises);
        },
        async handleSubmit() {
            const token = localStorage.getItem('auth_token');
            const requestData = { ...this.formData };
            Object.keys(this.foreignKeysForType).forEach(field => {
                const options = this.getOptionsForField(field);
                const selectedOption = options.find(opt => opt.name === requestData[field]);
                if (selectedOption) {
                    requestData[field] = selectedOption.id;
                }
            });
            const response = await fetch(`${this.apiBaseUrl}/${this.type}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`
                },
                body: JSON.stringify(requestData)
            });
            if (!response.ok) {
                throw new Error(`Ошибка сервера: ${response.status}`);
            }
            this.$router.push(`/list/${this.type}`);
        },
    },
    watch: {
        type: {
            immediate: true,
            handler() {
                this.foreignKeyOptions = {};
                this.formData = {};
                this.loadForeignKeyOptions();
            }
        }
    }
}
</script>


<template>
    <div>
        <Header></Header>
        <a href="javascript:history.back()">← Отмена</a>
        <h1>Добавление {{ type }}</h1>

        <form @submit.prevent="handleSubmit">
            <div v-for="field in fieldsForType" :key="field">
                <p>{{ field }}:</p>

                <select 
                    v-if="isForeignKey(field)"
                    v-model="formData[field]"
                >
                    <option
                        v-for="option in getOptionsForField(field)"
                        :key="option.id"
                        :value="option.name"
                    >
                        {{ option.name }}
                    </option>
                </select>

                <select
                    v-else-if="isChoiceField(field)"
                    v-model="formData[field]"
                >
                    <option
                        v-for="choice in getChoicesForField(field)"
                        :key="choice"
                        :value="choice"
                    >
                        {{ choice }}
                    </option>
                </select>

                <input
                    v-else
                    type="text"
                    v-model="formData[field]"
                >
            </div>
            <button type="submit">
                Создать
            </button>
        </form>
    </div>
</template>

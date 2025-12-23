<script>
import Header from '@/components/Header.vue';
import { fields } from '@/assets/types.js';

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
        }
    },
    computed: {
        fieldsForType() {
            return fields[this.type] || [];
        },
        apiBaseUrl() {
            return 'http://127.0.0.1:8000/bus-depot';
        },
    },
    methods: {
        async handleSubmit() {
            try {
                const token = localStorage.getItem('auth_token');

                const requestData = { ...this.formData };

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
            } catch {
                alert("Ошибка сервера")
            }
        }
    },
}
</script>

<template>
    <div>
        <Header></Header>

        <a href="javascript:history.back()">← Отмена</a>
        <h1>Добавление {{ type }}</h1>

        <form @submit.prevent="handleSubmit">
            <div v-for="field in fieldsForType" :key="field">
                <p>{{ field }}</p>
                <input
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

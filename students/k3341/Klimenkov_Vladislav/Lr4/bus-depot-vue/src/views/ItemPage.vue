<script>
import Header from '@/components/Header.vue';
import { namingFunctions, foreignKeys, getObjectName, titles } from '@/assets/types';

export default {
    name: "ItemPage",
    props: {
        type: {
            type: String,
            required: true
        },
        id: {
            type: String,
            required: true
        }
    },
    watch: {
        type: {
            handler: 'fetchItem',
            immediate: true
        },
        id: {
            handler: 'fetchItem',
            immediate: true
        }
    },
    components: {
        Header
    },
    computed: {
        apiUrl() {
            const baseUrl = 'http://127.0.0.1:8000/bus-depot';
            return `${baseUrl}/${this.type}/${this.id}`;
        },
        typeListBack() {
            return titles[this.type] || this.type;
        },
        deleteUrl() {
            const baseUrl = 'http://127.0.0.1:8000/bus-depot';
            return (id) => `${baseUrl}/${this.type}/${id}/`;
        },
    },
    data() {
        return {
            itemData: {},
            loading: false,
            error: null,
            title: "",
            foreignKeyNames: {},
            foreignKeyTypes: {},
        }
    },
    methods: {
        async fetchItem() {
            this.loading = true;
            this.error = null;
            this.foreignKeyNames = {};
            this.foreignKeyTypes = {};
            this.itemData = {};

            const token = localStorage.getItem('auth_token');

            if (!token) {
                this.error = 'Ошибка авторизации. Токен не найден.';
                this.loading = false;
                return;
            }

            try {
                const response = await fetch(this.apiUrl, {
                    method: 'GET',
                    headers: {
                        'Authorization': `Token ${token}`,
                        'Content-Type': 'application/json'
                    }
                });

                if (!response.ok) {
                    throw new Error(`Ошибка HTTP: ${response.status}`);
                }

                this.itemData = await response.json();
                this.title = await namingFunctions[this.type](this.itemData);

                await this.loadForeignKeyNames();
            } catch (err) {
                this.error = `Не удалось загрузить данные: ${err.message}`;
                console.error('Ошибка загрузки:', err);
            } finally {
                this.loading = false;
            }
        },
        async loadForeignKeyNames() {
            const fkList = foreignKeys[this.type] || [];

            for (const [fieldName, targetType] of fkList) {
                this.foreignKeyTypes[fieldName] = targetType
                const idValue = this.itemData[fieldName];

                try {
                    const name = await getObjectName(targetType.replaceAll('_', '-'), idValue);
                    this.foreignKeyNames[fieldName] = name;
                } catch {
                    this.foreignKeyNames[fieldName] = idValue;
                }
            }
        },
        async deleteItem(id, name) {
            if (!confirm(`Вы уверены, что хотите удалить '${name}'`)) {
                return;
            }
            const token = localStorage.getItem('auth_token');
            const response = await fetch(this.deleteUrl(id), {
                method: 'DELETE',
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json'
                }
            });
            if (response.ok) {
                this.$router.push(`/list/${this.type}`);
            } else {
                alert("При удалении элемента возникла ошибка");
            }
        },
        isForeignKey(key) {
            const fkList = foreignKeys[this.type] || [];
            return fkList.some(([fieldName]) => fieldName === key);
        },
        navigateToItem(type, id) {
            this.$router.push(`/list/${type}/${id}`);
        },
        navigateToList() {
            this.$router.push(`/list/${this.type}`);
        },
    },
}
</script>

<template>
<div>
    <Header></Header>
    <a href="javascript:history.back()">← Назад</a>
    <a 
        href="javascript:void(0)"
        @click="navigateToList()"
    >
        {{ typeListBack }}
    </a>
    <div v-if="loading">Загрузка...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
        <h1>{{ title }}</h1>
        <div v-for="(value, key) in itemData" :key="key">
            <p>
                <b>{{ key }}:</b>
                <div v-if="isForeignKey(key)">
                    <a 
                        href="javascript:void(0)"
                        @click="navigateToItem(foreignKeyTypes[key].replaceAll('_', '-'), value)"
                    >
                        {{ foreignKeyNames[key] }}
                    </a>
                </div>
                <div v-else>
                    {{ value }}
                </div>
            </p>
        </div>
        <router-link :to="{ name: 'EditPage', params: { type: type, id: id } }">
            Изменить
        </router-link>
        <button @click="deleteItem(id, title)">
            Удалить
        </button>
    </div>
</div>
</template>

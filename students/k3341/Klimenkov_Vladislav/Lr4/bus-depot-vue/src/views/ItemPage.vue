<script>
import Header from '@/components/Header.vue';
import { namingFunctions, clearCache } from '@/assets/types';

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
    components: {
        Header
    },
    computed: {
        apiUrl() {
            const baseUrl = 'http://127.0.0.1:8000/bus-depot';
            return `${baseUrl}/${this.type}/${this.id}`;
        }
    },
    data() {
        return {
            itemData: {},
            loading: false,
            error: null,
            title: "",
        }
    },
    methods: {
        async fetchItem() {
            this.loading = true;
            this.error = null;

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
            } catch (err) {
                this.error = `Не удалось загрузить данные: ${err.message}`;
                console.error('Ошибка загрузки:', err);
            } finally {
                this.loading = false;
            }
        },
    },
    mounted() {
        this.fetchItem();
        clearCache();
    },
}
</script>

<template>
<div>
    <Header></Header>
    <a href="javascript:history.back()">← Назад</a>
    <div v-if="loading">Загрузка...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
        <h1>{{ title }}</h1>
        <div v-for="(value, key) in itemData" :key="key">
            <p><b>{{ key }}:</b> {{ value }}</p>
        </div>
        <button>Изменить</button>
        <button>Удалить</button>
    </div>
</div>
</template>

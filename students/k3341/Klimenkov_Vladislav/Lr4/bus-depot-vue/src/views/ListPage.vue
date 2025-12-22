<script>
import Header from '@/components/Header.vue';
import { titles, namingFunctions } from '@/assets/types';

export default {
    name: 'ListPage',
    props: {
        type: {
            type: String,
            required: true
        }
    },
    components: {
        Header
    },
    computed: {
        pageTitle() {
            return titles[this.type] || this.type;
        },
        apiUrl() {
            const baseUrl = 'http://127.0.0.1:8000/bus-depot';
            return `${baseUrl}/${this.type}/`;
        }
    },
    data() {
        return {
            items: [],
            loading: false,
            error: null
        }
    },
    methods: {
        async fetchItems() {
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

                this.items = await response.json();

                for (const item of this.items) {
                    if (namingFunctions[this.type]) {
                        item.displayName = await namingFunctions[this.type](item);
                    } else {
                        item.displayName = `ID: ${item.id}`;
                    }
                }
            } catch (err) {
                this.error = `Не удалось загрузить данные: ${err.message}`;
                console.error('Ошибка загрузки:', err);
            } finally {
                this.loading = false;
            }
        },
    },
    mounted() {
        this.fetchItems();
    },
}
</script>


<template>
<div>
    <Header></Header>
    <a href="javascript:history.back()">← Назад</a>
    <h1>{{ pageTitle }}</h1>
    <div v-if="loading">Загрузка...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else-if="items.length === 0">
        Элементы не найдены
    </div>
    <div v-else>
        <a href="">+ Добавить</a>
        <div v-for="item in items" :key="item.id">
            <p>{{ item.displayName }}</p>
            <div>
                <router-link :to="{ name: 'ItemPage', params: { type: type, id: item.id } }">
                    Подробнее
                </router-link>
                <button>Изменить</button>
                <button>Удалить</button>
            </div>
        </div>
    </div>
</div>
</template>

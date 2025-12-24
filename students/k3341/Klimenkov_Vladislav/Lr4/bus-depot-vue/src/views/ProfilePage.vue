<script>
import Header from '@/components/Header.vue';

export default {
    components: {
        Header,
    },
    data() {
        return {
            username: localStorage.getItem("username")
        }
    }
}
</script>


<template>
    <Header ref="header"></Header>
    <h1>Профиль пользователя</h1>
    <p><b>Логин:</b></p>
    <p>{{ username }}</p>
    <p><b>Пароль:</b></p>
    <button>Изменить</button>
</template>

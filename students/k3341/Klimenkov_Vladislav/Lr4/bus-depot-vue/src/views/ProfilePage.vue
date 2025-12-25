<script>
import Header from '@/components/Header.vue';
import EditUsername from '@/components/EditUsername.vue';
import EditPassword from '@/components/EditPassword.vue';

export default {
    components: {
        Header,
        EditUsername,
        EditPassword,
    },
    data() {
        return {
            username: localStorage.getItem("username"),
            edit: null,
        }
    },
    methods: {
        handleUsernameUpdated(newUsername) {
            this.username = newUsername;
            this.edit = null;
            this.$refs.header.updateUsername();
        },
        handlePasswordUpdated() {
            this.edit = null;
            alert('Пароль успешно изменён');
        },
        handleCancelEdit() {
            this.edit = null;
        },
    },
}
</script>


<template>
    <Header ref="header"></Header>
    <h1>Профиль пользователя</h1>

    <EditUsername
        v-if="edit === 'username'"
        :current-username="username"
        @username-updated="handleUsernameUpdated"
        @cancel="handleCancelEdit"
    />

    <EditPassword 
        v-else-if="edit === 'password'"
        @cancel="handleCancelEdit"
        @success="handlePasswordUpdated"
    ></EditPassword>

    <div v-else>
        <p><b>Логин:</b></p>
        <p>{{ username }}</p>
        <button @click="edit = 'username'">Изменить</button>

        <p><b>Пароль:</b></p>
        <button @click="edit = 'password'">Изменить</button>
    </div>
</template>

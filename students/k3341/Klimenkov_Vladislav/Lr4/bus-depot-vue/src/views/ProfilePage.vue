<script>
import Header from '@/components/Header.vue';
import EditUsername from '@/components/EditUsername.vue';
import EditPassword from '@/components/EditPassword.vue';
import DeleteProfile from '@/components/DeleteProfile.vue';

export default {
    components: {
        Header,
        EditUsername,
        EditPassword,
        DeleteProfile,
    },
    data() {
        return {
            username: localStorage.getItem("username"),
            operation: null,
        }
    },
    methods: {
        handleUsernameUpdated(newUsername) {
            this.username = newUsername;
            this.operation = null;
            this.$refs.header.updateUsername();
        },
        handlePasswordUpdated() {
            this.operation = null;
            alert('Пароль успешно изменён');
        },
        handleCancelOperation() {
            this.operation = null;
        },
    },
}
</script>


<template>
    <Header ref="header"></Header>
    <h1>Профиль пользователя</h1>

    <EditUsername
        v-if="operation === 'edit_username'"
        :current-username="username"
        @username-updated="handleUsernameUpdated"
        @cancel="handleCancelOperation"
    />

    <EditPassword 
        v-else-if="operation === 'edit_password'"
        @cancel="handleCancelOperation"
        @success="handlePasswordUpdated"
    ></EditPassword>

    <DeleteProfile
        v-else-if="operation === 'delete_profile'"
        @cancel="handleCancelOperation"
    >
    </DeleteProfile>

    <div v-else>
        <p><b>Логин:</b></p>
        <p>{{ username }}</p>
        <button @click="operation = 'edit_username'">Изменить</button>

        <p><b>Пароль:</b></p>
        <button @click="operation = 'edit_password'">Изменить</button>

        <p><b>Профиль:</b></p>
        <button @click="operation = 'delete_profile'">Удалить профиль</button>
    </div>
</template>

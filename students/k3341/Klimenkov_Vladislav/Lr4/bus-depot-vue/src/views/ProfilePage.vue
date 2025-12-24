<script>
import Header from '@/components/Header.vue';
import EditUsername from '@/components/EditUsername.vue';

export default {
    components: {
        Header,
        EditUsername,
    },
    data() {
        return {
            username: localStorage.getItem("username"),
            showEditUsername: false,
        }
    },
    methods: {
        handleUsernameUpdated(newUsername) {
            this.username = newUsername;
            this.showEditUsername = false;
            this.$refs.header.updateUsername();
        },
        handleEditCancel() {
            this.showEditUsername = false;
        }
    },
}
</script>


<template>
    <Header ref="header"></Header>
    <h1>Профиль пользователя</h1>

    <EditUsername
        v-if="showEditUsername"
        :current-username="username"
        @username-updated="handleUsernameUpdated"
        @cancel="handleEditCancel"
    />

    <div v-else>
        <p><b>Логин:</b></p>
        <p>{{ username }}</p>
        <button @click="showEditUsername = true">Изменить</button>

        <p><b>Пароль:</b></p>
        <button>Изменить</button>
    </div>
</template>

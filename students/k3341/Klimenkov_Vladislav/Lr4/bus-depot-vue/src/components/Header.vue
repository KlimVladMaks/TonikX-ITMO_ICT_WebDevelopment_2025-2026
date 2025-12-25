<template>
    <div>
        <a href="\main">Главная</a>
        <a href="\profile">{{ username }}</a>
        <button @click="confirmLogout">
            Выйти
        </button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            username: localStorage.getItem("username"),
        }
    },
    methods: {
        confirmLogout() {
            if (confirm('Вы уверены, что хотите выйти?')) {
                this.handleLogout()
            }
        },

        async handleLogout() {
            try {
                const token = localStorage.getItem('auth_token')

                if (token) {
                    await axios.post('http://127.0.0.1:8000/auth/token/logout/', {}, {
                        headers: {
                            'Authorization': `Token ${token}`
                        }
                    })
                }

                this.clearAuthAndRedirect()
            } catch (error) {
                this.clearAuthAndRedirect()
            }
        },

        clearAuthAndRedirect() {
            localStorage.clear()
            this.$router.push('/auth')
        },

        updateUsername() {
            this.username = localStorage.getItem("username");
        }
    }
}
</script>

<template>
    <div>
        <button @click="confirmLogout">
            Выйти
        </button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
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
            localStorage.removeItem('auth_token')
            this.$router.push('/auth')
        }
    }
}
</script>

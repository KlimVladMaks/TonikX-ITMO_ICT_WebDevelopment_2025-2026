<script>
export default {
    data() {
        return {
            username: '',
            password: '',
            isLoading: false,
            errorMessage: ''
        }
    },

    methods: {
        async login() {
            this.errorMessage = ''
            this.isLoading = true

            try {
                const response = await fetch('http://127.0.0.1:8000/auth/token/login/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        username: this.username,
                        password: this.password
                    })
                })

                const data = await response.json()

                if (response.ok && data.auth_token) {
                    localStorage.setItem('auth_token', data.auth_token)
                    console.log('Токен сохранён:', data.auth_token)
                    this.$router.push('/main')
                } else {
                    this.errorMessage = "Неверный логин или пароль"
                }
            } catch (error) {
                this.errorMessage = 'Ошибка соединения с сервером'
            } finally {
                this.isLoading = false
            }
        }
    }
}
</script>


<template>
    <div>
        <a href="\auth">← Отмена</a>
        <h1>Вход</h1>
        <div v-if="errorMessage" class="error-message">
            {{ errorMessage }}
        </div>
        <p>Логин:</p>
        <input
            type="text"
            v-model="username"
            :disabled="isLoading"
        >
        <p>Пароль:</p>
        <input
            type="password"
            v-model="password"
            :disabled="isLoading"
        >
        <br>
        <button
            @click="login"
            :disabled="isLoading || !username || !password"
        >
            <span v-if="isLoading">Вход...</span>
            <span v-else>Войти</span>
        </button>
        <br>
        <a href="\signup">Зарегистрироваться</a>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            password: '',
            rePassword: '',
            isLoading: false
        }
    },
    methods: {
        async createAccount() {
            if (this.password !== this.rePassword) {
                alert('Пароли не совпадают');
                return;
            }

            const userData = {
                username: this.username,
                password: this.password,
                re_password: this.rePassword
            };

            this.isLoading = true;

            try {
                const response = await fetch('http://127.0.0.1:8000/auth/users/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(userData)
                });

                if (response.ok) {
                    alert('Аккаунт успешно создан. Теперь вы можете войти в него.');
                    this.$router.push('/login');
                } else {
                    console.log(await response.json());
                    alert("Ошибка при создании аккаунта");
                }
            } catch (error) {
                alert("Ошибка соединения с сервером");
            } finally {
                this.isLoading = false;
            }
        }
    }
}
</script>


<template>
    <div>
        <a href="\auth">← Отмена</a>

        <h1>Регистрация</h1>

        <p>Логин:</p>
        <input v-model="username" type="text">

        <p>Пароль:</p>
        <input v-model="password" type="password">

        <p>Повторить пароль:</p>
        <input v-model="rePassword" type="password">

        <br>
        <button
            @click="createAccount"
            :disabled="isLoading || !username || !password || !rePassword"
        >
            {{ isLoading ? 'Создание...' : 'Создать аккаунт' }}
        </button>
        <br>
        <a href="/login">Войти</a>
    </div>
</template>

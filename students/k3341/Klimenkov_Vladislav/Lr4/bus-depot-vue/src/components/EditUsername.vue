<script>
export default {
    props: {
        currentUsername: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            password: '',
            newUsername: this.currentUsername,
        }
    },
    methods: {
        handleCancel() {
            this.$emit('cancel');
        },
        async handleSave() {
            if (!this.password) {
                alert('Введите пароль');
                return;
            }
            
            if (!this.newUsername) {
                alert('Введите новый логин');
                return;
            }
            
            if (this.newUsername === this.currentUsername) {
                alert('Новый логин должен отличаться от текущего');
                return;
            }

            try {
                const token = localStorage.getItem('auth_token');
                console.log(JSON.stringify({
                        current_password: this.password,
                        new_username: this.newUsername
                    }));
                const response = await fetch('http://127.0.0.1:8000/auth/users/set_username/', {
                    method: 'POST',
                    headers: {
                        'Authorization': `Token ${token}`,
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        current_password: this.password,
                        new_username: this.newUsername
                    })
                });

                if (response.ok) {
                    localStorage.setItem('username', this.newUsername);
                    this.$emit('username-updated', this.newUsername);
                } else {
                    console.log(response)
                    alert('Ошибка при изменении логина');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Ошибка при подключении к серверу');
            }
        },
    },
}
</script>


<template>
<div>
    <a href="javascript:void(0)" @click="handleCancel">← Отмена</a>
    <h2>Изменить логин '{{ currentUsername }}'</h2>

    <p>Пароль:</p>
    <input
        type="password"
        v-model="password"
    >

    <p>Новый логин:</p>
    <input
        type="text"
        v-model="newUsername"
    >

    <br>
    <button @click="handleSave">
        Сохранить
    </button>
</div>
</template>

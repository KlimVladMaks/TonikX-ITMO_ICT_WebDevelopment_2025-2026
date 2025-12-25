<script>
export default {
    data() {
        return {
            username: localStorage.getItem("username"),
            password: '',
        }
    },
    methods: {
        handleCancel() {
            this.$emit('cancel');
        },

        async deleteProfile() {
            if (!confirm(`Вы уверены, что хотите удалить профиль '${this.username}'?`)) {
                return;
            }
            const token = localStorage.getItem('auth_token');
            const response = await fetch('http://127.0.0.1:8000/auth/users/me/', {
                method: 'DELETE',
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    current_password: this.password
                })
            });
            if (response.ok) {
                alert(`Профиль '${this.username}' был успешно удалён`)
                localStorage.clear();
                this.$router.push('/auth')
            } else {
                alert("Ошибка при удалении профиля")
            }
        }
    },
}
</script>


<template>
<div>
    <a href="javascript:void(0)" @click="handleCancel">← Отмена</a>
    <h2>Удаление профиля '{{ username }}'</h2>
    <p>Введите пароль:</p>
    <input type="password" v-model="password">
    <br>
    <button @click="deleteProfile">Удалить профиль</button>
</div>
</template>

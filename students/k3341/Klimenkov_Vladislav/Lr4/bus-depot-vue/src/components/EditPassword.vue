<script>
export default {
    data() {
        return {
            oldPassword: '',
            newPassword: '',
            reNewPassword: '',
        }
    },
    methods: {
        handleCancel() {
            this.$emit('cancel');
        },

        async handleSave() {
            if (!this.oldPassword || !this.newPassword || !this.reNewPassword) {
                alert('Все поля должны быть заполнены!');
                return;
            }

            if (this.newPassword !== this.reNewPassword) {
                alert('Новый пароль и его подтверждение не совпадают!');
                return;
            }

            const token = localStorage.getItem('auth_token');
            const url = `http://127.0.0.1:8000/auth/users/set_password/`;
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`
                },
                body: JSON.stringify({
                    new_password: this.newPassword,
                    current_password: this.oldPassword
                })
            });

            if (response.ok) {
                this.$emit('success');
            } else {
                console.log(response.json())
                alert("Ошибка при смене пароля");
            }
        },
    },
}
</script>


<template>
<div>
    <a href="javascript:void(0)" @click="handleCancel">← Отмена</a>
    <h2>Изменить пароль</h2>

    <p>Старый пароль:</p>
    <input
        type="password"
        v-model="oldPassword"
    >

    <p>Новый пароль:</p>
    <input
        type="password"
        v-model="newPassword"
    >

    <p>Повторить новый пароль:</p>
    <input
        type="password"
        v-model="reNewPassword"
    >

    <br>
    <button @click="handleSave">
        Сохранить
    </button>
</div>
</template>

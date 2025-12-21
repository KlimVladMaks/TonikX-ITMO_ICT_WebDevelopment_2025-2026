<script>
import Header from '@/components/Header.vue';

export default {
    name: "ItemPage",
    props: {
        type: {
            type: String,
            required: true
        },
        id: {
            type: Number,
            required: true
        }
    },
    components: {
        Header
    },
}
</script>

<template>
<div>
    <Header></Header>
    <a href="javascript:history.back()">← Назад</a>
    <p>{{ type }}, {{ id }}</p>
</div>
</template>

<script>
import Header from '@/components/Header.vue';

export default {
    name: "AddPage",
    props: {
        type: {
            type: String,
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
        <a href="javascript:history.back()">← Отмена</a>
    </div>
</template>

<script>
import Header from '@/components/Header.vue';

export default {
    name: 'ListPage',
    props: {
        type: {
            type: String,
            required: true
        }
    },
    components: {
        Header
    }
}
</script>


<template>
<div>
    <Header></Header>
    <a href="javascript:history.back()">← Назад</a>
    {{ type }}
</div>
</template>

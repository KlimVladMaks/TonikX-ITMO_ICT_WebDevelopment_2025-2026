<script>
    import Header from '@/components/Header.vue';

    export default {
        components: {
            Header
        }
    }
</script>

<template>
    <div>
        <Header></Header>
        <h1>Автобусный парк</h1>
        <ul>
            <li>
                <router-link :to="{ name: 'ListPage', params: { type: 'bus-types' } }">
                    Типы автобусов
                </router-link>
            </li>
            <li>
                <router-link :to="{ name: 'ListPage', params: { type: 'buses' } }">
                    Автобусы
                </router-link>
            </li>
            <li>
                <router-link :to="{ name: 'ListPage', params: { type: 'routes' } }">
                    Маршруты
                </router-link>
            </li>
            <li>
                <router-link :to="{ name: 'ListPage', params: { type: 'drivers' } }">
                    Водители
                </router-link>
            </li>
            <li>
                <router-link :to="{ name: 'ListPage', params: { type: 'driver-assignments' } }">
                    Назначения водителей
                </router-link>
            </li>
            <li>
                <router-link :to="{ name: 'ListPage', params: { type: 'bus-statuses' } }">
                    Статусы автобусов
                </router-link>
            </li>
        </ul>
    </div>
</template>

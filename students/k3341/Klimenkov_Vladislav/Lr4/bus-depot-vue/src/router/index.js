import {createRouter, createWebHistory} from "vue-router";

const routes = [
    {
        path: '/auth',
        component: () => import("@/views/AuthPage.vue")
    },
    {
        path: '/login',
        component: () => import("@/views/LoginPage.vue")
    },
    {
        path: '/signup',
        component: () => import("@/views/SignUpPage.vue"),
    },
    {
        path: '/main',
        component: () => import("@/views/MainPage.vue")
    },
    {
        path: '/',
        component: () => import('@/views/RootRedirect.vue')
    }
]

const router = createRouter({
   history: createWebHistory(), routes
})

export default router

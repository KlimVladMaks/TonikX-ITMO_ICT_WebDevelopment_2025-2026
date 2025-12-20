import {createRouter, createWebHistory} from "vue-router";
import AuthPage from "@/views/AuthPage.vue";
import LoginPage from "@/views/LoginPage.vue";


const routes = [
    {
        path: '/auth',
        component: AuthPage
    },
    {
        path: '/login',
        component: LoginPage
    }
]

const router = createRouter({
   history: createWebHistory(), routes
})

export default router

import {createRouter, createWebHistory} from "vue-router";
import AuthPage from "@/views/AuthPage.vue";
import LoginPage from "@/views/LoginPage.vue";
import MainPage from "@/views/MainPage.vue";
import SignUpPage from "@/views/SignUpPage.vue";


const routes = [
    {
        path: '/auth',
        component: AuthPage
    },
    {
        path: '/login',
        component: LoginPage
    },
    {
        path: '/signup',
        component: SignUpPage,
    },
    {
        path: '/main',
        component: MainPage
    }
]

const router = createRouter({
   history: createWebHistory(), routes
})

export default router

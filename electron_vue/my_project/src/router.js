// import Vue from 'vue';
// import { testWithSpectron } from 'vue-cli-plugin-electron-builder';
// import VueRouter from "vue-router";
import Home from "./components/view/Home";
import Header from "./components/layout/Header";
// Vue.use(VueRouter);

import { createWebHistory, createRouter } from 'vue-router'


const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/a',
        name: 'HelloWorld',
        component: Header

    }
]
const router = createRouter({
    history: createWebHistory(),
    routes
})


export default router;
import Vue from 'vue'
import Router from 'vue-router'
import {store} from '../store/store.js'
import Swal from 'sweetalert2'

// Containers
const DefaultContainer = () => import('@/containers/admin/DefaultContainer');
const Navbar = () => import('@/containers/blog/Navbar');

// Views
const Login = () => import('@/views/Login');

const Dashboard = () => import('@/views/admin/Dashboard');
const CreatePost = () => import('@/views/admin/CreatePost');
const PostList = () => import('@/views/admin/PostList');

const Index = () => import('@/views/blog/Index');
const Post = () => import('@/views/blog/Post');

const PageNotFound = () => import('@/views/Page404');


Vue.use(Router);

const router = new Router({
  mode: 'hash', // https://router.vuejs.org/api/#mode
  linkActiveClass: 'open active',
  scrollBehavior: () => ({y: 0}),
  routes: [
    {
      path: '/admin/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/',
      redirect: '/',
      name: 'Navbar',
      component: Navbar,
      children: [
        {
          path: '/',
          name: 'Index',
          component: Index
        },
        {
          path: '/:slug',
          name: 'post',
          component: Post
        },
      ]
    },
    {
      path: '/admin',
      redirect: '/admin/dashboard',
      name: 'Home',
      component: DefaultContainer,
      // Used for forbid access to the app qhen the user is not authenticated
      beforeEnter: (to, from, next) => {
        if (store.state.auth_status !== "success" && (to.name !== 'Login')) {
          next({name: 'Login'});
          Swal.fire(
            'Prohibido!',
            'Inicia sesión para ingresar a esta página',
            'error'
          )
        } else next()
      },
      children: [
        {
          path: 'dashboard',
          name: 'Dashboard',
          component: Dashboard
        },
        {
          path: 'post',
          name: 'Create',
          component: CreatePost
        },
        {
          path: 'post/:slug',
          name: 'editar-post',
          component: CreatePost
        },
        {
          path: 'listar',
          name: 'lista-post',
          component: PostList
        }
      ]
    },
    { path: "*", component: PageNotFound }
  ]
});

export default router


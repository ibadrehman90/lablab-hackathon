import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import DashboardPage from '../views/DashboardPage.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '',
    name: 'dashboard',
    component: DashboardPage,
    meta:{auth:true}
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginPage.vue'),
    meta:{hideTopbar: true,hideNavbar: true}
  },
  {
    path: '/register',
    name: 'signup',
    component: () => import('../views/SignupPage.vue'),
    meta:{hideTopbar: true,hideNavbar: true}
  },
  {
    path: '/profile',
    name: 'settings',
    component: () => import('../views/SettingsPage.vue'),
    meta:{auth:true,hideNavbar: false}
  },
  {
    path: '/templates',
    name: 'templates',
    component: () => import('../views/templates/_list.vue'),
    meta:{auth:true,hideNavbar: false}
  },
  {
    path: '/templates/blogpost',
    name: 'blogpost',
    component: () => import('../views/templates/BlogPost.vue'),
    meta:{auth:true,hideNavbar: false,hideTopbar: true}
  },
  {
    path: '/templates/textblob',
    name: 'textblob',
    component: () => import('../views/templates/TextBlob.vue'),
    meta:{auth:true,hideNavbar: false,hideTopbar: true}
  },
  {
    path: '/templates/commands',
    name: 'commands',
    component: () => import('../views/templates/CommandsPage.vue'),
    meta:{auth:true,hideNavbar: false,hideTopbar: true}
  },
  {
    path: '/templates/text-improver',
    name: 'textimprover',
    component: () => import('../views/templates/TextImprover.vue'),
    meta:{auth:true,hideNavbar: false,hideTopbar: true}
  },
  {
    path: '/templates/blog-outline',
    name: 'blogoutline',
    component: () => import('../views/templates/BlogOutline.vue'),
    meta:{auth:true,hideNavbar: false,hideTopbar: true}
  },
  {
    path: '/templates/cold-email',
    name: 'coldemail',
    component: () => import('../views/templates/ColdEmail.vue'),
    meta:{auth:true,hideNavbar: false,hideTopbar: true}
  },
  {
    path: '/feedback',
    name: 'feedback',
    component: () => import('../views/FeedBack.vue'),
    meta:{auth:true,hideNavbar: false,hideTopbar: false}
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach(async (to,fro,next) => {

  let isAuth = false
  if (localStorage.getItem('gghqw')) {
    isAuth = true
  } else {
    isAuth = false
  }

  if (!isAuth && to.name !== 'login' && to.meta.auth) {
    next('/login')
  } else {
    next()
  }

  
})



export default router

import Vue from 'vue'
import Router from 'vue-router'
import VueResource from 'vue-resource'
import criarLivro from '@/components/livro/criarLivro.vue'
import deletarLivro from '@/components/livro/deletarLivro.vue'
import listarLivro from '@/components/livro/listarLivro.vue'
import atualizarLivro from '@/components/livro/atualizarLivro.vue'
import cadastrarFuncionario from '@/components/pessoa/cadastrarFuncionario.vue'
import cadastrarUsuario from '@/components/pessoa/cadastrarUsuario.vue'
import loginFunc from '@/components/pessoa/loginFunc.vue'
import loginUsuario from '@/components/pessoa/loginUsuario.vue'
import principalUsuario from '@/components/pessoa/principalUsuario.vue'
import livros from '@/components/pessoa/livros.vue'
import alugarLivro from '@/components/pessoa/alugarLivro.vue'
import devolverLivro from '@/components/livro/devolverLivro.vue'
import removerUsuario from '@/components/pessoa/removerUsuario.vue'

Vue.use(VueResource)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/criarLivro',
      name: 'criarLivro',
      component: criarLivro
    },
    {
      path: '/deletarLivro',
      name: 'deletarLivro',
      component: deletarLivro
    },
    {
      path: '/listarLivro',
      name: 'listarLivro',
      component: listarLivro
    },
    {
      path: '/atualizarLivro',
      name: 'atualizarLivro',
      component: atualizarLivro
    },
    {
      path: '/cadastrarFuncionario',
      name: 'cadastrarFuncionario',
      component: cadastrarFuncionario
    },
    {
      path: '/cadastrarUsuario',
      name: 'cadastrarUsuario',
      component: cadastrarUsuario
    },
    {
      path: '/loginFunc',
      name: 'loginFunc',
      component: loginFunc
    },
    {
      path: '/loginUsuario',
      name: 'loginUsuario',
      component: loginUsuario
    },
    {
      path: '/principalUsuario',
      name: 'principalUsuario',
      component: principalUsuario
    },
    {
      path: '/livros',
      name: 'livros',
      component: livros
    },
    {
      path: '/alugarLivro',
      name: 'alugarLivro',
      component: alugarLivro
    },
    {
      path: '/devolverLivro',
      name: 'devolverLivro',
      component: devolverLivro
    },
    {
      path: '/removerUsuario',
      name: 'removerUsuario',
      component: removerUsuario
    },
    {
      path: '/',
      component: loginFunc
    }
  ]
})

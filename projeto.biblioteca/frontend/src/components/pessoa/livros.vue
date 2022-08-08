<template>
  <div id="livros">
    <h1>Listar Livros</h1>

    <p>
      <router-link :to="{ name: 'principalUsuario' }" class="routerlink">Página Principal</router-link>
    </p>
    <table class="table table-hover">
      <thead>
        <tr>
          <td>ID</td>
          <td>Título</td>
          <td>Autores</td>
          <td>Editora</td>
          <td>Ano</td>
          <td>ISBN</td>
          <td>Preço</td>
        </tr>
      </thead>

      <tbody>
        <tr v-for='livro in livros' v-bind:key='livro'>
          <td>{{ livro._id['$oid'] }}</td>
          <td>{{ livro.titulo }}</td>
          <td>{{ livro.autores }}</td>
          <td>{{ livro.editora }}</td>
          <td>{{ livro.ano }}</td>
          <td>{{ livro.isbn }}</td>
          <td>{{ livro.preco }}</td>
          <td>
            <router-link
              :to="{ name: 'alugarLivro', params: { id: livro._id['$oid'] } }"
              class="btn btn-primary">Alugar
            </router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      livros: []
    }
  },

  created: function () {
    this.fetchLivroData()
  },

  methods: {
    fetchLivroData: function () {
      this.$http.get('http://localhost:5000/index').then(
        (response) => {
          this.livros = response.body
        },
        (response) => {}
      )
    }
  }
}
</script>

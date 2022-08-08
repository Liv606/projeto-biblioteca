<template>
  <div id="reservarLivros">
    <h1>Listar Livros</h1>

    <p>
      <router-link :to="{ name: 'livros' }" class="routerlink">Alugar Livro</router-link>
    </p>
    <h2>Livros Reservados</h2>
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
        <tr v-for='livroReservado in livrosReservados' v-bind:key='livroReservado'>
          <td>{{ livroReservado._id['$oid'] }}</td>
          <td>{{ livroReservado.titulo }}</td>
          <td>{{ livroReservado.autores }}</td>
          <td>{{ livroReservado.editora }}</td>
          <td>{{ livroReservado.ano }}</td>
          <td>{{ livroReservado.isbn }}</td>
          <td>{{ livroReservado.preco }}</td>
          <td>
            <router-link
              :to="{ name: 'devolverLivro', params: { id: livroReservado._id['$oid'] } }"
              class="btn btn-danger">Devolver livro
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
      livrosReservados: []
    }
  },

  created: function () {
    this.fetchLivrosReservadosData()
  },

  methods: {
    fetchLivrosReservadosData: function () {
      this.$http.get('http://localhost:5000/reserva').then(
        (response) => {
          this.livrosReservados = response.body
        },
        (response) => {}
      )
    }
  }
}
</script>

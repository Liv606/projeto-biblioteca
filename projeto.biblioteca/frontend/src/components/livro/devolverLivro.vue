<template>
  <div id="devolverLivro">
    <h1>Devolver Livro</h1>

    <p>
      <router-link :to="{ name: 'principalUsuario' }" class="routerlink">Voltar para a página principal</router-link>
    </p>
    <form v-on:submit.prevent="devolverLivro">
      <table class="table">
        <div class="form-group">
          <tr>
            <td><label name="livroReservado_id">ID</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model='livroReservado.id'
              id="livroReservado_id"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="livroReservado_titulo">Título</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="livroReservado.titulo"
              id="livroReservado_titulo"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="livroReservado_autores">Autores</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="livroReservado.autores"
              id="livroReservado_autores"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="livroReservado_editora">Editora</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="livroReservado.editora"
              id="livroReservado_editora"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="livroReservado_ano">Ano</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="livroReservado.ano"
              id="livroReservado_ano"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="livroReservado_isbn">ISBN</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="livroReservado.isbn"
              id="livroReservado_isbn"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="livroReservado_preco">Preço</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="livroReservado.preco"
              id="livroReservado_preco"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td></td>
            <td><button class='btn btn-primary'>Devolver</button></td>
          </tr>
        </div>
      </table>
    </form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      livroReservado: {}
    }
  },
  created: function () {
    this.getLivroReservadoData()
  },
  methods: {
    getLivroReservadoData: function () {
      this.$http
        .get('http://localhost:5000/getidreserva/' + this.$route.params.id)
        .then(
          (response) => {
            this.livroReservado.id = this.$route.params.id
            this.livroReservado.titulo = response.body['titulo']
            this.livroReservado.autores = response.body['autores']
            this.livroReservado.editora = response.body['editora']
            this.livroReservado.ano = response.body['ano']
            this.livroReservado.isbn = response.body['isbn']
            this.livroReservado.preco = response.body['preco']
            this.$forceUpdate()
          },
          (response) => {}
        )
    },
    devolverLivro: function () {
      this.$http.get('http://localhost:5000/devolverLivro/' + this.livroReservado.id).then(
        (response) => {
          this.livroReservado = {}
          alert(response.body['mensagem'])
          this.$router.push('principalUsuario')
        },
        (response) => {
          alert(response.body['mensagem'])
        }
      )
    }
  }
}
</script>

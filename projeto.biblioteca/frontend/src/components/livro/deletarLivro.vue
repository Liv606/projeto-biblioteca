<template>
  <div id="deletarLivro">
    <h1>Deletar Livro</h1>

    <p>
      <router-link :to="{ name: 'listarLivro' }" class="routerlink">Voltar para a lista de livros</router-link>
    </p>
    <form v-on:submit.prevent="deleteLivro">
      <table class="table">
        <div class="form-group">
          <tr>
            <td><label name="livro_id">ID</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model='livro.id'
              id="livro_id"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="livro_titulo">Título</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="livro.titulo"
              id="livro_titulo"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="livro_autores">Autores</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="livro.autores"
              id="livro_autores"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="livro_editora">Editora</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="livro.editora"
              id="livro_editora"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="livro_ano">Ano</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="livro.ano"
              id="livro_ano"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="livro_isbn">ISBN</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="livro.isbn"
              id="livro_isbn"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="livro_preco">Preço</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="livro.preco"
              id="livro_preco"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td></td>
            <td><button class='btn btn-primary'>Deletar</button></td>
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
      livro: {}
    }
  },
  created: function () {
    this.getLivroData()
  },
  methods: {
    getLivroData: function () {
      this.$http
        .get('http://localhost:5000/getid/' + this.$route.params.id)
        .then(
          (response) => {
            this.livro.id = this.$route.params.id
            this.livro.titulo = response.body['titulo']
            this.livro.autores = response.body['autores']
            this.livro.editora = response.body['editora']
            this.livro.ano = response.body['ano']
            this.livro.isbn = response.body['isbn']
            this.livro.preco = response.body['preco']
            this.$forceUpdate()
          },
          (response) => {}
        )
    },
    deleteLivro: function () {
      this.$http.get('http://localhost:5000/deletarLivro/' + this.livro.id).then(
        (response) => {
          this.livro = {}
          alert(response.body['mensagem'])
          this.$router.push('listarLivro')
        },
        (response) => {
          alert(response.body['mensagem'])
        }
      )
    }
  }
}
</script>

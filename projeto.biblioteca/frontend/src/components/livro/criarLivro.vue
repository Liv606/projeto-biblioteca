<template>
  <div id="create-livro">
    <h1>Criar Livro</h1>

    <p>
      <router-link :to="{ name: 'listarLivro' }" class="routerlink">Voltar para a lista de livros</router-link>
    </p>
    <form v-on:submit.prevent="addLivro">
      <table class="table">
        <div class="form-group">
          <tr>
            <td><label name="livro_titulo">Título</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="livro.titulo"
              id="livro_titulo"
              required
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
              required
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
              required
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
              required
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
              required
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
              required
              />
            </td>
          </tr>

          <tr>
            <td></td>
            <td><button class="btn btn-primary">Criar</button></td>
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
  methods: {
    addLivro: function () {
      // Validação dos campos
      var ano = parseFloat(this.livro.ano)
      var isbn = parseFloat(this.livro.isbn)
      var preco = parseFloat(this.livro.preco)
      if (isNaN(ano)) {
        alert('O campo ano aceita apenas números')
        return false
      } else {
        this.livro.ano = this.livro.ano
      }
      if (isNaN(isbn)) {
        alert('O campo ISBN aceita apenas números')
        return false
      } else {
        this.livro.isbn = this.livro.isbn
      }
      if (isNaN(preco)) {
        alert('O campo preço aceita apenas números')
        return false
      } else {
        this.livro.preco = this.livro.preco
      }
      this.$http
        .post('http://localhost:5000/criarLivro', this.livro, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(
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

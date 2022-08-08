<template>
  <div id="alugarLivro">
    <h1>Alugar Livro</h1>

    <p>
      <router-link :to="{ name: 'livros' }" class="routerlink">Voltar para a lista de livros</router-link>
    </p>
    <form v-on:submit.prevent="alugarLivro">
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
            <td><button class='btn btn-primary'>Gerar QRCODE</button></td>
          </tr>
          </div>
      </table>
    </form>
    <!--<img id="imageQRCode" src="https://www.blogson.com.br/wp-content/uploads/2020/12/Gerar-QR-Code-com-jQuery-ou-JavaScript-1.png">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    $('button').click(function () {
    var conteudo = $('#livro_id').val()
    var GoogleCharts = 'https://chart.googleapis.com/chart?chs=500x500&cht=qr&chl='
    var imagemQRCode = GoogleCharts + conteudo
    $('#imageQRCode').attr('src', imagemQRCode)
    })-->
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
    alugarLivro: function () {
      this.$http
        .post('http://localhost:5000/alugarLivro', this.livro, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(
          (response) => {
            this.livro = {}
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

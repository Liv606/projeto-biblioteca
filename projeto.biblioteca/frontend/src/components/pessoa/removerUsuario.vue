<template>
  <div id="removerUsuario">
    <h1>Remover Usuário</h1>

    <p>
      <router-link :to="{ name: 'listarLivro' }" class="routerlink">Voltar para a lista de livros</router-link>
    </p>
    <form v-on:submit.prevent="remUsuario">
      <table class="table">
        <div class="form-group">
          <tr>
            <td><label name="usuario_nome">Nome Completo</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="usuario.nome"
              id="usuario_nome"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="usuario_email">E-mail</label></td>
            <td><input
              type="email"
              class="form-control"
              v-model="usuario.email"
              id="usuario_email"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="usuario_nascimento">Data de Nascimento</label></td>
            <td><input
              type="date"
              class="form-control"
              v-model="usuario.nascimento"
              id="usuario_nascimento"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="usuario_rg">Registro Geral (RG)</label>
            <td><input
              type="text"
              class="form-control"
              v-model="usuario.rg"
              id="usuario_rg"
              placeholder="Apenas números"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="usuario_cpf">CPF</label>
            <td><input
              type="text"
              class="form-control"
              v-model="usuario.cpf"
              id="usuario_cpf"
              placeholder="Apenas números"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="usuario_cep">CEP</label>
            <td><input
              type="text"
              class="form-control"
              v-model="usuario.cep"
              id="usuario_cep"
              placeholder="Apenas números"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="usuario_rua">Rua</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="usuario.rua"
              id="usuario_rua"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="usuario_bairro">Bairro</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="usuario.bairro"
              id="usuario_bairro"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="usuario_numero">Número</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="usuario.numero"
              id="usuario_numero"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="usuario_complemento">Complemento</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="usuario.complemento"
              id="usuario_complemento"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="usuario_celular">Celular</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="usuario.celular"
              id="usuario_celular"
              placeholder="Apenas números"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="usuario_login">Login</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="usuario.login"
              id="usuario_login"
              placeholder="Apenas números"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="usuario_senha">Senha</label></td>
            <td><input
              type="password"
              class="form-control"
              v-model="usuario.senha"
              id="usuario_senha"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td><label name="usuario_confirmarSenha">Confirmar Senha</label></td>
            <td><input
              type="password"
              class="form-control"
              v-model="usuario.confirmarSenha"
              id="usuario_confirmarSenha"
              disabled
              />
            </td>
          </tr>

          <tr>
            <td></td>
            <td><button class='btn btn-primary'>Remover usuário</button></td>
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
      usuario: {}
    }
  },
  created: function () {
    this.getUsuarioData()
  },
  methods: {
    getLivroData: function () {
      this.$http
        .get('http://localhost:5000/idremUsuario/' + this.$route.params.id)
        .then(
          (response) => {
            this.usuario.id = this.$route.params.id
            this.usuario.nome = response.body['nome']
            this.usuario.email = response.body['email']
            this.usuario.nascimento = response.body['nascimento']
            this.usuario.rg = response.body['rg']
            this.usuario.cpf = response.body['cpf']
            this.usuario.cep = response.body['cep']
            this.usuario.rua = response.body['rua']
            this.usuario.bairro = response.body['bairro']
            this.usuario.numero = response.body['numero']
            this.usuario.complemento = response.body['complemento']
            this.usuario.celular = response.body['celular']
            this.usuario.login = response.body['login']
            this.usuario.senha = response.body['senha']
            this.usuario.confSenha = response.body['confSenha']
            this.$forceUpdate()
          },
          (response) => {}
        )
    },
    remUsuario: function () {
      this.$http.get('http://localhost:5000/removerUsuario/' + this.usuario.id).then(
        (response) => {
          this.usuario = {}
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

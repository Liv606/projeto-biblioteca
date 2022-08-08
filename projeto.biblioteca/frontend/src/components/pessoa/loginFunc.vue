<template>
  <div id="login-func">
    <h1>Página de Login</h1>

    <form v-on:submit.prevent="loginFunc">
      <table class="table">
        <div class="form-group">
          <tr>
            <td><label name="loginFuncionario_ra">RA</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="loginFuncionario.ra"
              id="loginFuncionario_ra"
              placeholder="Apenas números"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="loginFuncionario_senha">Senha</label></td>
            <td><input
              type="password"
              class="form-control"
              v-model="loginFuncionario.senha"
              id="loginFuncionario_senha"
              required
              />
            </td>
          </tr>

          <tr>
            <td></td>
            <td><button class="btn btn-primary">Entrar</button></td>
          </tr>
        </div>
      </table>
    </form>
    <p>
      <router-link :to="{ name: 'cadastrarFuncionario' }" class="routerlink">Cadastrar novo funcionário</router-link>
    </p>
    <p>
      <router-link :to="{ name: 'cadastrarUsuario' }" class="routerlink">Cadastrar novo usuário</router-link>
    </p>
  </div>
</template>

<script>
export default {
  data () {
    return {
      loginFuncionario: {}
    }
  },
  methods: {
    loginFunc: function () {
      // Validação dos dados
      var ra = parseFloat(this.loginFuncionario.ra)
      if (isNaN(ra)) {
        alert('Número de RA incorreto')
        return false
      } else {
        this.loginFuncionario.ra = this.loginFuncionario.ra
      }
      this.$http
        .post('http://localhost:5000/loginFunc', this.loginFuncionario, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(
          (response) => {
            this.loginFuncionario = {}
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

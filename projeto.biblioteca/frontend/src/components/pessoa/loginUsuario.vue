<template>
  <div id="login-usuario">
    <h1>Página de Login</h1>

    <form v-on:submit.prevent="loginUsu">
      <table class="table">
        <div class="form-group">
          <tr>
            <td><label name="loginUsuario_ra">RA</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="loginUsuario.ra"
              id="loginUsuario_ra"
              placeholder="Apenas números"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="loginUsuario_senha">Senha</label></td>
            <td><input
              type="password"
              class="form-control"
              v-model="loginUsuario.senha"
              id="loginUsuario_senha"
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
      loginUsuario: {}
    }
  },
  methods: {
    loginUsu: function () {
      // Validação dos dados
      var ra = parseFloat(this.loginUsuario.ra)
      if (isNaN(ra)) {
        alert('Número de RA incorreto')
        return false
      } else {
        this.loginUsuario.ra = this.loginUsuario.ra
      }
      this.$http
        .post('http://localhost:5000/loginUsuario', this.loginUsuario, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(
          (response) => {
            this.login = {}
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

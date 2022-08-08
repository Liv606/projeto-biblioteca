<template>
  <div id="cadastrar-usuario">
    <h1>Cadastrar Usuário</h1>

    <p>
      <router-link :to="{ name: 'loginUsuario' }" class="routerlink">Voltar para a página de login</router-link>
    </p>
    <form v-on:submit.prevent="cadUsuario">
      <table class="table">
        <div class="form-group">
          <tr>
            <td><label name="usuario_nome">Nome Completo</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="usuario.nome"
              id="usuario_nome"
              required
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
              required
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
              required
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
              required
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
              required
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
              required
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
              required
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
              required
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
              required
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
              required
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
              required
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
              required
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
      usuario: {}
    }
  },
  methods: {
    cadUsuario: function () {
      // Validação dos campos
      var rg = parseFloat(this.usuario.rg)
      var cpf = parseFloat(this.usuario.cpf)
      var cep = parseFloat(this.usuario.cep)
      var num = parseFloat(this.usuario.numero)
      var celular = parseFloat(this.usuario.celular)
      var login = parseFloat(this.usuario.login)
      var senha = parseFloat(this.usuario.senha)
      var confSenha = parseFloat(this.usuario.confirmarSenha)

      if (isNaN(rg)) {
        alert('Campo RG aceita apenas números')
        return false
      } else {
        this.usuario.rg = this.usuario.rg
      }
      if (isNaN(cpf)) {
        alert('Campo CPF aceita apenas números')
        return false
      } else {
        this.usuario.cpf = this.usuario.cpf
      }
      if (isNaN(cep)) {
        alert('Campo CEP aceita apenas números')
        return false
      } else {
        this.usuario.cep = this.usuario.cep
      }
      if (isNaN(num)) {
        alert('Campo número de casa aceita apenas números')
        return false
      } else {
        this.usuario.num = this.usuario.num
      }
      if (isNaN(celular)) {
        alert('Campo celular aceita apenas números')
        return false
      } else {
        this.usuario.celular = this.usuario.celular
      }
      if (isNaN(login)) {
        alert('Campo login(RA) aceita apenas números')
        return false
      } else {
        this.usuario.login = this.usuario.login
      }
      if (senha !== confSenha) {
        alert('Confirmação de senha incorreta')
        return false
      } else {
        this.usuario.senha = this.usuario.senha
        this.usuario.confsenha = this.usuario.confsenha
      }
      this.$http
        .post('http://localhost:5000/cadastrarUsuario', this.usuario, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(
          (response) => {
            this.usuario = {}
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

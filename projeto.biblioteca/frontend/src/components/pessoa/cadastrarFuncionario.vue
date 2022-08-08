<template>
  <div id="cadastrar-funcionario">
    <h1>Cadastrar Funcionário</h1>

    <p>
      <router-link :to="{ name: 'loginFunc' }" class="routerlink">Voltar para a página de login</router-link>
    </p>
    <form v-on:submit.prevent="cadFuncionario">
      <table class="table">
        <div class="form-group">
          <tr>
            <td><label name="funcionario_nome">Nome Completo</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="funcionario.nome"
              id="funcionario_nome"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="funcionario_email">E-mail</label></td>
            <td><input
              type="email"
              class="form-control"
              v-model="funcionario.email"
              id="funcionario_email"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="funcionario_nascimento">Data de Nascimento</label></td>
            <td><input
              type="date"
              class="form-control"
              v-model="funcionario.nascimento"
              id="funcionario_nascimento"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="funcionario_rg">Registro Geral (RG)</label>
            <td><input
              type="text"
              class="form-control"
              v-model="funcionario.rg"
              id="funcionario_rg"
              placeholder="Apenas números"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="funcionario_cpf">CPF</label>
            <td><input
              type="text"
              class="form-control"
              v-model="funcionario.cpf"
              id="funcionario_cpf"
              placeholder="Apenas números"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="funcionario_cep">CEP</label>
            <td><input
              type="text"
              class="form-control"
              v-model="funcionario.cep"
              id="funcionario_cep"
              placeholder="Apenas números"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="funcionario_rua">Rua</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="funcionario.rua"
              id="funcionario_rua"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="funcionario_bairro">Bairro</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="funcionario.bairro"
              id="funcionario_bairro"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="funcionario_numero">Número</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="funcionario.numero"
              id="funcionario_numero"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="funcionario_complemento">Complemento</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="funcionario.complemento"
              id="funcionario_complemento"
              />
            </td>
          </tr>

          <tr>
            <td><label name="funcionario_celular">Celular</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="funcionario.celular"
              id="funcionario_celular"
              placeholder="Apenas números"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="funcionario_codigo">Código de Funcionário</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="funcionario.codigo"
              id="funcionario_codigo"
              placeholder="Apenas números"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="funcionario_login">Login</label></td>
            <td><input
              type="text"
              class="form-control"
              v-model="funcionario.login"
              id="funcionario_login"
              placeholder="Apenas números"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="funcionario_senha">Senha</label></td>
            <td><input
              type="password"
              class="form-control"
              v-model="funcionario.senha"
              id="funcionario_senha"
              required
              />
            </td>
          </tr>

          <tr>
            <td><label name="funcionario_confirmaSenha">Confirmar Senha</label></td>
            <td><input
              type="password"
              class="form-control"
              v-model="funcionario.confirmarSenha"
              id="funcionario_confirmarSenha"
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
      funcionario: {}
    }
  },
  methods: {
    cadFuncionario: function () {
      // Validação dos campos
      var rg = parseFloat(this.funcionario.rg)
      var cpf = parseFloat(this.funcionario.cpf)
      var cep = parseFloat(this.funcionario.cep)
      var num = parseFloat(this.funcionario.numero)
      var celular = parseFloat(this.funcionario.celular)
      var codigo = parseFloat(this.funcionario.codigo)
      var login = parseFloat(this.funcionario.login)
      var senha = parseFloat(this.funcionario.senha)
      var confSenha = parseFloat(this.funcionario.confirmarSenha)

      if (isNaN(rg)) {
        alert('Campo RG aceita apenas números')
        return false
      } else {
        this.funcionario.rg = this.funcionario.rg
      }
      if (isNaN(cpf)) {
        alert('Campo CPF aceita apenas números')
        return false
      } else {
        this.funcionario.cpf = this.funcionario.cpf
      }
      if (isNaN(cep)) {
        alert('Campo CEP aceita apenas números')
        return false
      } else {
        this.funcionario.cep = this.funcionario.cep
      }
      if (isNaN(num)) {
        alert('Campo número de casa aceita apenas números')
        return false
      } else {
        this.funcionario.num = this.funcionario.num
      }
      if (isNaN(celular)) {
        alert('Campo celular aceita apenas números')
        return false
      } else {
        this.funcionario.celular = this.funcionario.celular
      }
      if (isNaN(codigo)) {
        alert('Campo código aceita apenas números')
        return false
      } else {
        this.funcionario.codigo = this.funcionario.codigo
      }
      if (isNaN(login)) {
        alert('Campo login(RA) aceita apenas números')
        return false
      } else {
        this.funcionario.login = this.funcionario.login
      }
      if (senha !== confSenha) {
        alert('Confirmação de senha incorreta')
        return false
      } else {
        this.funcionario.senha = this.funcionario.senha
        this.funcionario.confsenha = this.funcionario.confsenha
      }
      this.$http
        .post('http://localhost:5000/cadastrarFuncionario', this.funcionario, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(
          (response) => {
            this.funcionario = {}
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

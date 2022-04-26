import React, { Component } from "react";
import { setLogin } from "../middleware/servicesCadastro";
import { Navigate } from "react-router-dom";

// export function getUser() {
//   const login = Navbar.getUser();
//   return login;
// }

export default class Navbar extends Component {
  constructor(props) {
    super(props);

    this.state = {
      login: {
        email: "",
        senha: "",
        auth: false,
      },
    };
  }

  getUser() {
    return this.state.login;
  }

  // componentDidMount(){

  // this.setState({
  // login: false
  // })

  // }
  handleBlur = (e) => {
    const { login } = this.state;
    let newLogin = login;

    newLogin[e.target.id] = e.target.value;
    console.log(e.target.value);
    this.setState({ login: newLogin });
    console.log(login);
  };
  handleSubmit = async (e) => {
    e.preventDefault();
    const { login } = this.state;
    console.log("login", this.state.login);
    try {
      var response = await setLogin(login);
      console.log(response);
      this.loginRedirect(response);
    } catch (error) {
      alert(error.response.data.detail);
    }
  };

  loginRedirect = (response) => {
    if (response.status === 200) {
      const { login } = this.state;
      this.setState({
        login: {
          email: login.email,
          senha: login.senha,
          auth: true,
        },
      });

      console.log(this.state.login);
      if (response.data.tipo === "Produtor") {
        // window.location.href = "/SMA-Handshake-Eng-Software-2022.1-/produtor";
        <Navigate to="/SMA-Handshake-Eng-Software-2022.1-/produtor" />;
      } else {
        // window.location.href = "/SMA-Handshake-Eng-Software-2022.1-/consumidor";
        <Navigate to="/SMA-Handshake-Eng-Software-2022.1-/consumidor" />;
      }
    } else {
      alert("Erro ao efetuar o login");
    }
  };

  render() {
    // const auth = this.state.login.auth;
    const { login } = this.state;
    console.log("====== render ========");
    console.log(this.state.login);
    return (
      <>
        <header>
          <div>
            <h1>
              <a href="/">SMA Handshake</a>
            </h1>
          </div>
          {!this.state.login.auth && (
            <div className="login-div">
              <form onSubmit={this.handleSubmit}>
                <label>Usuário</label>
                <input id="email" onBlur={this.handleBlur}></input>
                <label>Senha</label>
                <input
                  id="senha"
                  type="password"
                  onBlur={this.handleBlur}
                ></input>
                <button>Entrar</button>
              </form>
              <a href="cadastro">Cadastrar-se</a>
            </div>
          )}
          {this.state.login.auth && (
            <div>
              <p>{this.state.login.email}</p>
            </div>
          )}
        </header>
      </>
    );
  }
}

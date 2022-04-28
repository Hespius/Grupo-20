import React, { Component } from "react";
import { setLogin } from "../middleware/servicesCadastro";
import { Navigate } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { connect } from "react-redux";

// export function getUser() {
//   const login = Navbar.getUser();
//   return login;
// }

import {
  modificaEmail,
  modificaId,
  modificaNome,
  modificaAuth,
} from "../../src/redux/actions/AutenticationActions";

class Navbar extends Component {
  constructor(props) {
    super(props);

    this.state = {
      login: {
        email: "",
        senha: "",
        auth: false,
      },
      redirect: false,
      url: "",
    };
  }

  SetUser = (user) => {
    this.props.modificaNome(user.nome);
    this.props.modificaEmail(user.email);
    this.props.modificaId(user.id_usuario);
  };

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
      alert("Erro ao logar: " + error.message);
    }
  };

  loginRedirect = (response) => {
    if (response.status === 200) {
      console.log("LOGIN realizado com sucesso");
      const { login } = this.state;
      this.setState({
        login: {
          email: login.email,
          senha: login.senha,
        },
      });
      this.props.modificaAuth(true);
      //   console.log("salvando estado");
      this.SetUser(response.data);
      //   console.log("salvou estado");
      //   console.log("=========this.state.login=========", this.state.login);
      if (response.data.tipo === "Produtor") {
        // window.location.href = "/SMA-Handshake-Eng-Software-2022.1-/produtor";
        console.log("redirecionando produtor...");
        this.redirect = true;
        this.setState({
          redirect: true,
          url: "/produtor",
        });
      } else {
        // window.location.href = "/SMA-Handshake-Eng-Software-2022.1-/consumidor";
        console.log("redirecionando produtor...");
        this.redirect = true;
        this.setState({
          redirect: true,
          url: "/consumidor",
        });
      }
    } else {
      alert("Erro ao efetuar o login");
    }
  };

  componentDidMount() {
    this.mounted = true;
  }

  componentWillUnmount() {
    this.mounted = false;
  }

  render() {
    // const auth = this.state.login.auth;
    const { login } = this.state;
    // const { user } = useSelector((state) => console.log(state));
    const { nome, email, id } = this.props;
    if (this.redirect && window.location.href !== "/produtor") {
      this.redirect = false;
      return <Navigate to={this.state.url} />;
    }
    return (
      <>
        <header>
          <div>
            <h1>
              <a href="/">SMA Handshake</a>
            </h1>
          </div>
          {!this.props.auth && (
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
          {this.props.auth && (
            <div>
              <p>{email}</p>
            </div>
          )}
        </header>
      </>
    );
  }
}

const mapStateToProps = (state) => ({
  nome: state.AutenticationReducer.nome,
  email: state.AutenticationReducer.email,
  id: state.AutenticationReducer.id,
  auth: state.AutenticationReducer.auth,
});

export default connect(mapStateToProps, {
  modificaEmail,
  modificaId,
  modificaNome,
  modificaAuth,
})(Navbar);

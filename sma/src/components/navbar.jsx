import React, {Component} from 'react'

export default class Navbar extends Component {

    handleSubmit = () => {

    }

    render() {
        return (

            <>
            <header>
            <div>
                <h1><a href='/'>SMA Handshake</a></h1>
            </div>
            <div className='login-div'>
                <form onSubmit={this.handleSubmit}>
                <label>Usuário</label>
                <input></input>
                <label>Senha</label>
                <input></input>
                <button link='/mercadorias'>Entrar</button>
                </form>
                <a href='cadastro'>Cadastrar-se</a>
            </div>
            </header>
            </>

        )
    }

}
import React, {Component} from 'react'

export default class Cadastro extends Component {


    state = {
        cadastro:{
            tipo:'',
            nome:'',
            cpf_cnpj:'',
            telefone: '',
            estado: '',
            cidade: '',
            cep: '',
            logradouro:'' ,
            numero: '',
            email: '',
            senha: '',
        },
        checkSenha: '',
    }

    handleBlur = () => {

    }
    handleSubmit = () => {

    }

    render() {
        return (

            <>
            <div>
            </div>
            <div className='div-cadastro'>
                <form className='cadastro' onSubmit={this.handleSubmit}>
                <h1>Cadastro</h1>
                  <div className='div-global'>
                  <div className='div-form'>
                    <label>Tipo</label>
                    <input list="tipos" id='tipo' />
                    <datalist id="tipos">
                    <option value="Produtor" />
                    <option value="Consumidor" />
                    </datalist>
                    <label>Nome</label>
                    <input id='nome'></input>
                    <label>CPF/CNPJ</label>
                    <input id = 'cpf_cnpj'></input>
                    <label>Telefone</label>
                    <input id='telefone'></input>
                    <label>Estado</label>
                    <input id='estado'></input>
                    <label>Cidade</label>
                    <input id='cidade'></input>
                    </div>
                    <div className='div-form'>
                    <label>CEP</label>
                    <input id='cep'></input>
                    <label>Logradouro</label>
                    <input id='logradouro'></input>
                    <label>Nº</label>
                    <input id='numero'></input>
                    <label>E-mail</label>
                    <input id='email' type='email'></input>
                    <label>Senha</label>
                    <input id='senha' type='password'></input>
                    <label>Confirmar Senha</label>
                    <input id='checkSenha' type='password'></input>
                    </div>
                   <button className='confirmar-cadastro'>Cadastrar-se</button>
                    </div>
                </form>
            </div>
            </>

        )
    }

}
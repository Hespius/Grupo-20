import React, {Component} from 'react'
import './App.css';
import 'devextreme/dist/css/dx.greenmist.css';

import {
BrowserRouter,
Switch,
Route,
Routes,

} from "react-router-dom";

import Home from './components/home'
import Navbar from './components/navbar'
import Cadastro from './components/cadastro'
import Produtor from './components/produtor'
import Consumidor from './components/consumidor'
import Menu from './components/menu'
// import Compras from './components/compras'

class App extends Component {

state = {
login: {
email: '',
senha: '' ,

}

}

getUser = () =>{

console.log(this.state)

}

componentDidMount (){
const login = { email: 'aluno@ufabc.com.br' , senha: 'y'}
this.setState ({
login:login
})

}

render(){

const user = this.getUser()
return (
  <BrowserRouter>
{/* <Menu/> */}
<Navbar user= {this.state.login} />
<Routes>
    <Route exact path='/' element={ <Home/>} />
    <Route exact path='/cadastro' element={<Cadastro/>} />
    <Route exact path='/produtor' element={<Produtor/>} />
    <Route exact path='/consumidor' element={<Consumidor/>} />
    {/* <Route exact path='/compras' element={<Compras/>} /> */}
  </Routes>
</BrowserRouter>

);
}
}

export default App;
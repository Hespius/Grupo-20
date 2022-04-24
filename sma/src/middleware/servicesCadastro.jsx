import http from "./httpService";
// import {api_url} from '../config.json'

let backPath = "http://localhost:8000/usuarios";
// let backPath = "https://sma-ufabc202201-backend.herokuapp.com/usuarios"
export function setCadastro(cadastro) {
  return http.post(backPath + "/cadastrar", cadastro);
}

export async function setLogin(login) {
  return await http.post(backPath + "/login", login);
}

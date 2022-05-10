import http from "./httpService";
// import {api_url} from '../config.json'

let backPath = "http://localhost:8000/dashboard";
// let backPath = "https://sma-ufabc202201-backend.herokuapp.com/usuarios"
export function getReceita(id) {
  return http.get(backPath + `/receita/${id}`);
}

export function getDistribuicao(id) {
  return http.get(backPath + `/distribuicao/${id}`);
}

export function getVendasMensais(id) {
  return http.get(backPath + `/vendas-mensais/${id}`);
}

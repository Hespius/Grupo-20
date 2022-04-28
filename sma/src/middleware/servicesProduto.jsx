import http from "./httpService";
// import {api_url} from '../config.json'

let backPath = "http://localhost:8000/produtos";
// let backPath = "https://sma-ufabc202201-backend.herokuapp.com/produtos"

export async function setProduto(produto) {
  console.log("produto: ", produto);
  return await http.post(backPath + "/criar-oferta", produto);
}

export async function getCommodities() {
  return await http.get(backPath + "/commodities");
}

export async function getOfertas(produtorId) {
  console.log("->produtorId: ", produtorId);
  return await http.get(backPath + "/ofertas", { params: produtorId });
}

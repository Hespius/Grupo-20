import http from "./httpService";
// import {api_url} from '../config.json'

let backPath = "http://localhost:8000/produtos";
// let backPath = "https://sma-ufabc202201-backend.herokuapp.com/produtos"

export async function setProduto(produto, produtorId, commodityId) {
  return await http.post(backPath + "/cadastrar", {
    params: { produtorId: produtorId, commodityId: commodityId },
    data: produto,
  });
}

export async function getCommodities() {
  return await http.get(backPath + "/commodities");
}

export async function getOfertas(produtorId) {
  console.log("->produtorId: ", produtorId);
  return await http.get(backPath + "/ofertas", { params: produtorId });
}

import http from './httpService'
// import {api_url} from '../config.json'

let backPath = "https://sma-ufabc202201-backend.herokuapp.com/produtos"

export async function setProduto(produto){
    return await http.post(backPath + '/cadastrar', produto)
}

export async function getCommodities(){
    return await http.get(backPath + '/commodities')
}

export async function getOfertas(produtorId){
    return await http.get(backPath + '/ofertas', {params: produtorId})
}
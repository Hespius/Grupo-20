import http from './httpService'
// import {api_url} from '../config.json'

let backPath = "http://localhost:8000/produtos"
export async function setOrdem(ordem){
return await http.post(backPath + '/cadastrar', ordem)
}

export async function getOfertas(params){
    return await http.get(backPath + '/ofertas', {params: params})
}

export async function getCommodities(){
    return await http.get(backPath + '/commodities')
}
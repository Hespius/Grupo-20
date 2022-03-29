import http from './httpService'

backPath = ''
export function setCadastro(){
    return http.post(backPath)
}
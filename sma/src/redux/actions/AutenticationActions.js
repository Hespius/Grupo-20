import {
  MODIFICA_NOME,
  MODIFICA_EMAIL,
  MODIFICA_ID,
  MODIFICA_AUTH,
} from "../types";

export const modificaNome = (valor) => {
  return {
    type: MODIFICA_NOME,
    payload: valor,
  };
};

export const modificaEmail = (valor) => {
  return {
    type: MODIFICA_EMAIL,
    payload: valor,
  };
};

export const modificaId = (valor) => {
  return {
    type: MODIFICA_ID,
    payload: valor,
  };
};

export const modificaAuth = (valor) => {
  return {
    type: MODIFICA_AUTH,
    payload: valor,
  };
};

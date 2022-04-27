import {
  MODIFICA_NOME,
  MODIFICA_EMAIL,
  MODIFICA_ID,
  MODIFICA_AUTH,
} from "../types";

const INITIAL_STATE = {
  nome: "",
  email: "",
  id: 0,
  auth: false,
};

export default (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case MODIFICA_NOME:
      return { ...state, nome: action.payload };
    case MODIFICA_EMAIL:
      return { ...state, email: action.payload };
    case MODIFICA_ID:
      return { ...state, id: action.payload };
    case MODIFICA_AUTH:
      return { ...state, auth: action.payload };
    default:
      return state;
  }
};

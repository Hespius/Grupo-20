// import { createStore } from "redux";

// const initialState = {
//   user: {
//     id: "",
//     email: "",
//     auth: false,
//   },
// };

// const reducer = (state = initialState, action) => {
//   switch (action.type) {
//     case "LOGIN":
//       console.log("store login");
//       const newState = { ...state };
//       newState.user = {
//         // id: id,
//         // email: email,
//         auth: true,
//       };
//     default: {
//       return state;
//     }
//   }
// };


// const store = createStore(reducer);
// export default store;

import { createStore } from "redux";
import reducers from "./reducers";

const store = createStore(reducers);

export default store;
export default {
    namespaced: true,
    state: {
      token: null
    },
    getters: {
      isLogin: (state) => state.token !== null,
      token: (state) => {
        return state.token
      }
    },
    mutations: {
      SET_AUTH_TOKEN(state, token) {
        state.token = token;
      },
      REMOVE_AUTH_TOKEN(state) {
        state.token = null;
      },
    },
    actions: {
      setAuthToken(context, options) {
        context.commit('SET_AUTH_TOKEN', {
          token: options.token,
        });
      },
      removeAuthToken(context) {
        context.commit('REMOVE_AUTH_TOKEN');
      },
    },
  };
# 상태관리

###### 2020.06.08

## 라이브러리 설치
```bash
$ yarn add redux react-redux redux-thunk redux-persist @react-native-community/async-storage
```

1. redux : 상태관리 라이브러리
2. react-redux : redux를 react에 연결시켜주는 API(Provider)가 있는 라이브러리
3. redux-thunk : redux store와 작용하는 sync & async 처리를 위한 미들웨어
4. redux-persist : redux의 상태를 유지시키는 장치
5. @react-native-community/async-storate : ios 앱에서 localStorage 용으로 사용되는 저장소 API

## `modules/**.js`
```js
const ADD_TODO = 'ADD_TODO';

// action creators
function addTodo(text) {
  return {
    type: ADD_TODO,
    text
  };
}

// API call

// initialState
const initialState = {};

// reducers
function reducer(state=initialState, action) {
  switch (action.type) {
    default:
      return state;
  }
}

// reducer functions

// export api calls or actionCreators
const actionCreators = { };
export { actionCreators };

// export reducer
export default reducer;
```
> 각 모듈마다 리듀서를 만들어준다. (관리의 편의 성을 위해 나눠서 만들어준다.)

## `configureStore.js`
```js
import { applyMiddleware, combineReducers, createStore } from 'redux';
import { persistStore, persistReducer } from 'redux-persist';
import thunkMiddleware from 'redux-thunk';
import AsyncStorage from '@react-native-community/async-storage';

export default function configureStore() {

  const reducer = combineReducers({
    todoList,
  })

  const persistConfig = {
    key: 'root',
    storage: AsyncStorage
  }

  const persistedReducer = persistReducer(persistConfig, reducer);
  
  const middlewares = [thunkMiddleware];
  const middlewareEnhancer = applyMiddleware(...middlewares);

  const store = createStore(persistedReducer, undefined, middlewareEnhancer);
  const persistor = persistStore(store);

  return { store, persistor };
}
```
> 위에서 만들어진 모듈의 리듀서를 바로 스토어에 넣어서 사용할 수 도 있지만, 여러가지 미들웨어를 붙이고 모듈로 나뉘어진 리듀서를 합쳐서 만들 수 있는데, 위 파일은 그 역할을 하는 파일이다.
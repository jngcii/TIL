# 컴퍼넌트 테스트

###### 2020.06.05

## I. AddToDo Component

### 1) `tests/AddToDo.spec.js`
```js
/**
 * @format
 */

import "react-native";
import React from "react";
import { TextInput, Button } from "react-native";
import { shallow } from "enzyme";
import AddToDo from "../src/AddToDo";

describe("Rendering", () => {
  let wrapper;

  beforeEach(() => {
    wrapper = shallow(<AddToDo />);
  });
  // 모든 it 이라는 구문이 돌아갈 때 마다 새로운 렌더링을 해서 깨끗한 상태에서 테스트를 하겠다.

  it("is TextInput visible?", () => {
    expect(wrapper.find(TextInput)).toHaveLength(1);
  });

  it("is Button visible?", () => {
    expect(wrapper.find(Button)).toHaveLength(1);
  });
});

describe("Interaction", () => {
  let wrapper;
  let props;
  const txt = "some to do";

  beforeEach(() => {
    props = {
      onAdded: jest.fn(),
    }

    wrapper = shallow(<AddToDo {...props} />);

    wrapper.find(TextInput).simulate("changeText", txt);
    wrapper.find(Button).prop("onPress")();
  });

  it("is the onAdded callback called with input text?", () => {
    expect(props.onAdded).toHaveBeenCalledTimes(1);
    expect(props.onAdded).toHaveBeenCalledWith(txt);
  })
})
```
> beforeEach() : 모든 it 이라는 구문이 돌아갈 때 마다 새로운 렌더링을 해서 깨끗한 상태에서 테스트를 하겠다.

### 2) `yarn test`

### 3) 테스트 하나씩 green으로 만들기
```js
import React, { useState } from "react";
import { View, Button, TextInput } from "react-native";

function AddToDo({ onAdded }) {
  const [value, setValue] = useState("");

  const _onAdded = function() {
    onAdded(value);
  }

  return (
    <View>
      <TextInput value={value} onChangeText={setValue} />
      <Button onPress={_onAdded} />
    </View>
  );
}

export default AddToDo;
```
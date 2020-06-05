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

### 3) 테스트 하나씩 green으로 만들기 (`src/AddToDo.js`)
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


## II. ToDoList Component

### 1) `tests/ToDoList.spec.js`
```js
/**
 * @format
 */

import React from "react";
import { FlatList } from "react-native";
import { shallow } from "enzyme";
import ToDoList from "../src/ToDoList";

describe("Rendering", () => {
  let wrapper;
  let props;

  beforeEach(() => {
    props = {
      items: [1, 2, 3].map(i => { 
        return { id: i, keyword: `item ${i}`, completed: false }
      })
    }
    wrapper = shallow(<ToDoList {...props} />);
  });

  it("is FlatList visible?", () => {
    expect(wrapper.find(FlatList)).toHaveLength(1);
  });

  it("is props delivered to FlatList correctly?", () => {
    expect(wrapper.find(FlatList).prop('data')).toBe(props.items)
  })
});
```
> `.props('items')`로 컴퍼넌트가 받은 props를 가져올 수 있다.

### 2) `yarn test`

### 3) 테스트 하나씩 green으로 만들기 (`src/ToDoList.js`)
```js
import React from "react";
import { FlatList } from "react-native";

function ToDoList(props) {
  return (
    <FlatList data={props.items} />
  );
}

export default ToDoList;
```


## III. ToDoItem Component

### 1) `tests/ToDoItem.spec.js`
```js
/**
 * @format
 */
import React from "react";
import { Text, Button } from "react-native";
import { shallow } from "enzyme";
import ToDoItem, { styles } from "../src/ToDoItem";

describe("Rendering", () => {
  let wrapper;
  let props;

  beforeEach(() => {
    props = {
      item: {}
    }
    wrapper = shallow(<ToDoItem {...props} />);
  })

  it("is Text visible?", () => {
    expect(wrapper.find(Text)).toHaveLength(1);
  })

  it("are two Buttons visible?", () => {
    expect(wrapper.find(Button)).toHaveLength(2);
  })

  describe("Uncompleted", () => {
    it("Does it have default style?", () => {
      expect(wrapper.prop("style")).toBe(styles.default);
    })
  })

  describe("Uncompleted", () => {
    beforeEach(() => {
      props.item.completed = true;
      wrapper = shallow(<ToDoItem {...props} />);
    })

    it("Does it have completed style?", () => {
      expect(wrapper.prop("style")).toBe(styles.completed);
    })
  })
})


describe("Interaction", () => {
  let wrapper;
  let props;

  describe("Complete feature", () => {
    beforeEach(() => {
      props = {
        item: { id: 1, keyword: 'item 1', completed: false },
        onComplete: jest.fn(),
        onDelete: jest.fn(),
      }
      
      wrapper = shallow(<ToDoItem {...props} />);
      
      wrapper.find(Button).at(0).prop("onPress")();
    });
    
    it("is the onComplete callback called with input index?", () => {
      expect(props.onComplete).toHaveBeenCalledTimes(1);
      expect(props.onComplete).toHaveBeenCalledWith(props.item.id);
    })
  })

  describe("Delete feature", () => {
    beforeEach(() => {
      props = {
        item: { id: 1, keyword: 'item 1', completed: false },
        onComplete: jest.fn(),
        onDelete: jest.fn(),
      }
      
      wrapper = shallow(<ToDoItem {...props} />);
      
      wrapper.find(Button).at(1).prop("onPress")();
    });
    
    it("is the onDelete callback called with input index?", () => {
      expect(props.onDelete).toHaveBeenCalledTimes(1);
      expect(props.onDelete).toHaveBeenCalledWith(props.item.id);
    })
  })
})
```
> `.props('items')`로 컴퍼넌트가 받은 props를 가져올 수 있다.

### 2) `yarn test`

### 3) 테스트 하나씩 green으로 만들기 (`src/ToDoItem.js`)
```js
import React from "react";
import { View, Text, Button, StyleSheet } from "react-native";

function ToDoItem({ item, onComplete, onDelete }) {
  const onPressComplete = function() {
    onComplete(item.id);
  }

  const onPressDelete = function() {
    onDelete(item.id);
  }

  return (
    <View style={item.completed ? styles.completed : styles.default}>
      <Text></Text>
      <Button onPress={onPressComplete}></Button>
      <Button onPress={onPressDelete}></Button>
    </View>
  )
}

export const styles = StyleSheet.create({
  default: {
    backgroundColor: "white",
  },
  completed: {
    backgroundColor: "red",
  }
})

export default ToDoItem;
```

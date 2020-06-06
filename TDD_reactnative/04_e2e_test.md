# End To End Test (e2e test)

###### 2020.06.06

## I. ToDo 추가 시나리오

### 1) 테스트 코드 작성
- `e2e/firstTest.spec.js`
  ```js
  describe('TDDRN', () => {
    beforeEach(async () => {
      await device.reloadReactNative();
    });

    it('should have welcome screen', async () => {
      await expect(element(by.id('testRoot'))).toBeVisible();
    });

    it("Adding ToDo Item should work!", async () => {
      const text = "a new ToDo Item";
      await element(by.id("textInput")).tap();
      await element(by.id("textInput")).typeText(text);
      await element(by.id("addButton")).tap();
      await expect(element(by.text(text).withAncestor(by.id("toDoList")))).toBeVisible()
    })
  });
  ```

### 2) detox test (실패)

### 3) 성공할때까지 App.js에서 기능 구현



## II. ToDo 완료 시나리오

### 1) 테스트 코드 작성
- `e2e/firstTest.spec.js`
  ```js
  describe('TDDRN', () => {
    beforeEach(async () => {
      await device.reloadReactNative();
    });

    it('should have welcome screen', async () => {
      await expect(element(by.id('testRoot'))).toBeVisible();
    });

    it("Adding ToDo Item should work!", async () => {
      const text = "a new ToDo Item";
      await element(by.id("textInput")).tap();
      await element(by.id("textInput")).typeText(text);
      await element(by.id("addButton")).tap();
      await expect(element(by.text(text).withAncestor(by.id("toDoList")))).toBeVisible()
    })

    it("Completing ToDo Item should work!", async () => {
      const text = "a new ToDo Item";
      await element(by.id("textInput")).tap();
      await element(by.id("textInput")).typeText(text);
      await element(by.id("addButton")).tap();
      
      await element(by.id("completeButton")).multiTap(2);
      await expect(element(by.id("completed").and(by.text(text)).withAncestor(by.id("toDoList")))).toBeVisible()
      
    })
  });
  ```

### 2) detox test (실패)

### 3) 성공할때까지 App.js에서 기능 구현



## III. ToDo 삭제 시나리오

### 1) 테스트 코드 작성
- `e2e/firstTest.spec.js`
  ```js
  describe('TDDRN', () => {
    beforeEach(async () => {
      await device.reloadReactNative();
    });

    it('should have welcome screen', async () => {
      await expect(element(by.id('testRoot'))).toBeVisible();
    });

    it("Adding ToDo Item should work!", async () => {
      const text = "a new ToDo Item";
      await element(by.id("textInput")).tap();
      await element(by.id("textInput")).typeText(text);
      await element(by.id("addButton")).tap();
      await expect(element(by.text(text).withAncestor(by.id("toDoList")))).toBeVisible();
    })

    it("Completing ToDo Item should work!", async () => {
      const text = "a new ToDo Item";
      await element(by.id("textInput")).tap();
      await element(by.id("textInput")).typeText(text);
      await element(by.id("addButton")).tap();

      await element(by.id("completeButton")).multiTap(2);
      await expect(element(by.id("completed").and(by.text(text)).withAncestor(by.id("toDoList")))).toBeVisible();
      
    })

    it("Deleting ToDo Item should work!", async () => {
      const text = "a new ToDo Item";
      await element(by.id("textInput")).tap();
      await element(by.id("textInput")).typeText(text);
      await element(by.id("addButton")).tap();
      
      await element(by.id("deleteButton")).multiTap(2);
      await expect(element(by.text(text).withAncestor(by.id("toDoList")))).toBeNotVisible();
    })
  });
  ```

### 2) detox test (실패)

### 3) 성공할때까지 App.js에서 기능 구현


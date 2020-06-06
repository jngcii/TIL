# hit you with that DDUDU-list

## I. Installation

1. `npm install -g expo-cli`
2. `expo init DDUDU-ios`
3. `cd DDUDU-ios`
4. `expo install @react-navigation/native`
5. `expo install react-native-gesture-handler react-native-reanimated react-native-screens react-native-safe-area-context @react-native-community/masked-view`
     - 타 라이브러리와 expo간의 버전, 호환성을 위해 expo-cli를 이용해 설치하는 것을 추천
6. `yarn add @react-navigation/stack`
     - 이건 expo로 설치 못한단다.



### expo 선택 이유
- 무겁지 않은 서비스를 만들것이기 때문에 좀더 편할것 같았다.
- 배포가 편하다.
- 필요한 라이브러리중 호환이 필요한 라이브러리가 react-navigation이었는데, expo와 호환성이 좋았다.
- `@expo/vector-icons` 등 기본적인 라이브러리를 이용할 수 있다.
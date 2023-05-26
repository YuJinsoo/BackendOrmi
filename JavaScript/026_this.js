//this는 파이썬에서 self와 유사합니다.
//그렇지만 this는 예외사항이 너무 많아서
//논리적으로 이해하는 것이 거의 불가능합니다.

// this: 자기 자신을 호출한 것을 가리킵니다.
// a를 호출한 것이 window이기 때문에 this는 window를 출력합니다.
function a() {
  console.log(this);
}
a();

let myObj = {
  val1: 100,
  func1: function () {
    console.log(this);
  },
};
myObj.func1;

//
function sayName() {
  console.log(this.name);
}

var name = "Hero";
// 전역으로 선언한 name 변수의 앞에는 window 가 생략되어 있습니다.
// 때문에 window.name === "Hero" 가 성립합니다.
let peter = {
  name: "Peter Parker",
  sayName: sayName,
};

let bruce = {
  name: "Bruce Wayne",
  sayName: sayName,
};

sayName(); // window에 name이 "Hero" 로 설정되어있음
peter.sayName(); //"Peter Parker"
bruce.sayName(); // "Bruce Wayne"

// this 의 특징
function sayName() {
  console.log(this.name);
}
var name = "Hero";

let peter2 = {
  name: "Peter Parker",
  sayName: sayName,
};

let bruce2 = {
  name: "Bruce Wayne",
  sayName: peter2.sayName,
};

bruce2.sayName(); // Bruce Wayne

/*
1. 전역공간의 this는 window(node는 global) → 실제로는 window.globalThis, window.this 아닙니다.
    
    [자바스크립트에서 `globalThis`의 소름끼치는 폴리필](https://ui.toast.com/weekly-pick/ko_20190503)
    
2. 메서드로 호출한 경우 this는 멤버접근연산자 앞에 객체
3. 함수로 호출할 경우 this는 window(node는 global)
4. 화살표 함수의 경우 this는 상위스코프
5. 생성자 함수의 경우 this는 인스턴스
6. 콜백함수의 경우 this가 다르게 동작 할 수 있음

*/
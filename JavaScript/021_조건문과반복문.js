// if else if else
if (true) {
  console.log("hello");
}

if (false) {
  console.log("hello1");
} else if (false) {
  console.log("hello2");
} else if (true) {
  console.log("hello3");
} else {
  console.log("hello4");
}

//switch
if (true) console.log("중괄호 생략");

//if 로 썼을 때보다 가독성이 좋아지는 효과가 있습니다.
// 문자열도 들어갈 수 있습니다.
switch (2) {
  case 1:
    // 값1에 대한 실행 코드
    console.log(1);
    break;
  case 2:
    // 값2에 대한 실행 코드
    console.log(2);
    break;
  default:
    // 모든 case에 해당하지 않을 때 실행될 코드
    console.log("default");
    break;
}

switch (new Date().getDay()) {
  case 1:
    console.log("월요일입니다."); // document.write()
    break;
  case 2:
    console.log("화요일입니다.");
    break;
  case 3:
    console.log("수요일입니다.");
    break;
  case 4:
    console.log("목요일입니다.");
    break;
  case 5:
    console.log("금요일입니다.");
    break;
  default:
    console.log("금금요일입니다. 주말이 뭐죠?");
    break;
}

// 스위치는 점프가 아닙니다? case를 전부 읽습니다.
switch (new Date().getDay()) {
  case 1:
    console.log("월요일입니다."); // document.write()
    break;
  case 2:
    console.log("화요일입니다.");
    break;
  case 3:
    console.log("수요일입니다.");
  //   break;
  case 4:
    console.log("목요일입니다.");
    break;
  case 5:
    console.log("금요일입니다.");
    break;
  default:
    console.log("금금요일입니다. 주말이 뭐죠?");
    break;
}

switch (new Date().getDay()) {
  case 1:
  case 2:
  case 3:
  case 4:
  case 5:
    console.log("평일입니다.");
    break;
  case 6:
  case 7:
    console.log("주말입니다.");
    break;
}

//반복문
for (let i = 0; i < 10; i++) {
  console.log(i);
}
for (let i = 0; i < 10; i += 2) {
  console.log(i);
}

//무한반복
for (;;) {}

for (const key in [10, 20, 30]) {
  console.log(key); // Array는 index, Object는 key
}

for (const i of [10, 20, 30]) {
  console.log(i);
}

let x = 0;
while (x < 10) {
  console.log(x);
  //   x += 1;
  ++x;
}

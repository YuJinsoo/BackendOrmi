// 참고삼아서만 알고 있으시면 됩니다.
//https://www.freecodecamp.org/news/elegant-patterns-in-modern-javascript-roro-be01e7669cbd/
function mob(x, y, hp, mp, attack, depence, name, speed) {
  console.group(x, y, hp, mp, attack, depence, name, speed);
}

mob(10, 20, 100, 200, 100, 10, "hojun", 100); //10 20 100 200 100 10 'hojun' 100
mob((x = 10), (y = 20), 100, 200, 100, 10, "hojun", 100); //10 20 100 200 100 10 'hojun' 100
mob((y = 10), (x = 20), 100, 200, 100, 10, "hojun", 100); //10 20 100 200 100 10 'hojun' 100
// 내가 원하는 곳에서 값을 주는 것이 불가능합니다.
// 그렇기에 RORO 기법이라는 것이 생겼습니다.
// RORO :  receive and object, return an object

function mob(x = 100, y = 200, hp = 300, mp = 300) {
  console.log(x, y, hp, mp);
}

mob({ x: 200, y: 200, hp: 300, mp: 400 });

//////////

//////////

let one;
let two;
let three;

let test = { one, two, three };
test; //{one: undefined, two: undefined, three: undefined}

//파라미터                   //아규먼트
let { one, two, three } = { one: 10, two: 20, three: 30 };

// one은 변수
// one에다가 100이라는 값을 할당한 것입니다.
// object의 key와 value의 쌍으로 이뤄진 관계가 아닙니다.
// 물론 추후에 그렇게 될 것이지만요

// 변수를 먼저 선언한다음에 해야... 에러가 안나서 =가 필요합니다
let { one=100, two, three } = { two: 20, three: 30 };

// 아래 error나는 원리와 같습니다.
let { one:100, two, three } = { two: 20, three: 30 };

///////////////////

// 값을 안넣었을 때에도 잘 나오게 하는 방법
function mob({
    x = 100,
    y = 200,
    hp = 300,
    mp = 300
} = {}) {
    console.log(x, y, hp, mp)
}

mob({ x: 200, y: 200, hp: 300, mp: 400 })
mob() // 원래는 값 안넣고싶으면 mob({})


// 설명
// O
function 함수(a = 10, b = 20, c = 30) {
    return a + b + c
}
함수()

// X
function 함수({ a = 10, b = 20, c = 30 }) {
    return a + b + c
}
함수()

// O
function 함수({ a = 10, b = 20, c = 30 }) {
    return a + b + c
}
함수({}) // 이 코드를 축소한 코드가 위의 코드입니다.
// 참고삼아서만 알아두세요.
// let {one = 1, two = 2} = {one:100}
// let {one = 1, two = 2} = {}
// let {a=10, b=20, c=30} = undefined
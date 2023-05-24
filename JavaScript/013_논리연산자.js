//논리연산자 (&&, ||, !)

let x = true; // 1
let y = false; // 0

// &&는 곱
// ||는 합
// !는 부정

x && y; //false
x || y; //true
!y; // true
!x; // false

//실무에서 많이사용합니다. Boolean 변환용
!!y; // false
!!"hello";
!!NaN; // false
!!null; // false
!!undefined; // false

!![]; //true
Number.isNaN({}); // false
Number.isNaN([]); // false
// 와 object의 길이를 함께 판단하시면 됩니다.

/////
// javascript에서는 아래와 같은 단락평가를 자주 사용합니다.

null && "hello"; // null이 false이니깐 뒤에있는 'hello'를 확인하지 않음
"world" && "hello"; //'world'는 true이니깐 뒤에있는 'hello를 확인해야함 . hello를 리턴함

// 단락평가는 거의 ||를 사용합니다.
let name = "";
name = name || "이름이 입력되지 않았습니다."; // '이름이 입력되지 않았습니다.'
name; // '이름이 입력되지 않았습니다.'

// 로그인이 되어있으면 로그인 페이지를 넘겨주는 스킬
// 보통은 3항 연산자 + 단락평가로 사용합니다.
let 로그인여부 = true;
로그인페이지 = 로그인여부 && "<h1>환영합니다 고객님</h1>";
로그인페이지;

let pw = "";
pw = pw || "패스워드가 입력되지 않았습니다.";
pw;

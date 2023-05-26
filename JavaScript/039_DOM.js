// DOM 은 HTML 문서의 내용을 트리형태로 구조화하여 웹페이지와 프로그래밍 언어를 연결시켜주는 역할을 합니다.
// 이때 각각의 요소와 속성, 콘텐츠를 표현하는 단위를 '노드(node)'라고 합니다.

document.head;
document.body;
document.body.childNodes;
document.body.childNodes[1];
document.body.childNodes[1].tagName;
document.body.childNodes[1].innerText;
document.body.childNodes[1].document.body.childNodes[2]; //점만 찍어서 얼마나 많은 애트리뷰트가 있는지 확인해보세요.
document.body.childNodes[2].data;

/// DOM 트리에 접근하기

// 해당하는 Id를 가진 요소에 접근하기
document.getElementById();
// getElementById()는 tree 탐색을 사용합니다.
// 그래서 부하가 발생하기 때문에 for문 밖으로 빼주는게 최적화에 도움이 됩니다.

// 해당하는 모든 요소에 접근하기
document.getElementsByTagName();

// 해당하는 클래스를 가진 모든 요소에 접근하기
document.getElementsByClassName();

// css 선택자로 단일 요소에 접근하기
document.querySelector("selector");

// css 선택자로 여러 요소에 접근하기
document.querySelectorAll("selector");

//예제 with 040_DOM.html
const element1 = document.querySelector("#one");
element1; //<h1 id=​"one">​hello world​</h1>​
const element2 = document.querySelector("h1");
const element3 = document.querySelector(".two");
const element4 = document.querySelector("ul");

element4.childNodes;
/*
NodeList(7) [text, li.two, text, li, text, li, text]0: text1: li.two2: text3: li4: textassignedSlot: nullbaseURI: "file:///C:/Users/ABO/Desktop/BackendOrmi/JavaScript/040_DOM.html"childNodes: NodeList []data: "\n      "firstChild: nullisConnected: truelastChild: nulllength: 7nextElementSibling: linextSibling: linodeName: "#text"nodeType: 3nodeValue: "\n      "ownerDocument: documentparentElement: ulparentNode: ulpreviousElementSibling: lipreviousSibling: litextContent: "\n      "wholeText: "\n      "[[Prototype]]: Text5: li6: textlength: 7[[Prototype]]: NodeList
*/

const element5 = document.querySelector("li");
const element6 = document.querySelectorAll("li");
element6; // NodeList(3) [li.two, li, li]0: li.two1: li2: lilength: 3[[Prototype]]: NodeList
[...element6]; // (3)[(li.two, li, li)];

element6.forEach((element) => {
  element.innerText = "hello world!";
});

undefined;
element6.forEach((element, index) => {
  element.innerText = `hello world!${index}`;
});
undefined;

////
// DOM 제어 명령어
// 이벤트 삽입
// 이벤트의 타입에는 click, mouseover, mouseout, wheel 등 다양한 이벤트를 감지합니다.
// listener 함수의 인수에는 이벤트에 대한 정보가 담겨있습니다.

const myBtn = document.querySelector("button");

myBtn.addEventListener("click", function () {
  console.log("hello world");
  // myBtn.classList.remove("blue");     클래스를 제거합니다.
  // myBtn.classList.toggle("blue");     클래스를 토글합니다. 없으면 넣어주고, 있으면 제거합니다.
  // myBtn.classList.contains("blue");   해당하는 클래스가 있는지 확인합니다.
});

//
// #one 클릭하면 test 클래스 추가됨
const element_1 = document.querySelector("#one");
element1.addEventListener("click", () => {
  element1.classList.add("test"); // 클래스 제어
});

//
// 버튼 클릭하면 #one 글자색이 red toggle 됨
const btnRed = document.querySelector("button");
const title = document.querySelector("#one");
btnRed.addEventListener("click", () => {
  title.classList.toggle("red"); // 클래스 제어
});

// 요소제어
// DOM api를 이용하면 요소를 새롭게 생성하고, 위치하고, 제거할 수 있습니다.
// 1. `document.createElement(target)` : target 요소를 생성합니다.
// 2. `document.createTextNode(target)` : target 텍스트를 생성합니다.
// 3. `element.appendChild(target)` : target 요소를 element의 자식으로 위치합니다.
// 4. `element.removeChild(target)` : element의 target 자식 요소를 제거합니다.

const sectionTitle = document.createElement("h2");
sectionTitle.innerText = "hello sectiontitle";
document.querySelector("body").appendChild(sectionTitle);

//완전 생성하는 예제
const body = document.querySelector("body");
const myUl = document.createElement("ul");

for (let i = 0; i < 5; i++) {
  const myLi = document.createElement("li");
  myLi.innerText = "hello!";
  myUl.appendChild(myLi);
}

body.appendChild(myUl);

// 속성 제어하기

// 주의할 점은 JS에서 style 컨트롤하는 것은 카멜표기법 입니다.
const target = document.querySelector("p");
const txtColor = target.style.color; // 현재 스타일 정보를 가져옵니다.
target.style.color = "red"; // 현재 스타일 정보를 변경합니다.
target.style.fontWeight = "bold"; // 현재 스타일 정보에 font-weight 속성이 없다면 추가합니다.
target.style.color = null; // 현재 스타일 정보를 제거(초기화)합니다.

//
const body2 = document.querySelector("body");
const myimg = document.createElement("img");
myimg.setAttribute(
  "src",
  "https://img.wendybook.com/image_detail/img159/159599_01.jpg"
);
body2.append(myimg);

//data 속성
/*
<body>
  <h1 id="one">hello world</h1>
  <ul>
    <li class="two">one</li>
    <li>two</li>
    <li>three</li>
  </ul>
  <button>눌럿!</button>
  <img
    class="terran battle-cruiser"
    src="battle-cruiser.png"
    data-ship-id="324"
    data-weapons="laser"
    data-health="400"
    data-mana="250"
    data-skill="yamato-cannon"
  />
</body>*/
const img = document.querySelector("img");
console.log(img.dataset);
console.log(img.dataset.shipId);
console.log(img.dataset.weapons);

///////
// 이벤트 객체, 이벤트 target, currenttarget
const btn = document.createElement("button");
btn.innerText = "click!";
document.querySelector("body").append(btn);

//화살표 함수와 function으로 했을 때 this의 결과가 다릅니다.
btn.addEventListener("click", (event) => {
  console.log(event);
  console.log(event.target); // **
  console.log(event.currentTarget);
  console.log(this); // window
});
btn.addEventListener("click", function (event) {
  console.log(event);
  console.log(event.target); // **
  console.log(event.currentTarget);
  console.log(this); // button
});

//
// 캡처링과 버블링

//
// preventDefault()
// <!-- submit 의 기본 동작을 중지 -->
// <form action="">
//     <button type="submit" class="submit">제출</button>
// </form>
// <script>
//     const submit = document.querySelector('.submit');
//     submit.addEventListener('click', (event) => {
//         console.log('clicked');
//         event.preventDefault();
//     })
// </script>

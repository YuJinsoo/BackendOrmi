/// DOM 트리에 접근하기

// 해당하는 Id를 가진 요소에 접근하기
document.getElementById();
// getElementById()는 tree 탐색을 사용합니다.
// 그래서 부하가 발생하기 때문에 for문 밖으로 빼주는게 최적화에 도움이 됩니다.

// css 선택자로 단일 요소에 접근하기
document.querySelector("selector");

// css 선택자로 여러 요소에 접근하기
document.querySelectorAll("selector");

const myBtn = document.querySelector("button");

myBtn.addEventListener("click", function () {
  console.log("hello world");
  // myBtn.classList.remove("blue");     클래스를 제거합니다.
  // myBtn.classList.toggle("blue");     클래스를 토글합니다. 없으면 넣어주고, 있으면 제거합니다.
});

//요소추가
document.createElement(target); // target 요소를 생성합니다.
element.appendChild();
element.append(target);
//target 요소를 element의 자식으로 위치합니다. appendChild 와 다른점은 노드 뿐만 아니라 여러개의 노드를 한번에, 그리고 텍스트도 자식 노드로 포함시킬 수 있다는것 입니다.

//속성 제어하기
//
const body2 = document.querySelector("body");
const myimg = document.createElement("img");
myimg.setAttribute(
  "src",
  "https://img.wendybook.com/image_detail/img159/159599_01.jpg"
);
body2.append(myimg);

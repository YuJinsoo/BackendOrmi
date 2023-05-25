const 과일들 = ["사과", "파인애플", "수박"];
const 생선들 = ["조기", "갈치", "다금바리"];
const 합치면 = [...과일들, ...생선들];

console.log(합치면); //(6) ['사과', '파인애플', '수박', '조기', '갈치', '다금바리']

const 위니브1 = { 개리: 1, 빙키: 2 };
const 위니브2 = { 라이캣: 3 };
const 위니브3 = { ...위니브1, ...위니브2 };

console.log(위니브3); //{개리: 1, 빙키: 2, 라이캣: 3}

// 아래와 같이 값을 업데이트 하는 용도로도 사용합니다.
const 위니브4 = {
  ...위니브3,
  라이캣: 100,
};
console.log(위니브4); //{개리: 1, 빙키: 2, 라이캣: 100}

//
//////////// 디스트럭처링 === 언패킹

`
python 문법에서 언패킹
for i, j ,k in [(1,2,3),(4,5,6)]:
    print(i,j,k)
`;
let food1, food2, food3;

const categories = { food1: "과일", food2: "채소", food3: "육류" };

// 하나씩 빼는 법
food1 = categories.food1;
food2 = categories.food2;
food3 = categories.food3;

console.log(food1, food2, food3);

//디스트럭쳐링
//key와 변수명이 동일하게 해야 합니다
//let {food1, food2, food3} = categories;
categories = { fd1: "과일", fd2: "채소", fd3: "육류" };
let { fd1, fd2, fd3 } = categories;
console.log(fd1, fd2, fd3);

// 왼쪽이 디스트럭쳐링, 오른쪽이 객체리터럴입니다.
let { one } = { one: 1 };
console.log(one);

// 배열의 디스트럭쳐링
const arr = [1, 2, 3];
const [a, b, c] = arr;

for (const [a, b] of [
  [1, 2],
  [3, 4],
  [5, 6],
]) {
  console.log(a, b);
}

// 파이썬처럼 괄호를 없애지는 못합니다.
// for (const a, b of [[1, 2], [3, 4], [5, 6]]) {
//     console.log(a, b)
// }

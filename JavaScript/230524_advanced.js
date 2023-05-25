// 전체 product의 갯수와
// 전체 가격의 평균을 구해주세요.

// 주어진코드

fetch("http://test.api.weniv.co.kr/mall")
  .then((data) => data.json())
  .then((data) => {
    let arr = [];
    for (const i of data) {
      arr.push(i["price"]);
    }
    let avg = (arr.reduce((a, c) => a + c, 0) / data.length).toFixed(2);
    console.log(`프로덕트 개수 : ${data.length}`);
    console.log(`프로덕트 평균 가격 : ${avg}  원`);
  });

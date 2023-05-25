// 클로저
// 클로저란 폐쇠된 공간 안에 데이터에 접근하기 위한 테크닉입니다.

`
#python 에서...
def one(x):
    def two(y):
        return x**y
    return two

p2 = one(2)
p3 = one(3)

print(p2(3)) # 8
print(p3(3)) # 27
`;

function one(x) {
  function two(y) {
    return x ** y;
  }
  return two;
}

let p2 = one(2);
let p3 = one(3);

console.log(p2(3)); // 8
console.log(p3(3)); // 27

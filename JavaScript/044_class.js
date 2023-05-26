//class

//python => 대부분이 class로 되어있죠?
//javascript => calss가 ES6부터 나온 문법입니다. 원래 있던 문법이 아닙니다! 그전에는 생성자 함수로 사용했었습니다.

// 기존에 사용하던 생성자 함수와 prototype!
let myArr = new Array(1, 2, 3); //python에서 마치 클래스로 인스턴스를 만들어내듯이 찍어내는 겁니다.
let myArr2 = new Array(4, 5, 6);

myArr2.length;
myArr.length;

myArr.forEach((item) => {
  console.log(item);
});

myArr2.forEach((item) => {
  console.log(item);
});

console.dir(myArry);
// 이때 보여지는 [[prototype]] 는 무엇일까.. 여기 함수들이정의되어있음 join, pop, foreach 등등

//
function Factory() {}
function NewFactory(name) {
  this.name = name;
  this.sayYourName = function () {
    console.log(`삐리비리. 제 이름은 ${this.name}입니다. 주인님.`);
  };
}

let robot1 = new Factory();
// robot1 instanceof Factory
let robot2 = new NewFactory("브랜든2");
let robot3 = new NewFactory("브랜든3");
let robot4 = new NewFactory("브랜든4");

// 생성자 함수의 문제.
// 우리는 100개의 객체를 생성할때마다 역시 100개의 함수를 새로 만들고 있는것 입니다.  >>  자원의 낭비
// NewFactory객체를 만들 때마다 sayYourName 함수를 100개 만들고있는 것입니다.
//

// 프로토타입은 모든 인스턴스가 하나의 메서드를 공유하도록 만들어 자원을 더 효율적으로 사용하도록 도와줍니다.
function NewFactory2(name) {
  this.name = name;
}
NewFactory2.prototype.sayYourName = function () {
  console.log(`삐리비리. 제 이름은 ${this.name}입니다. 주인님.`);
};

////////////////
//객체의 상속
function Parent() {
  this.name = "재현";
}
Parent.prototype.rename = function (name) {
  this.name = name;
};
Parent.prototype.sayName = function () {
  console.log(this.name);
};

부모1 = new Parent();
부모1.name; //'재현'
부모1.rename("호준");
부모1.name; //'호준'

function Child() {
  Parent.call(this);
}

Child.prototype = Object.create(Parent.prototype);
Child.prototype.canWalk = function () {
  console.log("now i can walk!!");
};
Child.prototype.rename("호돌");
Child.prototype.sayName();

// 생성자 함수를 만들게 되면 위에서 Child가 Parent를 상속받았기 때문에
// Child가 Parent의 메서드나 멤버를 사용할 수 있습니다.
let 자식1 = new Child("호돌돌");

자식1.sayName(); //재현
자식1.rename("호돌돌");
자식1.sayName(); // 호돌돌

//
///////
//클래스
class Robot {
  // 클래스의 생성자 함수입니다. 하나의 클래스는 하나의 생성자만 정의할 수 있습니다.
  // 그리고 생성자 함수는 new 키워드가 호출될때 자동으로 실행됩니다.
  // python의 __init__() 입니다.
  constructor(name) {
    this.name = name;
  }

  // 메소드를 정의합니다. 메소드는 클래스가 생성한 인스턴스를 통해 사용할 수 있습니다.
  // 메서드 앞에 function 키워드가 없습니다.
  sayYourName() {
    console.log(`삐리비리. 제 이름은 ${this.name}입니다. 주인님.`);
  }
}

// 클래스 상속받기
class BabyRobot extends Robot {
  constructor(name) {
    super(name);
    this.ownName = "아이크";
  }

  sayBabyName() {
    // 또한 상속을 받게되면 부모 클래스의 메소드를 사용할 수 있게 됩니다. 때문에 this로 접근 할 수 있습니다.
    this.sayYourName();
    console.log("Suceeding you, Father!");
  }
}

let one = new Robot("one");
one.sayYourName(); //삐리비리. 제 이름은 one입니다. 주인님.

let two = new BabyRobot("two");
two.sayYourName(); // 삐리비리. 제 이름은 two입니다. 주인님.
two.sayBabyName(); //삐리비리. 제 이름은 two입니다. 주인님. Suceeding you, Father!

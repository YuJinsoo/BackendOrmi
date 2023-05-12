# colab 사용법

- MAC을 사용하는 경우 Ctrl 대신 Command입니다. Alt 대신 Option입니다.

1. **실행 단축키**
   1. (필수) `Ctrl(Command)` + `Enter` : 해당 셀 실행
   2. `Shift` + `Enter` : 해당 셀 실행 + 커서를 다음 셀로 이동
   3. (필수) `Alt(Option)` + `Enter` : 해당 셀 실행 + 코드 불록 하단 추가
2. **셀 삽입/삭제 관련 단축키**
   1. `Ctrl(Command)` + M A : 코드 셀 위에 삽입
   2. `Ctrl(Command)` + M B : 코드 셀 아래 삽입
   3. `Ctrl(Command)` + M D : 셀 지우기
   4. `Ctrl(Command)` + M Y : 코드 셀로 변경
   5. `Ctrl(Command)` + M M : 마크다운 셀로 변경
   6. `Ctrl(Command)` + M Z : 실행 취소
3. 수정 관련된 단축키
   1. `Ctrl(Command)` + `Alt(Option)` + 화살표위아래 : 동시 수정
   2. (자주) `Ctrl(Command)` + D : 같은 단어 찾아 동시 수정
   3. `Ctrl(Command)` + `Shift` + L : 동일 단어를 전체로 찾아 동시 수정
   4. `Alt(Option)` + `Shift` + 화살표위아래 : 해당내용을 위나 아래 복사해서 붙여넣기
   5. `Alt(Option)` + 화살표위아래 : 해당 내용을 위나 아래로 보내기
   6. (자주) `Ctrl(Command)` + `Alt(Option)` + 화살표위아래 : 위아래 동시 수정
   7. (자주) Home, End : 문장의 양 끝
   8. (필수) `Ctrl` + `/` : 주석
   9. (필수) `Shift` + `Del` : 한 줄 지우기
   10. (필수) `Tab`, `Ctrl` + `]` : 들여쓰기
   11. (필수) `Shift` + `Tab`, `Ctrl` + `[` : 내어쓰기
4. 단축키 보기 및 설정
   1. `Ctrl(Command)` + M H : 단축키 모음

# 마크다운

- 필수 마크다운

  ```
  # hello
  ## hello
  ### hello

  1. hello
  2. hello
  3. hello

  * hello
  * hello
  * hello
  ```

- 선택 마크다운(필수가 아니니 부담가지지마세요)

  ```
  # h1
  ## h2
  ### h3
  #### h4
  ##### h5
  ###### h6

  1. hello
  2. hello
  3. hello

  * hello
  * hello
  * hello

  - hello
  - hello
  - hello

  __굵게__
  **굵게**
  _기울여 쓰기_
  *기울여 쓰기*
  ~취소선~
  ~~취소선~~

  > 인용문
  [인라인 링크](https://velog.io)

  ![이미지설명](이미지링크)

  table은 markdown table generator사용해서 말들어주기
  https://www.tablesgenerator.com/markdown_tables

  체크박스 만드는 법
  * [ ] hello
  * [X] hello
  ```

# Python

```python
#행 단위 주석입니다.

"""
큰 따옴표로 세번 묶거나
작은따옴표로 세번 묶으면
열단위 주석이 됩니다.
"""

'''
큰 따옴표로 세번 묶거나
작은따옴표로 세번 묶으면
열단위 주석이 됩니다.
'''
```

    '\n큰 따옴표로 세번 묶거나\n작은따옴표로 세번 묶으면\n열단위 주석이 됩니다.\n'

```python
# 아래와 같이 열단위 주석으로 text 데이터를 넣을 수 도 있습니다.
data='''
큰 따옴표로 세번 묶거나
작은따옴표로 세번 묶으면
열단위 주석이 됩니다.
'''
data
```

    '\n큰 따옴표로 세번 묶거나\n작은따옴표로 세번 묶으면\n열단위 주석이 됩니다.\n'

- Code convention python
- https://google.github.io/styleguide/
- https://google.github.io/styleguide/pyguide.html

```python
def connect_to_next_port(self, minimum: int) -> int:
    """Connects to the next available port.

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.

    Raises:
      ConnectionError: If no available port is found.
    """
    if minimum < 1024:
        # Note that this raising of ValueError is not mentioned in the doc
        # string's "Raises:" section because it is not appropriate to
        # guarantee this specific behavioral reaction to API misuse.
        raise ValueError(f'Min. port must be at least 1024, not {minimum}.')
    port = self._find_next_open_port(minimum)
    if port is None:
        raise ConnectionError(
            f'Could not connect to service on port {minimum} or higher.')
    assert port >= minimum, (
        f'Unexpected port {port} when minimum was {minimum}.')
    return port
```

```python
connect_to_next_port
```

```python
# 띄어쓰기 4칸 (tab(실제로는 스페이스 4칸과 다릅니다), 6칸, 7칸 등 다 작동함.)
#
```

```python
# 아래와 같이 탭과 띄어쓰기 4번을 혼용하시면 error가 납니다.
for i in range(10):
    print(i)
    print('큰 따옴표로 세번 묶거나')
```

```python
a = 10     #int, 정수형
b = 10.1   #float, 실수
c = -1
d = True   #bool, 논리형(부울형, 참거짓형)
e = 'good'
f = '10'   #str, 문자열
g = 'kim'
h = 'honggildong'
i = 'example'
j = 10 + 2j #complex, 복소수
k = 0b110   #int, 2진법
l = 0o56    #int, 8진법
m = 0xAC    #int, 16진법

##########
def hello():
    return

class A:
    pass

n = hello # function
o = print # bulit-in function (https://docs.python.org/3/library/functions.html)
p = lambda x:x**2 # function
q = int # type
r = A # class
s = A() # instance
##########

print(f'type(10) : {type(a)}')
print(f'type(10.1) : {type(b)}')
print(f'type(-1) : {type(c)}')
print(f'type(True) : {type(d)}')
print(f'type(\'good\') : {type(e)}')
print(f'type(\'good\'.upper) : {type(e.upper)}')
print(f'\'10\' + \'10\' : {f + f}')
print(f'\'10\' * 3 : {f * 3}')
print(f'\'hong\' + \'gildong\' : {g + h}')
print(f'type(\'gildong\') : {type(h)}')
print(f'type(\'gildong100!!\') : {type(i)}')
print(f'type(10 + 2j) : {type(j)}')
print(f'type(0b110) : {type(k)}')
print(k)
print(f'type(0o56) : {type(i)}')
print(i)
print(f'type(0xAC) : {type(m)}')
print(m)
print(f'type(def func():...생략...) : {type(n)}')
print(f'type(print) : {type(o)}')
print(f'type(lambda x:x**2) : {type(p)}')
print(f'type(int) : {type(int)}')
```

    type(10) : <class 'int'>
    type(10.1) : <class 'float'>
    type(-1) : <class 'int'>
    type(True) : <class 'bool'>
    type('good') : <class 'str'>
    type('good'.upper) : <class 'builtin_function_or_method'>
    '10' + '10' : 1010
    '10' * 3 : 101010
    'hong' + 'gildong' : kimhonggildong
    type('gildong') : <class 'str'>
    type('gildong100!!') : <class 'str'>
    type(10 + 2j) : <class 'complex'>
    type(0b110) : <class 'int'>
    6
    type(0o56) : <class 'str'>
    example
    type(0xAC) : <class 'int'>
    172
    type(def func():...생략...) : <class 'function'>
    type(print) : <class 'builtin_function_or_method'>
    type(lambda x:x**2) : <class 'function'>
    type(int) : <class 'type'>

```python
# escape 문자 (대부분의 언어에서 공통으로 처리함)
# https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%8A%A4%EC%BC%80%EC%9D%B4%ED%94%84_%EB%AC%B8%EC%9E%90
print('hello \n world')
print('hello \t world')
print('hello \' world')
print('hello \" world')
print('hello \\ world')
```

    hello
     world
    hello 	 world
    hello ' world
    hello " world
    hello \ world

```python
# type -> string
hello = 10
print(r'hello \n world') # str -> raw 값으로 보줌. (Django 2.x까지 url parsing을 이렇게 사용함)
print(f'hello \n world {hello}') # f-string. python 3.6에서 등장. f-string을 사용하는 것을 추천함
print('hello world {}'.format(hello)) # formating
```

    hello \n world
    hello
     world 10
    hello world 10

```python
# type -> float
# 오일러의 수를 모른다 해서, 수학 연산이 약하다 해서 수업에 문제가 되지 않습니다.
print(2.3e3) # 무리수, 오일러 수(2.718에 수렴, 파이가 3.14인 것처럼)
print(2.3E3)

2.3 * (10 ** 3)
```

    2300.0
    2300.0





    2300.0

```python
print(2.3e-3) # 무리수, 오일러 수(2.718에 수렴, 파이가 3.14인 것처럼)
print(2.3E-3)

2.3 * (10 ** -3)
```

    0.0023
    0.0023





    0.0023

```python
type(2.3e-3)
```

    float

```python
class A: # 자동차 공장
    pass

a = A #class
b = A() #instance #자동차

print(type(a))
print(type(b))
```

    <class 'type'>
    <class '__main__.A'>

```python
# 변수를 처음 만나시면 type, dir을 해봅니다.
# type를 찍으면 검색 키워드를 알 수 있습니다.
# dir을 찍으면 속성을 알 수 있습니다.
type(a)
```

    int

```python
print(type(a))
```

    <class 'int'>

```python
dir(a)
```

    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__']

```python
# 실무에서 자주 사용하는 구문
type(10)
type(10) == int
type(10.1) == float
```

    True

```python
# 위만큼 자주 사용하지는 않지만 자주 사용하는 타입 확인 코드
a =10
isinstance(a, int)
isinstance(a, float)
```

    True

## 변수

```python
# CS 변수는 포스트잇
# 메모리 공간을 가리킵니다.

# x라는 포스트잇도 붙였지만
# y라는 포스트잇도 붙여져 있는 것입니다.
x = 10
y = 10

id(x), id(y) # id는 누구를 가리키고 있는지 그 주소값을 반환합니다.
```

    (140570220790288, 140570220790288)

```python
x is y
```

    True

```python
# -5 ~ 256 까지 메모리에 미리 할당해두고 사용함!
x = 257
y = 257

id(x), id(y), x is y # id는 누구를 가리키고 있는지 그 주소값을 반환합니다.
```

    (140568974617712, 140568974619248, False)

```python
# Python은 자체적으로 속도를 높이기 위한
# 여러가지 노력들을 해왔습니다.
# (아래 언급한 것 말고도 각각의 자료형에서 메모리를 효율적으로 관리하기 위한 노력들을 말씀드리겠습니다.)
# 구버전도 말씀을 드릴 것인데 이유는 여러분이 실무에가서 접할 환경이 최신 버전이 아니기 때문입니다.
# 야xx의 경우에는 Django 1.x, python 2.x를 사용하고 있어요.
# 대부분의 기업들이 한 번 구축해놓은 시스템은 바꾸기가 쉽지 않습니다.


# 그래서 -5 ~ 256은 먼저 메모리에 적재를 합니다.
```

```python
x = -5
y = -5

id(x), id(y), x is y # id는 누구를 가리키고 있는지 그 주소값을 반환합니다.
```

    (140570220789808, 140570220789808, True)

- 변수의 타입이란 무엇인가?
- 변수의 타입은 왜 있는 것일까?
- 어떤 고민을 통해 변수의 속성을 정했을까?

```python
'a' + 'a'
```

    'aa'

```python
# 왜 이어 붙였지?
# 컴퓨터 입장에서 a 는 97(인간이 보는 숫자) -> 0ㅌ61 결국 숫자!

```

```python
# cpython -> 이어 붙이라고 정의가 되어있어서!
# 사회 통념적인 약속 -> 코드로 구현
# type, dir
# 이러한 약속들은 매직메서드(__init__ ...)를 통해 구현하게 됩니다.
```

## 변수의 속성 변경

```python
'10' + '10'
```

    '1010'

```python
 # str 변수를 int로 형변환해서 더함
int('10') + int('10')
```

    20

```python
# point!!
# class가 중요한 게 아니라 이러한 '약속'을 우리가 변경할 수 있다!! 는 것이 중요함
class int(int):
    def __add__(self, a):
        return 'leehojun'

int('10') + int('10')
```

    'leehojun'

```python
class int(int):
    def __add__(self, a):
        return self * a

int('10') + int('10')
```

    100

```python
dir(10)
# __ 없는 함수는 편의기능? 이라고 생각하면 됨. 추가할수있음
```

    ['__abs__',
     '__add__',
     '__and__',
     '__bool__',
     '__ceil__',
     '__class__',
     '__delattr__',
     '__dir__',
     '__divmod__',
     '__doc__',
     '__eq__',
     '__float__',
     '__floor__',
     '__floordiv__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__index__',
     '__init__',
     '__init_subclass__',
     '__int__',
     '__invert__',
     '__le__',
     '__lshift__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__neg__',
     '__new__',
     '__or__',
     '__pos__',
     '__pow__',
     '__radd__',
     '__rand__',
     '__rdivmod__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rfloordiv__',
     '__rlshift__',
     '__rmod__',
     '__rmul__',
     '__ror__',
     '__round__',
     '__rpow__',
     '__rrshift__',
     '__rshift__',
     '__rsub__',
     '__rtruediv__',
     '__rxor__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__truediv__',
     '__trunc__',
     '__xor__',
     'as_integer_ratio',
     'bit_count',
     'bit_length',
     'conjugate',
     'denominator',
     'from_bytes',
     'imag',
     'numerator',
     'real',
     'to_bytes']

```python
class int(int):
    def 제곱(self, 승수):
        return self ** 승수

value = int('10')
print(dir(value))
```

    ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dict__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__module__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes', '제곱']

```python
value.제곱(3)
```

    1000

```python
# x -> 10 ,y -> 10, z ->10
x = 10
y = x
z = y
print(id(x), id(y), id(z))
```

    140570220790288 140570220790288 140570220790288

```python
x = 10
y = x
# x-> 10, y ->10
x =100
# x -> 100, y -> 10
print(x, y)
print(id(x), id(y))
```

    100 10
    140570220793168 140570220790288

## 변수의 속성

- 변수는 주로 스네이크 표기법을 많이 사용합니다. (물론 회사 컨벤션을 따르셔야 합니다.)
- 영문과 숫자를 사용할 수 있지만, 숫자로 시작하지는 못합니다.
- 특수문자는 사용하지 않아요.(언더바(\_)는 사용합니다. 스네이크 표기법, 특수문자나 이미중 사용 가능한 것들이 있기는 합니다. 권하지 않습니다.)
- 예약어는 사용하지 않습니다.(if, elif, while, \* for, etc)
- 대소문자는 구분합니다.
- 언더바로만 사용하거나 언더바로 시작할 수 있습니다.
- 대문자로 시작하는 변수를 사용할 수 있지만, 관습적으로 대문자로 시작하는 변수는 Class로 만들기 때문에 소문자로 시작하는 변수를 만들기를 권합니다. Class는 보통 파스칼 표기법을 따릅니다. 다만 회사 컨벤션마다 다릅니다.

```python
# 스네이크 표기법(python에서 주로)
hello_world = 10
# 카멜 표기법(JavaScript에서 주로)
helloWorld = 10
# 파스칼 표기법(Class 같은 곳에서 많이 사용합니다.)
Hello=10
```

```python
# 10hello = 100
hello10 = 100

# 특수문자도 변수명에 넣어서 사용할 수 있음
# 하지만 권장하지 않음
π = 3.14
print(π)

# _ 만은 자주 사용되는데 이렇게 사용되지 않음
_ = 100
print(_)
```

    3.14
    100

```python
for _ in range(10): # 언더바를 순회 안에서 변수로 사용하지 않을 때
    print('hello')
```

    hello
    hello
    hello
    hello
    hello
    hello
    hello
    hello
    hello
    hello

```python
# if = 100
# print = 100
# print(100)
```

## 입력과 출력

```python
x = input()
x
```

    10





    '10'

```python
x + x #사용자에게 받은 입력은 str
```

    '1010'

```python
print(10, 10, 10)
```

    10 10 10

```python
print('hello', 'world', 'hello')
```

    hello world hello

```python
print(x, x)
```

    10 10

```python
print('hello world', end='!')
print('hello world', end='!')
print('hello world', end='!')
```

    hello world!hello world!hello world!

```python
print('hello', 'world', sep='!')
print('010', '5044', '2903', sep='-') # 호준대표님 번호
```

    hello!world
    010-5044-2903

```python
이름 = '이호준'
나이 = 10
print('1. 제 이름은 이호준입니다. 제 나이는 10입니다.')
print('2. 제 이름은 ', 이름, '입니다. 제 나이는 ', 나이,'입니다.', sep='')
print('3. 제 이름은 %s입니다. 제 나이는 %d입니다.'%(이름, 나이)) # formatting 기법은 오래되기도하고... f-string으로 대체됨
print('4. 제 이름은 {}입니다. 제 나이는 {}입니다.'.format(이름, 나이)) # format 용법
print(f'5. 제 이름은 {이름}입니다. 제 나이는 {나이}입니다.') # f-string 기법
```

    1. 제 이름은 이호준입니다. 제 나이는 10입니다.
    2. 제 이름은 이호준입니다. 제 나이는 10입니다.
    3. 제 이름은 이호준입니다. 제 나이는 10입니다.
    4. 제 이름은 이호준입니다. 제 나이는 10입니다.
    5. 제 이름은 이호준입니다. 제 나이는 10입니다.

[포맷코드종류](https://www.notion.so/9fd33417740f4eba8715f5c4a1ed7c7b?v=e01ecdfe2f9448dcaad68b03a38057a5)

## formatting

```python
print(f'{100*10}')
```

    1000

```python
# 중괄호 안에서 복잡한 연산을 하는 것을 권하지 않습니다.
result = 10
print(f'{result}')
```

    10

```python
# 이런 문법은 필요에 의해 검색해서 사용하다 보면 익숙해집니다.
# 10자리로 출력하는데
print(f'{"hello":<10}') #왼쪽 정렬
print(f'{"hello":>10}') #오른쪽 정렬
print(f'{"hello":^10}') #중앙 정렬
```

    hello
         hello
      hello

```python
txt='hello'
i = 10
print(f'{txt:>10}')
print(f'{txt:>{i}}') # formatting 인자를 변수로 주는 법!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```

         hello
         hello

```python
# 이런 문법은 필요에 의해 검색해서 사용하다 보면 익숙해집니다.
# 10자리로 출력하는데
print(f'{"hello":!<10}') #왼쪽 정렬
print(f'{"hello":!>10}') #오른쪽 정렬
print(f'{"hello":!^10}') #중앙 정렬
```

    hello!!!!!
    !!!!!hello
    !!hello!!!

```python
# 이런 문법은 필요에 의해 검색해서 사용하다 보면 익숙해집니다.
# 10자리로 출력하는데
print(f'{"hello":=<10}') #왼쪽 정렬
print(f'{"hello":=>10}') #오른쪽 정렬
print(f'{"hello":=^10}') #중앙 정렬
```

    hello=====
    =====hello
    ==hello===

```python
# https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
print(f'{bin(9)[2:]:0>5}')
print(type(bin(9)))
```

    01001
    <class 'str'>

```python
bin(9|30)[2:].replace('1','#').replace('0',' ')
```

    '#####'

```python
# 실무에서 이정도로 활용을 합니다.
print(f'{"start":-^20}')
```

    -------start--------

```python
print(f'{0.12345:0.2f}') # 소수점 자리수 표현
```

    0.12

- 이 아래 코드는 필수는 아닙니다.
  학습시 참고만 부탁드립니다.

```python
# 이전 방식
print('나의 이름은 %s입니다'%('한사람'))
print('나의 이름은 "%s"입니다. 나이는 %d세이고 성별은 %s입니다.'%('한사람',33,'남성'))
print('나이는 %d세이고 성별은 %s입니다. 나의 이름은 %s입니다. '%(33,'남성','한사람'))
print('나이는 %03d세이고 신장은 %6.2f입니다. 나의 이름은 %s입니다. '%(33,56.789,'한사람'))
print('-' * 40)

# 파이썬(Python) 3 포맷팅 방식
print('나의 이름은 {}입니다'.format('한사람'))
print('나의 이름은 {0}입니다. 나이는 {1}세이고 성별은 {2}입니다.'.format('한사람',33,'남성'))
print('나이는 {1}세이고 성별은 {2}입니다. 나의 이름은 {0}입니다. '.format('한사람',33,'남성'))
print('나이는 {age}세이고 성별은 {gender}입니다. 나의 이름은 {name}입니다. '
         .format(name='한사람',age=33,gender='남성'))
print('만세삼창 :  {0}!!! {0}!!! {0}!!! '.format('만세'))
print('삼삼칠 박수 :  {0}!!! {0}!!! {1}!!! '.format('짝'*3,'짝'*7))
print('-' * 40)

# 파이썬(Python) 3.6 f-string 방식
something = '볼펜'
EA = 2
one_length = 5.343
scale = 'cm'

print(f'{something} {EA}개의 길이는 {one_length*EA}{scale} 입니다.')
print(f'{something} {EA}개의 길이는 {one_length*EA:.1f}{scale} 입니다.')
```

    나의 이름은 한사람입니다
    나의 이름은 "한사람"입니다. 나이는 33세이고 성별은 남성입니다.
    나이는 33세이고 성별은 남성입니다. 나의 이름은 한사람입니다.
    나이는 033세이고 신장은  56.79입니다. 나의 이름은 한사람입니다.
    ----------------------------------------
    나의 이름은 한사람입니다
    나의 이름은 한사람입니다. 나이는 33세이고 성별은 남성입니다.
    나이는 33세이고 성별은 남성입니다. 나의 이름은 한사람입니다.
    나이는 33세이고 성별은 남성입니다. 나의 이름은 한사람입니다.
    만세삼창 :  만세!!! 만세!!! 만세!!!
    삼삼칠 박수 :  짝짝짝!!! 짝짝짝!!! 짝짝짝짝짝짝짝!!!
    ----------------------------------------
    볼펜 2개의 길이는 10.686cm 입니다.
    볼펜 2개의 길이는 10.7cm 입니다.

```python
print('Python is [{:15}]'.format('good'))
print('Python is [{:<15}]'.format('good'))
print('Python is [{:>15}]'.format('good'))
print('Python is [{:^15}]'.format('good'))
print('당신의 나이는 [{:15}]세'.format(22))
print('당신의 나이는 [{:<15}]세'.format(22))
print('당신의 나이는 [{:>15}]세'.format(22))
print('당신의 나이는 [{:<15}]세'.format(22))
print('-' * 40)
```

    Python is [good           ]
    Python is [good           ]
    Python is [           good]
    Python is [     good      ]
    당신의 나이는 [             22]세
    당신의 나이는 [22             ]세
    당신의 나이는 [             22]세
    당신의 나이는 [22             ]세
    ----------------------------------------

```python
char_a = '5'
int_a = 5

'''기본적으로 {} 포맷팅의 특성을 그대로 가짐'''
print(1234567890)
print(f'{char_a:>5}') # >는 오른쪽정렬
print(f'{char_a:<5}') # <는 왼쪽정렬
print(f'{char_a:^5}') # ^는 가운데정렬
print(f'{int_a:0<5}')# <는 왼쪽정렬, 빈자리를 0으로 채울수도 있음
print(f'{int_a:^10.2f}') # ^ 가운데 정렬하면서 float 타입지정
```

    1234567890
        5
    5
      5
    50000
       5.00

```python
# f-string 에 \(backslash) 는 포함될 수 없다.
# \ 표현 가능안 r구문과 함께 쓸 수 없음...
print(f'{"hello":@^20}')
# print(f'{"hel\lo":@^20}') # SyntaxError: f-string expression part cannot include a backslash
print(fr'{"hello":@^20}')
# print(fr'{"hel\lo":@^20}') # SyntaxError: f-string expression part cannot include a backslash
print(r'123456\abcde\t\n\t\t\n') #backslash 표현이 됨!
```

    @@@@@@@hello@@@@@@@@
    @@@@@@@hello@@@@@@@@
    123456\abcde\t\n\t\t\n

## int

- python 에서는 숫자를 정수, 실수, 복소수로 나눠 표현합니다.
- 2진수, 8진수, 10진수, 16진수는 정수로 표현됩니다.
- overflow가 없습니다!

```python
a = 123165465499999999999999999999999999999999999999
print(type(a))
# python 2.x에서는 int 와 long 이있어서 구분해야 했지만 3.d에는 int만 있어서 아무리 큰수가 담겨도 int!

```

    <class 'int'>

```python
a = 10**100 # 구골(googol)
print(type(a))
print(a)
```

    <class 'int'>
    10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

```python
10 # 정수
-10 # 정수
10.1 # 실수

a=10
type(a)
dir(a)
```

    ['__abs__',
     '__add__',
     '__and__',
     '__bool__',
     '__ceil__',
     '__class__',
     '__delattr__',
     '__dir__',
     '__divmod__',
     '__doc__',
     '__eq__',
     '__float__',
     '__floor__',
     '__floordiv__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__index__',
     '__init__',
     '__init_subclass__',
     '__int__',
     '__invert__',
     '__le__',
     '__lshift__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__neg__',
     '__new__',
     '__or__',
     '__pos__',
     '__pow__',
     '__radd__',
     '__rand__',
     '__rdivmod__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rfloordiv__',
     '__rlshift__',
     '__rmod__',
     '__rmul__',
     '__ror__',
     '__round__',
     '__rpow__',
     '__rrshift__',
     '__rshift__',
     '__rsub__',
     '__rtruediv__',
     '__rxor__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__truediv__',
     '__trunc__',
     '__xor__',
     'as_integer_ratio',
     'bit_count',
     'bit_length',
     'conjugate',
     'denominator',
     'from_bytes',
     'imag',
     'numerator',
     'real',
     'to_bytes']

```python
 'bit_length' # bit로 바꾸었을 때 bit의 길이
 'to_bytes' # pc에서 저장하는 바이트의 형태로 숫자를 표현
```

```python
# 1Bit, 0 ~ 1 # bit - 1자리
# 1Bytes = 8bit, 00000000 ~ 11111111 # 1byte - 8bit
# 1KB (키로바이트) = 1024Bytes
# 1MB (메가바이트) = 1024KB
# 1GB (기가바이트) = 1024MB
# 1TB (테라바이트) = 1024GB
# 1PB (페타바이트) = 1024TB
```

```python
(9).bit_length() #1001
```

    4

```python
# 컴퓨터가 숫자를 어떻게 저장하는가?
# --> 컴퓨터는 음수를 자체적으로 표현할 수 없기에 2의 보수를 사용합니다.
# 1의 보수를 사용하게 되면 +0과 -0이 존재하게 됨으로 비트 하나를 낭비하게 됩니다.
# 따라서 2의 보수를 사용합니다.

(2).to_bytes(1, byteorder='little', signed=True)
(1).to_bytes(1, byteorder='little', signed=True)
(0).to_bytes(1, byteorder='little', signed=True)
(-1).to_bytes(1, byteorder='little', signed=True)
(-2).to_bytes(1, byteorder='little', signed=True)


```

    b'\xfe'

```python
# 0000 0001 # 1
# 1111 1110 # 1의 1의보수
# 1111 1111 # 1의 2의보수 => 0xff
```

```python
# 진법 변환 쉽게 하는 법 : 가장 가까운 승수를 찾아 더하거나 뺌
# 10 진법
# 0 1 2 3 4 5 6 7 8 9 -> 10 12 13
# 1324 = 1*10^3 + 3*10^2 + 2*10^1 + 4*10^0

# 2진법
# 0 1 -> 10 11
# 1001 = 1*2^3 + 0*2^2 + 0*2^1 + 1*2^0

# 8진법
# 0 1 2 3 4 5 6 7 -> 10

# 16진법
# 0 1 2 3 4 5 6 7 8 9 a b c e d f -> 10
```

```python
# color의 표현
# 2596be
# 000000 ~ ffff
# ff는 10진수로 무슨 숫자를 의미?
# 100 - 1 => ff-1이 됨
```

```python
a = 10
type(a)
```

    int

```python
int('10') + int('10')
```

    20

```python
int('10', 2) # 2진법으로 10
```

    2

```python
int('10', 8) # 8진법으로 10
```

    8

```python
int('10', 16) # 16지넙으로 10
```

    16

```python
print(0b110) # 바이너리
print(0o110) # 옥타
print(0x110) # 헥사
```

    6
    72
    272

```python
a = 10
type(a) == int
isinstance(a, int)
```

    True

## float(실수)

```python
a = 10.1
type(a)
```

    float

```python
dir(a)
```

    ['__abs__',
     '__add__',
     '__bool__',
     '__ceil__',
     '__class__',
     '__delattr__',
     '__dir__',
     '__divmod__',
     '__doc__',
     '__eq__',
     '__float__',
     '__floor__',
     '__floordiv__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getformat__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__int__',
     '__le__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__neg__',
     '__new__',
     '__pos__',
     '__pow__',
     '__radd__',
     '__rdivmod__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rfloordiv__',
     '__rmod__',
     '__rmul__',
     '__round__',
     '__rpow__',
     '__rsub__',
     '__rtruediv__',
     '__setattr__',
     '__setformat__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__truediv__',
     '__trunc__',
     'as_integer_ratio',
     'conjugate',
     'fromhex',
     'hex',
     'imag',
     'is_integer',
     'real']

```python
a = 10
b = 10.1

a+b # 다른 일부 언어에서는 허용되지 않습니다
```

    20.1

```python
# 부동소수점 오차(2진법으로 0.1이 무한대수가 발생합니다.)
0.1+0.2 # 대부분의 언어 공통입니다.
```

    0.30000000000000004

```python
a = 0.1
```

```python
# 20번 반복해보세요
a = a + 0.1
a
```

    1.0999999999999999

- [python 부동소수점 처리](https://docs.python.org/ko/3/tutorial/floatingpoint.html)
- https://0.30000000000000004.com/ 에서 언어별 해결책을 제시함
- 컴퓨터에서 부동소수점 숫자는 2진 분수로 표현되기에 무한대수가 발생한다.(무한히 반복하는 소수처럼...)
- 부동소수 표현은 **IEEE-754**로 표기되기로 약속되어있음
- [무한대수가 발생되는 원리](https://www.notion.so/paullabworkspace/5f34f21bf9a34015b170e7afd7da9593)

```python
# 왜 빈문자 개수를 찾았는데 6이 나올까?
'hello'.count('')
```

    6

## !! 오늘 배운 것 정리 230501

1. 단축키

   - (필수) Ctrl(Command) + Enter : 해당 셀 실행
   - (필수) Alt(Option) + Enter : 해당 셀 실행 + 코드 불록 하단 추가
   - (필수) Ctrl + / : 주석
   - (필수) Shift + Del : 한 줄 지우기
   - (필수) Tab, Ctrl + ] : 들여쓰기
   - (필수) Shift + Tab, Ctrl + [ : 내어쓰기

2. 마크다운

   ```
   # hello
   ## hello
   ### hello

   1. hello
   2. hello
   3. hello

   * hello
   * hello
   * hello
   ```

3. 주석

   ```python
   #행 단위 주석입니다.

   """
   큰 따옴표로 세번 묶거나
   작은따옴표로 세번 묶으면
   열단위 주석이 됩니다.
   """

   '''
   큰 따옴표로 세번 묶거나
   작은따옴표로 세번 묶으면
   열단위 주석이 됩니다.
   '''
   ```

4. PEP8 권고사항

   - 띄어쓰기는 4칸
   - 한 줄에 79자 이상을 사용하지 않는다.

5. 형의 종류(type, dir)

   - 컨벤션 자료형(list, tuple, dict, set)은 나중에 진행합니다.
   - int
   - float
   - bool
   - str
   - function
   - bulit-in function

6. 이스케이프 문자

   - https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%8A%A4%EC%BC%80%EC%9D%B4%ED%94%84_%EB%AC%B8%EC%9E%90

   ```python
   print('hello \n world')
   print('hello \t world')
   print('hello \' world')
   print('hello \" world')
   print('hello \\ world')
   ```

7. 실무에서 자주 사용하는 타입확인 구문

   ```python
   type(10)
   type(10) == int
   type(10.1) == float

   a = 10
   isinstance(a, int)
   isinstance(a, float)
   ```

8. 변수의 인사이트

   ```
   dir을 입력했을 때
   1. __hello__와 같은 형태의 메직 메서드는 속성을 표현한다
   2.  언더바가 없는 메서드는 해당 자료형의 편의 기능을 제공한다
   ```

9. 입력과 출력

   ```python
   x = input() #입력, 숫자를 입력해도 str
   print(x) #출력

   이름 = '이호준'
   나이 = 10
   print(f'제 이름은 {이름}입니다. 제 나이는 {나이}입니다.')
   print(f'{100 * 10}')
   ```

10. int 형

    - 2진수, 8진수, 16진수는 정수

11. float 형
    - 부동소수점 오차(2진법으로 변환했을 때 0.1이 무한대수가 발생합니다.)
      0.1 + 0.2 # 대부분의 언어 공통입니다.
    - https://docs.python.org/ko/3/tutorial/floatingpoint.html
    - https://0.30000000000000004.com/ 에서 언어별 해결책을 제시한다.

## str(문자열)

- 순서가 있는 **시퀀스 자료형**입니다.
- 작은 따옴표(' ')나 큰 따옴표(" "), 삼중따옴표('''str''', """str""")로 감싸는 것도 가능합니다. (삼중따옴표를 사용할 경우에는 줄단위의 문자열을 나타낼 수 있습니다.)
- 작은 따옴표 안에 큰 따옴표, 큰 따옴표 안에 작은 따옴표 사용이 가능합니다.
- 이스케이프 문자도 사용이 가능합니다.
- 리스트, 튜플도 시퀀스 자료형입니다.

```python
s ='paullab CEO leehojun'
s[0] # 0은 index입니다. 이렇게 호출하는 것을 indexing 이라고 합니다.
```

    'p'

```python
type(s)
```

    str

```python
dir(s)
```

    ['__add__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rmod__',
     '__rmul__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'capitalize',
     'casefold',
     'center',
     'count',
     'encode',
     'endswith',
     'expandtabs',
     'find',
     'format',
     'format_map',
     'index',
     'isalnum',
     'isalpha',
     'isascii',
     'isdecimal',
     'isdigit',
     'isidentifier',
     'islower',
     'isnumeric',
     'isprintable',
     'isspace',
     'istitle',
     'isupper',
     'join',
     'ljust',
     'lower',
     'lstrip',
     'maketrans',
     'partition',
     'removeprefix',
     'removesuffix',
     'replace',
     'rfind',
     'rindex',
     'rjust',
     'rpartition',
     'rsplit',
     'rstrip',
     'split',
     'splitlines',
     'startswith',
     'strip',
     'swapcase',
     'title',
     'translate',
     'upper',
     'zfill']

```python
# 문자열의 메서드
# 'capitalize','casefold','center','count','encode',
# 'endswith','expandtabs','find','format','format_map',
# 'index','isalnum','isalpha','isascii','isdecimal','isdigit',
# 'isidentifier','islower','isnumeric','isprintable','isspace',
# 'istitle','isupper','join','ljust','lower','lstrip',
# 'maketrans','partition','removeprefix','removesuffix',
# 'replace','rfind','rindex','rjust','rpartition','rsplit',
# 'rstrip','split','splitlines','startswith','strip','swapcase',
# 'title','translate','upper','zfill'
```

```python
s = 'paullab CEO leehojun'
s.lower(), s.upper()
# 특히 사용자에게 입력을 받는 경우 lower도 많이 사용합니다.
```

    ('paullab ceo leehojun', 'PAULLAB CEO LEEHOJUN')

```python
s = 'paullab CEO leehojun'
s.find('C'), s.index('C')
```

    (8, 8)

```python
# 견고한 코드란?
# 시간이 지나도 그대로 사용할 수 있고
# error가 예측 가능하게 나는 코드.
# 네이버에 이미지 슬라이딩 코드
# s.find('Z') => -1은 True이기 때문에 주의가 필요함
s.find('Z')
```

    -1

```python
# Error가 나면 Error를 주는 것이 좋을 수 있습니다.
# Error를 안주는 언어로 JavaScript.
# 에러처리를 할 거면 에러 주는 것을 사용하면 됨
s.index('Z')
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-8-b727d3398a36> in <cell line: 1>()
    ----> 1 s.index('Z')


    ValueError: substring not found

```python
s = 'paullab CEO leehojun'
s.find('CEO')
```

    8

```python
# .count() 함수 : 문자열이나 숫자를 셀 때 사용 (중요도 *****)
s = 'paullab CEO leehojun'
s.count('l')
```

```python
str([1, 2, 3, 4, 5])
```

    '[1, 2, 3, 4, 5]'

```python
str([1, 2, 3, 4, 5]).count(' ')
```

    4

```python
str([1, 2, 3, 4, 5]).count(',')
```

    4

```python
# 이런 유형의 문제를 많이 풀 것임.
str([1, 2, 11, 4, 111]).count('1')
```

    6

```python
# 윗줄과 같은 원리
str(list(range(0,10001))).count('8')
```

    4000

- https://codingdojang.com/scode/393?answer_mode=hide

```python
str([1,
     2,
     3,
     4,
     5]).count(' ')
#list는 콤마 다음에 공백이 없더라도 공백으로 인식, enter가 있어도 공백 1개로 인식 합니다.
# 원소 사이에 enter 없어도 4가 나옴
```

    4

```python
'hello'.count('')  # 문자 사이에 빈문자가 들어가있는 건가??
```

    6

```python
'a'.count('')
```

    2

```python
''.count('')
```

    1

```python
# 빈 문자열 + 빈문자열 = 빈문자열 이기 때문에 1개로 셈
'' + ''
```

    ''

```python
# 공백 제거. strip, rstrip, lstrip, relpace
'   hello   !  '.strip()
```

    'hello   !'

```python
'   hello   !  '.rstrip(), '   hello   !  '.lstrip()
```

    ('   hello   !', 'hello   !  ')

```python
# replace (중요도 *****)
'hello world hi'.replace(' ', '!')
'hello world hi'.replace('world', 'W@O@R@L@D').upper()
```

    'HELLO W@O@R@L@D HI'

```python
# 메서드 채이닝 : 메서드를 연속으로 호출
'hello world hi'.replace('world', 'W@O@R@L@D').upper().split('@')
# split()의 반환값은 list() 이기 때문에 메서드 채이닝을 하려면
# split 이후로는 list 메서드를 사용해야 함
```

    ['HELLO W', 'O', 'R', 'L', 'D HI']

```python
'hello world hi'.replace(' ', '') # 공백 제거!
```

    'helloworldhi'

```python
data = '''  "+ +-+ -+-"
  "++ -- +-+"
  "++-+ -+ -"
  "+ ++-+ -+"  '''
data.split('\n')[0].replace(' ','').replace('"','')

# Pythonic 하지 않다!
data.split('\n')[0].replace(' ',
                '').replace('"',
                '')

# Pythonic 하게! \ 붙여주면 다음줄에 이어서 됨.
data.split('\n')[0]\
                .replace(' ','')\
                .replace('"','')\
                .replace('"','')\
                .replace('"','')\
                .replace('"','')\

# 강사님 기법
processed_string = data.split('\n')[0].replace(' ','').replace('"','')
processed_string.replace('"','').replace('"','')

```

    '++-+-+-'

```python
# 영어 79자
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 79자
# 한글 39자
# 아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아 39자
```

```python
data = '''  "+ +-+ -+-"
  "++ -- +-+"
  "++-+ -+ -"
  "+ ++-+ -+"  '''
data.split('\n')[0].replace(' ','').replace('"','').replace('+','1').replace('-','0')

ord('A'), chr(65) # ord는 문자를 가지고 숫자로 변경. chr은 숫자를 문자로 변경합니다.

# ASCII code
# A : 65 a :97
# 대문자는 65~90 인데 소문자가 91부터 이어지지 않음! <<<< 유의해야 함!!!!!!!!!

num1 = data.split('\n')[0].replace(' ','').replace('"','').replace('+','1').replace('-','0')
num2 = data.split('\n')[1].replace(' ','').replace('"','').replace('+','1').replace('-','0')
num3 = data.split('\n')[2].replace(' ','').replace('"','').replace('+','1').replace('-','0')
num4 = data.split('\n')[3].replace(' ','').replace('"','').replace('+','1').replace('-','0')
int (num1, 2)
chr(int(num1, 2)), chr(int(num2, 2)), chr(int(num3, 2)),chr(int(num4, 2))
```

    ('j', 'e', 'j', 'u')

```python
# split (중요도 **** .)
'paullab CEO leehojun'.split(' ') #문자열을 쪼개어 줍니다.
'paullab!CEO!leehojun'.split('!')
'paullab,CEO,leehojun'.split(',')
```

    ['paullab', 'CEO', 'leehojun']

```python
# 퀴즈
'010 5044 2903'.split(' ')
'010-5044-2903'.split('-')
'010 5044-2903'.replace(' ','-').split('-')

# map
list(map(int,'010 5044 2903'.split(' ')))
list(map(int,'010-5044-2903'.split('-')))
list(map(int,'010 5044-2903'.replace(' ','-').split('-')))

# list comprehension ( list의 append 사용하는 것 보다 빠름 )
ls= '010 5044 2903'.split(' ')
[int(i) for i in ls]

# map, list comprehension 둘 다 새로운 list를 생성함. 원본 변경은 없음
```

    [10, 5044, 2903]

```python
# 원하는 결과값
# ['010', '5044','2903']
# [10,5044,2904]  # 010 은표현이 안되서 10 으로 해주세요
```

```python
# 강사님풀이
'010 5044 2903'.split() #공백단위가 들어가게 됩니다.
```

    ['010', '5044', '2903']

```python
# 지금 진도에서 과한 풀이방법... 뒤에서 상세하게 다룸!
def 제곱함수(x):
    return x ** 2

def 정수함수(x):
    return int(x)

list(map(제곱함수, [1, 2, 3]))
list(map(정수함수, ['1', '2', '3']))
list(map(int, ['1', '2', '3']))

list(map(int, ['010', '5044', '2903']))
list(map(int,'010 5044 2903'.split(' ')))
```

```python
# join 별 4.5개
'~'.join(['hello', 'world', 'hello'])
'!'.join(['hello', 'world', 'hello'])
''.join(['hello', 'world', 'hello']) # 자주 사용
' '.join(['hello', 'world', 'hello']) # 자주 사용
```

    'hello world hello'

```python
#  isalnum( ) / isalpha( ) / isascii( )
'hello'.isalpha() # 알파벳인지 확인함
```

    False

```python
'hel lo'.isalpha() # 띄어쓰기까지 알파벳인지 확인함 (띄어쓰기는 알파벳 아니라 false)
```

```python
'123'.isdigit() # 숫자인 문자인지 확인
```

    True

```python
'12a3'.isdigit(), '12 3'.isdigit()
```

    (False, False)

```python
'12a3'.isalnum(), '12 3'.isalnum()
```

    (True, False)

```python
'안녕하세요!'.isalpha(), '안녕하세요!'.isalnum()
```

    (False, False)

```python
#아스키코드인지 아닌지 판단해줍니다.
'paullab CEO leehojun'.isascii(), '123'.isascii()
```

    (True, True)

```python
# 퀴즈
# 문자열에 있는 모든 숫자를 더해주세요
answer = 0
for i in '123abc913sldlf':
    if i.isdigit():
        answer += int(i)
answer
```

    19

```python
# rjust( ) / ljust( ) / center( ) format용법으로 거의 커버가 되긴 함...
print('paullab CEO leehojun'.rjust(30)) #오른쪽 정렬
print('paullab CEO leehojun'.ljust(30)) #왼쪽 정렬
print('paullab CEO leehojun'.center(30))#가운데 정렬
```

              paullab CEO leehojun
    paullab CEO leehojun
         paullab CEO leehojun

```python
# zfill()
# 빈 공간을 문자 0으로 채워주는 함수
'hello'.zfill(20)
```

    '000000000000000hello'

```python
# 2진수 표현에 자주 사용함
'1001'.zfill(8)
```

    '00001001'

```python
'hello'.zfill(10).replace('0', '-')
```

    '-----hello'

```python
# translate()
# 규칙 테이블이며 규칙을 정해 데이터를 정렬해줌
규칙테이블 = str.maketrans({'\n':'', '\t':''})  # replace랑 똑같은것...임
'paullab \n\n\n CEO \t\t\t leehojun'.translate(규칙테이블)
# 같은 결과 replace로...
# 'paullab \n\n\n CEO \t\t\t leehojun'.replace('\n', '').replace('\t', '')
```

    'paullab  CEO  leehojun'

```python
# str.maketrans에서 규칙을 정할 때 똑같은 길이를 가지고 있어야 함
규칙테이블 = str.maketrans('\n\t', '  ')  # \n -> ' ' , \t -> ' '
'paullab \n\n\n CEO \t\t\t leehojun'.translate(규칙테이블)
```

    'paullab     CEO     leehojun'

```python
규칙테이블 = str.maketrans('le', '12')
'lehojun leeesnaghuck hahah'.translate(규칙테이블)
```

    '12hojun 1222snaghuck hahah'

## pep

```python
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa => 80자
# 아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아 => 42자면 한글 넘어갑니다.
# line에 딱 맞춰 들어간 것을 볼 수 있습니다.
# 강제사항은 아닙니다.
# 띄어쓰기 4번도 강제사항은 아닙니다.
# pep8, pep 20에 기술되어 있습니다. => pep(Python Enhancement Proposal)란 무엇인가요? 8이란 무엇인가요?
# pep8 : Style Guide for Python Code (https://peps.python.org/pep-0008/)
# pep20 : The Zen of Python (https://peps.python.org/pep-0020/) #이스터에그로 숨겨져 있습니다!
# https://peps.python.org/
import this
```

    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

## cpython

- 공식 홈페이지에서 python 다운로드 받는 것이 cpython입니다.
- https://github.com/python/cpython
- list를 구현한 코드 : https://github.com/python/cpython/blob/main/Objects/listobject.c

## 인덱싱과 슬라이싱

```python
name = 'Guido van Rossum'
print(name[0])
print(name[1])
print(name[2])
```

    G
    u
    i

```python
# s[start:stop:step]
s = 'paullab CEO leehojun'
s[5:]   # 5번째 부터 끝까지
s[:5]   # 처음부터 5번째까지 (index 4 까지)
s[3:10]
s[:]    # 처음부터 끝까지
s[0:20:2]
```

    'pulbCOleou'

```python
# 자주 사용되는 인덱싱 슬라이싱 코드
s = 'paullab CEO leehojun!'
s[:]    # string에서는 많이 사용하지 않지만 list에서 많이 사용합니다. (복사때문에...?)
s[:-1]  # 마지막 원소만 제외하고 다 슬라이싱 합니다.
```

    'paullab CEO leehojun'

```python
test = [1, 2, 3, 4]
test2 = test # 복사가 일어남
test2[0] = 1000
test, test2 ## 값이 둘 다 바뀜.
```

    ([1000, 2, 3, 4], [1000, 2, 3, 4])

```python
test = [1, 2, 3, 4]
test2 = test[:] # 새로운 리스트를 만들어서 test2에게 줌
test2[0] = 1000
test, test2 ## 값이서로 다름 test2만 바뀜
```

    ([1, 2, 3, 4], [1000, 2, 3, 4])

## 문자열의 연산

```python
s = 'hello world'
dir(s)

s + s
s*3
# s/s, s**s, s-s 는 ERROR
```

    'hello worldhello worldhello world'

## 형변환

- 형변환 : type을 변경하는 것입니다.

### 형변환 int float

```python
x = int(input())
x + x # but 알파벳 입력하면 error!
```

    10



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-100-449880225891> in <cell line: 2>()
          1 x = int(input())
    ----> 2 if x.isdigit():
          3     x = int(x)
          4 x + x # but 알파벳 입력하면 error!


    AttributeError: 'int' object has no attribute 'isdigit'

```python
x = input()
if x.isdigit():
    x = int(x) # but 알파벳 입력하면 error!
x + x
```

    10





    20

```python
# int('abc') #error
int(10.1) #버림
int('10') #형변환 가능
# int('10.1') #형변환 불가능
```

    10

```python
# float('abc') #error
float(10.1) #버림
float('10') #형변환 가능
float('10.1') #형변환 가능
```

    10.1

```python
int('10a')  # 되는 언어가 있어서 보여드림 ex) JavaScript
# python 에서는 허용하지 않습니다.
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-108-2b848668e0ee> in <cell line: 1>()
    ----> 1 int('10a')  # 되는 언어가 있어서 보여드림
          2 # python 에서는 허용하지 않습니다.


    ValueError: invalid literal for int() with base 10: '10a'

### 형변환 string

```python
def hello():
    pass

str(123)
str(True)
str(None)
str(type)

str(hello)  # <function hello at 0x~~~~>
str([1,2,3])
str((1,2,3))
str({1,2,3})
str({'one':1, 'two':2})
```

    "{'one': 1, 'two': 2}"

### 형변환 bool

```python
# ***** 별 다섯 개!
if True:
    print('hi')

if 'hello':
    print('hi')

# 문자열이 빈문자열 아니면 모두 True
print(bool(''))
print(bool('a'))
print(bool('False'))
print(bool('True'))
# 숫자는 0만 False, 나머지는 True
print(bool(0))
print(bool(-1))
print(bool(124))
print(bool(100.1))
print(bool(None) ) # None은 비어있음을 명시해주는 키워드. False

# 컨벤션 자료형은 비어있으면 False입니다.
print(bool([]))
print(bool({}))
print(bool([1]))

```

    hi
    hi
    False
    True
    True
    True
    False
    True
    True
    True
    False
    False
    False
    True

```python
# python 에서는 컨벤션이 비어있으면 False이기 때문에 이용하는 방법!?
# >> javascript는 안그럼..
ls = [1,2,3]
while ls:
    print(ls.pop())
```

    3
    2
    1

```python
# list로 형변환
s = '10'
l = list(s)
l
```

    ['1', '0']

```python
s = 'leehojun'
l = list(s)
l
```

    ['l', 'e', 'e', 'h', 'o', 'j', 'u', 'n']

```python
# tuple로 형변환
s = '10'
t = tuple(s)
t
```

    ('1', '0')

```python
s = 'leehojun'
t = tuple(s)
t
```

    ('l', 'e', 'e', 'h', 'o', 'j', 'u', 'n')

```python
# dictionary 로 형변환
# name = 'leehoun'
# dict(name) # 단순 문자만 넣으면 error

s = [('name', 'leehojun'), ('age', 10)]
d = dict(s)
d
```

    {'name': 'leehojun', 'age': 10}

```python
# set 으로 형변환
# set은 순서를 보장하지 않고, 중복된 원소를 제외함
name = 'leehojun'
set(name)
```

    {'e', 'h', 'j', 'l', 'n', 'o', 'u'}

```python
# len() 함수는 __len__
len('hello world')
len([1,2,3,4])
len({1,2,3})
```

    3

```python

```

```python
#연습문제 2번
def function(input):
    return input*2

user_input = input('문자를 입력해 주세요: ')
function(user_input)

# print(input('문자를입력해주세!: ')*2 # 이렇게도 똑같음
```

    문자를 입력해 주세요abc





    'abcabc'

```python
#연습문제 3번
num = 1234567890
list(str(num))[3]

```

    '4'

## 산술연산

```python
a =10
b=3
print(f'10 + 3 == {a + b}')
print(f'10 - 3 == {a - b}')
print(f'10 / 3 == {a / b}')
print(f'10 // 3 == {a // b}')   # 몫만 나옵니다.(정수)
print(f'10 * 3 == {a * b}')
print(f'10 ** 3 == {a ** b}')
print(f'10 % 3 == {a % b}')     # 나머지
```

    10 + 3 == 13
    10 - 3 == 7
    10 / 3 == 3.3333333333333335
    10 // 3 == 3
    10 * 3 == 30
    10 ** 3 == 1000
    10 % 3 == 1

```python
# 연산자 우선순위
# and, or, 4칙연산, 제곱정도만 알면 코딩하는데 큰 무리가 없음.
# 모르면 읽는데 어려움이 생기기도 함...
# 헷갈릴 때에는 괄호 씌워서 하기!!
# point
# ** > *
# and > or
print(3 ** 2 * 3)
print(3 * 3 ** 2)   # 연산자 우선순위 ** > * 이기 때문에 3 ** 2 를 먼저함
print(3 + 3 * 2)

#
```

    27
    27
    9

## 비교연산

```python
# 비교연산자
a =10
b=3

print(f'10 > 3 == {a > b}')
print(f'10 >= 3 == {a >= b}')
print(f'10 < 3 == {a < b}')
print(f'10 <= 3 == {a <= b}')
print(f'10 == 3 == {a == b}')
print(f'10 != 3 == {a != b}')
```

## 논리연산

- or 과 and 연산의 경우 마지막 단락평가한 값을 return 한다. <br/>(return 이 True, False로 고정된 것이 아님)
  - x or y 일 때, x == True 이면 return x 아니면 return y
  - x and y 일 때, x == True 이면 return y 아니면 return x

```python
from google.colab import drive
drive.mount('/content/drive')
```

```python
# and 는 곱
# or 는 합
# not 은 반대
# True 1
# False 0
# 중요한 포인트는 저렇게 쓸 때, 언제 True가 되는지 정리하는 것

print(True and False)
print(True or False)

if True and False:
    print('hello and')

if 10>3 and 8%3==0:
    print('world and')

if True or False:
    print('hello or')

if 10>3 or 8%3==0:
    print('world or')

# and는 언제 True가 되나요?
# --> 모두 True 일 때
# or는 언제 True가 되나요?
# --> 하나라도 True 일 때
```

    False
    True
    hello or
    world or

```python
# 문제 링크 : https://codingdojang.com/scode/350?answer_mode=hide
answer = 0
for i in range(101):
    if i % 3 == 0 or i % 5 == 0:  ## 3과 5의 공배수를 찾고싶으면 and!
        answer += i

answer # 2418
```

    2418

```python
# and or를 안 쓰면...
result = 0
for i in range(101):
    if i % 3 == 0:
        result += i
        continue
    if i % 5 == 0:
        result += i

result
```

    2418

```python
not True
```

    False

```python
not False
```

    True

```python
# python 입장에서 보는 코드
# False and ??? => 물음표에 무엇이 나오든 False
# 그래서 Python도 저 풀음표를 해석하지 않습니다.

def solution():
    1/0 # ZeroDivisionError


if False and solution():
    print('solution must be error')
# 무조건 결말이 결정되어 있는 코드는 뒤에있는 나머지 코드를 해석하지 않음!!
```

```python
def solution():
    1/0 # ZeroDivisionError


if True or solution():
    print('solution must be error')
# 무조건 결말이 결정되어 있는 코드는 뒤에있는 나머지 코드를 해석하지 않음!!
```

    solution must be error

```python
# 단락 평가 (컴퓨터가 어디까지 보는지 판단해서 활용)
username='' # 사용자가 아무것도 입력하지 않았을 경우
username = username or 'licat'
username
```

    'licat'

```python
username='leehojun' # 사용자가 아무것도 입력하지 않았을 경우
print(username or 'licat') ## < 이게 왜 username 혹은 'licat'이 출력되는거죠??
username = username or 'licat'
username
```

    leehojun





    'leehojun'

```python
# and 와 ro의 우선순위 ( and > or)
for i in range(21):
    if i % 3 == 0 and i % 5 == 0 or i % 2 == 0:
        print(i)

for i in range(21):
    if (i % 3 == 0 and i % 5 == 0) or i % 2 == 0:
        print(i)
```

    0
    2
    4
    6
    8
    10
    12
    14
    15
    16
    18
    20
    0
    2
    4
    6
    8
    10
    12
    14
    15
    16
    18
    20

```python
# 아래는 출력값이 다릅니다. 우선순위가 낮은 or가 먼저 나왔기 때문입니다.
# 헷갈리시면 괄호를 사용해주세요!
for i in range(21):
    if (i % 3 == 0 or i % 5 == 0) and i % 2 == 0:
        print(i)

for i in range(21):
    if i % 3 == 0 or i % 5 == 0 and i % 2 == 0:
        print(i)
```

    0
    6
    10
    12
    18
    20
    0
    3
    6
    9
    10
    12
    15
    18
    20

## 비트연산 (중요도 하)

```python
# & (곱하기)
# 1001 == 9
# 0010 == 2
# ----
# 0000
```

    False

```python
9&8
```

    8

```python
# | (더하기, 대신 자리 올림이 되진 않습니다.)
# 1001 == 9
# 0011 == 3
# ----
# 1011

9|3
```

    11

```python
# ^ (XOR exclusive-or : 같으면 0 다르면 1)
# 1001 == 9
# 0011 == 3
# ----
# 1010

9^3
```

    10

```python
# ~ (not 연산자)
print(~9) # 2의 보수를 취함(9에게 +1 한 다음에 -를 취하면 됨)
print(~-7)
print(~0)
```

    -10
    6
    -1

```python
# << >> (shift 비트 이동 연산자)
3 << 2
# 0011 == 3
# 1100 == 3 << 2

```

    0

```python
7 >> 2
# 0111 == 7 >> 2
```

    1

## 디스코드 단축키

- :ok

## 할당연산

```python
# a = 10
# a = a + 10
a =  + 10 # 위 식에서 a를 지우면, 양수를 표현하는 10 만남아서, a 에 10 대입
a
```

    10

```python
a = 10
a += 10
a
```

    20

```python
a = 10
a //= 10 # = 앞에 산술연산 모두 가능
a
```

    1

```python
# Python에서 특이하게 증감연산자 (++a, a++, --a, a--) 가 없습니다.
```

## 식별연산자

```python
# 앞으로 아래 2개 함수를 활용해서 Python에 컨벤션 자료형이
# 어떻게 구성되어있는지 확인해볼겁니다.
# id()
# is()
```

```python
a = 250
b = 250
print(id(a), id(b))
a is b # id가 같은지 확인하는?
```

    139979164213264 139979164213264





    True

```python
a = [1,2,3]
b = [1,2,3]
print(id(a), id(b))
a is b
```

    139977916699776 139977914682624





    False

```python
a[0] = 100
a, b
```

    ([100, 2, 3], [1, 2, 3])

```python
a = [1,2,3]
b = [1,2,3]
a == b  # Python에서 등호(==)는 type과 value를 봅니다.
# javascript에서 ==는 type과 id를 봐서 false가 나옴
```

    True

```python
# is 연산자는 id를 비교합니다.
id(a) == id(b) # 이게 False 면 is 도 False
```

    False

## not의 위치

```python
a = 10
b = 100
a is not b
# a not is b error
```

    True

```python
a = 10
b = [10,20,30]
a not in b
```

    False

## 멤버연산

```python
print('a' in 'helalo world')
print('a' in 'hello world')
print('a' in ['a', 'b'])
print('a' in {'a': 10, 'b': 20}) # dictionary에서는 key값만 확인함.
# 10 in {'a': 10, 'b': 20} # dictionary에서는 value값을 in으로 확인할 수 없음
print(10 in {'a': 10, 'b': 20}.values()) # dict()의 value를 확인하고싶으면 .values() 사용!
print(10 in {10, 20, 30})
```

    True
    False
    True
    True
    True
    True

```python
'a' not in ['aa', 'bb'] # list에 'a' 인 원소는 없어서 not in 의 결과가 True
```

    True

```python
10 in [10,20,30]
[10] in [10,20,30]
[10] in [[10],20,30]
[10, 20] in [10,20,30]
[10, 20] in [[10,20],30]
# 요소끼리만 확인하고 싶으면 set으로 변환하여 .issubset 함수를 사용...
set([10, 20]).issubset(set([10,20,30]))
{10, 20}.issubset({10,20,30})
```

    True

## !!연습문제

```python
#1번
a = 100
print((a > 100) and (a < 200)  )   # False
print((a > 100) or (a < 200)   )   # True
print((a >= 100) and (a <= 200))   # True
print((a >= 100) or (a <= 200) )   # True
```

    False
    True
    True
    True

```python
#2번
b = 25
(b % 2 == 0) and (b % 5 == 0) # False
```

    False

```python
#3번
c = 1000
# 결과값은 10입니다.
answer = c // 100
if c % 100 != 0:
    answer += 1

answer
```

    10

```python
#4번
# 그리디 알고리즘

user_input = int(input('금액을 입력해주세요! :'))
money_unit = [100, 500, 1000, 5000]

def solution(input):
    result = []
    while money_unit:
        now = money_unit.pop()
        result.append(input//now)
        input -= (input//now) * now

    result.reverse()
    return result

print(solution(user_input))

```

    금액을 입력해주세요! :8800
    [3, 1, 3, 1]

```python
#4번 강사님 풀이
남은금액 = int(input())
오천원 = 남은금액 // 5000
남은금액 = 남은금액%5000

천원 = 남은금액 // 1000
남은금액 = 남은금액%1000

오백원 = 남은금액 // 500
남은금액 = 남은금액%500

백원 = 남은금액 // 100
남은금액 = 남은금액%100

print(오천원, 천원, 오백원, 백원)
```

    8800
    1 3 1 3

## !! 오늘 배운 것 정리 230502

1. str
   - 순서가 있는 **시퀀스 자료형**입니다.
   - 작은 따옴표(' ')나 큰 따옴표(" "), 삼중따옴표('''str''', """str""")로 감싸는 것도 가능합니다. <br/>(삼중따옴표를 사용할 경우에는 줄단위의 문자열을 나타낼 수 있습니다.)
   - 작은 따옴표 안에 큰 따옴표, 큰 따옴표 안에 작은 따옴표 사용이 가능합니다.
   - 이스케이프 문자도 사용이 가능합니다.
   - 리스트, 튜플도 시퀀스 자료형입니다.
   - 메서드
     - lower
     - index, find
     - count
     - strip
     - replace
     - split, join
     - isdigit
2. 슬라이싱

   - 시퀀스형 자료형을 자를 수 있습니다.
   - 형태

   ```
   # s[start:stop:step]
   s = 'paullab CEO leehojun'
   s[5:]
   s[:5]
   s[3:10]
   s[:]
   s[0:20:2]
   # 자주 사용되는 코드
   s = 'paullab CEO leehojun!'
   s[:] # string에서는 많이 사용하지 않지만 list에서 많이 사용합니다.
   s[:-1] # 마지막 요소만 제외하고 다 슬라이싱 합니다.
   ```

3. 형변환

   - 형변환 : type을 변경하는 것입니다.
   - int, float, str 등 자료형에 이름으로 형태를 변경할 수 있습니다.
   - 그 중에서도 bool이 매우 중요합니다.

   ```
   # 별 5개
   # bool 형으로 형변환 하는 것
   if True:
       print('hi')

   if 'hello':
       print('hi')

   # 정말 많이 사용하는 코드
   l = [1, 2, 3]
   while l:
       print(l.pop())

   bool('') # 빈 문자열을 제외하고 모두 True
   bool('a')
   bool('False') # 문자열 False이기 때문에 True
   bool(0) # 0을 제외하고 모두 True
   bool(-1)
   bool(100)
   bool(None) # None은 비어있음을 명시해주는 키워드, False
   bool([]) # 컨벤션 자료형은 비어있으면 False입니다.
   bool({})
   ```

4. 산술연산

   ```
   a = 10
   b = 3

   print(f'10 + 3 == {a + b}')
   print(f'10 - 3 == {a - b}')
   print(f'10 / 3 == {a / b}')
   print(f'10 // 3 == {a // b}') # 몫만 나옵니다.(정수만요!)
   print(f'10 * 3 == {a * b}')
   print(f'10 ** 3 == {a ** b}')
   print(f'10 % 3 == {a % b}') # 나머지
   ```

5. 논리연산

   ```
   # and 는 곱
   # or 는 합
   # not은 반대
   # True 1
   # False 0
   # 중요한 포인트는 저렇게 했을 때 언제 True가 되는지 정리하는 것

   print(True and False)
   print(True or False)
   print(True or True)

   # https://codingdojang.com/scode/350?answer_mode=hide
   for i in range(101):
       if i % 3 == 0 and i % 5 == 0:
           print(i)
   ```

6. 할당연산
   ```
   a = 10
   a += 10 # a = a + 10
   a //= 2
   ...

7. is, in

   1. is

      ```
      a = [1, 2, 3]
      b = [1, 2, 3]

      id(a), id(b)
      a == b # 값이 같은 것과 메모리에 같은 공간에 저장되어 있다는 얘기는 다른 얘기입니다!
      ```

   2. in
      ```
      'a' in 'helalo world'
      'a' in 'hello world'
      'a' in ['a', 'b']
      'a' in {'a':10, 'b':20}
      # 10 in {'a':10, 'b':20} # dict안에있는 value값이 있는지 확인하고 싶으면
      10 in {'a':10, 'b':20}.values()
      10 in {10, 20, 30}
      ```

## ipynb를 md 파일로 다운로드 하는 명령어

- `!`로 시작하는 것은 쉘 명령어입니다
- !jupyter nbconvert --to markdown a.ipynb

## 함수

1. 코드를 재사용 할 수 있으며, 실수를 줄일 수 있습니다.
2. 코드의 구조를 한 눈에 파악할 수 있습니다.

```python
def 부지매입():
    pass

def 설계도면작성():
    pass

def 인력모집():
    pass

def 벽돌쌓기():
    pass

def 지붕올리기():
    pass

# 함수 이름만 봐도... --> 건축 또는 집짓기?
# 새로운 사람이 코드을 읽을 때(ex 신입사원이 왔을 때)
# 3년에 한 번 이직
# 7년에 한 번 이직
# 오래 있으신 분들
부지매입()
설계도면작성()
인력모집()
벽돌쌓기()
지붕올리기()
```

```python
# 파선아실 : 파라미터는 선언할 때, 아규먼트는 실제
# x, y 는 파라미터, 5, 7 은 아규먼트
def function(x, y):
    z = x + y
    return z
print(f'function(5, 7) = {function(5, 7)}')
```

    function(5, 7) = 12

```python
# 같은 코드 1
def function(x, y):
    z = x + y
print(f'function(5, 7) = {function(5, 7)}')
```

    function(5, 7) = None

```python
# 같은 코드 2
def function(x, y):
    z = x + y
    return None
print(f'function(5, 7) = {function(5, 7)}')
```

    function(5, 7) = None

```python
# 같은 코드 3
def function(x, y):
    z = x + y
    return
print(f'function(5, 7) = {function(5, 7)}')
```

    function(5, 7) = None

```python
def hello():
    print('1')
    print('2')
    print('3')

print(hello())
```

    1
    2
    3
    None

```python
# 함수 연습문제 1
def one():
    print('one1')
    print('one2')
    print('one3')
    return 100

def two():
    print('two1')
    print('two2')
    one()
    return

print(two())
```

    two1
    two2
    one1
    one2
    one3
    None

```python
# 함수 연습문제 2
def one():
    print('one1')
    print('one2')
    print('one3')
    return 100

def two():
    print('two1')
    print('two2')
    x = one()
    return x + x

print(two())
```

```python
# 함수 연습문제 3
def one(a, b):
    print('one1')
    print('one2')
    print('one3')
    return a+b

def two(x):
    y = 100
    print('two1')
    print('two2')
    x = one(x, y)
    return x + x

print(two(10))
```

    two1
    two2
    one1
    one2
    one3
    220

```python
# 함수 연습문제 4
def one():
    print('one')
    return 10

def two():
    print('two')
    return 10

def three():
    print('three')
    return 10

a = one()
b = two()
c = three()
print(a+b)
print(a+b+c)
print('\n 좋지 않은 예')
# 좋지 않은 예
print(one() + two())
print(one() + two() + three())
#결과는 변수에 저장해서 사용하라!
```

    one
    two
    three
    20
    30

     좋지 않은 예
    one
    two
    20
    one
    two
    three
    30

```python
# 함수란 무엇일까요?
# 함수의 이름은 메모리 상의 코드 블럭을 가리키는 변수입니다.
leehojun = print
leehojun('hello world') # 소괄호는 가리키는 함수 블록을 실행시키는 명령어가 됩니다.
```

    hello world

```python
id(leehojun), id(print)
```

    (140487111775536, 140487111775536)

```python
# 함수는 단순 변수처럼 활용할 수 있다!
l = [leehojun, print, leehojun ,print]
leehojun('hello')
l[0]('hi')
```

    hello
    hi

```python
# 함수에 아규먼트로 함수를 넘겨줄 수 있다! 왜냐하면 변수처럼 다루니깐
def hello(a):
    a('hello')
    a('hello')
    a('hello')

print(hello(print))
```

    hello
    hello
    hello
    None

```python
def hello():
    def custom_sum(a,b): # 중첩함수. Nested Function
        return a+b
    return custom_sum

c = hello() # hello의 return 인 custom_sum
c(10,100)
```

    110

## 함수의 기본 기능

```python
# 파선아실 : 파라미터는 선언할 때, 아규먼트는 실제
# x, y 는 파라미터, 5, 7 은 아규먼트
def function(x, y):
    z = x + y
    return z
print(f'function(5, 7) = {function(5, 7)}')
```

```python
# return을 만나게 되면 함수는 종료가 됩니다.
def function(x, y):
    z = x + y
    return z
    print('hello') # return 이후 코드라서 실행되지 않음
print(function(5, 7))
```

    12

```python
# return을 빨리 만나게 해주세요 ==> early return 기법!!
# 조건이 부합하지 않으면 바로 return을 하도록 하는 코딩 패턴
# 이렇게 작성함으로써, 가독성이 좋은 코드
def custom_sum(x, y):
    ## 숫자가 아닐 때
    if (type(x) != int and type(x)!= float) or ( type(y) != int and type(y) != float):
        return '연산할 수 없습니다.'                        ## 함수 종료하면서 문자열 출력
    z = x + y       # 여기가 100 줄이라고 가정하면... 조건을 미리 판별하는게 성능면에서 좋음
    return z

print(custom_sum(5, 'abc'))
```

    연산할 수 없습니다.

```python
# 한글코딩의 장점
# 1. 고유명사(한라산, 새싹멤버) -> 기획자와 소통하기도 좋습니다.
# 2. 알고리즘 가독성은 괜찮습니다.

# 한글코딩의 단점
# 싫어하시는 분도 많습니다.
# 한영키 바꾸는 것
# 프로젝터는 조금 힘들 수 있어요. 일부 모듈에서만 사용할 수 있습니다.
```

```python
# 함수 안에 함수를 만들 수 있다. 중첩함수(Nested Function)

def one():
    def two():
        print('hello1')
    def three():
        print('hello2')
    return 100
print(one())
```

    100

```python
# 함수 안의 함수와 변수는 밖에서 호출할 수 없습니다.
# 함수가 끝나면 함수 내부에 있던 것들은 초기화 된다고 생각하면 됨 --> scope 공부 필요
# 만약 print(x), two()실행됬다면 two()와 x가 정의되어있을 것임... jupyter notebook의 런타임 문제!
def one():
    def two():
        print('hello1')
    def three():
        print('hello2')
    two()
    three()
    x= 1000
    return 100
one()
# print(x)  # NameError : name 'x' is not defined
# two()     # NameError : name 'two' is not defined
```

    hello1
    hello2



    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-7552550a2195> in <cell line: 14>()
         12 one()
         13 # print(x) # NameError : name 'x' is not defined
    ---> 14 two()


    NameError: name 'two' is not defined

```python
# 함수 안의 함수와 변수를 해보았으니
# 이번에는 함수 밖에 함수와 변수를 해보도록 하겠습니다.

def test():
    print('test')

def one():
    test()  # 함수 scope 기준에서 밖에 있는 함수를 호출한 상황. 가능하다!!!!

def two():
    test()

one()
two()
test()
```

    test
    test
    test

```python
# 위 원리와 마찬가지로 밖에 있는 변수를 '가져오는 것' 만 가능합니다.
# 수정은 안됩니다.
test = 10

def one():
    print(test)

def two():
    print(test)

one()
two()
```

    10
    10

```python
# 위 원리와 마찬가지로 밖에 있는 변수를 '가져오는 것' 만 가능합니다.
# 밖에 있는 변수의 수정이 안됨!
test = 10

def one():
    test += 10 # UnboundLocalError: local variable 'test' referenced before assignment

one()
```

## 지역 변수와 전역 변수

```python
# 전역변수에 접근은 가증하지만 수정이 되진 않습니다.
a = 100
def f():
    a = a+10 # error
f()
```

### global

- 전역변수임을 알려주는 예약어 **`global`**

```python
# 전역변수를 함수 내부에서 수정이 되게 하는 코드입니다.
# 권하지 않습니다.
a = 100
def f():
    global a    # 실무에서 사용 안합니다.
    a = a+1     # 전역변수는 함수 스코프에서 수정이 가능합니다
f()
print(a)
```

    101

```python
# 정해진 루트 외에 다른 루트로 값을 수정하려고 하지 마세요...
# 밖의 값을 수정하고 싶을 때에는 이런 방식으로 해야 합니다.
a = 100
def f(a):
    return a+1
a = f(a)
print(a)
```

    101

```python
# 순수함수 : 밖의 변수를 사용하지 않아 예측이 가능한 함수
def f(x):
    return x + x + 100

f(10)
f(20)
# 아규먼트 값에 따라 다르지만 아규먼트의 2배 + 100 이라는 사실은 변하지 않음.
```

    140

```python
# 순수함수가 아닌것
test = 100
def f(x):
    return x + x + 100 + test

f(10)
# 아규먼트 값에 따라 다르지만
# 아규먼트의 2배 + 200 이라는 사실은 변하지 않는가?? --> no
# test 값이 다른 곳에서 조작되어 값이 변경되면  +200 이 안될 수 있음
# 예측이 불가능하게 되는 문제가 발생함!!!!!
```

```python
# 지역변수와 전역변수 이어서
# 전역변수 : 전역에서 접근할 수 있는 변수
# 지역변수 : 함수 내에서만 접근 할 수 있는 변수
```

```python
a = 100
def one():
    a = 10
    print(a)

one()
print(a)
```

    10
    100

```python
# 자신의 공간에 변수가 선언되어 있지 않다면 바깥쪽으로 전역까지 1 scope씩 찾아 올라갑니다.
# 안쪽으로는 찾지 않습니다
# 전역에도 없으면 error를 발생시킵니다.

a = 100
def one():
    a = 10
    def two():
        def three():
            a = 1000
            print(a)
        three()
        print(a)

    two()
    print(a)

one()
print(a)
```

    1000
    10
    10
    100

```python
# 변수를 탐색할 때 함수 함수 스코프 전체를 읽기 때문에
# two() 함수에서 print(a) 아래에 a를 선언하면
# two() 함수 스코프에 a 가 있는데 정의되기 전으로 인식하여
# 에러가 발생함!
a = 100
def one():
    a = 10
    def two():
        def three():
            a = 1000
            print(a)
        three()
        print(a)
        # a = 10 # UnboundLocalError: local variable 'a' referenced before assignment

    two()
    print(a)

one()
print(a)
```

### nonlocal

- 함수 내에서 중첩된 함수를 사용할 경우 문제가 발생할 수 있습니다.
- 중첩된 함수에서 변수를 사용할 때, 사용한 변수가 지역변수가 아닌 전역변수로 인식되어 예상치 못한 결과가 발생할 수 있습니다.
- 이때, **`nonlocal`**키워드를 사용하여 변수가 전역변수가 아닌, 해당 중첩된 함수 내에서 사용되는 변수임을 명시해줄 수 있습니다.

```python
# inner가 outer의 변수를 건드리고 싶은데
# inner 안에서는 outer의 변수 x에 대한 수정권한이 없습니다.
x = 100
def outer():
    x = 1
    def inner():
        nonlocal x # 1단계 위 scope의 x 임을 명시
        x += 1
        print(x)
    inner()
    print(x)

outer()
print(x)
```

    2
    2
    100

```python
# 위의 문제에 global을 사용한다면?
x = 100
def outer():
    x = 1
    def inner():
        global x # 1단계 위의 scope의 x 임을 명시
        x += 1
        print(x)
    inner()
    print(x)

outer()
print(x)
```

    101
    1
    101

## 재귀함수(recursion)

- 내가 나를 호출하는 것입니다.
- 재귀 <--> for문은 대부분 호환 가능합니다.
- 반복문 사용하시기를 권합니다.
- 어렵고 효율도 안좋아요!
- 필수적으로 사용하는 곳이 있습니다. (어디일까?? 다이나믹 프로그래밍, 분할, 정복, 다익스트라 등)

```python
# sys.setrecursionlimit -> 제한을 늘릴 수 있음
# 실행시키지 마세요... 뻗을 수 있습니다.
# def 숫자출력():
#     print(1)
#     return 숫자출력()
# 숫자출력()
```

- for 과 recursion 비교

```python
# for 로 팩토리얼
# 5! = 5*4*3*2*1
result = 1

# 1 * 2 * 3 * 4 * 5
for i in range(1,6):
    result *=i


result
```

    120

```python
# 재귀로 팩토리얼

def f(n):
    if n <= 1:
        return 1
    else:
        return n * f(n-1)

f(5)

```

    120

```python
# for로 문자열 거꾸로 출력하기
s = 'hello'
result = ''
for i in s:
    result = i + result

result
# 실무에서는 이런식으로 거꾸로 만들지 않습니다. 이건 예제를 위해...
# 슬라이싱이 일반 for문보다 8배 빠릅니다.
# s[::-1]
```

    'olleh'

```python
def reverse(s):
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:])+ s[0]

reverse('hello')

'''
호출함수            리턴값
reverse('hello')    reverse('ello') + 'h'
reverse('ello')     reverse('llo') + 'e'
reverse('llo')      reverse('lo') + 'l'
reverse('lo')       reverse('o') + 'l'
reverse('o')        'o'
'''
```

    "\nreverse('hello')    reverse('ello') + 'h'\nreverse('ello')     reverse('llo') + 'e'\nreverse('llo')      reverse('lo') + 'l'\nreverse('lo')       reverse('o') + 'l'\nreverse('o')        'o'\n"

```python
# 피보나치 수열
# 재귀가 얼마나 비효율적인지 보여드리기 위해서 진행
# 1 1 2 3 5 8 13 21

# 이해안됨...왜??

curr = 1
next = 1
for i in range(1, 5):
    curr, next= next, curr + next

next
print(list(range(1,5)))
```

    [1, 2, 3, 4]

```python
# 피보나치 재귀

def f(n):
    if n == 1 or n == 2:
        return 1
    return f(n-1) + f(n-2)

f(1), f(2), f(3), f(4), f(5), f(6)
```

    (1, 1, 2, 3, 5, 8)

```python
f(35)
```

    9227465

```python
# 재귀함수의 비효율을 이렇게 해결할 수 있다
# 그러나 가능하면 for문을 이용해주세요!

from functools import lru_cache

# 재귀함수 호출시 이미 계산된 fib(n)값을 저장해뒀다가 호출될때 값을 가져다가 쓰는 방법.
# 어떻게 저장하고 사용하는거지??
@lru_cache(maxsize=None)
def fib(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)

fib(40)
```

    102334155

## !!함수 연습문제

```python
# 연습문제 1
a = 'pithon'

def 함수1():
    def 함수2():
        print('love')

    print('I')
    함수2()
    return "python"


a = 함수1()
print(a)

# I
# love
# python

```

    I
    love
    python

```python
# 연습문제 2
# 실력이 있으신 분들은 견고한 코드가 될 수 있도록 해야 합니다
def plus(num1, num2):
    if (type(num1) != float and type(num1) !=int) and(type(num2) != float and type(num2) !=int):
        return '숫자가 아니기에 연산할 수 없습니다.'

    return num1 + num2

def minus(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

# 람다식 풀이
# plus = lambda num1, num2 : num1 + num2
# minus = lambda num1, num2 : num1 - num2
# multiply = lambda num1, num2 : num1 * num2
# divide = lambda num1, num2 : num1 / num2

print(f'plus : {plus(10, 5)}')
print(f'minus : {minus(10, 5)}')
print(f'multiply : {multiply(10, 5)}')
print(f'divide : {divide(10, 5)}')

```

    plus : 15
    minus : 5
    multiply : 50
    divide : 2.0

```python
# 실력이 있으신 분은 견고한 코드가 될 수 있도록 해주셔야 합니다.
def plus(num1, num2):
    if type(num1) == int and type(num2) == int:
        return num1 + num2
    return float('inf') # 어떤 수보다도 크게 판정됩니당

# 혹은 아래처럼 예외 처리하는 문구 추가
def plus(num1, num2):
    try:
        return num1 + num2
    except:
        return float('inf')

print(float('inf') > 1000000000000000000000000)

# 테스트 주도 개발 <<<<<<<<<<<<
# 실무에서 이런 식으로 테스트하기 때문에 예외가 발생할 수 있는 상황에 대해 처리해줘야 견고한 코드가 될 수 있음
print(f"plus : {plus(10, 5)}")
print(f"plus : {plus(10, '5')}")
print(f"plus : {plus('10', 5)}")
print(f"plus : {plus('10', '5')}")
print(f"plus : {plus(10, 'a')}")
print(f"plus : {plus(10, True)}")
print(f"plus : {plus(False, 5)}")
print(f"plus : {plus(10, 10.1)}")
```

    True
    plus : 15
    plus : inf
    plus : inf
    plus : 105
    plus : inf
    plus : 11
    plus : 5
    plus : 20.1

```python
# 연습문제 3
# x의 n제곱을 구하는 함수를 만들어주세요.
# 재귀함수를 이용하여 만들어야하며, x은 0이 아닙니다. (x, n > 1)

def power(x, n):
    if n == 1:
        return x
    else:
        return x * power (x, n-1)

power(3,2)

## lambda 식 풀이
def lampower(x,n):
    if n==1:
        return x
    else:
        return x * (lambda x : lampower(x,n-1))(x)

lampower(3,3)

## 클로저 풀이??
# 팩토리 함수라고도 하고, 클로져 라고도 합니다.
def clo_power(x):
    def power_num(y):
        return x ** y
    return power_num

# 여기서 설정된 clo_power(x) 의 x 값이 휘발되지 않고 가지고 있음!!!
# 한번 객체로 구현된 x 값은 접근할 수 없게 되는데, 변하면 안되는 수를 이런식으로 변하지 않도록 감춰줄 수도 있음!
clo_power_base3 = clo_power(3)
clo_power_base3(4)
```

    81

```python
# 재귀로 위 코드보다 속를 빠르게 한 코드
def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        recur = power(x, n/2)       # 절반씩 나누어 곱해줌
        return y * y
    else:
        recur = power(x, (n-1)/2)   # 홀수일 경우 한번 곱해주고 절반 절반 곱해줌
        return x * recur * recur
```

```python
## 최승현님 코드 :  놀라워라~~ 분할 정복 알고리즘??? 확인!!
# 재귀를 Log(n,2) 만 호출하게 된다고 합니다..
def my_pow(num1, num2):
    if num2 == 0:
        return 1
    if num2 == 1:
        return num1
    if num2 % 2 == 0:
        half = my_pow(num1, num2 // 2)
        return half * half
    else:
        half = my_pow(num1, num2 // 2)
        return half * half * num1

my_pow(2,3)
```

    8

## list(리스트)

- 순서를 가진 데이터들의 집합(Sequence)
- 값의 변경이 가능
- 리스트 안에 리스트로 다차원의 리스트를 만드는 것도 가능
- 리스트 안에 다른 오브젝트(dictionary, set, tuple 등)를 넣는 것이 가능

```python
l = [1000, 2000, 3000, 1000, 2000, 3000]
id(l[0]), id(l[3]) # 두 id 가 같다!
# l[3] = 4000       #이렇게 값을 바꾸면 달라진다.
# print(l)
# id(l[0]), id(l[3])
```

    [1000, 2000, 3000, 4000, 2000, 3000]





    (139899103062352, 139899103060016)

```python
# 컨벤션 자료형 (dictionary, tuple, set, list)은
# 메모리 효율을 위해서
# 같은 값이 있을 경우 같은 id를 가리키게 설계되어 있습니다.
```

```python
l = [10 ,20 ,30, 40]
l[0] = 1000
l
```

    [1000, 20, 30, 40]

```python
# string은... index로 접근해서 값을 수정할 수 없음
s = 'hello world'
s[0] = 'k' # error 발생.
s
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-14-2b1c16f71298> in <cell line: 2>()
          1 s = 'hello world'
    ----> 2 s[0] = 'k'
          3 s


    TypeError: 'str' object does not support item assignment

```python
# 다차원 리스트
data = [[1,2,3],
        [4,5,6],
        [7,8,9]]

data
```

    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

```python
data[0]
```

    [1, 2, 3]

```python
data[0][0]
```

    1

```python
data = [[1,2,3],
        [4,5,6],
        [7,8,9]]

data[0][0] *= 2
data[0][1] *= 2
data[0][2] *= 2
data[1][0] *= 2
data[1][1] *= 2
data[1][2] *= 2
data[2][0] *= 2
data[2][1] *= 2
data[2][2] *= 2
data
```

    [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

```python
data = [[1,2,3],
        [4,5,6],
        [7,8,9]]

for i in range(3):
    data[i][0] *=2
    data[i][1] *=2
    data[i][2] *=2

data
```

    [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

```python
data = [[1,2,3],
        [4,5,6],
        [7,8,9]]

for i in range(3):
    for j in range(3):
        data[i][j] *=2

data
```

    [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

```python
# 데이터 사이언스.. 수학용어
'''
3               == 스칼라
[3,4]           == 벡터
[[1,2,3],
[4,5,6],
[7,8,9]]        == 매트릭스
[[[1],[2],[3]],
[[4],[5],[6]],
[[7],[8],[9]]]  == 텐서(다차원, 3차원 이상)

텐서플로우 : 인공지능 라이브러리 중 유명한 라이브러리
'''
```

```python
# 리스트에서 주의해야 하는 연산!
x = [10] * 3
x
```

    [10, 10, 10]

```python
x[0] = 100
x
```

    [100, 10, 10]

```python
x = [[10]*2] * 3
print(x)
x[0][0] = 100
x
```

    [[10, 10], [10, 10], [10, 10]]





    [[100, 10], [100, 10], [100, 10]]

```python
## 곱하기 연산시 1차원은 괜찮지만 차수가 깊어지면, 안에 있는 list들은 주소를 복사하게 되서
## 원소 하나만 바꿨을 때 모든 값이 다 바뀌어 버리게 됨

x = [[[10] * 3] * 3] * 4
x[0][0][0] = 1000
print(x)

id(x[0][0]), id(x[0][1]) ## 아이디가 같음... 그래서 원소x[0][0][0] 에 값 넣으면 모든 3차 첫원소 값이 바뀜
```

    [[[1000, 10, 10], [1000, 10, 10], [1000, 10, 10]], [[1000, 10, 10], [1000, 10, 10], [1000, 10, 10]], [[1000, 10, 10], [1000, 10, 10], [1000, 10, 10]], [[1000, 10, 10], [1000, 10, 10], [1000, 10, 10]]]





    (139899100548032, 139899100548032)

```python
# list의 더하기
[1,2,3] + [1,2,3] #많이 사용합니다!
```

    [1, 2, 3, 1, 2, 3]

```python
l = [10,20,30]
type(l), dir(l), help(l)
```

    Help on list object:

    class list(object)
     |  list(iterable=(), /)
     |
     |  Built-in mutable sequence.
     |
     |  If no argument is given, the constructor creates a new empty list.
     |  The argument must be an iterable if specified.
     |
     |  Methods defined here:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __contains__(self, key, /)
     |      Return key in self.
     |
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __iadd__(self, value, /)
     |      Implement self+=value.
     |
     |  __imul__(self, value, /)
     |      Implement self*=value.
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __reversed__(self, /)
     |      Return a reverse iterator over the list.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |
     |  __sizeof__(self, /)
     |      Return the size of the list in memory, in bytes.
     |
     |  append(self, object, /)
     |      Append object to the end of the list.
     |
     |  clear(self, /)
     |      Remove all items from list.
     |
     |  copy(self, /)
     |      Return a shallow copy of the list.
     |
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |
     |  extend(self, iterable, /)
     |      Extend list by appending elements from the iterable.
     |
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |
     |      Raises ValueError if the value is not present.
     |
     |  insert(self, index, object, /)
     |      Insert object before index.
     |
     |  pop(self, index=-1, /)
     |      Remove and return item at index (default last).
     |
     |      Raises IndexError if list is empty or index is out of range.
     |
     |  remove(self, value, /)
     |      Remove first occurrence of value.
     |
     |      Raises ValueError if the value is not present.
     |
     |  reverse(self, /)
     |      Reverse *IN PLACE*.
     |
     |  sort(self, /, *, key=None, reverse=False)
     |      Sort the list in ascending order and return None.
     |
     |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
     |      order of two equal elements is maintained).
     |
     |      If a key function is given, apply it once to each list item and sort them,
     |      ascending or descending, according to their function values.
     |
     |      The reverse flag can be set to sort in descending order.
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  __class_getitem__(...) from builtins.type
     |      See PEP 585
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __hash__ = None






    (list,
     ['__add__',
      '__class__',
      '__class_getitem__',
      '__contains__',
      '__delattr__',
      '__delitem__',
      '__dir__',
      '__doc__',
      '__eq__',
      '__format__',
      '__ge__',
      '__getattribute__',
      '__getitem__',
      '__gt__',
      '__hash__',
      '__iadd__',
      '__imul__',
      '__init__',
      '__init_subclass__',
      '__iter__',
      '__le__',
      '__len__',
      '__lt__',
      '__mul__',
      '__ne__',
      '__new__',
      '__reduce__',
      '__reduce_ex__',
      '__repr__',
      '__reversed__',
      '__rmul__',
      '__setattr__',
      '__setitem__',
      '__sizeof__',
      '__str__',
      '__subclasshook__',
      'append',
      'clear',
      'copy',
      'count',
      'extend',
      'index',
      'insert',
      'pop',
      'remove',
      'reverse',
      'sort'],
     None)

## 리스트의 메서드

```python
# 'append',  'clear',  'copy',  'count',  'extend',
# 'index',  'insert',  'pop',  'remove',  'reverse',  'sort'
# 모르는 것이 있는지 확인해보기
```

- append

```python
## append
l = [1,2,3]
l.append(4)
l
```

    [1, 2, 3, 4]

```python
l = [1,2,3]
l.append([1,2,3])
l
```

    [1, 2, 3, [1, 2, 3]]

- extend

```python
## extend
l = [1,2,3]
l.extend(4) # error : TypeError: 'int' object is not iterable
# iterable(__next__가 있는 것)한 객체만 넣을 수 있다.
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-40-3472de3ce524> in <cell line: 3>()
          1 ## extend
          2 l = [1,2,3]
    ----> 3 l.extend(4) # error


    TypeError: 'int' object is not iterable

```python
l = [1,2,3]
l.extend('hello')
l
```

    [1, 2, 3, 'h', 'e', 'l', 'l', 'o']

```python
l = [1,2,3]
l.extend({'one': 10, 'two' : 20})
l
```

    [1, 2, 3, 'one', 'two']

```python
l = [1,2,3]
l.extend({10,20,30})
l
```

    [1, 2, 3, 10, 20, 30]

```python
## extend - 요소 여러 개를 추가할 때
# 인자로는 iterable 요소만 가능하다
l = [1,2,3]
l.extend([1,2,3])
l
```

    [1, 2, 3, 1, 2, 3]

- clear

```python
## clear
l = [1,2,3]
l.clear()
l
# l = [] 이렇게 씀..
```

    []

- copy

```python
## copy
# list를 할당하게 되면 하나의 list를 공유하게 됨
제주과일가게 = [['바나나', 1000], ['수박', 2000], ['딸기', 3000]]
서울과일가게 = 제주과일가게
서울과일가게[0] = ['바나나', 2000]
서울과일가게, 제주과일가게
```

    ([['바나나', 2000], ['수박', 2000], ['딸기', 3000]],
     [['바나나', 2000], ['수박', 2000], ['딸기', 3000]])

```python
제주과일가게 = [['바나나', 1000], ['수박', 2000], ['딸기', 3000]]
서울과일가게 = 제주과일가게.copy() # 얕은 복사
서울과일가게[0] = ['바나나', 2000]
서울과일가게, 제주과일가게
```

    ([['바나나', 2000], ['수박', 2000], ['딸기', 3000]],
     [['바나나', 1000], ['수박', 2000], ['딸기', 3000]])

```python
제주과일가게 = [['바나나', 1000], ['수박', 2000], ['딸기', 3000]]
서울과일가게 = 제주과일가게[:] # 얕은 복사
서울과일가게[0] = ['바나나', 2000]
서울과일가게, 제주과일가게
```

```python
s = 'hello world'
s[:4]
```

    'hell'

```python
l = [10,20,30,40,50]
l[:3]
ll = l[:]
id(l), id(ll)  ## 주소가 다름. 값은 같지만
```

    (139899102159488, 139899102153280)

```python
# 이 이상의 강의는 얕은복사, 깊은복사에서 해결이 됩니다
제주과일가게 = [['바나나', 1000], ['수박', 2000], ['딸기', 3000]]
서울과일가게 = 제주과일가게[:] # 얕은 복사
print(id(서울과일가게[0]), id(제주과일가게[0]))
print(id(서울과일가게[0][0]), id(제주과일가게[0][0]))
서울과일가게[0][1] = 3000
서울과일가게, 제주과일가게 ## 얕은복사로 했는데도 값이 똑같아지네..?

```

    139899102081152 139899102081152
    139899100884272 139899100884272





    ([['바나나', 3000], ['수박', 2000], ['딸기', 3000]],
     [['바나나', 3000], ['수박', 2000], ['딸기', 3000]])

```python
l = [1,2,3]
ll = l[:]
l[0] = 1000
l, ll
```

    ([1000, 2, 3], [1, 2, 3])

```python
l = [1,2,3]
ll = l.copy()
l[0] = 1000
l, ll
```

    ([1000, 2, 3], [1, 2, 3])

- count

```python
## count
l = [1,2,3,1,1,1,2,3,2,3,1,1]
l.count(1)

# 연산 때문에 list에 비슷한 자료형만 넣는 걸 추구하기도 한다
```

    6

- index

```python
## index
# 슬라이싱에 활용하기도함
a = [10,1,1,11,2,23,12, 11]
a.index(11) # 같은 수가 있어도 맨 앞에 나오는 index를 리턴함
```

    3

```python
a = [10,1,1,11,2,23,12, 11]
a.index(11)
a[:a.index(11)]
```

    [10, 1, 1]

```python
a = [10,20,30]
a.insert(2, 1000) #해당 인덱스에 값을 넣고 뒤에 값을 뒤로 미룸
a
```

    [10, 20, 1000, 30]

- pop

```python
[i for i in range(1,20) if i%2 == 0]
```

    [2, 4, 6, 8, 10, 12, 14, 16, 18]

```python
## pop ***** (별 5)
l = [10,20,30,40,50]
print(l.pop())
print(l)
print(l.pop(0)) # 0번째 index를 뽑음
print(l)
```

    50
    [10, 20, 30, 40]
    10
    [20, 30, 40]

```python
## 중간 정리
# append : 맨 뒤에 추가
# pop : 맨 뒤에서 값을 뽑아내고, index가 들어갈 경우 index에서 뽑습니다.
# insert : index에 값을 삽입하고 원래 있던 값을 뒤로 밀어버립니다.
```

- remove

```python
## remove
l = [10,20,30,40,50]
l.remove(20) # 예를 들어 for를 돌면서 remove를 하지 않길 바랍니다.
l
```

    [10, 30, 40, 50]

```python
l = [20,20,20,20]
for i in range(len(l)):
    print(len(l)) # length가 계속 변하기 때문에 의도치 않은 에러가 날 수 있습니다
    l.remove(20)
```

    4
    3
    2
    1

```python
# 무한 반복입니다.
# l = [20,20,20,20]
# for i in range(len(l)):
#     print(len(l))
#     l.append(20)
```

```python
# 예..
l = [10,20,30,40,50,20,20,20]
for i in range(l.count(20)):
    l.remove(20)
print(l)
```

    [10, 30, 40, 50]

```python
# 실무에서
# 어떤 값을 전부 없애거나 전부 찾는 것
# 즉, 조건에 부합하는 것
def f(x):
    return x !=20

# True인 것만 반환해줍니다.
list(filter(f, [10,20,30,40,50,20,20,20]))
```

    [10, 30, 40, 50]

```python
filter(f, [10,20,30,40,50,20,20,20])
```

    <filter at 0x7ff4b131c6d0>

```python
range(100) # 메모리를 0~ 99 한 번에 할당하지 않음. (python 3.x 부터)
# 시작과 끝 값만 가지고 다음값으로 이동 후 끝값에 도달했는지 확인만 함.
```

    range(0, 100)

```python
for i in filter(f, [10,20,30,40,50,20,20,20]):
    print(i)
```

    10
    30
    40
    50

```python
list(filter(lambda x: x!=20, [10,20,30,40,50,20,20,20]))
```

    [10, 30, 40, 50]

- reverse

```python
## reverse
l = [ 5,6,4,3,8,9,1]
l.reverse() # 역 정렬이 아니고 원본을 변경합니다
l
```

    [1, 9, 8, 3, 4, 6, 5]

```python
l = [ 5,6,4,3,8,9,1]
reversed(l) # 역 정렬이 아니고 원본을 변경하지 않습니다.
print(reversed(l))
print(list(reversed(l)))
print(l) #l은 그대로
```

    <list_reverseiterator object at 0x7f3ccc453df0>
    [1, 9, 8, 3, 4, 6, 5]
    [5, 6, 4, 3, 8, 9, 1]

```python
# l.reverse() : 리스트에 메서드 이며, return None입니다! 원본이 역순, 원본을 만집니다.
# reversed() : 빌트인펑션이며, return 역순 입니다! 원본을 만지지 않습니다.
```

```python
l = [ 5,6,4,3,8,9,1]
print(l.reverse())
print(l)
```

    None
    [1, 9, 8, 3, 4, 6, 5]

```python
print(reversed(l))
print(list(reversed(l)))
print(l)
```

    <list_reverseiterator object at 0x7f3ccc2feb00>
    [5, 6, 4, 3, 8, 9, 1]
    [1, 9, 8, 3, 4, 6, 5]

```python
print(type(range(10)))
```

    <class 'range'>

```python
array = [n for n in range(3)]
print(array)
array2 = [[0 for n in range(3)] for k in range(3)]
print(array2) #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

```

    [0, 1, 2]
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

```python
a, b, c = 1,2,3
a,b,c

```

    (1, 2, 3)

- sort

```python
l = [1,5,4,2,8,5,10,9,2,3]
l.sort() # 원본을 만지고, 반환값은 None
l
```

    [1, 2, 2, 3, 4, 5, 5, 8, 9, 10]

```python
l = [1,5,4,2,8,5,10,9,2,3]
print(sorted([1,5,4,2,8,5,10,9,2,3])) # 원본을 수정하지 않고, 반환값은 정렬된 새 리스트
print(l)
```

    [1, 2, 2, 3, 4, 5, 5, 8, 9, 10]
    [1, 5, 4, 2, 8, 5, 10, 9, 2, 3]

```python
# 실무에서 역정렬 이렇게 하진 않음..
l = [1,5,4,2,8,5,10,9,2,3]
l.sort()
l.reverse()
l
```

    [10, 9, 8, 5, 5, 4, 3, 2, 2, 1]

```python
l = [1,5,4,2,8,5,10,9,2,3]
l.sort(reverse=True) # 내림차순 정렬 시 reverse 인자에 True
l
```

    [10, 9, 8, 5, 5, 4, 3, 2, 2, 1]

```python
l = [1,5,4,2,8,5,10,9,2,3]
print(sorted(l, reverse=True)) # 내림차순 정렬 시 reverse 인자에 True
print(l)
```

    [10, 9, 8, 5, 5, 4, 3, 2, 2, 1]
    [1, 5, 4, 2, 8, 5, 10, 9, 2, 3]

```python
# 많이 사용하는 문법!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

l = [[1, 10, 'leehojun'],
     [20, 30, 'hojun'],
     [10, 20, 'weniv!'],
     [1, 2, 'hello world'],
     [55, 11, 'sun']]

# 1. 글자 수 대로 정렬해주세요.
def f(x):
    return len(x[2]) # len(x[-1])

print(sorted(l, key=f, reverse=False))
print(sorted(l, key=lambda x : len(x[-1]), reverse=False))

# 2. 맨 앞에 위치한 숫자대로 정렬해주세요.
def f2(x):
    return x[0]

print(sorted(l))   # 아무것도 지정하지 않으면 요소의 첫 번째 요소를 기준으로 정렬
print(sorted(l, key=f2))
print(sorted(l, key=lambda x: x[0]))

# 3. 중앙에 위치한 값대로 정렬해주세요.
def f3(x):
    return x[1]

print(sorted(l, key=f3))
print(sorted(l, key=lambda x: x[1]))


l = [[1, 10, 32],
     [20, 30, 11],
     [10, 20, 22],
     [1, 2, 13],
     [55, 11, 44]]


# 4. 3개의 전체 합이 작은 순서대로 출력해주세요.

def f4(x):
    return x[0]+ x[1] +x[2]

def f5(x):
    return sum(x)

print(sorted(l,key=f4))
print(sorted(l,key=f5))
print(sorted(l,key=lambda x : sum(x)))
print(sorted(l,key=sum))
```

    [[55, 11, 'sun'], [20, 30, 'hojun'], [10, 20, 'weniv!'], [1, 10, 'leehojun'], [1, 2, 'hello world']]
    [[55, 11, 'sun'], [20, 30, 'hojun'], [10, 20, 'weniv!'], [1, 10, 'leehojun'], [1, 2, 'hello world']]
    [[1, 2, 'hello world'], [1, 10, 'leehojun'], [10, 20, 'weniv!'], [20, 30, 'hojun'], [55, 11, 'sun']]
    [[1, 10, 'leehojun'], [1, 2, 'hello world'], [10, 20, 'weniv!'], [20, 30, 'hojun'], [55, 11, 'sun']]
    [[1, 10, 'leehojun'], [1, 2, 'hello world'], [10, 20, 'weniv!'], [20, 30, 'hojun'], [55, 11, 'sun']]
    [[1, 2, 'hello world'], [1, 10, 'leehojun'], [55, 11, 'sun'], [10, 20, 'weniv!'], [20, 30, 'hojun']]
    [[1, 2, 'hello world'], [1, 10, 'leehojun'], [55, 11, 'sun'], [10, 20, 'weniv!'], [20, 30, 'hojun']]
    [[1, 2, 13], [1, 10, 32], [10, 20, 22], [20, 30, 11], [55, 11, 44]]
    [[1, 2, 13], [1, 10, 32], [10, 20, 22], [20, 30, 11], [55, 11, 44]]
    [[1, 2, 13], [1, 10, 32], [10, 20, 22], [20, 30, 11], [55, 11, 44]]
    [[1, 2, 13], [1, 10, 32], [10, 20, 22], [20, 30, 11], [55, 11, 44]]

```python
# https://codingdojang.com/scode/408?answer_mode=hide
# 좌표평면 문제가 나오면 차원 축소나 차원 확대가 가능한 문제인지 확인

point = [1,3,4,8,13,17,20]

# slicing 이용해서 짝지어줌
print(list(zip(point, point[1:]))) ## 원하는대로 묶어줬는지 확인
#하지만 실무에서 이렇게 형변환 하는건 메모리 낭비가 심해서 이렇게 하면 안됨

print(sorted(zip(point, point[1:]), key=lambda x:x[1]-x[0]))
sorted(zip(point, point[1:]), key=lambda x:x[1]-x[0])[0]
```

    [(1, 3), (3, 4), (4, 8), (8, 13), (13, 17), (17, 20)]
    [(3, 4), (1, 3), (17, 20), (4, 8), (13, 17), (8, 13)]





    (3, 4)

```python
# built in function zip()
list(zip('hello!', 'world')) # 짧은 길이 기준으로 같은 인덱스끼리 tuple로 묶어줌
```

    [('h', 'w'), ('e', 'o'), ('l', 'r'), ('l', 'l'), ('o', 'd')]

```python
# https://school.programmers.co.kr/learn/courses/30/lessons/120835?language=python3
# 응급도
# [3, 76, 24]
# 우선순위
# [3, 1, 2]
l = [3, 76, 24]
정렬된값 = sorted(l,reverse=True)
#정렬된값    # [76, 24, 3]
#원하는값    # [3, 1, 2]

# l을 정렬해서 우선순위 순서대로 정렬을 해야
# 원래 l 순서에서의 우선순위 값을 만들어 줄 수 있습니다
# 즉 정렬된 값의 원소가 l에서 몇 번째 있는지 넣어주면 됨
결과값 = [정렬된값.index(l[0]) + 1 ,정렬된값.index(l[1]) + 1,정렬된값.index(l[2]) +1 ]
결과값

## 내가 따로 푼 것
def solution(emergency): # 3 76 24
    descend = sorted(emergency, reverse=True) # 76 24 3
    #answer = [descend.index(emergency[i]) + 1 for i in range(len(emergency)) ]
    answer = [descend.index(i) +1 for i in emergency]
    return answer

## 자료
def solution(emergency):
    order = sorted(emergency, reverse=True)
    answer = list(map(lambda x : order.index(x)+1 , emergency))
```

    [3, 1, 2]

```python
# 문자는 알파벳 순으로...
l = ['c','d', 'a','b', 'e', 'y']
l.sort()
print(l)

# 문자열은 길이순보다 같은 문자 반복이 더 순위가 높음
k = [ 'ab','aaa', 'aa', 'ak', 'aii', 'aaaa', 'ac', 'a']
k.sort()
print(k)
```

    ['a', 'b', 'c', 'd', 'e', 'y']
    ['a', 'aa', 'aaa', 'aaaa', 'ab', 'ac', 'aii', 'ak']

## !! 오늘 배운 것 정리 230503

1. 함수

   1. 코드 덩어리(정말 쉽게 설명하면)
   2. 코드를 재사용 할 수 있으며, 실수를 줄일 수 있습니다.
   3. 코드의 구조를 한 눈에 파악할 수 있습니다.
   4. 형태
      ```python
      # 파선아실(파라미터는 선언할 때, 아규먼트는 실제)
      def function(x, y):
          z = x + y
          return z
      print(f'function(5, 7) = {function(5, 7)}')
      ```
   5. 함수 안에 함수와 함수 안에 변수는 밖에서 접근이 불가합니다.
   6. 지역 변수와 전역 변수
      - 전역변수 : 전역에서 접근할 수 있는 변수
      - 지역변수 : 함수 내에서만 접근할 수 있는 변수
      ```python
      # 전역변수는 각 함수에서 접근은 가능하지만 수정이 되진 않습니다.
      # only read
      # global이라는 키워드로 밖에 있는 변수를 수정할 수도 있지만 권하지 않습니다.
      # 권하지 않기에 요약자료에도 없습니다.
      a = 100
      def f():
          a = a + 1
      f()
      ```
   7. 재귀함수

      - 내가 나를 호출하는 것입니다.
      - 재귀 <-> for문은 대부분 호환이 가능합니다.
      - 반복문 사용하시기를 권합니다!
      - 어렵고 효율도 안좋아요! (얼마나 효율이 안좋은지도 확인해보겠습니다.)
      - 필수적으로 사용하는 곳이 있습니다.

      ```python
      def f(n):
          if n <= 1:
              return 1
          else:
              return n * f(n-1)

      f(5)
      ```

2. list (리스트)

   - 순서를 가진 데이터들의 집합(Sequence)
   - 리스트는 값의 변경
   - 리스트 안에 리스트로 다차원의 리스트를 만드는 것도 가능
   - 리스트 안에 다른 딕셔너리, 셋, 튜플 등을 넣는 것도 가능합니다

   ```python
   l = [10, 20, 30, 40]
   print(l[0]) # 순서로 값 호출
   l[0] = 1000 # 값의 변경 가능
   print(l)

   data = [[1, 2, 3], # 다차원 배열
       [4, 5, 6],
       [7, 8, 9]]

   print(data)
   ```

   - 리스트 메서드
     - append : 맨 뒤에 값 추가
     - clear : 모든 값 지우기
     - copy : 얕은 복사
     - count : 갯수 세기
     - extend : 확장하기(뒤에 순회 가능한 객체가 들어오면 순차적으로 추가)
     - index : 위치 찾기
     - insert : 삽입하기
     - pop: 맨 뒤에서 값 꺼내기(index가 들어오면 index에서 값 꺼냄)
     - remove : 값 지우기
     - reverse : 역순
     - sort : 정렬

## 깊은 복사와 얕은 복사

- python 에서는 하나의 컨벤션 안에 같은 값이 있으면 같은 곳을 가리키게 해서 저장하고있다. (메모리 효율을 증가시키기 위해서)

```python
# 아무런 복사도 이뤄지지 않은 상태
# 같은 공간을 l, ll이 가리키고 있음
l = [[1,2,3],[4,5,6]]
ll = l
ll[0][0] = 10
print(l, ll)
print(id(l) == id(ll)) ## list 객체가 가리키는 주소가 같다
```

    [[10, 2, 3], [4, 5, 6]] [[10, 2, 3], [4, 5, 6]]
    True

```python
# python 에서는 하나의 컨벤션 안에 같은 값이 있으면 같은 곳을 가리키게 해서 저장하고있다.
# (메모리 효율을 증가시키기 위해서)
l = [1000,2000,3000,1000,1000,1000]
id(l[0]),id(l[3]),id(l[4]),id(l[5])  ## 모두 같은 값을 가지고 있음
```

    (140688095079824, 140688095079824, 140688095079824, 140688095079824)

```python
# 얕은 복사
l = [1000, 2000, 3000, 4000, 5000, 6000]
ll = l.copy()
# ll[0] = 10  ## ll[0]만 변경됨
print(l, ll)
print(id(l[0]) == id(ll[0]))      # 얕은 복사를 해도 리스트 안에 들어간 값은 같은 주소를 가리키고 있음. -5~256 아니어도
print(id(l) == id(ll))            # 각 리스트는 다른 공간에 선언되어 있다.
```

    [1000, 2000, 3000, 4000, 5000, 6000] [10, 2000, 3000, 4000, 5000, 6000]
    False
    False

```python
# 얕은 복사
l = [1,2,3,4,5,6]
ll = l.copy()   # list의 메서드 copy는 얕은 복사
print(id(l) != id(ll))
```

    True

```python
# 얕은 복사
l = [[1,2,3],[4,5,6]]
ll = l.copy()
# ll[0][0] = 10     # l[0][0]과 같이 수정됨 >> 얕은복사는 1 depth만 복사
ll[0] = 100         # ll만 수정됨. >> 1depth라서 l과 ll은 다르다
l, ll
```

    ([[1, 2, 3], [4, 5, 6]], [100, [4, 5, 6]])

```python
id(l[0]),id(ll[0])
```

    (140688095079824, 140688095080208)

- 깊은복사

```python
# 깊은 복사
import copy
l = [[1, 2, 3], [4, 5, 6]]
ll = copy.deepcopy(l)
ll[0][0] = 10

# 모든 차원에 있는 원소의 주소가 다 다름
print(id(l), id(ll))
print(id(l[0]), id(ll[0]))
print(id(l[0][0]), id(ll[0][0]))
```

    140688091500032 140688091499968
    140688092484544 140688092637632
    140689408082160 140689408082448

```python
# 깊은 복사
import copy

l = [[1,2,[1,[999,998]]], [4,5,[2,[333,332]]]]
ll = copy.deepcopy(l)
ll[0][2][1][0] = 10     # ll만 수정됨
print(l)
print(ll)
print(id(l), id(ll))
print(id(l[0]), id(ll[0]))
print(id(l[0][0]), id(ll[0][0]))
```

    [[1, 2, [1, [999, 998]]], [4, 5, [2, [333, 332]]]]
    [[1, 2, [1, [10, 998]]], [4, 5, [2, [333, 332]]]]
    140688637413824 140688093000960
    140688092756800 140688093976128
    140689408082160 140689408082160

- 얕은 복사는 1 계층만 복사합니다.
  > .copy(), slicing( [ ] ), sorted() ...
- 깊은 복사는 n 계층까지 모두 복사합니다.

- 나를 이해시키는 단 하나의 코드는 반드시 존재합니다.

- 얕은복사 기타등등

```python
# sorted도 얕은 복사!
l = [[1,2],[3,4],[5,6]]
ll = sorted(l)
ll[0][0] = 10           # 얕은 복사라 2차원 원소는 같이 바뀜
print(l, ll)
print(id(l) == id(ll))  # 얕은 복사라 리스트 id는 다름
```

    [[10, 2], [3, 4], [5, 6]] [[10, 2], [3, 4], [5, 6]]
    False

```python
# 얕은 복사
# copy를 써도 마찬가지. slicing으로 복사하는것은 얕은복사
l = [[1, 2, 3], [4, 5, 6]]
ll = l[:]
l[0] = 100      # 한쪽만 바뀜
l, ll
```

    ([100, [4, 5, 6]], [[1, 2, 3], [4, 5, 6]])

```python
# 얕은 복사
# copy를 써도 마찬가지. slicing으로 복사하는것은 얕은복사
l = [[1, 2, 3], [4, 5, 6]]
ll = l[:]
l[0][0] = 100       # 한쪽만 바뀜
l, ll
```

    ([[100, 2, 3], [4, 5, 6]], [[100, 2, 3], [4, 5, 6]])

```python
# 얕은 복사
# 리스트 컴프리헨션은 안배운 내용이니 keep
# for 배운다음 다시 와서 복습하기!
l = [[1, 2, 3], [4, 5, 6]]
ll = [i for i in l]
l[0][0] = 100
l, ll
```

    ([[100, 2, 3], [4, 5, 6]], [[100, 2, 3], [4, 5, 6]])

```python
# 1단계 깊은 복사
# 리스트 컴프리헨션은 안배운 내용이니 keep해두시고
# for문 배운다음 다시 오셔서 복습하시기를 권해드립니다.
l = [[1, 2, 3], [4, 5, 6]]
ll = [i[:] for i in l]
l[0][0] = 100
l, ll
```

    ([[100, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]])

## 다차원 리스트

```python
a = [[1, 2, 3],
     [11, 22, 33],
     ['leehojun', 20, 30]]

# jun 만 뽑아주세요

print(a[2][0][-3:])
print(a[2][0][5:])
```

    jun
    jun

## 리스트에서 built-in function 이용

```python
#1차원
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(max(a)) #최댓값
print(min(a)) #최솟값
print(sum(a)) #전체값의 합
```

    8
    1
    36

```python
#2차원
a = [[1, 2, 3],
     [11, 22, 33],
     [10, 2000, 30]]
print(max(a))   # 리스트 비교시 첫번째 요소로 비교함
print(min(a))
# sum(a) # error    # 요소가 리스트인 리스트는 sum을 못함
max(a, key=lambda x:x[1])   # min과 max도 key를 주어서 기준값을 설정해줄 수 있음
min(a, key=lambda x:x[1])
# sum(a) error
sum(a, [])
```

    [11, 22, 33]
    [1, 2, 3]





    [1, 2, 3, 11, 22, 33, 10, 2000, 30]

```python
#2차원
a = [[1, 2, 3, 'a'],
     [11, 22, 33, 'aaa'],
     [10, 2000, 30, 'aa']]

print(max(a, key=lambda x:x[1]))
max(a, key=lambda x:len(x[3])) # 같은문자 반복일경우 더긴거~
```

    [10, 2000, 30, 'aa']





    [11, 22, 33, 'aaa']

```python
# 이름, 별점, 객실 수, 가격
호텔 = [
    ['이스트소프트 호텔', 5, 100, 155000],
    ['삼스트소프트 호텔', 4, 80, 145000],
    ['사스트소프트 호텔', 2, 70, 135000],
      # 마지막에 콤마를 허락하는 언어는 제한적(특히 JSON에서는 엄격해서 허락하지 않습니다.)
      ]

max(a, key=lambda x:x[3])   # 가장 가격이 높은 것을 뽑아낼 수 있음
min(a, key=lambda x:x[3])   # 가장 가격이 저렴한 것을 뽑아낼 수 있음

```

- 제이슨 제너레이터
- https://json-generator.com/
- 자주 사용하면서 익숙해지길?

## 리스트의 순회

```python
#1차원
a = [1, 2, 3, 4, 5, 6, 7, 8]

for i in a:     # for 변수 in 순회가능한객체:
     print(i)
```

    1
    2
    3
    4
    5
    6
    7
    8

```python
#2차원
a = [[1, 2, 3],
     [11, 22, 33],
     [13, 20000, 300000]]

for i in a:
    print(i)
    print('---')
print('end')
```

    [1, 2, 3]
    ---
    [11, 22, 33]
    ---
    [13, 20000, 300000]
    ---
    end

```python
#2차원
a = [[1, 2, 3],
     [11, 22, 33],
     [13, 20000, 300000]]

for i in a:
    for j in i:
        print(j, end=' ')
    print('\n---')
print('end')
```

    1 2 3
    ---
    11 22 33
    ---
    13 20000 300000
    ---
    end

## range

```python
# range(start, stop, step)
# 슬라이싱 같은 규칙
# 슬라이싱은 ':' 콜론으로 연결
# range 는 ',' 컴마로 연결

print(list(range(100)))
# 2.x 에는 list였지만, 3.x에서는 range 클래스로 바뀌어 형변환 해줘야함

print(list(range(5, 10)))

print(list(range(0, 101, 2))) #짝수
print(list(range(1, 101, 2))) #홀수
print(list(range(100, 1, -2)))

print(sum(range(0,101))) # sum은 iterable이면 합할 수 있기 때문에 list로 형변환 하는건 리소스 낭비

```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    [5, 6, 7, 8, 9]
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
    [100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
    5050

## list comprehension

```python
# l = [1,2,3,4, ...] # 너무 힘들다
# list(range(1,101)) # 리소스 낭비

# for 문으로 넣기
l = []
for i in range(1, 101):
    l.append(i)

```

```python
# for 문으로 넣기. 원소 연산해서 넣을 수있음
l = []
for i in range(1, 11):
    l.append(i**i)

l

l = [i**i for i in range(1,11)]
l

l = [i for i in range(1,11)]
l

```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

```python
l = []
for i in range(1, 100):
    if i %3 == 0 or i %5 == 0:
        l.append(i)

a = [i for i in range(1, 100) if i %3 == 0 or i %5 == 0]
a
```

## tuple(튜플)

- 튜플은 순서가 있는 시퀀스형 자료형입니다.
- 참조값은 변경이 불가능(immutable) 합니다.
- 다른 자료형을 입력할 수 있으며, 튜플 안에 튜플로 다차원의 튜플을 만드는 것도 가능합니다.
- 값의 중복을 허락합니다.

```python
t = (10,20,30)
# t[1] = 1000 # error
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-112-bf7b4a9b8e82> in <cell line: 2>()
          1 t = (10,20,30)
    ----> 2 t[1] = 1000 # error


    TypeError: 'tuple' object does not support item assignment

```python
l = [1, 2, 3]
t = (l, 20, 30) # tuple에서 불변인 것은 t가 l을 참조하고 있다는 것
l[0] = 1000     # tuple 안의 list 의 원소는 변경이 가능하다
t
```

    ([1000, 2, 3], 20, 30)

```python
# tuple 도 slicing 가능하다.
# slicing은 새로운 tuple을 만들어줌!
t = (10,20,30,40,50)
print(t[:2])
```

    (10, 20)

```python
print(type(t))
dir(t)
```

    <class 'tuple'>





    ['__add__',
     '__class__',
     '__class_getitem__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__mul__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rmul__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'count',
     'index']

```python
# 메서드 count, index
t = (10,20,30,40,50,20)
t.index(20), t.count(20)
```

    (1, 2)

```python
t = tuple('leehojun')
print(t)
t = tuple()
print(t)
t = tuple(range(10))
print(t)
t = (1)     #이렇게 넣으면 상수 취급함
print(t)
t = (1,)    #원소 하나인 tuple은 마지막에 ,
print(t)
```

    ('l', 'e', 'e', 'h', 'o', 'j', 'u', 'n')
    ()
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    1
    (1,)





    'a'

## dictionary(딕셔너리)

- 딕셔너리는 순서가 없는 자료형입니다.
- 사전형은 Key와 Value 가 하나의 묶음으로 이루어진 자료 체계입니다.
- 값의 변경이 가능합니다.
- 다른 자료형을 입력할 수 있습니다.
- 키의 중복은 허락하지 않고, 값의 중복을 허락합니다.

> dict는 Python 3.6 버전부터 순서를 저장하는 구조로 변경되었습니다. 따라서 순서를 보장하지 않는 다는 말은 3.5 이하 버전에서는 맞고, 3.6이상 버전에서는 틀린 말입니다. <br>
> 좋은 아티클 : https://blog.hwahae.co.kr/all/tech/6662

```python
data = [{
    '게시물 번호': 1,
    '게시자': '이호준',
    '게시물 내용': '...'
},{
    '게시물 번호': 1,
    '게시자': '이호준',
    '게시물 내용': '...'
},{
    '게시물 번호': 1,
    '게시자': '이호준',
    '게시물 내용': '...'
}]

data[0]['게시자']
data[1]['게시물 내용'] = '강의내용 대박'
data
```

    [{'게시물 번호': 1, '게시자': '이호준', '게시물 내용': '...'},
     {'게시물 번호': 1, '게시자': '이호준', '게시물 내용': '강의내용 대박'},
     {'게시물 번호': 1, '게시자': '이호준', '게시물 내용': '...'}]

```python
d = {'one' : '하나', 'two' : '둘', 'three' : '셋'}
d['one']
```

    '하나'

```python
d['two'] = '투'
d
```

    {'one': '하나', 'two': '투', 'three': '셋'}

- dictionary 생성하는 다양한 방법

```python
d = {}  # 비어있는 dict
print(type(d))  #dict

d = {10} #set
print(type(d))

d = dict()
print(type(d))  #dict

d = {'one':1}
print(type(d)) #dict
```

    <class 'dict'>
    <class 'set'>
    <class 'dict'>
    <class 'dict'>

```python
d = {'one' : '하나', 'two' : '둘', 'three' : '셋'}
d.items()
```

    dict_items([('one', '하나'), ('two', '둘'), ('three', '셋')])

```python
dict([('one', '하나'), ('two', '둘'), ('three', '셋')])
```

    {'one': '하나', 'two': '둘', 'three': '셋'}

```python
dict([['one', '하나'], ['two', '둘'], ['three', '셋']])
```

    {'one': '하나', 'two': '둘', 'three': '셋'}

```python
dict(name='leehojun', age=10)
```

    {'name': 'leehojun', 'age': 10}

```python
print(list(zip('ABC', '123', 'abc')))

# zip으로 dictionary 생성할 수 있음
dict(zip('ABC', '123')) #형변환.
```

    [('A', '1', 'a'), ('B', '2', 'b'), ('C', '3', 'c')]





    {'A': '1', 'B': '2', 'C': '3'}

```python
# 연습문제
# dict와 list를 사용해서 아래와 같은 형태로 데이터를 만들어주세요
# 원하는 형태{'ㅁ': [10,20], 'B': [20,30], 'C': [30,40]}
print(dict(zip(['A','B','C'], [[10,20],[20,30],[30,40]])))
print(dict(zip('ABC', [[10,20],[20,30],[30,40]])))
print(dict(zip('ABC', [list(element) for element in zip([10,20,30],[20,30,40])])))

l = [10,20,30,40]
dict(zip('ABC', zip(l,l[1:])))
```

    {'A': [10, 20], 'B': [20, 30], 'C': [30, 40]}
    {'A': [10, 20], 'B': [20, 30], 'C': [30, 40]}
    {'A': [10, 20], 'B': [20, 30], 'C': [30, 40]}





    {'A': (10, 20), 'B': (20, 30), 'C': (30, 40)}

```python
# dict 의 in 연산자
# key의 포함 여부를 확인할 수 있음
'B' in {'A': (10, 20), 'B': (20, 30), 'C': (30, 40)}
```

    True

```python
# built in function len 사용가능
len({'A': (10, 20), 'B': (20, 30), 'C': (30, 40)})
```

    3

- get()
- ['key'] 와 같은 결과이지만 [ ]는 없는 key를 검색할 경우 에러를 뱉지만, get()은 None을 리턴함
- get() 함수의 두번째 인사로 없는 key 검색 시 리턴할 default 값을 설정할 수 있다

```python
# dictionary 메서드 get()
# key 값으로 value 값을 찾음
# python 은 switch 구문이 없어서 dictionary로 구현했었는데~
# 아래 match case 구현되어서 구 문법이 되었군요...
def switch(day):
    return {
        1 : '월요일',
        2 : '화요일',
        3 : '수요일',
        4 : '목요일',
        5 : '금요일',
        6 : '토요일',
        7 : '일요일',
    }.get(day, '요일을 찾지 못했습니다.')

switch(7)
## 이 구문의 문제점은 없는 key를 입력했을 때 erorr가 발생함
# switch(8) # error
switch(8) #get을 사용하면 None을 주는데, get에 인자로 못찾는 값일 때 리턴할 값을 설정할 수 있습니다.
```

    '요일을 찾지 못했습니다.'

```python
# 3.10 버전에 switch 도입됨
# match case (https://codechacha.com/ko/python-switch-case/)
def number_to_string(agrument):
    match agrument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
            return "nothing"


print(number_to_string(0))
print(number_to_string(1))
print(number_to_string(2))
print(number_to_string(3))
print(number_to_string(4))
```

    zero
    one
    two
    nothing
    nothing

```python
!python --version
```

    Python 3.10.11

```python
%%timeit
# 시간재는것
s = 0
for i in range(1000):
    s +=1
# 라인 바이 라인으로 풀어져서 pvm(python virtual machine)에서 돌아가서 느림
```

    108 µs ± 40.7 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

```python
%%timeit
sum([i for i in range(1000)])
# list comprehension이 for문보다 빠르지만 list로 형변환이 있음
```

    77.7 µs ± 3.34 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

```python
%%timeit
sum(range(1000))
# 형변환도 안해서 빠름
```

    36.9 µs ± 1.39 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

- keys(), values(), items()

```python
# key 값만
{'A': (10, 20), 'B': (20, 30), 'C': (30, 40)}.keys()
```

    dict_keys(['A', 'B', 'C'])

```python
# vlaue 값만
{'A': (10, 20), 'B': (20, 30), 'C': (30, 40)}.values()
```

    dict_values([(10, 20), (20, 30), (30, 40)])

```python
# 쌍으로
{'A': (10, 20), 'B': (20, 30), 'C': (30, 40)}.items()
```

    dict_items([('A', (10, 20)), ('B', (20, 30)), ('C', (30, 40))])

```python
# fromkeys 는 가끔사용
dict.fromkeys('leehojun')
```

    {'l': None, 'e': None, 'h': None, 'o': None, 'j': None, 'u': None, 'n': None}

```python
# 모든 value에 두 번째 인자의 값이 들어감
dict.fromkeys('leehojun', 100)
```

    {'l': 100, 'e': 100, 'h': 100, 'o': 100, 'j': 100, 'u': 100, 'n': 100}

```python
keys = ('name','age','grade')
values = ('leehojun','10','수')
dict.fromkeys(keys, values)
```

    {'name': ('leehojun', '10', '수'),
     'age': ('leehojun', '10', '수'),
     'grade': ('leehojun', '10', '수')}

```python
# update
d = {'one' : '하나', 'two' : '둘', 'three' : '셋'}
d.update({'one' : 1, 'two' : 2})
d
```

    {'one': 1, 'two': 2, 'three': '셋'}

## 딕셔너리 순회

```python
# key만 순회합니다.
d = {'two' : 2, 'three' : '셋'}
for i in d:
    print(i)

```

    two
    three

```python
# value 는 이렇게~
d = {'two' : 2, 'three' : '셋'}
for i in d:
    print(d[i])
```

    2
    셋

## 언패킹

```python
# 패킹   : 1, 2, 3 => [1,2,3]
# 언패킹 : [1,2,3] => 1, 2, 3
```

```python
a, b, c = (10, 20, 30)  #소괄호든 대괄호든 각각 값이 들어감
a
```

    (10, 20, 30)

```python
i, j = [10,20]
```

```python
# 위에랑 같은 원리
for i, j in [[10,20], [30,40],[50,60]]:
    print(i, j)
```

    10 20
    30 40
    50 60

```python
for i, j, k in [[10, 20, [1, 2]], [30, 40, [3, 4]], [50, 60, [5, 6]]]:
    print(i, j, k)
```

    10 20 [1, 2]
    30 40 [3, 4]
    50 60 [5, 6]

```python
# value swap
a = 10
b = 15
a, b = b ,a
a, b
```

    (15, 10)

```python
d = {'A': (10, 20), 'B': (20, 30), 'C': (30, 40)}
for i, j in d.items(): # items는 쌍으로 주기 때문에 i, j로 받음
    print(i, j)
```

## max를 이용한 dict 최대 value의 key 값 가져오기

```python
d = {
    'test1' : 10,
    'test2' : 20,
    'test3' : 31,
    'test4' : 11,
}

max(d.values()) # 최대인 value만 찾을 뿐..
print(max(d, key=lambda x : d[x]))
print(max(d, key=d.get))            ## 많이 사용하는 코드
```

    test3
    test3

```python
## 두개 이상의 dictionary를 새 dict()로 병합하기
a = {'2' : 2, '4' :4}
b = {'1' : 1 , '3' : 3}
c = {'a' : 64 , 'b' : 77}

## 이 방식으로는 key가 겹치면 뒤에 있는 값으로 덮어씌워진다.
d = dict(a, **b)
print(d)
d = dict(a, **b, **c)
print(d)
```

    {'2': 2, '4': 4, '1': 1, '3': 3}
    {'2': 2, '4': 4, '1': 1, '3': 3, 'a': 64, 'b': 77}

```python
## key value 바꾸기
d = {'a' : 64 , 'b' : 77}

newd = {}
for key, value in d.items():
    newd[value] = key

print(newd)

# dictionary comprehension
print({v:k for k,v in d.items()})

# zip으로 dict
print(dict(zip(d.values(), d.keys())))
```

    {64: 'a', 77: 'b'}
    {64: 'a', 77: 'b'}
    {64: 'a', 77: 'b'}

## set(셋, 집합)

- 집합 자료형은 중복을 허용하지 않으며
- 순서가 없는 자료형
-

```python
n = set([1,1,2,2,3,3,4])
print(n)
```

    {1, 2, 3, 4}

```python
s = set('hello world')
print(s)
```

    {'h', 'o', 'w', ' ', 'e', 'l', 'd', 'r'}

```python
# add 값 1개 추가할 때
n = set([1,1,2,2,3,3,4])
n.add(1000)
print(n)
```

    {1, 2, 3, 4, 1000}

```python
# update 값 여러개 추가할 때
n = set([1,1,2,2,3,3,4])
n.update([1000, 2000, 3000])
print(n)
```

    {1, 2, 3, 4, 1000, 2000, 3000}

```python
# remove 값이 없으면 오류를 출력함.
# discard는 지유려는 값이 없어도 오류를 출력하지 않음
n = set([1,1,2,2,3,3,4])
n.remove(1)
print(n)
n.discard(1)

```

    {2, 3, 4}

- pop 은 실무에서 잘 사용하지 않습니다. 값을 랜덤하게 뽑아내기 때문입니다. 높은 확률로 앞에서부터 뽑아내긴 하지만 확률에 기대는 코딩을 하지 않기를 바랍니다. 공식문서에서는 랜덤하게 뽑아낸다고 되어 있습니다.

  > https://docs.python.org/3.11/library/stdtypes.html#frozenset.pop

```python
# 교집합. 별 3개
a = {1, 2, 3}
b = {3, 4, 5}
print(a&b) #교집합
print(a.intersection(b))
```

    {3}
    {3}

```python
# 합집합.
a = {1, 2, 3}
b = {3, 4, 5}
print(a|b)
print(a.union(b))
# a + b # error
```

    {1, 2, 3, 4, 5}
    {1, 2, 3, 4, 5}

```python
# 차집합
# 이녀석은 다행히 사칙연산 - 가 됨
my_cafe = set(['americano', 'water', 'yogurt strawberry blended', 'cafe latte'])
other_cafe = set(['americano', 'water', 'green tea'])

print(my_cafe - other_cafe)
print(my_cafe.difference(other_cafe))
```

    {'cafe latte', 'yogurt strawberry blended'}
    {'cafe latte', 'yogurt strawberry blended'}

```python
# 대칭차집합 안중요함
# A와 B 집합의 합집합에서 교집합을 뺀 것
s = {1, 2, 3, 4}
ss = {3, 4, 5, 6}

s^ss
set.symmetric_difference(s, ss)
```

    {1, 2, 5, 6}

```python
# .issubset()
# 호출한 set이 인자의 subset인지...
s = {1, 2, 3, 4}
ss = {3, 4, 5, 6}
print(s.issubset({1, 2}))       # s가 {1,2} 의 서브셋이냐
print(s.issubset({1, 2, 3, 4, 5, 6}))  # s가 {1, 2, 3, 4, 5, 6}의 서브셋이냐

s < {1, 2, 3, 4, 5, 6} #진부분집합(<->진상위집합)
s <= {1, 2, 3, 4, 5, 6} #부분집합(<->상위집합)
```

    False
    True





    True

```python
# 코딩 테스트 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/120888
# my_string     result
# "poeple"      "peol"
def solution(my_string):
    answer = ''
    return set(my_string)

solution('people')
```

    {'e', 'l', 'o', 'p'}

```python
# set으로 안풀기
result = ''
for i in "people":
    if i not in result:
        result += i

result
```

    'peol'

```python
# 그냥 set으로 바꾸면 순서가 엉망진창!
def solution(my_string):
    answer = ''
    return ''.join(set(my_string))

solution('people')
```

    'leop'

```python
# set으로 풀기
def solution(my_string):
    s = set(my_string)
    result = ''
    for i in my_string:
        if i in s:
            result += i
            s.remove(i)

    return result

solution('people')
```

    'peol'

## !! 연습문제

```python
# 연습문제1
student_score = {
		'홍의': 97,
		'원희': 60,
		'동해': 77,
		'변수': 79,
		'창현': 89,
}

# 학생들의 **총점**을 구하는 코드를 작성하세요.
a = sum(student_score.values())
print(a)

# 학생들의 **평균 점수**를 구하는 코드를 작성하세요.
b = sum(student_score.values()) / len(student_score)
print(b)

# 점수가 가장 **높은** 학생의 이름과 그 점수를 구하는 코드를 작성하세요.
c = max(student_score, key=student_score.get)
print(c, max(student_score.values()))
print(c, student_score.get(c)) # == student_score[c]

# 점수가 가장 **낮은** 학생의 이름과 그 점수를 구하는 코드를 작성하세요.
d = min(student_score, key=student_score.get)
print(d, min(student_score.values()))
```

    402
    80.4
    홍의 97
    홍의 97
    원희 60

```python
# 연습문제2
like = ['볶음밥', '라면', '국수', '파스타', '치킨', '짜장면', '국밥']
dislike = ['국밥', '짬뽕', '찜닭', '파스타', '국수', '카레', '덮밥']
menu = list(set(like) - set(dislike))
print(list(set(like).difference(set(dislike))))
print(menu)
```

    ['라면', '치킨', '짜장면', '볶음밥']
    ['라면', '치킨', '짜장면', '볶음밥']

## !! 오늘 배운 것 정리 230504

1. sort

   - sorted는 원본을 만지지 않는 'built-in function', 정렬입니다.
   - sort는 원본을 만지는 '리스트 메서드', 정렬입니다.
   - sort의 다양한 예

     ```python
     l = [[1, 10, 'leehojun'],
         [20, 30, 'hojun'],
         [10, 20, 'weniv!'],
         [1, 2, 'hello world'],
         [55, 11, 'sun']]

     # 1. 글자 수 대로 정렬해주세요.
     def f(x):
         return len(x[2])

     print(sorted(l, key=f, reverse=False))
     print(sorted(l, key=lambda x:len(x[2]), reverse=False))

     # 2. 맨 앞에 위치한 숫자대로 정렬해주세요.
     def f2(x):
         return x[0]

     print(sorted(l))
     print(sorted(l, key=f2))
     print(sorted(l, key=lambda x:x[0]))

     # 3. 중앙에 위치한 값대로 정렬해주세요.

     def f3(x):
         return x[1]

     print(sorted(l))
     print(sorted(l, key=f3))
     print(sorted(l, key=lambda x:x[1]))

     l = [[1, 10, 32],
         [20, 30, 11],
         [10, 20, 22],
         [1, 2, 13],
         [55, 11, 44]]

     # 4. 3개의 전체 합이 작은 순서대로 출력해주세요.

     def f4(x):
         return x[0] + x[1] + x[2]

     def f5(x):
         return sum(x)

     print(sorted(l, key=f4))
     print(sorted(l, key=f5))
     print(sorted(l, key=lambda x: sum(x)))
     print(sorted(l, key=sum))
     ```

2. 깊은 복사와 얕은 복사

   1. 깊은 복사 : 완전히 다른 객체를 만듭니다.(깊은 복사는 n 계층까지 모두 복사)

      ```python
      # 깊은 복사
      import copy

      l = [[1, 2, 3], [4, 5, 6]]
      ll = copy.deepcopy(l)
      ll[0][0] = 10
      l, ll
      ```

   2. 얕은 복사 : 내용물은 같은 다른 객체를 만듭니다.(얕은 복사는 1 계층만 복사)
      ```python
      # 얕은 복사
      l = [[1, 2, 3], [4, 5, 6]]
      ll = l[:] # l.copy, sorted를 써도 마찬가지입니다.
      l[0][0] = 100
      l, ll
      ```

3. range

   ```python
   # range(start, stop, step)
   # 슬라이싱은 ':'(콜론)으로 연결되어 있고
   # range는 ','(콤마)로 연결되어 있습니다.

   print(list(range(100)))
   # python 2.x에서 python 3.x에 range를 사용하고 싶다면 xrange(10)
   print(list(range(5, 10)))

   print(list(range(0, 101, 2))) #짝수
   print(list(range(1, 101, 2))) #홀수
   print(list(range(100, 1, -2)))
   print(sum(list(range(0, 101))))
   print(sum(range(0, 101))) # 이렇게 형 변환을 하지 않고 sum하시는 것을 권합니다.
   ```

4. list comprehension

   ```python
   # l = []
   # for i in range(1, 11):
   #     l.append(i**i)
   # l

   l = [i**i for i in range(1, 11)]
   l
   ```

5. tuple

   - 튜플은 순서가 있는 시퀀스형 자료형입니다.
   - 참조값은 변경이 불가능(immutable) 합니다.
     ```python
     t = (10, 20, 30)
     t[1] = 1000 # error
     ```
   - 다른 자료형을 입력할 수 있으며, 튜플 안에 튜플로 다차원의 튜플을 만드는 것도 가능합니다.
   - 값의 중복을 허락합니다.
   - 메서드는 index와 count밖에 없습니다.

6. dict (딕셔너리, 사전형)

   - 딕셔너리는 순서가 없는 자료형입니다.
   - 사전형은 Key와 Value 가 하나의 묶음으로 이루어진 자료 체계입니다.
   - 값의 변경이 가능합니다.
     ```python
     d = {'one' : '하나', 'two' : '둘', 'three' : '셋'}
     print(d['one']) # 호출
     d['two'] = '투' # 변경
     d
     ```
   - 다른 자료형을 입력할 수 있습니다.
   - 키의 중복은 허락하지 않고, 값의 중복을 허락합니다.
   - dict를 활용한 switch 만들기

     ```python
     def switch(day):
         return {
             1 : '월요일',
             2 : '화요일',
             3 : '수요일',
             4 : '목요일',
             5 : '금요일',
             6 : '토요일',
             7 : '일요일',
         }.get(day, '요일을 찾지 못했습니다.')

     switch(8)
     ```

   - max를 이용한 dict 최대 value의 key값 가져오기

     ```python
     d = {
         'test1': 10,
         'test2': 20,
         'test3': 31,
         'test4': 11,
     }

     # max(d.values()) # 이걸로는 뭔가 찾아내기 힘듭니다.
     max(d, key=lambda x: d[x])
     max(d, key=d.get) #많이 사용하는 코드입니다.
     ```

7. 언패킹

   - 언패킹 예
     ```python
     for i, j, k in [[10, 20, [1, 2]], [30, 40, [3, 4]], [50, 60, [5, 6]]]:
         print(i, j, k)
     ```
   - swap 예
     ```python
     # swap
     a = 10
     b = 15
     a, b = b, a
     a, b
     ```

8. set (셋, 집합)
   - 집합 자료형은 중복을 허용하지 않으며
   - 순서가 없는 자료형
     ```python
     n = set([1, 1, 2, 2, 3, 3, 4])
     print(n)
     ```
   - 메서드
     - add : 값 추가
     - update : 값 여러개 추가
     - remove : 제거
     - copy : 값 복사
     - union : 합집합
     - intersection : 교집합
     - difference : 차집합
     - issubset : 부분집합

```python
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import re  # re module <- regex

import csv
import os

path = os.getcwd()
file_ls = os.listdir(path)
file_ls

```

    ['.config', 'sample_data']

## (질의응답) max(student_score, key=student_score.get) 은 어떻게 동작하는가?

```python
def f(x):
    print(x, ll[x])
    return ll[x]

l = [2, 4, 5, 3, 6, 0, 7, 1]
ll = [10, 20, 30, 40, 50, 60, 70, 80]

max(l, key=f)
```

    2 30
    4 50
    5 60
    3 40
    6 70
    0 10
    7 80
    1 20





    7

```python
max(student_score, key=student_score.get)
```

```python
def f(x):
    print(x, len(ll[x]))
    return len(ll[x])

l = [2, 4, 5, 3, 6, 0, 7, 1]
ll = ['hello', 'a', 'bb', 'ccc', 'a', 'bbbb', 'hello world', 'cc']

max(l, key=f)
```

    2 2
    4 1
    5 4
    3 3
    6 11
    0 5
    7 2
    1 1





    6

```python
def 함수(x):
    return d.get(x)

d = {
      'test1': 10,
      'test2': 20,
      'test3': 31,
      'test4': 11,
}

# max(d, key=함수)
# max(d, key=lambda x: d[x])
# max(d, key=d.get)
```

    'test3'

```python
def f(x):
    return len(x)
l = ['a', 'bb', 'ccc', 'dd']

# max(l, key=len)
max(l,key=f)
```

    'ccc'

```python
def 함수(x):
    return d.get(x)

수학 = {
      '학생1': 10,
      '학생2': 20,
      '학생3': 31,
      '학생4': 11,
}

과학 = {
      '학생1': 11,
      '학생2': 17,
      '학생3': 13,
      '학생4': 11,
      '학생5': 25,
      '학생6': 100
}

수학점수가가장큰사람 = max(수학, key=수학.get)
과학점수가가장큰사람 = max(과학, key=과학.get)
print(max(수학, key=과학.get))
sorted(수학, key=과학.get)
```

    학생2





    ['학생1', '학생4', '학생3', '학생2']

## (질의응답) 함수 아규먼트 순서

```python
def f(a, b, c):
    print(a, b, c)

# f() # error
# f(100, 10) # error
f(a=100, b=200, c=300)
f(c=300, a=100, b=200)  # 실무에서 이렇게 순서를 바꿔서 넣지 않고 지켜준다.

# 실무에서 언제 사용할까?
# 파라메터, 아규먼츠가 매우 많을 때! # 참고. roro패턴?
# 이런 함수가 나오면 이 함수가 무엇을 뜻하는 것일까요?
# addNewControl("Title", 20, 50, 100, 50, 200, 300, 150)
# addNewControl(title="Title", height=20, width=50, textlen = 100, ...)
# 어? 컨트롤 박스를 만드는 구나...
```

    100 200 300
    100 200 300

```python
# 파라메터에 default 값을 설정할 수 있다.
# 이때는 파라메터에 값을 전달하지 않아도 dafault값으로 적용됨
def f(a=10, b=20, c=30):
    print(a, b, c)

f()
f(100, 10)
f(a=100, b=200, c=300)
f(c=300, a=100, b=200)
```

    10 20 30
    100 10 30
    100 200 300
    100 200 300

```python
# c만 default value를 안주게 되면 error, 순서대로 안주어야 합니다.
# default를 안주려면 순서대로 안주어야 함
def f(a=10, b=20, c):
    print(a, b, c)

# f() # error
# f(100, 10) # error
# f(a=100, b=200, c=300) # error
# f(c=300, a=100, b=200) # error
# f(c=300) # error
```

```python
# 순서대로 default값을 안 주어야 하기 때문에 a에 값을 주지 않은 경우
def f(a, b=20, c=10):
    print(a, b, c)

# f() # error
f(7)
f(100, 10)
f(a=100, b=200, c=300)
f(c=300, a=100, b=200)
```

    7 20 10
    100 10 10
    100 200 300
    100 200 300

## (질의응답) zip, map등 한 번 순회가 되면 순회가 안 되는 이유

- zip, map, filter, reversed etc..

```python
a = [1, 2, 3]
b = ['a', 'b', 'c']

z = zip(a, b)
print(list(z)) # [(1, 'a'), (2, 'b'), (3, 'c')]

# zip 객체는 한 번 사용되었으므로 빈 리스트가 반환됩니다.
print(list(z)) # []
```

    [(1, 'a'), (2, 'b'), (3, 'c')]
    []

```python
li = [1, 2, 3]
st = ['a', 'b', 'c']
z = zip(li, st)

for i in z:
    print(i)

for i in z:
    print(i)
```

    (1, 'a')
    (2, 'b')
    (3, 'c')

```python
li = [1, 2, 3]
st = ['a', 'b', 'c']
i = iter(zip(li, st))
next(i)
# next(i)
# next(i)
# next(i) # StopIteration
# for 문도 StopIteration이 발생하기 전까지만 돌리고
# 예외가 발생하면 루프를 나가도록 예외처리가 되어있습니다.
```

    (1, 'a')

```python
li = [1, 2, 3]
z = map(lambda x:x**2, li)

for i in z:
    print(i)

for i in z:
    print(i)
```

    1
    4
    9

```python
li = [1, 2, 3]
z = reversed(li)

for i in z:
    print(i)

for i in z:
    print(i)
```

    3
    2
    1

```python
li = [1, 2, 3]
z = filter(lambda x:x>1, li)

for i in z:
    print(i)

for i in z:
    print(i)
```

    2
    3

```python
# sorted는 많이 사용되는 함수라
# 계속 순회가 가능하게 설계가 되어있습니다.
# 이런 설계를 뒤에서 우리가 직접 해보게 될 것입니다.
li = [1, 2, 3]
z = sorted(li)

for i in z:
    print(i)

for i in z:
    print(i)
```

    1
    2
    3
    1
    2
    3

## 조건문

- if, elif, else, continue, break

```python
x = 2
if x > 1 and x < 10:
	print('Hello')
```

    Hello

```python
if True:
    print('hello')
```

    hello

```python
if 1231415000:
    print('hello')
```

    hello

```python
def f():
    return False    # True
if f():
    print('hello')
    print('one')
print('two')
```

    two

```python
if '':  # [], {}, '' 는 모두 False 취급
    print('hello')
    print('one')
print('two')
```

    two

```python
if ' ':  # 공백은 공백문자가 있음
    print('hello')
    print('one')
print('two')
```

    hello
    one
    two

```python
if [               ]: # 이건 빈 list
    print('hello')
    print('one')
print('two')
```

    two

```python
if [,]: # syntax error
    print('hello')
    print('one')
print('two')
```

      File "<ipython-input-53-93a84ea78cc5>", line 1
        if [,]:
            ^
    SyntaxError: invalid syntax

```python
if [10,
    20,
    30, # 마지막 콤마는 허락. 소괄호, 중괄호, 대괄호에 공백은 병합합니다.
    ]:
    print('hello')
    print('one')
print('two')
```

    hello
    one
    two

```python
if None:
    print('flase')
```

```python
class int(int):
    def __eq__(self, next):
        return True

if int('11') == int('10'):  # == 는 __eq__
    print('hello')
```

    hello

```python
if 10 > 11:
    print('one')
    print('two')
print('three')
else:   # error
    print('four')

```

      File "<ipython-input-62-18edc0e13c27>", line 5
        else:
        ^
    SyntaxError: invalid syntax

```python
if 10 > 11:
    print('one')
    print('two')
else:
    print('three')

```

    three

```python
# else가 없어도 되는 경우
def f():
    if 10 >11:
        return 'one'
    return 'two'

print(f())
```

    two

```python
# 여러 개의 if 문을 단축할 수 있는 방법 =>
# 가독성이 좋아지는 것을 선택하세요! 정답은 없습니다.
# and 구문으로 if 구문을 합칠 수 있습니다.

x=10

if x > 5:
    if type(x) == int:
        print('one')

if x > 5 and type(x) == int: # 요런식을 선택하는 것을 권합니다
    print('one')
```

```python
x = 10

if x > 5:
    if type(x) == int:
        if x%2 == 0:
            print('one')

if x > 5 and type(x) == int and x%2==0:
    print('one')

print('oo')
```

    one
    one
    oo

```python
if True:
    print('hello')
else:
    print('hello')
else: # error
    print('hello')
else:
    print('hello')
```

```python

```

```python
if True:
    print('hello')
if True:
    print('hello')
if True:
    print('hello')
else:
    print('hello')
```

```python
if True:
    print('hello')
elif True:
    print('hello')
elif True:
    print('hello')
else:
    print('hello')
```

```python
elif True: # error 위에 구문이 있어야 합니다.
    print('hello')
elif True:
    print('hello')
else:
    print('hello')
```

```python
score = 81
money = 0

if score >= 90:     # 만약에 조건이 참이라면
    print('mom : i\'m so happy!')
    money += 1000000
elif score >= 80:   # 그렇지 않고 만약에 조건이 참이라면
    print('mom : i\'m happy!')
    money += 100000
elif score >= 70:    # '그렇지 않고 만약에' 에서 '그렇지 않고'가 만족이 안되기 때문에 실행되지 않음
    print('mom : i\'m so...!')
    money += 10000
elif score >= 60:
    print('mom : i\'m so...!')
    money += 1000
else:
    print('mom : i\'m...!')
print(money)
# if, elsif, else 구문을 함께 썼다면 한 덩어리가 되어
# 하나만 실행이 되고 나머지는 실행이 되지 않습니다.
```

    mom : i'm happy!
    100000

```python
# Ctrl + M    M 누르시면 마크다운
# Ctrl + M    Y 누르시면 코드블록
```

## if 심화

```python
# 강사님은 권장하지 않음
# 가독성을 떨어뜨린다고 생각하기 때문
if 10 > 5: print('hello') # 1줄에 사용하는 것이 가능합니다.
```

    hello

```python
if 1 > 5: print('hello')
elif 5 > 1: print('world')
```

    world

```python
if 1 > 5: print('hello')
elif 1 > 5: print('world')
else: print('hello world')
```

    hello world

```python
# 3항 연산자는 가독성을 해치지 않는 선에서 많이 사용함
print('one') if 5 > 1 else print('two')
```

    one

```python
# 괄호로 묶는 게...
(print('one') if 5 > 1 else print('two'))
```

```python
# error 이렇게 사용하지 않습니다!
# if 5 > 1 print('one') else print('two')

# 위 3항연산자와 같음
if 5 > 1:
    print('one')
else:
    print('two')

```

```python
# 할당이나 return에서 많이 사용합니다.
# 할당이나 return을 할 때 어떤 조건을 달고 싶을 경우
# 그런데 일반 if 문과 else문이 거창하다고 생각이 되었을 때
y = 100
x = 'one' if y > 80 else None

print(x)
```

    one

```python
def f(y):
    if y > 80:
        x = 'one'
    else:
        x = None
    return x

print(f(100))
print(f(30))
```

    one
    None

```python
def f(y):
    if y > 80:
        return 'one'
    return None

print(f(100))
print(f(30))
```

    one
    None

```python
# 위 if 문을 3항연산자로 바꾼다면
def f(y):
    return 'one' if y > 80 else None

print(f(100))
print(f(30))
```

    one
    None

```python
def custom_sum(x):
    return sum(x)

custom_sum([1,2,3,4,5,6])   # 다 더한 값 21
custom_sum([1,2,3,4,'5',6]) # float('inf')
```

```python
# 이해를 돕기 위해 만든 예제. 효율적이진 않습니다.
def custom_sum(x):
    return sum(x) if len(list(filter(lambda x: type(x)==int, x))) == len(x) else float('inf')

print(custom_sum([1,2,3,4,5,6]))   # 다 더한 값 21
custom_sum([1,2,3,4,'5',6]) # float('inf')
```

    21





    inf

```python
l = [1,2,3, '4','6']
print(list(filter(lambda x: type(x)==int, l)))
print(len(list(filter(lambda x: type(x)==int, l))))
print(len(l))
```

    [1, 2, 3]
    3
    5

```python
# 문제 다음 if문을 3항 연산자로 표현해주세요
# if x %2 == 0:
#     홀짝여부 = '짝수'
# else:
#     홀짝여부 = '홀수'

x = 9
홀짝여부 = '짝수' if x%2==0 else '홀수' # 홀짝여부 = '홀수' if x%2 else '짝수' # 같은 것.
홀짝여부
```

    '홀수'

```python
# 3항 연산자의 중첩
# '조건1 True' if '조건1' else '조건2 True' if '조건2' else '조건1, 조건2가 False'
```

```python
# '조건1 True'
# if '조건1'
# else '조건1 False 조건2 True'
#     if '조건2'
#     else '조건1, 조건2가 False'
```

```python
x = 15
if x %2 ==0:
    배수 = '2X' # 2의 배수
elif x%3 == 0:
    배수 = '3X' # 3의 배수
else:
    배수 = '?' #2의 배수도, 3의 배수도 아니다

배수
```

    '3X'

```python
x = 17

배수 = '2X' if x%2==0 else '3X' if x%3 ==0 else '?'
배수
```

    '?'

## 반복문

```python
# for 변수 in 순회가능한객체:
#     code
```

```python
# 순회가능한객체 != 시퀀스형자료
# 시퀀스 자료형은 순서가 있는 것일 뿐, 순회가능한것과 다르다
# 순회 가능한 객체 > 시퀀스 자료형
```

```python
for i in 'hello world':
    print(i)
```

```python
for i in 10:    #error
    print(i)

for i in 10.1:    #error
    print(i)
```

```python
# list
for i in [1,2,3]:
    print(i)
```

    1
    2
    3

```python
# tuple
for i in (1,2,3):
    print(i)
```

    1
    2
    3

```python
# set - 순서를 보장하진 않음
for i in {1, 2, 3}:
    print(i)
```

    1
    2
    3

```python
# dict - key 만 순회함
for i in {'one':1, 'two':2, 'three':3}:
    print(i)

```

    one
    two
    three

```python
# 순환가능한 객체에는 range, enumerate, zip, map, sorted, reversed, filter ...
for i in range(10):
    print(i)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

```python
언어순위 = ['Python', 'JavaScript', 'JAVA', 'Ruby']
for i in 언어순위:
    print(i)

for i in enumerate(언어순위):
    print(i)    # tuple

for i in enumerate(언어순위, 1):  # 1부터..
    print(i)    # tuple

for i in enumerate(언어순위, 101):  # 101부터..
    print(i)    # tuple
```

    Python
    JavaScript
    JAVA
    Ruby
    (0, 'Python')
    (1, 'JavaScript')
    (2, 'JAVA')
    (3, 'Ruby')
    (1, 'Python')
    (2, 'JavaScript')
    (3, 'JAVA')
    (4, 'Ruby')
    (101, 'Python')
    (102, 'JavaScript')
    (103, 'JAVA')
    (104, 'Ruby')

```python
for i, j in enumerate(언어순위):
    print(i, j)    # tuple을 unpacking 해서...
```

    0 Python
    1 JavaScript
    2 JAVA
    3 Ruby

```python
'1'.isdigit()
'0'.isdigit()
```

    True

## !! 오늘 배운 것 정리

- 조건문

  - 조건에 따라 코드를 분기할 수 있는 구문
  - if, elif, else
  - elif와 else는 단독으로 사용이 되지 않습니다.
  - 예시(score에 값을 변경해보면서 money 값을 확인해주세요.)

  ```python
  score = 81
  money = 0

  if score >= 90: # 만약에 조건이 참이라면
      print('mom : i\'m so happy!')
      money += 1000000
  elif score >= 80: # 그렇지 않고 만약에 조건이 참이라면
      print('mom : i\'m happy!')
      money += 100000
  elif score >= 70: # '그렇지 않고 만약에'에서 '그렇지 않고'가 만족이 안되기 때문에 실행하지 못합니다.
      print('mom : i\'m so...!')
      money += 10000
  elif score >= 60:
      print('mom : i\'m so...!')
      money += 1000
  else:
      print('mom : i\'m...!')
  print(money)
  ```

  - 3항 연산자

  ```python
  def f(y):
  return 'one' if y > 80 else None
  ```

- 정해진 순서를(next) 반복하는 것
  - 형태
  ```python
  # for 변수 in 순회가능한객체:
  #     code
  ```
  - 순회 가능한 객체(이터러블 객체) : 문자열, 리스트, 튜플, 딕셔너리, 셋, range, enumerate, map, set, sorted, reverse 등
  - 순회 불가능한 객체 : int, float 등
  - code 안에서 변수를 사용하지 않을 경우 언더바를 관습적으로 사용합니다.
  ```python
  # for _ in 순회가능한객체:
  #     code
  ```

```python
n = 1234
str(n)
list(str(n))
```

    ['1', '2', '3', '4']

## 반복문 이어서

```python
for _ in range(3):
    print('hello world')
```

    hello world
    hello world
    hello world

```python
for _, i in [[1,2 ], [3,4], [5,6]]:
    print('hello world')
    print(_)
```

    hello world
    1
    hello world
    3
    hello world
    5

```python
s = 0
for i in range(0, 101, 2):
    s += i

s

```

    2550

```python
listx= [100,200,300,400]
strx= 'abcd'
dictx = {'one':1, 'tow':2}
listxlter = iter(listx)
strxlter= iter(strx)
dictIter = iter(dictx)

# 시퀀스형 자료형에만 next가 되는 것이 아니고 다음 순회값을 지정할 뿐
print(next(listxlter),next(listxlter),next(listxlter),next(listxlter))
print(next(strxlter),next(strxlter),next(strxlter),next(strxlter))
print(next(dictIter),next(dictIter))
```

    100 200 300 400
    a b c d
    one tow

```python
# for True:         # 이렇게 사용하는거 아님.
#     print('hello')

for i in [1,2,3]:   # for는 []에있는 원소를i에 넣어주고 i가 []에 있는가? True > 포문...
    print(i)
```

    1
    2
    3

## break와 continue

```python
for i in range(10):
    print(i)
    if i == 5:
        break;
```

    0
    1
    2
    3
    4
    5

```python
# break는 모든 for를 중단시키는 것은 아님
# 자신을 감싸고 있는 단일 반복문만 탈출합니다.
for i in range(10):
    print('---------------')
    print(i)
    for j in range(10):
        print(i, j)
        if j == 5:
            break;  #바로 인접한? 한 단계 접한 반복문 탈출
```

```python
# continue 는 다음 루프로 갑니다
# 아래 코드에서 continue는 의미가 없습니다.
for i in range(10):
    print(i)
    if i == 5:
        continue;
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

```python
# continue 는 다음 루프로 갑니다
# continue 아래에 있는 코드를 실행하지 않고 다음 loop로 들어가기 때문에
# print(i)를 실행하지 않아 '5'가 출력되지 않음
for i in range(10):
    if i == 5:
        continue;
    print(i)
```

    0
    1
    2
    3
    4
    6
    7
    8
    9

```python
# 무한루프
# 실행과 동시에 정지를 눌러주세요
# l의 메모리가 계속 커지니까.. 효율이 매우 좋지 않음!!
l = [1]
for i in l:
    l.appen(i+1)
    print(i)
```

```python
# 무한루프 - generator
# 실행과 동시에 정지를 눌러주세요
# ??????????????????
```

## for 문과 else 구문

```python
# 다른 언어에서는 이 구문이 작동되지 않습니다.
for i in range(10):
    if i == 5:
        break
else:
    print('정상종료')
```

```python
# 반복문 + else 구문은 반복문에 break를 쓰지 않고 정상 종료되었을 때 else 구문이 실행됩니다.

for i in range(10):
    if i == 5:
        pass
else:
    print('정상종료')
```

    정상종료

## 리스트 표현식 (list comprehension)

```python
# 별 3.5개
# list 안에 반복문이나 조건문을 넣어 한 번에 리스트를 생성하는 기법
# for 문보다 list comprehension이 더 빠릅니다. (가독성 + 속도우위)

l = []
for i in range(10):
    l.append(i)
l
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```python
# list comprehension
l = [i for i in range(10)]
l
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```python
# for
l = []
for i in range(10):
    if i % 2 == 0:
        l.append(i)
l

# list comprehension
l = [i for i in range(10) if i%2==0]
l

# list(range(0,10,2)) #이것도 가능하고 직관적
```

    [0, 2, 4, 6, 8]

```python
l = ['aa', 'abc', 'bbb', 'ccc', 'aba']
k = [i for i in l if 'a' in i]
k
```

    ['aa', 'abc', 'aba']

```python
l = []
for i in range(10):
    if i%2 == 0:
        l.append(i)
    elif i%3 == 0:
        l.append(i)

# [i for i in range(10) if i%2==0 elif i%3==0] # syntax error
[i for i in range(10) if i%2==0 or i%3==0]


```

    [0, 2, 3, 4, 6, 8, 9]

```python
# 구구단

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i, j, i*j)

'''
# stop 0
# 손이나 문자열로 늘여뜨려놓고 내가 뭘 줄일 수 있을까 고민하세요
2 1 2
2 2 4
2 3 6
2 4 8
2 5 10
2 6 12
2 7 14
2 8 16
2 9 18
3 1 3
3 2 6
3 3 9
3 4 12
3 5 15
3 6 18
3 7 21
3 8 24
3 9 27
'''

# step 1~100 이렇게 한 단계식 줄여가봅시다.
# for i in range(1, 10):
#     print(2, i, 2*i)

# for 단 in range(2, 10):
#     for i in range(1, 10):
#         print(단, i, 단*i)


```

```python
# 별찍기
# 별 트리 만들기, 원 만들기...
'''
*
**
***
****
'''
```

```python
user_input = int(input('찍을 별의 층수'))
for i in range(user_input):
    print('*'*(i+1))
```

    찍을 별의 층수5
    *
    **
    ***
    ****
    *****

```python
# 이중 포문을 list comprehension으로
l = []
for i in range(2,10):
    for j in range(1,10):
        l.append([i, j, i*j])

[[i,j,i*j] for i in range(2,10) for j in range(1,10)]
```

## 다중 리스트 순회

```python
#다중 리스트 for문
skill = [
        ('고기잡이', 100),
        ('고기팔기', 120),
        ('낚시', 5),
        ('통발', 5),
        ('큰그물', 5)
]

for i,j in skill:
    print(i,j)
```

    고기잡이 100
    고기팔기 120
    낚시 5
    통발 5
    큰그물 5

```python
# 다중 리스트 unpacking!

skill = [
        ('고기잡이', [1, 100]),
        ('고기팔기', [1, 120]),
        ('낚시', [2, 100]),
        ('통발', [2, 100]),
        ('큰그물', [2, 100])
]

for i, [x, y] in skill:
    print(i, x, y)
```

    고기잡이 1 100
    고기팔기 1 120
    낚시 2 100
    통발 2 100
    큰그물 2 100

```python
# 다중 리스트 unpacking!
# tuple이어로 list로 unpacking 된다!
skill = [
        ('고기잡이', (1, 100)),
        ('고기팔기', (1, 120)),
        ('낚시', (2, 100)),
        ('통발', (2, 100)),
        ('큰그물', (2, 100))
]

for i, [x, y] in skill:
    print(i, x, y)
```

    고기잡이 1 100
    고기팔기 1 120
    낚시 2 100
    통발 2 100
    큰그물 2 100

```python
# 다중 리스트 unpacking!
# str이어도 list로 unpacking 된다! 단 길이는 맞춰주어야 한다!
skill = [
        ('고기잡이', 'aa'),
        ('고기팔기', 'bb'),
        ('낚시', 'cc'),
        ('통발', 'ab'),
        ('큰그물', 'ef')
]

for i, [x, y] in skill:
    print(i, x, y)
```

    고기잡이 a a
    고기팔기 b b
    낚시 c c
    통발 a b
    큰그물 e f

```python
skill_name = ['고기잡이', '고기팡기', '낚시']
skill_point =  [100,120,5]

for i, j in zip(skill_name, skill_point):
    print(i, j)
```

    고기잡이 100
    고기팡기 120
    낚시 5

```python
skill = [
        ('고기잡이', 100, 'SS'),
        ('고기팔기', 120, 'SSS'),
        ('낚시', 5, 'C'),
        ('통발', 5, 'C'),
        ('큰그물', 5, 'C')
]

for skillName, skillLevel, skillGrade in skill:
    print(skillName, skillLevel, skillGrade)
```

    고기잡이 100 SS
    고기팔기 120 SSS
    낚시 5 C
    통발 5 C
    큰그물 5 C

```python
# 문제
# data에는 다음과 같은 데이터가 있습니다.
# 각각 skill 이름, skill 제한레벨, skill 포인트, skill 등급입니다.
# 아래와 같이 출력해주세요
data = [
        ('고기잡이', (1, 100, 'S')),
        ('고기팔기', (1, 120, 'A')),
        ('낚시', (2, 100, 'A')),
        ('통발', (2, 100, 'B')),
        ('큰그물', (2, 100, 'S'))
]
# 출력값
# '축하합니다. S등급의 skill 고기잡이를 습득하셨습니다!
# 해당 스킬은 레벨 제한 1에 스킬 포인트 100 입니다.

for name, [level, point, rank] in data:
    print(f'축하합니다. {rank}등급의 skill {name}를 습득하셨습니다!\n해당 스킬은 레벨 제한 {level}에 스킬 포인트 {point} 입니다.')

# print 함수는 부하가 큰 함수이기 때문에 여러번 찍는 것은 지양해주세요
```

    축하합니다. S등급의 skill 고기잡이를 습득하셨습니다!
    해당 스킬은 레벨 제한 1에 스킬 포인트 100 입니다.
    축하합니다. A등급의 skill 고기팔기를 습득하셨습니다!
    해당 스킬은 레벨 제한 1에 스킬 포인트 120 입니다.
    축하합니다. A등급의 skill 낚시를 습득하셨습니다!
    해당 스킬은 레벨 제한 2에 스킬 포인트 100 입니다.
    축하합니다. B등급의 skill 통발를 습득하셨습니다!
    해당 스킬은 레벨 제한 2에 스킬 포인트 100 입니다.
    축하합니다. S등급의 skill 큰그물를 습득하셨습니다!
    해당 스킬은 레벨 제한 2에 스킬 포인트 100 입니다.

## while

```python
# 반복문 : for, while
a = 1
while a < 10 : # True인 동안에 계속 실행
    print(a)
    a += 1
```

    1
    2
    3
    4
    5
    6
    7
    8
    9

```python
## 실무에서 while을 사용하는 부분
# while 특정요소:
#     특정요소 값 꺼내는 문법
#     특정요소가 모두 없어질 때까지 돌아감

l = [1,2,3]
while l:    # l이 다 비면([]가 되면 ) False
    print(l.pop())

print('while문이 종료되었습니다')
```

    3
    2
    1
    while문이 종료되었습니다

```python
s = {1,2,3}
while s:
    print(s.pop())
```

    1
    2
    3

```python
# 중복되는 문자 중 가장 처음 등장한 문자의 index
s = 'abkkkbnbbbccdennnnneefefg'
ss = set(s)
while ss:
    c = ss.pop()
    print(c, s.index(c))
```

    e 13
    c 10
    b 1
    a 0
    g 24
    k 2
    n 6
    f 21
    d 12

```python
# 이러한 무한반복은 메모리를 모두 소진합니다.
# 서버가 뻗을 수도 있습니다.
while True:
    user_input = input('$')
    split_data = user_input.split(' ')
    if split_data[0] == 'mkdir':
        print(f'{split_data[1]} 폴더가 생성되었습니다.')
    elif split_data[0] == 'rmdir':
        print(f'{split_data[1]} 폴더가 제거되었습니다.')
    elif split_data[0] == 'exit':
        print('프로그램을 종료합니다.')
        break
```

    $exit
    프로그램을 종료합니다.

```python
# up down game
import random

result = random.randint(1, 100) # 1부터 100 사이 랜덤한 정수

while True:
    user_input = int(input('정수를 입력해주세요'))

    if user_input > result:
        print('down')
    elif user_input < result:
        print('up')
    else:
        print('맞췄습니다.')
        print('프로그램을 종료합니다.')
        break
```

```python
# 구구단
x = 2
y = 1
while x < 10:
    while y < 10:
        print( x, y, x*y)
        y += 1
    x += 1
    # y = 1     # 2단이 출력되지 않는 이유.. 초기화를 해줘야 다음 while문에 들어갈 수 있다
```

    2 1 2
    2 2 4
    2 3 6
    2 4 8
    2 5 10
    2 6 12
    2 7 14
    2 8 16
    2 9 18

```python
# 소수 계산으로 될 때에는 부동소수점 문제가 발생하므로
# == 연산자보다는 대소비교로 해주는게 안전하다
count = 0.0
while True:
    print(count)
    if count >= 0.3: ## count == 0.3 이면 무한루프 돌아버림
        break;
    count += 0.1
print('end')
```

    0.0
    0.1
    0.2
    0.30000000000000004
    end

```python
# 반복문 + else 구문은 반복문에 break를 쓰지 않고 정상 종료되었을 때 else 구문이 실행됩니다.
# 아무 출력값 없음
i = 0
while i< 10:
    if i == 5:
        break;
    i += 1
else:
    print('정상종료')

```

```python
# 반복문 + else 구문은 반복문에 break를 쓰지 않고 정상 종료되었을 때 else 구문이 실행됩니다.
# while의 판별문으로 종료되었기 때문에 '정상종료' 출력
i = 0
while i< 10:
    if i == 5:
        pass;
    i += 1
else:
    print('정상종료')

```

    정상종료

- https://school.programmers.co.kr/learn/courses/30/lessons/120871

```python
# step 1
count10 = 0
n = 15
while count10 < n+1 :
    print(count10)
    count10 += 1
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15

```python
#step 2 조건만 구현
count10 = 0 # 10진수 숫자
count3 = 0  # 3x마을에서 쓰는 숫자
n = 5
while count10 < n + 1 :
    count10 += 1
    count3 += 1
    # 3x마을에서 쓰는 숫자에는 3의 배수나 '3'이 있으면 안됨
    # 저주의 숫자를 지나가도 저주의 숫자일 수 있음. 12 -> 13 , 30 ->31...
    if count3 %3 == 0 or '3' in str(count10):
        count3 += 1
    print(count10, count3)
count3
```

    1 1
    2 2
    3 4
    4 5
    5 7
    6 8





    8

```python
#step 3 조건이 반복되도록 구현
def solution(n):
    count10 = 0
    count3 = 0
    while count10 < n :
        count10 += 1
        count3 += 1
        while count3 %3 == 0 or '3' in str(count3):
            count3 += 1
        print(count10, count3)
    return count3

```

    1 1
    2 2
    3 4
    4 5
    5 7
    6 8
    7 10
    8 11
    9 14
    10 16





    16

```python
# 간단하게 푸는 법
def solution(n):
    return [i for i in range(1, 1001) if i%3 != 0 and not('3' in str(i))][n-1]

```

```python
#step 2
count10 = 0
count3 = 0 # 3x마을에서 쓰는 숫자
n = 15
while count10 < n + 1 :
    if count10 %3 == 0: count10 +=1
    print(count10)
    count10 += 1
```

    1
    2
    4
    5
    7
    8
    10
    11
    13
    14
    16

## try ~ except ~ else

```python
# try:
#     실행문
# except:
#     예외 발생 시 처리문
# else:
#     예외 발생하지 않을 경우 실행문
```

```python
try:
    i = 1
    j = 1
    x = i/j
except:
    print("error")
else:
    print(x)
```

    1.0

## 실제 데이터를 가지고 연습 (JSON generator)

```python
data = [
  {
    "_id": "6459c9fe3d0040c8a253004e",
    "age": 35,
    "eyeColor": "brown",
    "name": "Maritza Powers",
    "gender": "female"
  },
  {
    "_id": "6459c9fe1ab73b21c300ba5b",
    "age": 26,
    "eyeColor": "green",
    "name": "Poole Gregory",
    "gender": "male"
  },
  {
    "_id": "6459c9fe3ca1e2052816fbdb",
    "age": 29,
    "eyeColor": "brown",
    "name": "Dionne Gates",
    "gender": "female"
  },
  {
    "_id": "6459c9fe5dcc9442e5c6bc6c",
    "age": 40,
    "eyeColor": "blue",
    "name": "Deann Patterson",
    "gender": "female"
  },
  {
    "_id": "6459c9fe7ff066d546ec3a73",
    "age": 32,
    "eyeColor": "blue",
    "name": "Kerry Hernandez",
    "gender": "female"
  }
]

# 반복문을 사용해도 좋지만,
# 반복문을 사용할 수 없다면 index로만 계산해도 좋습니다.

# 1. 회원들의 age 평균
total = 0
for i in data:
    total += i.get('age')

average = total/len(data)
print(average)

## map
average2 = sum(map(lambda x : x.get('age'), data))/len(data)
print(average2)


# 2. 회원들의 남녀 성비
female = 0
male = 0

for i in data:
    if i.get('gender') == 'male':
        male += 1
    else:
        female +=1

female_ratio = female/len(data)
male_ratio = male/len(data)

print(female_ratio, male_ratio)

##map
li = list(map(lambda x: x.get('gender') == 'male', data))
female = li.count(False)/len(data)
male = li.count(True)/len(data)
print(female, male)

## filter
male = len(list(filter(lambda x:x.get('gender') == 'male', data))) / len(data) * 100
female = len(list(filter(lambda x:x.get('gender') == 'female', data))) / len(data) * 100
print(female, male)

## comprehesion
list_gender = [i['gender'] for i in data]
male = list_gender.count('male')/len(data)
female = list_gender.count('female')/len(data)
print(female, male)
```

    32.4
    32.4
    0.8 0.2
    0.8 0.2
    80.0 20.0
    0.8 0.2

```python
## 오늘의 질문 1
# 람다함수를 재귀로 사용할 수 있나요?

factorial = lambda x : 1 if x == 0 else x * factorial(x-1)
factorial(5)

## 프로그래머스
# solution = lambda .... 이렇게 가능하다
```

    120

```python
## 오늘의 질문 2
skill = [('고기잡이', 1, 100),
         ('고기팔기', 1, 120),
         ('낚시', 2, 80),
         ('덫깔기', 2, 70)]

## enumerate 할때는 인덱스랑 안 헷갈리도록 이름을 바꿔주는게 좋음
for idx, obj in enumerate(skill):
    print(idx, obj)
```

    0 ('고기잡이', 1, 100)
    1 ('고기팔기', 1, 120)
    2 ('낚시', 2, 80)
    3 ('덫깔기', 2, 70)

## 알아야 하는 buit in function

> A <br>
> abs() all() any()

> B<br>
> bin() bool()

> C<br>
> chr()

> D<br>
> dict() dir()

> E<br>
> enumerate() eval()

> F<br>
> filter() float()

> G<br>
> globals()

> H<br>
> help()
> hex()

> I<br>
> id() input() int() isinstance() issubclass() iter()

> L<br>
> len() list() locals()

> M<br>
> map() max() min()

> N<br>
> next()

> O<br>
> object() oct() open() ord()

> P<br>
> pow() print() property()

> R<br>
> range() repr() reversed() round()

> S<br>
> set() setattr() slice() sorted() staticmethod()
> str() sum() super()

> T<br>
> tuple() type()

> V<br>
> vars()

> Z<br>
> zip()

### 수학적 함수

- abs( ) : 괄호 안에 있는 값을 절대값으로 출력해줍니다.
- all( ) : 괄호 안에 있는 값들이 모두 True(False)일 때 True(False)를 출력합니다.
- any( ) : 괄호안에 있는 값이 하나라고 True이면 True로 출력합니다.
- pow( ) : 제곱을 출력합니다.
- max( ) : 값의 최댓값을 출력합니다.
- min( ) : 값의 최솟값을 출력합니다.
- sum( ) : 값의 합계를 출력합니다.
- len( ) : 문자열의 길이를 출력합니다.
- sorted( ) : 데이터를 정렬해줍니다.
- reversed( ) : 정렬되지 않은 상태에서 값을 역순으로 출력합니다.

```python
# 절대값 사용..
abs(-1)

# all은 모든 요소가 True이어야 True를 리턴. 아니면 False
print(all([True, True, True]))
print(all([True, True, False]))
print(all(['a', '', 1]))
print(all(['a', ' ', 1]))
print(all([3 < 5, 12%2==0 , 15%5==0]))

# 아래처럼 조건문 대신 쓴 기억은 없음..
# 판별식 말고 함수의 리턴을 저런시긍로 받아서 쓴 적은 있음
if all([3 < 5, 12%2==0 , 15%5==0]):
    print('hello')
if all([3 < 5,
        12%2==0,
        15%5==0]):
    print('hello')

# all(True, True, True)
# TypeError: all() takes exactly one argument (3 given)

pow(2,3) # 2 ** 3
```

    True
    False
    False
    True
    True
    hello
    hello





    8

```python
print(sum([[1,2],[3,4],[5,6]], []))
print(sum([1,2, 3,4, 5,6], 100))
# sum([1,2,3,4,5,6],{1,2,3}) #error
```

    [1, 2, 3, 4, 5, 6]
    121

```python
# len()은 __len__() attribute!
# __len__이 없는 것들 : map, zip, filter...

class str(str):
    def __len__(self):
        return 1000

len(str('hello world'))
```

    1000

```python
# len(zip([1,2,3], 'abc')) # error
len(list(zip([1,2,3], 'abc')))
```

    3

### 형변환 함수

- set( )
- dict( )
- hex( ) : 16진법
- bin( ) : 2진법
- oct( ) : 8진법
- bool( )
- str( )
- ord( ) : 각각의 문자에 대한 숫자값을 출력해줍니다.(유니코드표를 참고하세요.)
- float( )
- tuple( )
- chr( ) : 숫자값을 통해서 문자를 출력합니다.
- list( )
- range( )
- complex( )

```python
l = [1,2,3]
type(l)
```

    list

```python
# 아래 3개는 int형
# bin()
# oct()
# hex()
bin(7) #return 은 str'0b111'
0b111           # 7
type(0b111)     # int
int('111',2)    # 7
int('0b111',2)  # 7
# int(0b111, 2) # error 첫 번째 인자는 strsolution
```

    7

```python
ord('A'), chr(65)    # 65, 'A'
```

    (65, 'A')

```python
# list(range(start, stop, step))
print(list(range(0,10,2)))
print(list(range(0,10)))
print(list(range(10)))
print(list(range(-10,10,2)))
print(list(range(0,-10,-2)))
```

    [0, 2, 4, 6, 8]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]
    [0, -2, -4, -6, -8]

### 도움말

```python
def jinsoo():
    '''
    유진수가 작성한 함수
    '''
    return

help(jinsoo)
```

    Help on function jinsoo in module __main__:

    jinsoo()
        유진수가 작성한 함수

### object 관련 함수

- dir( )
- id( )
- type( )

```python
# dir() #directory 의 약자로 대상이 가진 attribute를 모두 출력합니다
# attribute란 무엇인가? class에서 배울 멤버 + 메서드 입니다.
```

```python
def f():
    return 100

f.name = 'leehojun'
print(f.name)
print(f.__name__)
# dir(f)

f.my = 'hahah'  # setattr() 없이 바로 만들 수 있음???
print(f.my)
```

    leehojun
    f
    hahah

```python
# 배우는 재미
# 단시간에 될 수 없습니다 => 경쟁력

```

```python
l =10
# 복사가 제대로 이루어졌나?
id(l) # 얕은복사, 깊은복사
```

    140025093292560

```python
type('abc') # str
print(type('abc')) # <class 'str'>
# print(type(f)) # <class 'function'>

# class가 전체 Python을 관통하고 있습니다.

```

    <class 'str'>
    <class 'function'>

### 유용한 순회 가능 객체

- enumerate( ) : 값에 순위를 매기고 싶을 때 사용합니다.
- range( )
- filter( )
- zip( )
- map( )

```python
# enumerate()
print(list(enumerate([10,20,30])))
print(list(enumerate([10,20,30], start=100)))
print(list(enumerate([10,20,30], 1000)))
# print(list(enumerate([10,20,30], 'abc'))) # error start인자에는 int가 와야 함

```

    [(0, 10), (1, 20), (2, 30)]
    [(100, 10), (101, 20), (102, 30)]
    [(1000, 10), (1001, 20), (1002, 30)]

```python
def 함수(x):
    return x >15
print(list(filter(함수, [10, 20, 30, 40])))

# filter 의 function 인자에 None 가능
# 여러 가지 자료형이 섞여 있을 때 값이 들어있는(유효한) 것만 찾을 경우
print(list(filter(None, [True, True, False, False])))
print(list(filter(None, [[], 'abc', '', ''])))
```

    [20, 30, 40]
    [True, True]
    ['abc']

```python
# zip 여러개의 iterable 한 객체를 순서대로 묶어서 tuple 원소로 가지고있음
list(zip('abc', 'def', range(3), [1,2,3],[4,5,6,7]))
```

    [('a', 'd', 0, 1, 4), ('b', 'e', 1, 2, 5), ('c', 'f', 2, 3, 6)]

```python
x = [5,4,6,8,2]
list(zip('abcedfg', sorted(x))) # sorted()의 리턴도 iterable한 객체라서 가능

```

    [('a', 2), ('b', 4), ('c', 5), ('e', 6), ('d', 8)]

```python
x = [5,4,6,8,2]
y = [7,6,45,4,2,3,3]
list(zip('abcdefg', zip(x,y)))
```

    [('a', (5, 7)), ('b', (4, 6)), ('c', (6, 45)), ('d', (8, 4)), ('e', (2, 2))]

## arg, kargs

- 가변 아규먼트, 가변 키워드 아규먼트

```python
def print_args(*args):  # 꼭 args가 아니어도 됩니다.
    print(args)
    # for x in args:
    #     print(x)

print_args(100, True, 'leehojun')
```

    (100, True, 'leehojun')

```python
def print_kwargs(a, **kwargs):  # 꼭 kwargs가 아니어도 됩니다.
    print(a)
    print(kwargs)
    # for i in kwargs:
    #     print(i)

print_kwargs(100, name='leehojun', age='10')
```

    100
    {'name': 'leehojun', 'age': '10'}

```python
def print_kwargs(*kwargs):
    print(kwargs)
    for i in kwargs:
        print(i)

value = {'one':10, 'two':20}
print_kwargs(*value)
## asterisk가 1개이면 key만... 받아짐
## key와 value 모두를 넘기기 위해 2개를 사용


```

    ('one', 'two')
    one
    two

```python
def print_args(*args, b): # error 입니다.
    print(args)
    # for x in args:
    #     print(x)

print_args(100, True, 'leehojun')
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-63-c563cefd0862> in <cell line: 6>()
          4     #     print(x)
          5
    ----> 6 print_args(100, True, 'leehojun')


    TypeError: print_args() missing 1 required keyword-only argument: 'b'

```python
def print_args(b, *args):
    print(args)
    # for x in args:
    #     print(x)

print_args(100, True, b= 'leehojun')# error 입니다.
```

```python
# 정상. 그냥 인자는 가변 인자보다 앞에 와야 한다.

def print_args(b, *args):
    print(args)
    # for x in args:
    #     print(x)

print_args(100, True, 'leehojun')
```

    (True, 'leehojun')

```python
# * 의 기능은 남은 데이터들의 packing. list로 packing 함 음청 신기하네~~
# ** 면 dict로 packing 하는 것.
one, two, *three = 1, 2, 3, 4, 5
print(one)
print(two)
print(three)
```

    1
    2
    [3, 4, 5]

## lambda

- lambda는 익명함수라고 하며, 이름이 없는 함수

```python
leehojun = lambda x: x**2
print(type(leehojun))
print(type(lambda x: x**2))


```

    <class 'function'>
    <class 'function'>

```python
def 함수(x):
    return x ** 2
print(dir(함수))
print(dir(lambda x: x**2))

## lambda는 __name__ 이름 값이 lambda
print(함수.__name__)
print((lambda x: x**2).__name__)

# 두 개의 차이는 참조 카운팅이 있고 없고의 차이
```

    ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    함수
    <lambda>

```python
def add(x, y):
    return x + y
def sub():
    pass
def div():
    pass
def mul():
    pass
caculator = [add, sub, div, mul]
print(caculator[0](10, 20)) # 0번째 값은 add 입니다.


# 이런식으로 하면 참조 카운트가 늘어남
calculator2 = [lambda x ,y : x + y,
               lambda x ,y : x - y,
               lambda x ,y : x / y,
               lambda x ,y : x * y]

print(calculator2[0](10,20)) #0번째 값은 add 입니다.
print(calculator2[1](10,20)) #0번째 값은 sub 입니다.
```

    30
    30
    -10

```python
def f():
    return lambda x, y:x + y

f()(10, 20)
```

    30

```python
def f():
    return lambda x: lambda i : i**2

f()(1)(10) # f()(i)(x)
```

    100

```python
def f():
    return lambda x: lambda i : x*i**2

f()(2)(10) # f()(i)(x)
```

    400

### lambda 실무 응용

- `lambda`가 응용되는 곳 : map, filter, max, min, sorted

```python
# 실무에서도 많이 사용합니다.
def 제곱(x):
    return x ** 2

# 재사용하는 경우 함수로 전달하는 경우도 있습니다.
list(map(제곱, [1,2,3,4]))
list(map(제곱, [1,2,3,4]))

list(map(lambda x: x**2, [1,2,3,4]))
```

```python
# 실전문제
숫자 = [1, 2, 3, 4, 5]
승수 = [2, 2, 2, 3, 3]

##1. 숫자의 승수를 zip으로 맵핑해서 진행하세요.
result1 = list(zip(숫자, 승수))
print(result1)

kk = [(숫자[i], 승수[i]) for i in range(len(숫자))]

##2. 숫자를 승수만큼 승수하여 결과값을 표현해주세요.
result2 = list(map(lambda x: x[0]**x[1], zip(숫자, 승수)))
print(result2)

# zip을 안쓴다면... 이렇게 가능함
kk = list(map(lambda x, y: x ** y, 숫자, 승수))
print(kk)

# list comprehension
print([i**j for i, j in zip(숫자, 승수)])

##3. 승수한 값이 100이상인 값을 출력하세요.
result3 = list(filter(lambda x: x > 100, map(lambda x: x[0]**x[1], zip(숫자, 승수))))
print(result3)

# list comprehension
print([i**j for i, j in zip(숫자, 승수) if i**j > 100])

##4. 승수한 값을 모두 더하세요.
result4 = sum(map(lambda x: x[0]**x[1], zip(숫자, 승수)))
print(result4)

# list comprehension
print(sum([i**j for i, j in zip(숫자, 승수)]))

```

    [(1, 2), (2, 2), (3, 2), (4, 3), (5, 3)]
    [1, 4, 9, 64, 125]
    [1, 4, 9, 64, 125]
    [1, 4, 9, 64, 125]
    [125]
    [125]
    203
    203

```python
array = [1,5,2,3,6,8,7 ]
next(enumerate(array))
```

    1

## !! 오늘 배운 것 정리 230509

- 반복문

  - 정해진 순서를(next) 반복하는 것
  - 형태

  ```python
  # for 변수 in 순회가능한객체: # stopItoration까지 반복
  #     code

  # while 조건: # true까지 반복
  #     code
  ```

  - 순회 가능한 객체(이터러블 객체) : 문자열, 리스트, 튜플, 딕셔너리, 셋, range, enumerate, map, set, sorted, reverse 등
  - 순회 불가능한 객체 : int, float 등
  - code 안에서 변수를 사용하지 않을 경우 언더바를 관습적으로 사용합니다.

  ```python
  # for _ in 순회가능한객체:
  #     code
  ```

  - 반복문 다음 else 구문 : break 없이 정상 종료 되면 실행
  - 반복문 안에 break 구문 : 자신을 감싸고 있는 반복문 1개 탈출
  - 반복문 안에 continue 구문 : 다음 루프로 넘어감
  - 반복문 안에 pass : 공백만 채워줄 뿐 아무 기능 없음

- bulit-in function

  - 수학적 통계에 활용되는 함수

    - abs( ) : 괄호 안에 있는 값을 절대값으로 출력해줍니다.
    - all( ) : 괄호 안에 있는 값들이 모두 True(False)일 때 True(False)를 출력합니다.
    - any( ) : 괄호안에 있는 값이 하나라고 True이면 True로 출력합니다.
    - pow( ) : 제곱을 출력합니다.
    - max( ) : 값의 최댓값을 출력합니다.
    - min( ) : 값의 최솟값을 출력합니다.
    - sum( ) : 값의 합계를 출력합니다.
    - len( ) : 문자열의 길이를 출력합니다.
    - sorted( ) : 데이터를 정렬해줍니다.
    - reversed( ) : 정렬되지 않은 상태에서 값을 역순으로 출력합니다.

  - 형변환 함수

    - set( )
    - dict( )
    - hex( ) : 16진법
    - bin( ) : 2진법
    - oct( ) : 8진법
    - bool( )
    - str( )
    - ord( ) : 각각의 문자에 대한 숫자값을 출력해줍니다.(유니코드표를 참고하세요.)
    - float( )
    - tuple( )
    - chr( ) : 숫자값을 통해서 문자를 출력합니다.
    - list( )
    - range( )
    - complex( )

  - 도움말

    - help( )

  - object 관련 함수

    - dir( )
    - id( )
    - type( )

  - 순회 가능한 객체
    - enumerate( ) : 값에 순위를 매기고 싶을 때 사용합니다.
    - range( )
    - sorted( )
    - reversed( )
    - filter( )
    - zip( )
    - map( )

- args, kargs

  - 가변 아규먼트, 가변 키워드 아규먼트

  ```python
  def print_args(*args): # 꼭 args가 될 필요는 없습니다.
      print(args)

  print_args(100, True, 'leehojun')

  ####

  def print_kwargs(**kwargs): # 꼭 kargs가 될 필요는 없습니다.
  print(kwargs)

  print_kwargs(name='leehojun', age='10')
  ```

- lambda

  - lambda 는 익명함수라고 하며, 이름이 없는 함수
  - 보통은 다시 사용되지 않을 함수를 선언할 때 사용

  ```python
  leehojun = lambda x : x**2

  # def leehojun(x):
  #     return x ** 2

  list(map(lambda x : x ** 2, [1, 2, 3, 4]))
  ```

## 클래스

- 클래스는 데이터(멤버)와 기능(메서드)을 가지고 있는 인스턴트 객체를 생성하기 위한 역할을 합니다.
- 우리가 배우고 있는 Python은 객체지향 프로그래밍 언어

```python
class CarFactory(object): # 첫 문자는 대문자입니다.(관습)
    max_speed = 300
    max_people = 5

    # self는 자기자신을 가리키기 때문에 함수를 호출한 인스턴스를 가리킵니다.
    def move(self,x):
        print(x, '의 스피드로 움직이고 있습니다.')

    def stop(self):
        print('멈췄습니다.')

# 클래스로 바로 접근해서 무엇을 하는 것을 권고하지 않습니다.
# 인스턴스 변수와 클래스 변수에 대한 개념을 제대로 알지 못하는 상태에서...
print(CarFactory.max_speed)

k5 = CarFactory() # 붕어빵(인스턴스) = 붕어빵틀(클래스)
k3 = CarFactory() # 차(인스턴스) = 자동차공장(클래스)

```

```python
class CarFactory(object):
    max_speed = 300
    max_people = 5

    def move(self):
        print('움직이고 있습니다.')

    def stop(self):
        print('멈췄습니다.')

print(CarFactory.max_speed)

k5 = CarFactory()
k3 = CarFactory()
k5.move()
k3.move()
k5.stop()
k3.stop()
print(k5.max_speed)
```

    300
    의 스피드로 움직이고 있습니다.
    의 스피드로 움직이고 있습니다.
    멈췄습니다.
    멈췄습니다.
    300

```python
# 메서드 : 클래스 내의 함수
# 멤버 : 클래스 내의 변수

# 클래스는 멤버와 메서드로 이루어져있는데 멤버와 메서드를 어트리뷰트라고 함
# 메서드는 일반 메서드와 매직 메서드로 나줘짐
# 클래스는 틀 인스턴스는 찍어나온 것

class CarFactory(object):
    max_speed = 300
    max_people = 5

    def __init__(self, user_input_name):   # 인스턴스가 만들어질 때 실행되는 메서드
        self.name = user_input_name

    def move(self):
        print(self.name, f'{f"{self.name}":>10}차가 움직이고 있습니다.') # 문자열이 아닐 수 있는  변수는 이렇게 포매팅!

    def stop(self):
        print(self.name, '차가 멈췄습니다.')

print(CarFactory.max_speed)

k5 = CarFactory('케이파이브')
k3 = CarFactory('케이쓰리')
k5.move()
k3.move()
k5.stop()
k3.stop()
print(k5.max_speed)
```

    300
    케이파이브      케이파이브차가 움직이고 있습니다.
    케이쓰리       케이쓰리차가 움직이고 있습니다.
    케이파이브 차가 멈췄습니다.
    케이쓰리 차가 멈췄습니다.
    300

```python
print(type(k3))
print(dir(k3))
# 'max_people', 멤버
# 'max_speed', 멤버
# 'move', 메서드
# 'name', 멤버
# 'stop' 메서드
```

    <class '__main__.CarFactory'>
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'max_people', 'max_speed', 'move', 'name', 'stop']

```python
l = [10,20,30]
print(type(l))
print(dir(l))
# 메소드
# 'append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
```

    <class 'list'>
    ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

```python
# 이런 식으로 정의되어있음! cpython에서 찾아볼 수 있다!

# class list(object):
#     def __add__(self):
#         pass
#     def __class__(self):
#         pass
#     def __class_getitem__(self):
#         pass
#     def __contains__(self):
#         pass
#     def __delattr__(self):
#         pass
#     def __delitem__(self):
#         pass
#     def __dir__(self):
#         pass
#     def __doc__(self):
#         pass
#     def __eq__(self):
#         pass
#     def __format__(self):
#         pass
#     def __ge__(self):
#         pass
#     def  생략.(self):
#         pass
#     def append(self):
#         pass
#     def clear(self):
#         pass
#     def copy(self):
#         pass
#     def count(self):
#         pass
#     def extend(self):
#         pass
#     def index(self):
#         pass
#     def insert(self):
#         pass
#     def pop(self):
#         pass
#     def remove(self):
#         pass
#     def reverse(self):
#         pass
#     def sor(self):
#         pass
```

```python
d = {'one':1, 'two':2}
# d.three = 30 # AttributeError
d['three'] = 30 # 'three' 키에 30 값인 원소 생성
print(d['three'])
```

    30

```python
# 클래스 변수
# 클래스 바로 하위에 자리하고 있는 변수
# 모든 인스턴스 객체들이 공유
# 클래스 이름을 통해서 접근할 수 있음

class Car(object):
	kinds = []
	speed = 300
    # IndentationError: unindent does not match any outer indentation level
    # self.kk = 10  # error

    # kind가 인스턴스 레벨에 없어서
    # class 변수로 접근하는 거고
    # speed는 값을 = 로 할당했기 때문에 인스턴스 변수가 생기는 것.
	def add_kinds(self, name):
		self.kinds.append(name)
	def change_speed(self, speed):
		self.speed = speed

k5 = Car()
k3 = Car()
k5.add_kinds('k5')
k3.add_kinds('k3')
k5.change_speed(500)
k3.change_speed(250)

print('k5.kinds:', k5.kinds)
print('k3.kinds:', k3.kinds)
print('k5.speed:',k5.speed) # speed는 공유하지 않음
print('k3.speed:',k3.speed)
# Car.mama
# k5.mama
```

    k5.kinds: ['k5', 'k3']
    k3.kinds: ['k5', 'k3']
    k5.speed: 500
    k3.speed: 250

```python
# 클래스 변수
# 클래스 바로 하위에 자리하고 있는 변수
# 모든 인스턴스 객체들이 공유
# 클래스 이름을 통해서 접근할 수 있음

class Car(object):
    kinds = []
    speed = 300
    # IndentationError: unindent does not match any outer indentation level
    # self.kk = 10  # error

    # kind가 인스턴스 레벨에 없어서
    # class 변수로 접근하는 거고
    # speed는 값을 = 로 할당했기 때문에 인스턴스 변수가 생기는 것.
    def add_kinds(self, name):
        Car.kinds.append(name)
        self.kinds.append(name)

    def change_speed(self, speed):
        self.speed = speed

k5 = Car()
k3 = Car()
k5.speed = 500  # k5 인스턴스 안에 speed라는 변수를 만들어서 500을 넣음
k3.speed        # k3 에서 speed 부르면 클래스 멤버인 speed를 호출

print(k5.speed)
print(k3.speed)
print(Car.speed)

print(id(k5.speed), '인스턴스 멤버')
print(id(k3.speed), '클래스 멤버')
print(id(Car.speed), '클래스 멤버')

k5.add_kinds('k5')
k3.add_kinds('k3')

print(k5.kinds)
print(k3.kinds)
print(Car.kinds)

print(id(k5.kinds), '클래스 멤버')
print(id(k3.kinds), '클래스 멤버')
print(id(Car.kinds), '클래스 멤버')

## 할당연산자를 사용하면... 인스턴스 멤버로 변경됨!?
```

    500
    300
    300
    140191215498768 인스턴스 멤버
    140191215498864 클래스 멤버
    140191215498864 클래스 멤버
    ['k5', 'k5', 'k3', 'k3']
    ['k5', 'k5', 'k3', 'k3']
    ['k5', 'k5', 'k3', 'k3']
    140191215148224 클래스 멤버
    140191215148224 클래스 멤버
    140191215148224 클래스 멤버

```python
# 클래스 멤버인지 인스턴스 멤버인지!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Car(object):
    kinds = []
    speed = 300
    test = []
    # self.maybenot = 10 # NameError: name 'self' is not defined

    def add_kinds(self, name):
        self.kinds.append(name)

    def change_speed(self, speed):
        self.speed = speed

    def change_test(self, nn):
        self.test += [nn]   ## 이거는 클래스 멤버 test에 추가
        self.test = [nn*2]  ## 이거는 인스턴스 멤버 변수 생성

k5 = Car()
k3 = Car()
k5.speed = 500  # k5 인스턴스 안에 speed라는 변수를 만들어서 500을 넣음
k3.speed        # k3 에서 speed 부르면 클래스 멤버인 speed를 호출

print(k5.speed)
print(k3.speed)
print(Car.speed)

print(id(k5.speed), '인스턴스 멤버')
print(id(k3.speed), '클래스 멤버')
print(id(Car.speed), '클래스 멤버')

k5.add_kinds('k5')
k3.add_kinds('k3')

print(k5.kinds)
print(k3.kinds)
print(Car.kinds)

print(id(k5.kinds), '클래스 멤버')
print(id(k3.kinds), '클래스 멤버')
print(id(Car.kinds), '클래스 멤버')

## 할당연산자를 사용하면... 인스턴스 멤버로 변경됨!?
k5.change_test('test5')
k3.change_test('test3')

print(k5.test)
print(k3.test)
print(Car.test)

print(id(k5.test), '인스턴스 멤버')
print(id(k3.test), '인스턴스 멤버')
print(id(Car.test), '클래스 멤버')
```

    500
    300
    300
    140191215499920 인스턴스 멤버
    140191215498608 클래스 멤버
    140191215498608 클래스 멤버
    ['k5', 'k3']
    ['k5', 'k3']
    ['k5', 'k3']
    140191213398848 클래스 멤버
    140191213398848 클래스 멤버
    140191213398848 클래스 멤버
    ['test5test5']
    ['test3test3']
    ['test5', 'test3']
    140191213351104 인스턴스 멤버
    140191213439424 인스턴스 멤버
    140191213183232 클래스 멤버

```python
주인공 = ['licat', 10000]
class MobFactory(object):
    def __init__(self, 이름, 공격력, 체력, 마력, 크기_너비, 크기_높이, 아이템확률, x, y):
        self.name = 이름
        self.power = 공격력
        self.hp = 체력
        self.mp = 마력
        self.width = 크기_너비
        self.height = 크기_높이
        self.drop_rate = 아이템확률

    def attack(self):
        주인공[1] -= self.power
        print(f'{self.name}이 {self.power}데미지로 공격했습니다.')
        print(f'주인공의 체력이 {주인공[1]}이 되었습니다.')

    def __add__(self, next): # 슬라임 + 슬라임...
        if self.name == '슬라임':
            return MobFactory(f'왕{self.name + next.name}',
                              self.power + next.power,
                              10, 10, 2, 2, 100, 1, 1 )
        return None

슬라임 = MobFactory('슬라임', 1, 10, 10, 2, 2, 100, 1, 1)
오크 = MobFactory('오크', 100, 100, 10, 5, 5, 80, 1, 1)
고블린 = MobFactory('고블린', 10, 10, 10, 2, 2, 60, 1, 1)
드래곤 = MobFactory('드래곤', 1000, 500, 10, 100, 100, 10, 20, 0)
해골 = MobFactory('해골', 10, 5, 10, 2, 2, 100, 1, 1)

슬라임.attack()
왕슬라임 = 슬라임 + 슬라임
print(왕슬라임.power)
왕슬라임.name

```

    슬라임이 1데미지로 공격했습니다.
    주인공의 체력이 9999이 되었습니다.
    2





    '왕슬라임슬라임'

```python
# 캐릭터 클래스 만들어보기.
# 상상력!!!!! 체력회복, 이동, 스킬 등등~
class Character(object):
    def __init__(self, 이름, 체력, 마력, 공격력, 사정거리, 크기_너비, 크기_높이, x, y):
        self.name = 이름
        self.hp = 체력
        self.mp = 마력
        self.power = 공격력
        self.range = 사정거리
        self.width = 크기_너비
        self.height = 크기_높이
        self.pos_x = x
        self.pos_y = y

    def move_x(self, n):
        self.pos_x += n
        print('x 방향으로 이동중입니다.')
        print(f'현재 캐릭터의 위치는 {self.pos_x}, {self.pos_y}')

    def move_y(self, n):
        self.pos_x += n
        print('y 방향으로 이동중입니다.')
        print(f'현재 캐릭터의 위치는 {self.pos_x}, {self.pos_y}')

    def attack(self, mob):
        if isinstance(mob, MobFactory):
            mob.hp -= self.power
            print(f'{self.name}이 {mob.name}을 {self.power}로 공격하였습니다.')
            print(f'{mob.name}의 체력이 {mob.hp}가 되었습니다.')
        else:
            print('공격할 수 없는 대상입니다.')

라이캣 = Character('licat', 10000, 2000, 10, 5, 5, 5, 0, 0)
무라 = Character('mura', 7000, 5000, 30, 15, 3, 3, 1, 2)

라이캣.move_x(10)
라이캣.attack(드래곤)
무라.attack(라이캣)


```

    x 방향으로 이동중입니다.
    현재 캐릭터의 위치는 10, 0
    licat이 드래곤을 10로 공격하였습니다.
    드래곤의 체력이 490가 되었습니다.
    공격할 수 없는 대상입니다.

```python
# 조금 쉬운 예제
# 이 코드는 가능하면 두 세번 써보시길 권해드립니다.

class BlogFactory(object):
    def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
        self.title = 제목
        self.content = 내용
        self.count = 조회수
        self.writer = 글쓴이
        self.create_date = 생성날짜

게시글1 = BlogFactory(
    '오늘 제주의 날씨',
    '오늘 제주의 날씨는 참 좋네요! 미세먼지 농도도 낮아요!',
    '0',
    '이호준',
    '2023/05/10')

게시글2 = BlogFactory(
    '오늘 부산의 날씨',
    '오늘 부산의 날씨는 참 좋네요! 파도도 낮아요!',
    '10000',
    '김재현',
    '2023/05/10')

게시글3 = BlogFactory(
    '오늘 강원도의 날씨',
    '오늘 강원도의 날씨는 참 좋네요! 공기가 상쾌해요!',
    '9999',
    '남궁 범',
    '2023/05/10')

# 모든 요소 불러내는 법
# objects.all()

data = [게시글1, 게시글2, 게시글3]

for i in data:
    print(i.title)

print()

for i in data:
    if i.writer == '이호준':
        # django 에서는 이런 식으로 태그로 감싸서..
        print(i.title)
        print(i.content)
        print(i.count)
        print(i.writer)
        print(i.create_date)

print()

for i in data:
    if i.writer == '이호준':
        # django 에서는 이런 식으로 태그로 감싸서..
        print(f'<h2>{i.title}</h2>')
        print(f'<p>{i.content}</p>')
        print(f'<p>{i.count}</p>')
        print(f'<p>{i.writer}</p>')
        print(f'<p>{i.create_date}</p>')

```

    오늘 제주의 날씨
    오늘 부산의 날씨
    오늘 강원도의 날씨

    오늘 제주의 날씨
    오늘 제주의 날씨는 참 좋네요! 미세먼지 농도도 낮아요!
    0
    이호준
    2023/05/10

    <h2>오늘 제주의 날씨</h2>
    <p>오늘 제주의 날씨는 참 좋네요! 미세먼지 농도도 낮아요!</p>
    <p>0</p>
    <p>이호준</p>
    <p>2023/05/10</p>

- Data model : https://docs.python.org/3/reference/datamodel.html
- 매직메서드 정의된것 설명나와있음
- 저 페이지에서 `__lt__` 로 검색하면 기호랑 관련된거 볼수있음

```python
# 조금 쉬운 예제 + 알파

class BlogFactory(object):
    dataset = []
    def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
        self.title = 제목
        self.content = 내용
        self.count = 조회수
        self.writer = 글쓴이
        self.create_date = 생성날짜
        self.dataset.append(self)

    def __str__(self):  # print 함수에 인자로 들어갔을 때 반환될 스트링..
        return 'hello'

게시글1 = BlogFactory(
    '오늘 제주의 날씨',
    '오늘 제주의 날씨는 참 좋네요! 미세먼지 농도도 낮아요!',
    '0',
    '이호준',
    '2023/05/10')

게시글2 = BlogFactory(
    '오늘 부산의 날씨',
    '오늘 부산의 날씨는 참 좋네요! 파도도 낮아요!',
    '10000',
    '김재현',
    '2023/05/10')

게시글3 = BlogFactory(
    '오늘 강원도의 날씨',
    '오늘 강원도의 날씨는 참 좋네요! 공기가 상쾌해요!',
    '9999',
    '남궁 범',
    '2023/05/10')

# 모든 요소 불러내는 법
# objects.all()

게시글1.dataset

for i in 게시글1.dataset:
    print(i.title)

print(게시글1, 게시글2)


```

    오늘 제주의 날씨
    오늘 부산의 날씨
    오늘 강원도의 날씨
    hello hello

```python
# 중요한 예제입니다.

class BlogFactory(object):
    dataset = []
    def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
        self.title = 제목
        self.content = 내용
        self.count = 조회수
        self.writer = 글쓴이
        self.create_date = 생성날짜
        self.dataset.append(self)

    def __str__(self):  # print 함수에 인자로 들어갔을 때 반환될 스트링..
        return f'제목 : {self.title}, 내용 : {self.content[:10]}, 글쓴이: {self.writer}'

게시글1 = BlogFactory(
    '오늘 제주의 날씨',
    '오늘 제주의 날씨는 참 좋네요! 미세먼지 농도도 낮아요!',
    '0',
    '이호준',
    '2023/05/10')

게시글2 = BlogFactory(
    '오늘 부산의 날씨',
    '오늘 부산의 날씨는 참 좋네요! 파도도 낮아요!',
    '10000',
    '김재현',
    '2023/05/10')

게시글3 = BlogFactory(
    '오늘 강원도의 날씨',
    '오늘 강원도의 날씨는 참 좋네요! 공기가 상쾌해요!',
    '9999',
    '남궁 범',
    '2023/05/10')

print(게시글1)
print(게시글2)


```

    제목 : 오늘 제주의 날씨, 내용 : 오늘 제주의 날씨는, 글쓴이: 이호준
    제목 : 오늘 부산의 날씨, 내용 : 오늘 부산의 날씨는, 글쓴이: 김재현

```python
## 오늘의 질문!!!!!!!!!!!!!!!!!!!!!
# 질문 : id를 객체가 아니라 count라는 정수값을 지정해줘서 증가시키고 싶습니다.
# 답 : 아래코드처럼 사용하시면 됩니다.
class BlogFactory(object):

    count = 0

    def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
        ## 이런스킬... 자동으로 id를 매기고 총 생성된 개수도 알 수 있겠다.
        BlogFactory.count += 1
        self.id = BlogFactory.count
        self.title = 제목
        self.content = 내용
        self.count = 조회수
        self.writer = 글쓴이
        self.create_date = 생성날짜

    def __str__(self):
        return f'{self.id}. 제목 : {self.title}, 내용 : {self.content[:5]}'

게시글1 = BlogFactory(
        '오늘 제주의 날씨',
        '오늘 제주의 날씨는 참 좋네요! 블라블라',
        '0',
        '이호준',
        '2023/05/10',
    )

게시글2 = BlogFactory(
        '오늘 부산의 날씨',
        '오늘 부산의 날씨는 참 좋네요! 블라블라',
        '1000000',
        '김재현',
        '2023/05/10',
    )

print(게시글1)
print(게시글2)
```

```python
class Counter:
    def __init__(self, value = 0):
        self.value = value

    def increment(self, delta = 1):
        self.value += delta

    def decrement(self, delta = 1):
        self.value -= delta

counter = Counter()
print(counter.value)
counter.increment(10)
print(counter.value)
counter.decrement(5)
print(counter.value)
```

    0
    10
    5

```python
class UserInfo(object):

    user_total_list = []

    def __init__(self, name, nickname, phone, email, gender, language):
        self.name = name
        self.nickname = nickname
        self.phone = phone
        self.email = email
        self.gender = gender
        self.commit_count = 0
        self.language = language
        self.user_total_list.append(self)

    def __str__(self):
        return f'이름:{self.name}, 닉네임:{self.nickname}, 커밋수:{self.commit_count}, 언어:{self.language}'

    def commit(self):
        self.commit_count += 1
        print(f'{self.name}님이 커밋을 수행했습니다.')

    def revert(self):
        if self.commit_count == 0:
            print('되돌릴 게시물이 없습니다.')
        else:
            self.commit_count -= 1
            print(f'총 커밋한 횟수 : {self.commit_count}입니다.')

    def delete_member(self):
        idx = self.user_total_list.index(self)
        self.user_total_list.pop(idx)
        print(f'{self.name}님이 삭제되었습니다')

    def user_number(self):
        return len(self.user_total_list)

    def user_num():
        return len(UserInfo.user_total_list)

    @classmethod
    def class_user_num(cls):
        return len(cls.user_total_list)


라이캣 = UserInfo('licat',
               'li',
               '010-1234-1234',
               'lili@weniv.com',
               'male',
               ['python', 'JAVA'])
무라 = UserInfo('mura',
              'mu',
              '010-1234-1234',
              'mu@weniv.com',
              'female',
              ['python', 'JavaScript'])
진수 = UserInfo('jinsoo',
              'jin',
              '010-1234-1234',
              'jin@weniv.com',
              'male',
              ['python', 'C++'])

print(UserInfo.user_num())
print(UserInfo.class_user_num())

라이캣.commit()
라이캣.commit()
라이캣.commit()

무라.commit()
무라.commit()
무라.revert()
무라.revert()
무라.revert()

진수.commit()
진수.commit()

print(라이캣)
print(무라)
print(진수)

print(라이캣.user_number())

진수.delete_member()

print(라이캣.user_number())          # 인스턴스 함수
print(UserInfo.user_num())          # 그냥함수
print(UserInfo.class_user_num())    # 클래스함수
```

    3
    3
    licat님이 커밋을 수행했습니다.
    licat님이 커밋을 수행했습니다.
    licat님이 커밋을 수행했습니다.
    mura님이 커밋을 수행했습니다.
    mura님이 커밋을 수행했습니다.
    총 커밋한 횟수 : 1입니다.
    총 커밋한 횟수 : 0입니다.
    되돌릴 게시물이 없습니다.
    jinsoo님이 커밋을 수행했습니다.
    jinsoo님이 커밋을 수행했습니다.
    이름:licat, 닉네임:li, 커밋수:3, 언어:['python', 'JAVA']
    이름:mura, 닉네임:mu, 커밋수:0, 언어:['python', 'JavaScript']
    이름:jinsoo, 닉네임:jin, 커밋수:2, 언어:['python', 'C++']
    3
    jinsoo님이 삭제되었습니다
    2
    2
    2

```python
# 각 class 만들고 인스턴스 2개 이상 넣어서 활용(출력, 수정) 해보세요
# 총 30분

class UserInfo(object):

    user_total_list = []

    def __init__(self, name, nickname, phone, email, gender, language):
        self.name = name
        self.nickname = nickname
        self.phone = phone
        self.email = email
        self.gender = gender
        self.commit_count = 0
        self.language = language
        self.user_total_list.append(self)

    def __str__(self):
        return f'이름:{self.name}, 닉네임:{self.nickname}, 커밋수:{self.commit_count}'

    def commit(self):
        self.commit_count += 1
        print(f'{self.name}님이 커밋을 수행했습니다.')

    def revert(self):
        if self.commit_count == 0:
            print('되돌릴 게시물이 없습니다.')
        else:
            self.commit_count -= 1
            print(f'총 커밋한 횟수 : {self.commit_count}입니다.')

    def delete_member(self):
        idx = self.user_total_list.index(self)
        self.user_total_list.pop(idx)
        print(f'{self.name}님이 삭제되었습니다')

    def user_num(self):
        return len(self.user_total_list)

라이캣 = UserInfo('licat', 'li', '010-1234-1234', 'lili@weniv.com', 'male', ['python', 'JAVA'])
무라 = UserInfo('mura', 'mu', '010-1234-1234', 'mu@weniv.com', 'female', ['python', 'JavaScript'])
진수 = UserInfo('jinsoo', 'jin', '010-1234-1234', 'jin@weniv.com', 'male', ['python', 'C++'])

라이캣.commit()
라이캣.commit()
라이캣.commit()

무라.commit()
무라.commit()
무라.revert()
무라.revert()
무라.revert()

진수.commit()
진수.commit()

print(라이캣)
print(무라)
print(진수)

print(라이캣.user_num())

진수.delete_member()

print(라이캣.user_num())

print('\n\n')

class BookInfo(object):

    total_book_list = []

    def __init__(self, title, writer, number, price, publisher):
        self.title = title
        self.writer = writer
        self.number = number
        self.price = price
        self.publisher = publisher
        self.review = []
        self.total_book_list.append(self)

    def __str__(self):
        return f'제목:{self.title}, 저자:{self.writer}, 가격:{self.price}'

    def write_review(self, content):
        self.review.append(content)
        print(f'책 {self.title}의 후기가 작성되었습니다.')

    def view_review(self):
        print(f'{self.title}의 책 리뷰 :')
        print(self.review)



파이썬길잡이 = BookInfo('파이썬 길잡이1', '이호준', '800', '23000','빠빠')
파이썬길잡이2 = BookInfo('파이썬 길잡이2', '이호준', '850', '25000','빠빠')

print(파이썬길잡이)
print(파이썬길잡이2)

파이썬길잡이.write_review('매우매우좋아요!')
파이썬길잡이.write_review('정말좋아요!')
파이썬길잡이.write_review('좋아요!')

파이썬길잡이.view_review()

```

    licat님이 커밋을 수행했습니다.
    licat님이 커밋을 수행했습니다.
    licat님이 커밋을 수행했습니다.
    mura님이 커밋을 수행했습니다.
    mura님이 커밋을 수행했습니다.
    총 커밋한 횟수 : 1입니다.
    총 커밋한 횟수 : 0입니다.
    되돌릴 게시물이 없습니다.
    jinsoo님이 커밋을 수행했습니다.
    jinsoo님이 커밋을 수행했습니다.
    이름:licat, 닉네임:li, 커밋수:3
    이름:mura, 닉네임:mu, 커밋수:0
    이름:jinsoo, 닉네임:jin, 커밋수:2
    3
    jinsoo님이 삭제되었습니다
    2



    제목:파이썬 길잡이1, 저자:이호준, 가격:23000
    제목:파이썬 길잡이1, 저자:이호준, 가격:23000
    책 파이썬 길잡이1의 후기가 작성되었습니다.
    책 파이썬 길잡이1의 후기가 작성되었습니다.
    책 파이썬 길잡이1의 후기가 작성되었습니다.
    파이썬 길잡이1의 책 리뷰 :
    ['매우매우좋아요!', '정말좋아요!', '좋아요!']

```python
# 1번째 스텝
# 공개되는 정보, 공개되지 않는 정보
# 멤버(정적 수치, 문자열)와 메서드(기능)

class Product(object):

    def __init__(self, 품명, 가격):
        self.product_name = 품명
        self.price= 가격


class UserInfo(object):

    def __init__(self,
                 이름,
                 이메일,
                 비밀번호,
                 주요접속기기,
                 주요접속국가,
                 주요접속지역,
                 마지막접속일자,
                 회원가입날짜,
                 별명,
                 적립금,
                 생일,
                 휴대폰번호,
                 휴대폰인증여부,
                 고객등급,
                 휴면계정여부):

        self.이름 = 이름
        self.이메일 = 이메일
        self.비밀번호 = 비밀번호
        # self.주요접속기기 =
        # self.주요접속국가 =
        # self.주요접속지역 =
        # self.마지막접속일자 =
        # self.회원가입날짜 =
        # self.별명 =
        self.적립금 = 적립금
        # self.생일 =
        # self.휴대폰번호 =
        # self.휴대폰인증여부 =
        self.고객등급 = 고객등급
        # self.휴면계정여부 =

    def 물품구매(self, product):
        self.적립금 -= product.price

    def 회원탈퇴(self):
        pass

    def 장바구니등록(self):
        pass

자전거 = Product('bycle', 10000)

이호준 = UserInfo(
    이름 = '이호준',
    이메일 = 'hojun@gmail.com',
    비밀번호 = 'helloworld!',
    주요접속기기 = 'Android',
    주요접속국가 = 'Korea',
    주요접속지역 = 'Jeju',
    마지막접속일자 = '23/05/10',
    회원가입날짜 = '23/05/10',
    별명 = 'jun',
    적립금 = 1000000,
    생일 = '13/13',
    휴대폰번호 = '010-1234-1234',
    휴대폰인증여부 = True,
    고객등급 = 'VIP',
    휴면계정여부 = False)


이호준.물품구매(자전거)
이호준.적립금
```

    990000

```python
# python read only method 만드는법??
```

```python
import hashlib

pw = hashlib.sha256()
pw.update('helloworld!'.encode('utf-8'))
print(pw.hexdigest()) # 영화, 음악, 소설, 암호 뭐든지 64자로 만듭니다.

# 단방향으로 바꿔줌. 결과물을 보고 input을 알 수 없음!


```

    98d234db7e91f5ba026a25d0d6f17bc5ee0a347ea2216b0c9de06d43536d49f4

```python
class Car(object):

    MaxSpeed = 300
    MaxPeoeple = 5

    def __init__(self):
        pass

    def move(self, x):
        pass

    def stop(self):
        print('멈췄습니다.')

    @staticmethod #decorator
    def 스피드배속(현재스피드, 배속할스피드):
        print(f'현재 {현재스피드 * 배속할스피드}의 스피드로 달리고 있습니다.')

Car.스피드배속(100, 2)  # 붕어빵 찍는 틀이 얼마나 붕어빵을 만들어내는가?
```

    현재 200의 스피드로 달리고 있습니다.

```python
# 예를들어
# 클래스에서 함수를 호출해서 사용하고 싶을 때 static 메서드가 필요하다!

# class Hotel():
#     pass

# Hotel.빈방있는호텔() #전체 호텔의 빈방이 있는
# 호텔1.빈방() #호텔 1의 빈방
```

## 상속 (inheritance)

```python
# 이 예제는 기억하고 있으셔야 합니다.

class Car(object):
    maxSpeed = 300
    maxPeople = 5
    def move(self, x):
        print(x, '의 스피드로 달리고 있습니다.')
    def stop(self):
        print('멈췄습니다.')

class HybridCar(Car):
    battery = 1000
    batteryKM = 300

class ElectricCar(HybridCar):
    battery = 2000
    batteryKM = 600


k5 = HybridCar()
electricCarK5 = ElectricCar()
k5.maxSpeed
print(electricCarK5.maxSpeed)
print(electricCarK5.battery)

# dir(Car)
# dir(k3)
print(dir(Car))
print(dir(k3))
```

    300
    2000
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'maxPeople', 'maxSpeed', 'move', 'stop']
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add_kinds', 'change_speed', 'change_test', 'kinds', 'speed', 'test']

```python
Hyk3 = HybridCar()
k3 = Car()
elk3 = ElectricCar()

# 상속받은 멤버, 함수는 같은 id 를 가리킨다!
print(id(Hyk3.maxSpeed), id(k3.maxSpeed))   # 같음
print(id(Hyk3.move), id(k3.move))           # 같음

elk3.move(10)

```

    140191215500816 140191215500816
    140191213345152 140191213345152
    10 의 스피드로 달리고 있습니다.

## !! 오늘 배운 것 정리 230510

- 클래스

  - 클래스는 데이터(멤버)와 기능(메서드)을 가지고 있는 인스턴트 객체를 생성하기 위한 역할
  - 우리가 배우고 있는 Python을 객체 지향 프로그래밍 언어

    ```
    현실                                코드
    차 ---------------------------> class Car()
    정수 -------------------------> class int()
    실수 -------------------------> class float()

    인간이 만들어
    놓은 현실 세계에서의
    정의 또는 약속 --------------> class

    1 + 1 = 2가 컴퓨터 입장에서는 10일 수도 있고
    'A' + 'A' = 'AA'가 아니라 컴퓨터 입장에서는 130일 수 있습니다.
    현실세계에서 '인간끼리' 약속을 코드에 세계로 옮긴거에요.
    ```

  - 예제 1

    ```python
    # 메서드 : 클래스 내에 함수
    # 멤버 : 클래스 내에 변수
    # 애트리뷰트 : 멤버 + 메서드
    class CarFactory(object):
        max_speed = 300
        max_people = 5
        def move(self):
            print('차가 움직이고 있습니다.')
        def stop(self):
            print('차가 멈췄습니다.')

    k5 = CarFactory()
    k3 = CarFactory()
    k5.move()
    k3.move()
    k5.stop()
    k3.stop()
    print(k5.max_speed)
    ```

  - 예제2

    ```python
    # 클래스 변수
    # 클래스 바로 하위에 자리하고 있으며
    # 모든 인스턴스가 공유합니다.
    # 인스턴스 변수
    # 인스턴스 영역 안에서만 사용하는 변수
    class Car(object):
        # kinds가 인스턴스에 없기에 class변수로 접근
        # speed는 값을 = 로 할당했기에 인스턴스변수 생성
        kinds = []
        speed = 300
        def add_kinds(self, name):
            self.kinds.append(name) # self.kinds = [name]로 사용하면 인스턴스 변수가 됩니다.
        def change_speed(self, speed):
            self.speed = speed

    k5 = Car()
    k3 = Car()
    k5.speed = 500
    k3.speed # 클래스 변수는 값을 공유한다고 했는데?
    ```

  - 예제3

    ```python
    # 쉽고 중요한 예제!
    # 이 코드는 가능하면 손으로 2 ~ 3번 써보시길 권해드립니다.

    class BlogFactory(object):
        def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
            self.title = 제목
            self.content = 내용
            self.count = 조회수
            self.writer = 글쓴이
            self.create_date = 생성날짜

    게시글1 = BlogFactory(
            '오늘 제주의 날씨',
            '오늘 제주의 날씨는 참 좋네요! 블라블라',
            '0',
            '이호준',
            '2023/05/10',
        )

    게시글2 = BlogFactory(
            '오늘 부산의 날씨',
            '오늘 부산의 날씨는 참 좋네요! 블라블라',
            '1000000',
            '김재현',
            '2023/05/10',
        )

    게시글3 = BlogFactory(
            '오늘 강원의 날씨',
            '오늘 강원의 날씨는 참 좋네요! 블라블라',
            '10000',
            '범남궁',
            '2023/05/10',
        )

    data = [게시글1, 게시글2, 게시글3]
    for i in data:
        if i.writer == '이호준':
            print(i.title)
            print(i.content)
            print(i.count)
            print(i.create_date)
    ```

- 클래스 상속

  - 클래스에서 상속은 상속해주는 클래스(Parent Class, Super class)의 내용(속성과 메소드)을 상속받는 클래스(Child class, sub class)가 가지게 되는 것
  - 코드 예

    ```python
    # 이 예제는 기억하고 있으셔야 합니다.
    class Car:
        maxSpeed = 300
        maxPeople = 5
        def move(self, x):
            print(x, '의 스피드로 달리고 있습니다.')
        def stop(self):
            print('멈췄습니다.')

    class HybridCar(Car):
        battery = 1000
        batteryKM = 300

    class ElectricCar(HybridCar):
        battery = 2000
        batteryKM = 600

    K3 = Car()
    HyK3 = HybridCar()
    ElHyK3 = ElectricCar()
    # id(K3.maxSpeed), id(HyK3.maxSpeed)
    # id(K3.move), id(HyK3.move)

    ElHyK3.move(10)
    ```

```python
# 우리가 앞으로 알고리즘에서 할 코드입니다.
# 예방주사 차원에서 진행

# 프로그래머스 lv4, lv5는 효율성 체크가 있는데 이럴 경우 반복문으로 해결이 잘 안됨.
# 클래스로 구현해야 되는 경우가 대부분임

```

```python
# linked list 예제 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

노드1 = Node(10)
노드2 = Node(20)
노드3 = Node(30)

# 노드1.data
노드1.next = 노드2
노드2.next = 노드3

노드1.next.data         # 노드2.data
노드1.next.next.data    # 노드2.data.next # 노드3.data

```

    30

```python
# linked list 예제 2 - 데이터 두개 가진 노드
class Node:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
        self.next = None

노드1 = Node(1, 2)
노드2 = Node(3, 4)
노드3 = Node(5, 6)

노드1.next = 노드2
노드2.next = 노드3

print(노드1.next.data1)
print(노드1.next.data2)
print(노드1.next.next.data1)
print(노드1.next.next.data2)

```

    3
    4
    5
    6

## 메서드 오버라이딩

- 부모 클래스에서 상속받은 메서드를 자식 클래스에서 같은 이름으로 선언하여 사용하는 것 (덮어쓴다 - 오버라이딩)

```python
# 파이썬에서느 오버로딩(이름이 같고 인자수, 타입이 다른 함수 정의)이 공식적으로 지원하지 않음
# --> 오버로딩 하는 방법은 @dispatch 데코레이터 쓰면 됨....
# 오버로딩 : 같은 이름의 메소드를 여러 개 선언하여 다양한 아규먼트에 대응할 수 있게 하는 기법을 의미합니다.

class Car(object):
    maxSpeed = 300
    maxPeople = 5
    def move(self, x):
        print(x, '의 스피드로 달리고 있습니다.')
    def stop(self):
        print('멈췄습니다.')

class HybridCar(Car):
    battery = 1000
    batteryKM = 300

class ElectricCar(HybridCar):
    battery = 2000
    batteryKM = 600

    def move(self, x):
        print(self.batteryKM, '만큼 달릴 수 있습니다.')
        print(x, '스피드로 달리고 있습니다.')

# 자신의 고유 영역에서 선언된 멤버와 메서드를 우선적으로 찾습니다.

k5 = HybridCar()
electricCarK5 = ElectricCar()
print(k5.maxSpeed)
print(electricCarK5.maxSpeed)
print(electricCarK5.battery)
print(electricCarK5.move(10))
```

    300
    300
    2000
    600 만큼 달릴 수 있습니다.
    10 스피드로 달리고 있습니다.
    None

```python
# 어디에 있는 멤버, 함수를 가져올까??
# 나와 가장 가까운 곳에 있는 곳에서 가져온다. (상속순서, 상속 바로 위)

class Car(object):
    maxSpeed = 300
    def move(self, x):
        print(x, '의 스피드로 달리고 있습니다.')


class HybridCar(Car):
    battery = 1000


class ElectricCar(HybridCar):
    battery = 2000

    def move(self, x):
        print(x, '스피드로 모터힘으로! 달리고 있습니다.')


class Test(ElectricCar):
    pass


car1 = ElectricCar()
car1.move(10)
```

    10 스피드로 모터힘으로! 달리고 있습니다.

### 다중상속

```python
# 다중상속. 다이아몬드 상속인 경우...

class A(object):
    maxSpeed = 300


class B(A):
    battery = 1000


class C(A):
    battery = 2000


class D(B, C):
    pass

D.mro() # [__main__.D, __main__.B, __main__.C, __main__.A, object]

D.battery # 1000
# 나와 가장 가까운 곳에서 가져온다!
# D class는 B를 먼저 상속받으니 B의 battery를 가져옴

```

    1000

- 비공개 속성 (attribute)

```python
## __는 문법적으로 접근이 안됩니다. (공식)
# 변수를 보호할 수 있습니다.
# 변수를 변경하는 것을 보다 엄격하게 관리할 수 있습니다.

# _ 는 공식 X
# _ 는 문법적으로 접근이 가능합니다.(회사 컨벤션마다 다릅니다.)


class Car(object):
    __maxSpeed = 300
    _maxPeople = 5
    wheel = 4
    def move(self, x):
        print(x, '의 스피드로 달리고 있습니다.')
        print(self.__maxSpeed, '의 스피드로 달리고 있습니다.')
    def stop(self):
        print('멈췄습니다.')

k5 = Car()
# k5.__maxSpeed   # error # AttributeError
## __로 시작하는 변수는 아얘 호출이 안됨

k5._maxPeople   # 접근가능
k5.wheel        # 당연히 접근 가능
k5.move(10) ## 함수로 값에 접근하는 것은 가능. 변경은 되나??
```

    10 의 스피드로 달리고 있습니다.
    300 의 스피드로 달리고 있습니다.

## 이터레이터

```python
# 단순한 이터레이터를 만들어보자!

class MyIter:
    def __init__(self, stop):
        self.currentValue = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.currentValue >= self.stop:
            raise StopIteration     # 에러 발생시키는 구문 raise
        self.currentValue += 1
        return self.currentValue

mi = MyIter(5)

for i in mi:
    print(i, end=' ')

# 똑같이 한 번만 출력됨. 아래는 출력 안됨
for i in mi:
    print(i, end=' ')


```

    1 2 3 4 5

```python
# 단순한 이터레이터를 만들어보자!

class MyIter:
    def __init__(self, stop):
        self.currentValue = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.currentValue >= self.stop:
            raise StopIteration     # 에러 발생시키는 구문 raise
        result = self.currentValue
        self.currentValue += 1
        return result

mi = MyIter(5)

for i in mi:
    print(i, end=' ')

# 한 번만 출력됨. 아래는 출력 안됨
# 왜냐하면 Stopiteration이 계속 발생하기 때문에 for가 바로 종료됨
for i in mi:
    print(i, end=' ')


```

    0 1 2 3 4

```python
# 단순한 이터레이터를 만들어보자!

class MyIter:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        self.currentValue = 0
        return self

    def __next__(self):
        if self.currentValue >= self.stop:
            raise StopIteration     # 에러 발생시키는 구문 raise
        result = self.currentValue
        self.currentValue += 1
        return result

mi = MyIter(5)
# for는 __iter__를 먼저 실행하고, next로 StopIteraion 까지
for i in mi:
    print(i, end=' ')

# __iter__ 에 초기 값을 0으로 세팅하기 때문에
# for 문 진입시 0으로 초기화해서 __next__호출되어도 StopIteraion이 발생 안 됨
for i in mi:
    print(i, end=' ')

```

    0 1 2 3 4 0 1 2 3 4

```python
# 단순한 이터레이터를 만들어보자!

class MyIter:
    def __init__(self, stop):
        self.currentValue = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.currentValue >= self.stop:
            raise StopIteration     # 에러 발생시키는 구문 raise
        result = self.currentValue
        self.currentValue += 1
        return result

mi = MyIter(5)

i = iter(mi)
next(i)
next(i)
next(i)
next(i)
next(i)
# next(i) # StopItertaion

```

    4

- 언패킹

```python
a, b, c, d = MyIter(4)
print(a, b, c, d)
```

    0 1 2 3

```python
a, b, c, d = range(4)
print(a, b, c, d)

## 값이 들어가는 것을 보면 결국 unpacking은 순회를 통해서 값을 넣어주는 것!
## 왜냐하면 __iter__와 __next__가 없다면 return 값이 없기 때문!!!
```

    0 1 2 3

## 제너레이터 generator

- 제너레이터란, 이터레이터를 생성해주는 함수를 의미합니다.

```python
def gen():
    count = 0
    while True:
        yield count
        count += 1

gen() # 무한반복이 아니라 generator object가 나옴
# gen() 은 계속 실행중이고 yield 에서 기다렸다가 다음 순회? 때 값을 생성해주고
# 다시 다음 yield에서 기다림

for i in gen():
    print(i)
    if i == 10:
        break
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10

```python
def gen():
    count = 0
    while True:
        yield count
        count += 2

l = [10,20,30,40,50]
list(zip(l,gen())) ## zip은 짧은 iterable기준으로 순회를 돌기 때문에 유용!

```

    [(10, 0), (20, 2), (30, 4), (40, 6), (50, 8)]

```python
## 제너레이터는 GC(garbege collector)가 수거해가지 않음..??

def gen():
    count = 1
    while True:
        yield count
        count += 1
        if count == 6:
            count = 1

과목 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
list(zip(과목, gen()))
```

    [('A', 1),
     ('B', 2),
     ('C', 3),
     ('D', 4),
     ('E', 5),
     ('F', 1),
     ('G', 2),
     ('H', 3),
     ('I', 4),
     ('J', 5),
     ('K', 1)]

## 데코레이터 decorator

```python
# 아래 예와 같이 실무에서 활용합니다.
#

@login
def 비밀게시판():
    return render()

@check_vip
def vip_coupon():
    return render()

# 데이터 전처리:
# 데이터에 이상치(이상한 값), 결측치(비어있는 값)등을 처리
# ['10', 1, 2, 3, '20'] -> [10, 1, 2, 3, 20]

@데이터 전처리
sum(data)

@데이터전처리후페센테이지
sum(data)

# [10, 20, 30] -> 60%
```

```python
def one():
    return lambda x, y: x + y

더하기 = one()
더하기(10, 10)
```

    20

```python
def one():
    def two(x,y):
        return x+y
    return two

더하기 = one()
더하기(10, 10)
```

    20

```python
# 중요한 코드입니다.
# 손으로 2~3번 써보시기를 권합니다.

def print_hello(func): # def decorator_name(below function)
    def wrap_func():
        print('hello')
        func()
    return wrap_func

@print_hello
def func1():
    print('function1 입니다.')

func1()

# 함수를 호출하면 함수 위에 decorator가 있는지 확인한다.
# decorator가 있다면 데코레이터의 func인자에 호출한 함수를 넣어준다.

```

    hello
    function1 입니다.

```python
# 데코레이터 여러개 테스트해보기

def print_hello(func): # def decorator_name(below function)
    def wrap_func():
        print('hello')
        func()
    return wrap_func

def print_world(func):
    def wrap_func():
        print('world')
        func()
    return wrap_func

# 함수 선언부에서 한 줄씩 올라가면서 확인하는듯 하오...
@print_world
@print_hello
def func1():
    print('function1 입니다.')

func1()

```

    hello
    world
    function1 입니다.

```python
def 인사말(func):
    def wrap_func():
        print('안녕하세요.')
        func()
    return wrap_func

@인사말
def 자기소개1():
    print('이호준입니다')


@인사말
def 자기소개2():
    print('홍길동입니다.')

def 작별인사():
    print('안녕히계세요.')

자기소개1()
자기소개2()
작별인사()

```

    안녕하세요.
    이호준입니다
    안녕하세요.
    홍길동입니다.
    안녕히계세요.

```python
# 인자가 있는 함수의 데코레이터 사용하기

def 인사말(func):
    def wrap_func(arg): # 이렇게 랩 함수에 인자 자리를 만들어줘야함.
        print('안녕하세요.')
        func(arg)
    return wrap_func

@인사말
def 자기소개1(name):
    print(f'{name}입니다')

@인사말
def 자기소개2(name):
    print(f'{name}입니다.')

def 작별인사():
    print('안녕히계세요.')

자기소개1('이호준')
자기소개2('홍길동')
작별인사()

```

    안녕하세요.
    이호준입니다
    안녕하세요.
    홍길동입니다.
    안녕히계세요.

```python
# 실무에서 데코레이터

def 전처리(func):
    def wrap_func(iterable):
        iterable = list(map(int, iterable))
        return func(iterable)
    return wrap_func

@전처리
def 평균(li):
    return sum(li) / len(li)

평균(['1', 2, 3, '4'])

```

    2.5

```python
def 전처리(func):
    def wrap_func(iterable):
        return func(list(map(int, iterable)))
    return wrap_func

@전처리
def 평균(li):
    return sum(li) / len(li)

평균(['1', 2, 3, '4'])
```

    2.5

```python
# 이상하긴하지만...
def 전후처리(func):
    def wrap_func(iterable):
        i = list(map(int, iterable))
        calculate = func(i)
        result = str(calculate) + '%'
        return result
    return wrap_func

@전후처리
def 평균(li):
    return sum(li) / len(li)

평균(['1', 2, 3, '4'])
```

    '2.5%'

```python
# 데코레이터 실습 문제
# 다음 값이들어갔을 때, 숫자만 모두 더하는 코드를 완성하세요
li = ['10', True, False, '21', 0 ,10, 20]

def 전처리(func):
    def wrap_func(array):
        ## True, False는 int 타입으로 됨....
        a = list(filter(lambda x : isinstance(x, int) and not isinstance(x, bool), array))
        result = func(a)
        return result
    return wrap_func

@전처리
def customsum(li):
    return sum(li)


customsum(li)


```

    [0, 10, 20]





    30

```python
def decorator1(func):
    def wrapper():
        print('decorator1 - wrapper func id:', id(func))
        func()
    print('decorator1 wapper id: ', id(wrapper))
    return wrapper

def decorator2(func):
    def wrapper():
        print('decorator2 - wrapper func id:', id(func))
        func()
    print('decorator2 wapper id: ', id(wrapper))
    return wrapper

# 데코레이터를 여러 개 지정 wrapper 함수가 위의 decorator의 func로 들어감
@decorator1
@decorator2
def hello():
    print('hello')

hello()
id(hello)
# 가장 바깥쪽 wrapper 함수와 id가 같다!
# hello() << decorator1의 return wrapper
```

    decorator2 wapper id:  140662148697248
    decorator1 wapper id:  140662148695664
    decorator1 - wrapper func id: 140662148697248
    decorator2 - wrapper func id: 140662148697104
    hello





    140662148695664

```python
def decorator1(func):
    def wrapper():
        func()
    print('decorator1 - func id:', id(func))
    print('decorator1 wapper id:', id(wrapper))
    return wrapper

def decorator2(func):
    def wrapper():
        func()
    print('decorator2 - func id:', id(func))
    print('decorator2 wapper id:', id(wrapper))
    return wrapper

# 데코레이터를 여러 개 지정 wrapper 함수가 위의 decorator의 func로 들어감
@decorator1
@decorator2
def hello():
    print('hello')

hello()
print(id(hello))
# 가장 바깥쪽 wrapper 함수와 id가 같다!
```

    decorator2 - func id: 140661872843008
    decorator2 wapper id: 140661872846320
    decorator1 - func id: 140661872846320
    decorator1 wapper id: 140661872846464
    hello
    140661872846464

- 데코레이터에 아규먼트 넣기!

```python
# 데코레이터에 argument를 넣는 방법
# 한번 더 감싸줘야 함
def deco1(name):
    print(name)
    def deco2(func):
        def wrapper():
            print('decorator1')
            func()
        return wrapper
    return deco2

# 데코레이터를 여러 개 지정
@deco1('hojun')
def hello():
    print('hello')

hello()
```

    hojun
    decorator1
    hello

## 모듈과 패키지

```python
# 현재 폴더에 test1.py 파일을 생성했고
# name = 'leehojun'
# age = 10

# class Human():
#     pass

# def hello():
#     pass
```

```python
# 연습 1 : 파일

import test1

print(test1.name)
print(test1.hello())
```

    leehojun
    None

```python
# 같은 이름이 있었을 경우
# 마지막에 추가된 변수명으로 할당한다.
# !! 주의 !!
# import * 는 포함시키는 변수, 메서드, 클래스 명을 알 수 없으므로
# 주의해서 사용해야 한다.

# 연습 2 : 파일 > 변수
# from 파일 import 변수명 으로 도 가능

from test2 import name
from test1 import name

print(name)
```

```python
# 연습 3 : 폴더 > 파일
# one이라는 것은 여기서는 폴더이름 입니다.
# two는 file이름
from one import two

print(two.name)
```

    hello world

```python
# 연습 4 : 폴더 > 폴더 > 파일
# 폴더 안에 폴더는 . 으로 진입한다

from one.two import three

print(three.name)
```

    walalalala

```python
# 연습 5 : as 키워드로 별칭 정하기
import test1 as t

t.hello()
```

    hello world

```python
# Python 모듈
import pandas as pd
import numpy as np
```

```python

# 패키지 설치 !pip install 패키지이름

# 설치된 패키지 확인
!pip list
```

```python
import random as rd
rd.randint(0,10)
# random.randint(0,10) # 별칭 정하면 원래일므은 안됨

```

    6

## 파일 입출력

```python
# open(파일이름, 파일모드)
# 파일이 생성됨!
f = open('python.txt', 'w') # 파일모드 : r(read), w(write, 덮어씁니다.), a(append 추가합니다)
f.close()
```

```python
f = open('python.txt', 'w')
s = 'hello\nworld'
f.write(s)
f.close()
```

```python
#문제 모듈안쓰고
data1 = ['one', 'two', 'three']
data2 = [10,20,30]
'''
{
    "one" : 10,
    "two" : 20,
    "three" : 30
}
'''

d = dict(zip(data1, data2))

f = open ('data2.json', 'w')
s = '{'
for i, j in zip(data1, data2):
    s += f'\n    \"{i}\" : {j},'

s = s[0:-1]
s += '\n}'
print(s)
f.write(s)
f.close()
```

    {
        "one" : 10,
        "two" : 20,
        "three" : 30
    }

```python
import json

data1 = ['one', 'two', 'three']
data2 = [10,20,30]
'''
{
    "one" : 10,
    "two" : 20,
    "three" : 30
}
'''

d = dict(zip(data1, data2))
s = json.dumps(d, indent=4) ## 단순히 json 형식의 string으로 바꿔주는 함수
print(s)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent='\t') ## file object가 있기 때문에 파일에 쓰는것까지~
f.close()
```

    {
        "one": 10,
        "two": 20,
        "three": 30
    }

## 파일 읽기

- readline() : 라인 별로 읽습니다.

```python
f = open('python.txt', 'r')
while True:
	line = f.readline()
	if not line:
		break
	print(line, end='')
f.close()
```

    hello
    world

- readlines() : 전체 텍스트를 한꺼번에 읽어 줄 순서대로 list로 저장해 반환합니다

```python
f = open('python.txt', 'r')
lines = f.readlines()
# print(lines)        # ['hello\n', 'world']
# print(type(lines))  # list
for line in lines:
	print(line)
f.close()
```

    ['hello\n', 'world']
    <class 'list'>
    hello

    world

- read() : 파일 전체 내용을 읽어올 수 있습니다

```python
f = open('python.txt', 'r')
data = f.read()
print(data)
f.close()
```

    hello
    world

```python
## 위에 한 줄씩 풀력하던 예제들이 2줄 개행되었던 이유는
# print 함수가 이미 개행 옵션을 가지고 있기 때문입니다.

f = open('python.txt', 'r')
lines = f.readlines()
for line in lines:
	print(line, end='')
f.close()
```

    hello
    world

## 파일 내용 추가

```python
f = open('python.txt', 'w')
s = ''

for i in range(5):
    s += f'{i}명 참여 중입니다.\n'

f.write(s)
f.close()
```

```python
f = open('python.txt', 'a') # 다시 'w'로 열면 처음부터 덮어 씀
s = ''

for i in range(5, 11):
    s += f'{i}명 참여 중입니다.\n'

f.write(s)
f.close()
```

- 파일이 계속 열려있는 상태가 유지
- 메모리 효율

## 파일 열기와 닫기를 동시

- 파이썬 객체를 파일에 저장 : 피클링
- 파일에어 객체를 읽어오기 : 언피클링

```python
with open('test.txt', 'w') as f:
	f.write('Life is too short, you need python')
```

## 파일 입출력 심화과정

- github(https://github.com/paullabkorea/xlsxwriter) 에서 모든 소스코드를 다운로드 받으실 수 있습니다.
- 엑셀 차트, 이미지 삽입, 한글파일 -> DataFrame 변환을 통한 데이터 분석 등은 요약강좌에서 다루지 않습니다.
- 무료책인 인공지능을 활용한 업무자동화 책(2021 Version Notion)을 활용하면 좀 더 활용성이 극대화된 코딩이 가능합니다.(크롤링, 워드파일 크롤링, PDF크롤링, 문자 보내기 등)
- 업무자동화 Notion 링크 : https://paullabworkspace.notion.site/2021-6192ed4219fc4e7a96e10b22cfa27c80

```python
!pip3 install xlsxwriter
```

    Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/
    Collecting xlsxwriter
      Downloading XlsxWriter-3.1.0-py3-none-any.whl (152 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m152.7/152.7 kB[0m [31m10.5 MB/s[0m eta [36m0:00:00[0m
    [?25hInstalling collected packages: xlsxwriter
    Successfully installed xlsxwriter-3.1.0

```python
# 엑셀 다루는 패키지 openpyxl, xlrd, xlwt ...
# 그중에서 강사님은 xlsxwriter 괜찮다고 생ㄱ각해서 이걸로..
# 다른 사용자가 만든 모듈들


```

```python
import xlsxwriter as xw
```

```python
# 엑셀 파일 생성하기
workbook = xw.Workbook('test.xlsx')

# 파일 안에 워크시트 생성하기
worksheet = workbook.add_worksheet('test')

data = ['AA', 'BB', 'CC', 'DD']
worksheet.write('A1', data[0])
worksheet.write('B1', data[1])
worksheet.write('C1', data[2])
worksheet.write('D1', data[3])

worksheet.write('A2', 1)
worksheet.write('B2', 2)
worksheet.write('C2', 3)
worksheet.write('D2', 4)

worksheet.write(2,0, 10)    # 행, 열, 값
worksheet.write(2,1, 20)
worksheet.write(2,2, 30)
worksheet.write(2,3, 40)

workbook.close()
```

```python
# 엑셀 파일 생성하기
workbook = xw.Workbook('testtest.xlsx')

# 파일 안에 워크시트 생성하기
worksheet2 = workbook.add_worksheet('test2')

홍길동 = [33, 88, 24]
이호준 = [34, 66, 77]
김철수 = [78, 82, 36]

홍길동.append(sum(홍길동)/len(홍길동))
이호준.append(sum(이호준)/len(이호준))
김철수.append(sum(김철수)/len(김철수))

항목 = ['이름', '국어', '영어', '수학', '평균']
for i in range(len(항목)):
    worksheet2.write(0, i, 항목[i])

worksheet2.write(1, 0, '홍길동')
for i in range(len(홍길동)):
    worksheet2.write(1, i+1, 홍길동[i])

worksheet2.write(2, 0, '이호준')
for i in range(len(이호준)):
    worksheet2.write(2, i+1, 이호준[i])

worksheet2.write(3, 0, '김철수')
for i in range(len(김철수)):
    worksheet2.write(3, i+1, 김철수[i])

workbook.close()
```

```python
# 자동화 하기 전에.... 배보다 배꼽이 더 큰지 확인하기
# 개발 시간 + 유지 보수
```

## OS 모듈

```python
import os
os.getcwd()  # 현재폴더위치를 string으로
```

    '/content'

```python
os.listdir()    # 현재위치에 있는 폴더, 파일 목록을 list로
```

    ['.config',
     'testtest.xlsx',
     'test.xlsx',
     'python.txt',
     'test1.py',
     '__pycache__',
     'data.json',
     'data2.json',
     '.ipynb_checkpoints',
     'one',
     'sample_data']

```python
for i in os.listdir():
    if len(i.split('.')) >= 2:
        if i.split('.')[1] == 'py' or i.split('.')[1] == 'txt':
            print(i)
```

    python.txt
    test1.py

```python
for i in os.listdir():
    if i[0] != '.' and '.' in i:
        if i.split('.')[1] == 'py' or i.split('.')[1] == 'txt':
            print(i)

```

    python.txt
    test1.py

```python
os.mkdir('hello') #폴더를 생성할 일이 업습니다.
```

```python
# glob.. 처음본다
# glob 모듈의 glob 함수는 사용자가 제시한 조건에 맞는 파일명을 리스트 형식으로 반환한다.
# 조건에 정규식을 사용할 수 없으며 엑셀 등에서도 사용할 수 있는
# '*'와 '?'같은 와일드카드만을 지원한다.

import glob

glob.glob("*.py")
```

    ['test1.py']

```python

```

## advanced 문제

```python
@writefile
def add(a, b):
    return a + b

writefile의 데코레이터 기능은 아래와 같은 형식으로 result.txt에 항상 저장되게 하는 것입니다.
{
    "a": 10,
    "b": 20,
    "a+b": 30
}
```

```python
import json

def writefile(func):
    def wrapper(arg1, arg2):
        f = open('result.txt', 'w')
        d = {'a': arg1, 'b': arg2, 'a+b': func(arg1, arg2)}
        f.write(json.dumps(d, indent='\t'))
        f.close()
        ## 원래 add의 정수 리턴은 있어야 함
        return func(arg1, arg2)
    return wrapper

@writefile
def add(a, b):
    return a + b

add(10, 20)
```

    30

## !! 오늘 배운 것 정리 230511

- 제너레이터
  - 제너레이터란, 이터레이터(순회 가능한 객체)를 생성해주는 함수
  - 예제 1
    ```python
    def gen():
        count = 0
        while True:
            yield count
            count += 1
    for i in gen():
        print(i)
        if i == 10:
            break
    ```
- 데코레이터

  - 함수 앞 뒤로 다른 역활을 해주는 기능을 붙이고 싶을 때 사용
  - 코드 예

    ```python
    def print_hello(func):
        def wrap_func():
            print('hello start')
            func()
            print('hello end')
        return wrap_func

    @print_hello
    def func1():
        print('func1 입니다.')

    func1()
    ```

- 파이썬 모듈

  - 모듈 : 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일
  - 패키지 : 파이썬 모듈들을 계층적으로 관리
  - 모듈 사용 예1

  ```python
  # 같은 폴더 내 test1.py
  name = 'leehojun'
  age = 10

  def hello():
      pass

  class Human():
      pass

  # 같은 폴더 내 실행 파일
  import test1

  print(test1.name)
  print(test1.hello())
  ```

  - 예2

  ```python
  # 연습 3 (폴더 > 파일 생성)
  # one이라는 것이 여기서는 폴더입니다!
  # two가 file 이름이에요.
  from one import two

  print(two.name)
  ```

  - 예3

  ```python
  # 연습 4 (폴더 > 폴더 > 파일 생성)
  # 런타임 재시작 하세요!
  from one.two import three

  print(three.name)
  ```

- 파일 입출력
  - 파일을 읽고 쓰는 것
    - 파일 쓰기
    ```python
    f = open('python.txt', 'w')
    # 파일모드 : r(read), w(write, 처음부터 덮어씁니다.), a(append)
    s = 'hello\nworld'
    f.write(s)
    f.close()
    ```
    - 파일 읽기
    ```python
    f = open('python.txt', 'r')
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
    f.close()
    ```
    ```python
    f = open('python.txt', 'r')
    data = f.read()
    print(data)
    f.close()
    ```

## Python Error

- Python 에서는 에러를 만나게 되면 코드(서비스)가 멈춥니다.
- 여러분일이 짠 코드가 서비스에 영향이 끼쳐지지 않도록 시니어 분들이 견고한 코드를 작성해놨을 겁니다.
- TDD, 테스트 주도 개발 등 Test를 할 수 있는 환경 등이 갖춰져 있습니다.
- 작성한 코드는 실서비스로 배포되지 않습니다. 작성한 코드는 테스트 서버로 일단 배포되서 잘 작동하는지 테스트 해봅니다.
- 에러가 발생해도 멈추지 않도록 처리해놔야 함
- https://docs.python.org/ko/3/library/exceptions.html

```python
1/0
```

    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-9-9e1622b385b6> in <cell line: 1>()
    ----> 1 1/0


    ZeroDivisionError: division by zero

```python
for i in range()
    print(i)
```

      File "<ipython-input-10-f5f7d28ce00f>", line 1
        for i in range()
                        ^
    SyntaxError: expected ':'

```python
#Name Error
print(x)
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-29a9822e258e> in <cell line: 2>()
          1 #Name Error
    ----> 2 print(x)


    NameError: name 'x' is not defined

```python
# type error
x = 10
y = '20'
print(x+y)
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-daabb66859a4> in <cell line: 4>()
          2 x = 10
          3 y = '20'
    ----> 4 print(x+y)


    TypeError: unsupported operand type(s) for +: 'int' and 'str'

```python
# IndexError: list index out of range
li = [1,2,3]
print(li[3])
```

    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-13-9460933b46ac> in <cell line: 2>()
          1 li = [1,2,3]
    ----> 2 print(li[3])


    IndexError: list index out of range

```python
# Key Error
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])
```

    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-14-8f9ea626777a> in <cell line: 3>()
          1 # Key Error
          2 my_dict = {'a': 1, 'b': 2}
    ----> 3 print(my_dict['c'])


    KeyError: 'c'

```python
# Value Error
int('a')
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-15-b8f9f0574b88> in <cell line: 2>()
          1 # Value Error
    ----> 2 int('a')


    ValueError: invalid literal for int() with base 10: 'a'

```python
# Attribute Error
my_list = [1, 2, 3]
print(my_list.appeeend(4))
```

    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-16-eb0bc41007a3> in <cell line: 3>()
          1 # Attribute Error
          2 my_list = [1, 2, 3]
    ----> 3 print(my_list.appeeend(4))


    AttributeError: 'list' object has no attribute 'appeeend'

```python
# Type Error
def add(x, y):
    return x + y

add(1, 2, 3)
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-17-cbb8c8b9d43a> in <cell line: 5>()
          3     return x + y
          4
    ----> 5 add(1, 2, 3)


    TypeError: add() takes 2 positional arguments but 3 were given

## 예외 처리

```python
try:
    # 예외가 발생할 가능성이 있는 코드
except:
    # 예외 처리 코드
```

```python
def div(a, b):
    return a/b

try:
    div(1,0) # Zerodivision 에러 발생하는 코드
except:
    print('예외발생')

# 예외가 발생하지만 프로그램이 정상종료됨
```

    예외발생

```python
def div(a, b):
    return a/b

def f():
    try:
        return div(1,0) # Zerodivision 에러 발생하는 코드
    except:
        print('예외발생')

result = f() + f()
print(result)
# 예외처리를 해도 에러가 발생함. except일때 None이 리턴되서...
```

    예외발생
    예외발생



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-19-eb3f81f9d654> in <cell line: 10>()
          8         print('예외발생')
          9
    ---> 10 result = f() + f()
         11 print(result)
         12 # 예외가 발생하지만 프로그램이 정상종료됨


    TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

```python
def div(a, b):
    return a/b

def f():
    try:
        return div(1,0) # Zerodivision 에러 발생하는 코드
    except:
        return float('inf')

result = f() + f()
print(result)
```

    inf

```python
try:
    # 예외가 발생할 가능성이 있는 코드
except:
    # 예외 처리 코드
else:
    # 예외가 발생하지 않을 때 실행되는 코드
```

```python
try:
    # 예외가 발생할 가능성이 있는 코드
    1/0
except:
    # 예외 처리 코드
    print('예외발생')
else:
    # 예외가 발생하지 않을 때 실행되는 코드
    print('정상종료!')
```

      File "<ipython-input-23-46fba07648ac>", line 4
        return 0
        ^
    SyntaxError: 'return' outside function

```python
try:
    # 예외가 발생할 가능성이 있는 코드
    1/2
except:
    # 예외 처리 코드
    print('예외발생')
else:
    # 예외가 발생하지 않을 때 실행되는 코드
    print('정상종료!')
```

    정상종료!

```python
# while, for, try-except 구문에서 else는
# 정상 종료되었을 때 실행됨
```

```python
# try + finally
# 에러가 나면 코드가 멈추기 때문에 except와 함께 사용합니다.
# finally는 예외발생 여부와 관계없이 반드시 실행되는 코드 구문

try:
    # 예외가 발생할 가능성이 있는 코드
finally:
    # 예외 발생 여부와 상관없이 항상 실행되는 코드
```

```python
try:
    1/0
finally:
    print('finally')

print('hello world')
#코드는 멈추지만 finally는 진행되고 넘춤..

```

    finally



    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-25-7db3cd53a009> in <cell line: 1>()
          1 try:
    ----> 2     1/0
          3 finally:
          4     print('finally')
          5


    ZeroDivisionError: division by zero

```python
# try + except + finally

try:
    # 예외가 발생할 가능성이 있는 코드
except:
    # 예외 처리 코드
finally:
    # 예외 발생 여부와 상관없이 항상 실행되는 코드
```

```python
try:
    1/0
except:
    print('hello')
finally:
    print('world')
```

    hello
    world

```python
# try + except + else + finally
try:
    # 예외가 발생할 가능성이 있는 코드
except:
    # 예외 처리 코드
else:
    # 예외가 발생하지 않을 때 실행되는 코드
finally:
    # 예외 발생 여부와 상관없이 항상 실행되는 코드
```

```python
try:
    1/1
except:
    print('예외발생')
else:
    print('정상종료')
finally:
    print('finally')
```

    정상종료
    finally

```python
## 에러를 발생시키는 코드 raise 에러이름
raise
```

    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-29-b8bfe78cb41b> in <cell line: 2>()
          1 ## 에러를 발생시키는 코드 raise
    ----> 2 raise


    RuntimeError: No active exception to reraise

```python
# raise 에러이름
raise ValueError
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-31-96bae104f54a> in <cell line: 2>()
          1 # raise 에러이름
    ----> 2 raise ValueError


    ValueError:

```python
raise Leehojun  # NameError: name 'Leehojun' is not defined
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-33-61eba9777a7b> in <cell line: 1>()
    ----> 1 raise Leehojun  # NameError: name 'Leehojun' is not defined


    NameError: name 'Leehojun' is not defined

```python
raise ValueError('코드를 잘~~ 좀 만들어주세요.')
# ValueError: 코드를 잘~~ 좀 만들어주세요.
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-34-1b33900d34c0> in <cell line: 1>()
    ----> 1 raise ValueError('코드를 잘~~ 좀 만들어주세요.')


    ValueError: 코드를 잘~~ 좀 만들어주세요.

```python
# except 에러이름 해주면
# 해당 에러 발생할 때 그 구문으로 이동되서 실행된다.

try:
    # raise ValueError
    1/0
except ValueError:
    print('ValueError')
except ZeroDivisionError:
    print('ZeroDivisionError')


print(ZeroDivisionError)
print(type(ZeroDivisionError))
print(dir(ZeroDivisionError))
## error도 클래스다!!

```

    ZeroDivisionError
    <class 'ZeroDivisionError'>
    <class 'type'>
    ['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__', '__traceback__', 'args', 'with_traceback']

- 에러 만들기

```python
class Leehojun(Exception): #Exception을 상속받으면 됩니다.
    def __init__(self):
        super().__init__('입력된 값이 leehojun이 아닙니다.')

if 'leehojun' != input():
    raise Leehojun
else:
    print('leehojun이 맞습니다!')
```

    ㅁㄴㅇ



    ---------------------------------------------------------------------------

    Leehojun                                  Traceback (most recent call last)

    <ipython-input-39-4297290162e2> in <cell line: 5>()
          4
          5 if 'leehojun' != input():
    ----> 6     raise Leehojun
          7 else:
          8     print('leehojun이 맞습니다!')


    Leehojun: 입력된 값이 leehojun이 아닙니다.

## 클로저, 팩토리 함수

```python
def one():
    def two():
        return 10
    return two

hello = one() # hello = two
```

```python
def one(x):
    def two():
        # 여기서 x를 사용할 수 있음. 자유변수?
        return x + x
    return two

hello = one(10)
hello()
```

    20

```python
# 팩토리 함수 = 클로저
# 내부에 숨겨진 값을 가진 오브젝트를 찍어낸다고 해서 팩토리 함수라고도 부름
# 일반적으로 클로저 라고 부름

def one(x):
    def two(a, b):
        # 여기서 x를 사용할 수 있음. 자유변수?
        return a + b + x
    return two

hello = one(10) # hello == two
hello(2,3) # hello() == two()
```

    15

```python
def user(username, usermoney):
    def buy(productname, productprice):
        leftmoney = usermoney - productprice
        return f'{productname}을 {username}님이 구매하셔서 계좌에 {leftmoney} 남아있습니다.'
    return buy

buy = user('leehojun', 100000)
buy('자전거', 80000)
```

    '자전거을 leehojun님이 구매하셔서 계좌에 20000 남아있습니다.'

```python
def user(username, usermoney):
    def buy(productname, productprice):
        leftmoney = usermoney - productprice
        return f'{productname}를 {username}님이 구매하셔서 계좌에 {leftmoney}가 남아있습니다.'
    return buy

buy = user('leehojun', 1000000)
buy('자전거', 100000)
```

    '자전거를 leehojun님이 구매하셔서 계좌에 900000가 남아있습니다.'

```python
def user(username, usermoney):
    def userbuy(productname, productprice):
        leftmoney = usermoney - productprice
        return f'{productname}를 {username}님이 구매하셔서 계좌에 {leftmoney}가 남아있습니다.'
    return buy

이호준구매 = user('leehojun', 1000000)
이호준구매('자전거', 100000)

홍길동구매 = user('hongildong', 1000000)
홍길동구매('킥보드', 500000)

# 이호준 구매와 홍길동 구매로는 계좌를 조작할수 있나요?
# 계좌 변수인 username, usermoney를 조작할 수 없습니다.
```

    '킥보드를 leehojun님이 구매하셔서 계좌에 500000가 남아있습니다.'

```python
# S은행에 입사를 했습니다. 여러분들의 권한은 이호준구매 등의 구매 함수만 조작할 수 있습니다.
# 이렇게 되면 계좌 정보를 접근할 수가 없습니다.
# 접근 통제, 제한, 변수 보호 등으로 사용합니다.

```

## !! 오늘 배운 것 정리 230512 - 마지막

- 애러처리
  - Python에서는 애러를 만나면 코드가(서비스가) 멈춥니다.
  - 예제
    ```python
    try:
        # 예외가 발생할 가능성이 있는 코드
    except:
        # 예외 처리 코드
    else:
        # 예외가 발생하지 않을 때 실행되는 코드
    finally:
        # 예외 발생 여부와 상관없이 항상 실행되는 코드
    ```
- 파일입출력
  - 열기와 닫기를 동시에
  ```python
  with open('test.txt', 'w') as f:
    f.write('Life is too short, you need python')
  ```
  - 파일에 추가
  ```python
  f = open('python.txt', 'a') # 다시 write 모드로 하면 처음부터 덮어 씁니다.
  s = ''
  for i in range(5, 11):
      s += f'{i}명 참여 중입니다. \n'
  f.write(s)
  f.close()
  ```

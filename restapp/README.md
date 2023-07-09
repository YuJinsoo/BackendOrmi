
# Django REST Framework - DRF

- API 통신을 위한 서버

- 지금까지 Server Side Rendering을 함. 서버에서 template 렌더링해서 보내줌

- REST: API

- DRM
  - 설치 : python -m pip install djangorestframework
  - settings.py 안에 `INSTALLED_APPS` 에 등록

  

-  API란? 
  - 시스템 간의 인터페이스
  - 백과 프론트가 각각 커지기 때문에 서로 데이터만 주고 받는 형태로 시스템을 개발하기 위한 필수요소입니다.

1. `RESTful API`
  - Representational State Transfer의 약어로, 웹상에서 클라이언트와 서버 간의 통신을 위한 아키텍처 스타일입니다.
   - RESTful API는 HTTP를 사용하여 데이터를 요청하고 응답하는 방식으로 동작합니다. 
   - 일반적으로 JSON 또는 XML과 같은 데이터 형식으로 응답을 제공합니다.
 
2. `SOAP API`
  - Simple Object Access Protocol의 약어로, XML 기반의 메시지 교환 프로토콜입니다. 
  - SOAP API는 웹 서비스와 클라이언트 간에 데이터를 교환하는 데 사용됩니다.


- API 의 데이터 교환 형식은 JSON, XML, CSV, binary를 사용합니다.


## Serializer(시리얼라이저)
- RESTful API 서버를 만들기 위해 가장 중요한 요소입니다.

- 직렬화(Serialization)    : Data -> JSON
- 역직렬화(DeSerialization) : JSON -> Data

- Django REST Framework의 가장 중요한 기능 중 하나입니다.
- 모델 데이터나 쿼리셋 등을 JSON 또는 XML과 같은 직렬화 가능한 데이터로 변환할 수 있습니다. 
- 반대로 JSON 또는 XML과 같은 직렬화 가능한 데이터를 파싱하여 모델 인스턴스나 쿼리셋으로 변환할 수 있습니다.

>> 왜 이렇게 하나?? 서버의 부담을 줄이기 위한 RESTful 한 개발?


## DRF로 설계한 응답 확인하기 - Postman

기존 개발 방식과 다르게 Django Rest Framework으로 개발을 하게 되면 API 통신을 이용하게 됩니다. 
이에 따라 화면 구성은 하지 않고 요청에 따른 응답값을 serializer를 통해 데이터만 보내주게 되는 것이죠.
그래서 기존에 템플릿을 통해 랜더링된 화면을 확인할 수 없으니 해당 요청에 대한 응답이 제대로 작동하는 지 확인하려면 postman을 이용해야합니다.
간단한 GET 요청의 경우, url과 method만 잘 넣어주면 제대로 동작 테스트를 할 수 있지만,
 POST 요청의 경우 csrf 토큰에 대한 추가적인 처리를 해주어야 합니다.

  - 먼저 Write 클래스에 대한 POST 요청 동작을 만들어주기 위해서는
  1. 요청에서 GET을 먼저 선택해주세요.
  2.url 주소에서 http://127.0.0.1:8000/blog/write/ 를 입력해주세요. (마지막 / 를 꼭 입력해야 오류가 나지 않습니다.)
  3. Send 버튼을 눌러 GET 요청을 보내줍니다.
이미지

POST 요청만 만든 클래스에 GET 요청을 보내게 되면,
당연히 오류가 발생하면서 해당 요청에 대한 응답은 실패하게 됩니다.
그런데 이때 결과창의 Cookies 탭을 눌러보면 csrftoken이 생성된 것을 볼 수 있습니다.

이미지

이제 이 값으로
1. 요청의 Headers 탭을 선택해주세요.
2. 마지막에 key값을 X-CSRFToken로 입력, value 값을 Cookies탭의 csrftoken의 Value값을 복사해서 붙어넣어주세요.

이미지

이렇게 두 단계를 거치게 되면 해당 csrftoken으로 POST 요청을 테스트할 수 있게 됩니다.
위와 같은 설정으로 csrf token을 가지고 온 뒤, POST 요청을 테스트하시면 결과를 화면없이 확인할 수 있습니다 🙂

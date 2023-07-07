
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

# 세션과 쿠키. (아직 정리가 잘 안됨)

## HTTP 프로토콜의 특징

1. 비연결성 (connectionless)
2. 상태없음 (stateless)

- 서버가 클라이언트의 요청에 응답을 하는 순간 HTTP 연결은 끊어지며, 클라이언트에서 새로운 요청을 해야 다시 HTTP 연결이 맺어지게 됩니다
- 웹에서 애플리케이션을 구현하는데 큰 걸림돌로 작용하게 됩니다. 
- 상태가 없다라는 것은 각각 요청이 독립적으로 취급되어 여러 페이지에 걸쳐 흐름이 이어져야하는 서비스를 구현하기 어려워지기 때문입니다.

이런 특징 때문에 cookie 를 사용해서 연결(혹은 흐름)을 유지하는 것처럼 서비스를 이용할 수 있습니다.
웹페이지 접속 시 서버 >> 클라이언트에게 쿠키를 전달, 클라이언트에서 저장
다시 서버에 요청이 왔을 때 요청에 cookie를 포함시키는데 서버에서 쿠키를 보고 어디서 왔는지 확인할 수 있습니다.

## Cookie란?
- 접속한 웹사이트에 의해 작성된 파일입니다. 
- 사용자가 어떠한 웹 사이트를 방문할 때 서버에서 사용자의 컴퓨터에 저장하는 작은 기록 정보 파일입니다.
- HTTP에서 클라이언트의 상태 정보를 클라이언트의 PC에 저장하였다가 필요시 정보를 참조하거나 재사용할 수 있다.
- 사이트에서 Cookie를 확인해 유저의 로그인 상태를 유지하거나 유저의 사이트 이용설정을 기억한다거나 유저의 지역 관련정보를 제공합니다.

1. 웹서버에서 웹브라우저로 HTTP response의 헤더를 이용해서 작은 정보를 보냅니다. 
2. 이때 보내지는 정보를의 하나에 쿠키가 포함되어 있습니다. 
3. 쿠키는 서버 접속할때마다 자동전송됩니다. 
4. 물론 쿠키를 만든 웹사이트 이외에서는 다른 사이트가 만든 쿠키를 볼 수 없습니다.

### 쿠키 특징
1. 이름, 값, 만료일(저장 기간 설정), 경로 정보로 구성되어 있다.
2. 클라이언트에 총 300개의 쿠키를 저장할 수 있다.
3. 하나의 도메인 당 20개의 쿠키를 가질 수 있다.
4. 하나의 쿠키는 4KB(=4096byte)까지 저장 가능하다.

### 쿠키의 동작 순서
1. 클라이언트가 페이지를 요청한다. (사용자가 웹사이트 접근)
2. 웹 서버는 쿠키를 생성한다.
3. 생성한 쿠키에 정보를 담아 HTTP 응답을 돌려줄 때, 클라이언트에게 돌려준다.
4. 넘겨 받은 쿠키는 클라이언트가 가지고 있다가(로컬 PC에 저장) 다시 서버에 요청할 때 요청과 함께 쿠키를 전송한다.
5. 동일 사이트 재방문시 클라이언트의 PC에 해당 쿠키가 있는 경우, 요청 페이지와 함께 쿠키를 전송한다.

### 사용 예시
1. 방문했던 사이트에 다시 방문 하였을 때 아이디와 비밀번호 자동 입력
2. 팝업창을 통해 "오늘 이 창을 다시 보지 않기" 체크

---
## session

일정 시간동안 같은 사용자(브라우저)로부터 들어오는
일련의 요구를 하나의 상태로 보고, 그 상태를 일정하게 유지시키는 기술이다.
여기서 일정 시간은 방문자가 웹 브라우저를 통해 웹 서버에 접속한 시점으로부터 웹 브라우저를 종료하여 연결을 끝내는 시점을 말한다.
즉, 방문자가 웹 서버에 접속해 있는 상태를 하나의 단위로 보고 그것을 세션이라고 한다.

- 클라이언트별 정보를 브라우저가 아닌 웹서버에 저장하는 것
- django의 session은 쿠키에 sessionid만을 저장하여, 클라이언트와 웹서버간 연결성을 확보한 뒤 sessionid를 통해 커뮤니케이션 합니다.
- session의 라이프사이클은 브라우저에 의존합니다. 같은 브라우저를 사용하고 있다면 링크를 통해서 다른 사이트로 이동할때도 sessionId는 쿠키로써 쭉 유지되고, 브라우저를 닫으면 사라집니다.

### session의 원리

1. 유저가 웹사이트에 접속
2. 웹사이트의 서버가 유저에게 sessionId를 부여
3. 유저의 브라우저가 이 sessionId를 cookie에 보존
4. 통신할때마다 sessionId를 웹서버에 전송(따라서 django의 경우 request객체에 sessionId가 들어있음)
5. sessionId에 의해 웹사이트는 많은 접속 유저중 특정 유저를 인식할 수 있음

### 세션 특징
1. 웹 서버에 웹 컨테이너의 상태를 유지하기 위한 정보를 저장한다.
2. 웹 서버의 저장되는 쿠키(=세션 쿠키)
3. 브라우저를 닫거나, 서버에서 세션을 삭제했을때만 삭제가 되므로, 쿠키보다 비교적 보안이 좋다.
4. 저장 데이터에 제한이 없다.(서버 용량이 허용하는 한...)
5. 각 클라이언트 고유 Session ID를 부여한다. Session ID로 클라이언트를 구분하여 각 클라이언트 요구에 맞는 서비스 제공

### 세션의 동작 순서
1. 클라이언트가 페이지를 요청한다. (사용자가 웹사이트 접속)
2. 서버는 접근한 클라이언트의 Request-Header 필드인 Cookie를 확인하여, 클라이언트가 해당 session-id를 보냈는지 확인한다.
3. session-id가 존재하지 않는다면, 서버는 session-id를 생성해 클라이언트에게 돌려준다.
4. 서버에서 클라이언트로 돌려준 session-id를 쿠키를 사용해 서버에 저장한다. 쿠키 이름 : JSESSIONID
5. 클라이언트는 재접속 시, 이 쿠키(JSESSIONID)를 이용하여 session-id 값을 서버에 전달

### 사용 예시
화면이 이동해도 로그인이 풀리지 않고 로그아웃하기 전까지 유지

참조 : https://www.daleseo.com/http-session/


--- 

## cache?

## JWT??
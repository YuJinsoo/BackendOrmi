## 도메인

- ip는 사람이 이해하고 기억하기 어렵기 때문에 이를 위해서 각 ip에 이름을 부여할 수 있게 했는데, 이것을 도메인이라고 한다.
- 즉, 도메인은 장치를 식별하기 위한 주소

- 컴퓨터의 이름과 최상위 도메인으로 구성되어 있다. 예를들면 아래와 같다.
  - naver : 컴퓨터 이름
  - com : 최상위 도메인

- DNS라고 알려진 도메인 이름 시스템은 브라우저에 입력된 도메인 이름을 컴퓨터가 읽을 수 있는 IP로 변환합니다. 
- 해당 시스템은 ICANN에서 감독하고 있으며, 번호를 찾기 위해 이름을 찾는 매우 두꺼운 옛날 전화번호부 책과 흔히 비교되곤 합니다.

### 도메인 구성요소
1. 도메인 네임 스페이스(Domain Name Space)
  - 최상위에 루트 DNS 서버가 존재하고 , 그 하위로 인터넷에 연결된 모든 노드가 연속해서 이어진 계층구조로 구성

2. 네임서버(Name Server)
  - 주소를 변환 시키기 위해 도메인 네임 스페이스의 트리구조에 대한 정보가 필요한데, 이 정보를 가진 서버 도메인 이름을 IP주소로 변환하는 것을 네임 서비스

3. 리졸버(Resolver)
  - DNS클라이언트의 요청을 네임 서버로 전달하고 네임 서버로부터 도메인이름과 IP 주소를 받아 클라이언트에게 제공하는 기능을 수행


### 도메인 동작 순서
1. 웹 브라우저에 www.naver.com을 입력하면 먼저 PC에 저장된 Local DNS(기지국 DNS 서버)에게 "www.naver.com"이라는 hostname"에 대한 IP 주소를 요청한다.

> Local DNS(기지국 DNS 서버) 란?
> 기본적으로 인터넷을 사용하기 위해선 IP를 할당해주는 통신사(KT, SK, LG 등...)에 등록하게 된다.
> 컴퓨터의 LAN선을 통해 인터넷이 연결되면, 가입했던 각 통신사의 기지국 DNS 서버가 등록되게 된다.
> 그러니까 KT를 사용하는 집이면 KT DNS가 되고, SK통신사 사용하는 집이면 SK DNS가 자동으로 셋팅 된다.
> Local DNS 에는 "www.naver.com 의 IP 주소"가 있을 수도 없을 수도 있다. (본 설명에서는 Local DNS에 "www.naver.com 의 IP 주소"가 없다고 가정 한다.)

  - 만일 예전에 네이버에 접속했던 전적이 있다면, Local DNS에 접속정보가 캐싱이 되어있어, 바로 PC에 IP 주소를 주고 끝난다. (바로 1번 → 8번으로 넘어가 빠르게 웹페이지에 접속할수 있다)

2. 그러면 Local DNS는 이제 "www.naver.com 의 IP 주소"를 찾아내기 위해 다른 DNS 서버들과 통신(DNS 쿼리)을 시작한다.
먼저 Root DNS 서버에게 "www.naver.com 의 IP 주소"를 요청한다.

> Root DNS(루트 네임서버) 란?
> Root DNS는 인터넷의 도메인 네임 시스템의 루트 존이다.
> ICANN이 직접 관리하는 절대 존엄 서버로, TLD DNS 서버 IP들을 저장해두고 안내하는 역할을 한다.
> 전세계에 961개의 루트 DNS가 운영되고 있다.

3. Root DNS 서버 는 "www.naver.com 의 IP 주소" 를 찾을 수 없어 Local DNS 서버에게 "www.naver.com 의 IP 주소 찾을 수 없다고 다른 DNS 서버에게 물어봐" 라고 응답을 한다.

4. 이제 Local DNS 서버는 com 도메인을 관리하는 TLD DNS 서버(최상위 도메인 서버)에 다시 www.naver.com에 대한 IP 주소를 요청한다.

> TLD(Top-Level Domain, 최상위 도메인) DNS Server 란?
> TLD는 도메인 등록 기관(Registry)이 관리하는 서버로, 도메인 네미의 가장 마지막 부분을 말한다.
> 예를들어 웹사이트에서 한번쯤은 봐왔던 .com 이나 co.kr 같은 도메인들을 관리하고 부여하는 서버이다.
> Authoritative DNS 서버 주소를 저장해두고 안내하는 역할을 한다. (밑에서 배움)

5. com 도메인을 관리하는 DNS 서버에도 해당 정보가 없으면, Local DNS 서버에게 "www.naver.com 의 IP 주소 찾을 수 없음. 다른 DNS 서버에게 물어봐" 라고 응답을 한다.

6. 이제 Local DNS 서버는 naver.com DNS 서버(Authoritative DNS 서버)에게 다시 "www.naver.com 의 IP 주소" 를 요청한다.

> Authoritative DNS Server 란?

> 실제 개인 도메인과 IP 주소의 관계가 기록/저장/변경되는 서버.
> 그래서 권한의 의미인 Authoritative가 붙는다.
> 일반적으로 도메인/호스팅 업체의 ‘네임서버’를 말하지만, 개인이나 회사 DNS 서버 구축을 한 경우에도 여기에 해당하게 된다.

7. naver.com DNS 서버 에는 "www.naver.com 의 IP 주소" 가 있다.
그래서 Local DNS 서버에게 "www.naver.com에 대한 IP 주소는 222.122.195.6" 라는 응답을 한다.

8. 이를 수신한 Local DNS는 www.naver.com 의 IP 주소를 캐싱을 하고 이후 다른 요청이 있을시 응답할 수 있도록 IP 주소 정보를 단말(PC)에 전달해 준다.

> 이렇게 Local DNS 서버가 여러 DNS 서버에 차례대로 (Root DNS 서버 → TLD DNS 서버(.com) → Authoritative DNS 서버(naver.com) 요청하여 그 답을 찾는 과정을 재귀적 쿼리 Recursive Query 라고 부른다.

### 동작 요약
1. Host가 Root에 IP를 물어봄
2. com으로 끝나니까, com을 전담하는 DNS server를 알려줌
3. example.com을 전담하는 DNS server를 알려줌
4. Sub domain DNS server를 알려줌
5. 해당 Domain에 대한 IP 주소를 Host에게 보냄 
6. IP 주소 get!

### DNS 서버 종류

- Local DNS 서버
- Root DNS 서버
  - root DNS는 최상위 DNS서버로 해당 DNS부터 시작해서 아래 딸린 노드 DNS서버에게 차례차례 물어보는 트리 구조로 짜여있습니다.

  - 모든 DNS서버들은 Root DNS 주소를 가지고 있고, 모르는 Domain name이 요청되면 가장 먼저 Root DNS에 물어보는것입니다.

  - 하지만 Root DNS에 없다면, TLD(최상위 도메인) 서버에 물어본다.

- TLD(Top-Level Domain)
  - 종류에 따라 gTLD, New gTLD, ccTLD

- Second-level DNS 서버 (2차 도메인)

- Sub DNS 서버 (최하위 서버)
  - www. dev. mail. cafe. 등등 을 구분하는 최하위 서버를 말한다

### 도메인 등록

- 도메인을 호스팅 서비스에서 구매하면 도메인을 생성합니다. 호스팅 업체에서 자동으로 네임서버를 제공합니다. 하지만, AWS랑 연결하기 위해서는 네임서버를 AWS에서 도메인 영역을 생성했을 때 알려주는 것으로 다시 등록해야 합니다.

- 클라우드(AWS LightSail의 네트워크 탭)에 도메인 영역을 생성하고 등록해줍니다.

- 도메인 영역을 등록하면 사용가능한 네임서버를 확인할 수 있습니다.

- 도메인 호스팅 사이트에 가서 해당 도메인에 네임서버를 등록해줍니다.

- `네트워킹`탭에 도메인 이름을 선택하고, 레코드 추가 버튼을 눌러 연결하고자 하는 주소의 이름을 입력합니다.(고정아이피 이름) 

- 저장하면 도메인 이름을 브라우저에 도메인 이름을 치면 접속됩니다.


### 도메인 등록 이모저모

- 클라우드 하는곳에서 안해도 싼곳에서 그냥 해도됨.
- cafe24, 가비아, 포크번, 네임칩, 호스팅케이알
- 도메인주소가 완전히 세팅된 이후에 HTTPS도 적용할 수 있습니다.

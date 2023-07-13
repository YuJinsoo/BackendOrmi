# Docker

- 애플리케이션을 개발하고 전달하고 실행할 수 있는 오픈 플랫폼 입니다.
- 도커는 컴퓨터의 다른 환경으로 부터 분리되어 독립된 환경에서 내 애플리케이션을  실행할 수 있습니다.
- 컨테이너 라는 독립된 환경에서 내 애플리케이션이 실행됩니다.

- 도커기반의 가상머신을 `컨테이너` 라고 합니다.
- 개발한 애플리케이션을 컨테이너 단위로 패키징해서 어느 pc든지 docker만 깔려있으면 os레벨까지 다 실행시킬 수 있는 기술!

- 압축파일처럼 세팅한 것을 `이미지` 라고 하고 도커 레지스트리에 저장됨
- 그 이미지를 pc에 받아서 설치하게 되면 그것을 `컨테이너`라고함

## 도커와 가상머신 차이점
- 가상머신은 PC의 리소스를 설정한대로 무조건 나눠서 가져가지만 도커는 아님.
  - 8G pc에 2G짜리 가상머신 3개 설치하면 pc는 2G만 활용할수있음
  - docker는 2G라고해도 항상 2G를 사용하는게 아니기 때문에 좀더 많은 개수 설치 가능

## 왜 도커를 사용하는가?
- 도커를 이용하면 다른 사람이 만든 도커이미지를 이용해서 애플리케이션을 내 OS에 별도로 설치하지 않고 실행할 수 있습니다.
- 실행에 필요한 환경이 격리되어있기때문에 여러 애플리케이션을 실행해도 내 OS의 환경에 영향을 주지 않고 또한 영향을 받지 않습니다.
이를 통해 항상 일관된 실행을 유지할 수 있습니다.


> docker desktop은 로컬에 설치해서 하는 것이니 변수가 많습니다. 도커를 사용할 때 사용해보세요!


## 도커설치 및 기본 명령어

- curl은
```bash
# 도커 설치 스크립트 다운로드
curl -fsSL https://get.docker.com -o get-docker.sh

# 도커 설치 스크립트 실행
sudo sh get-docker.sh
```

- 실행된다면 정상적으로 설치가 된 것입니다. 버전확인
```bash
docker --version
docker compose cersion
sudo docker
```


- 도커는 도커 데몬이라는 프로그램이 있고 그 위에 실행됩니다. 하지만 도커 데몬이 서버가 켜질 때 자동으로 실행되는 프로그램이 아니므로 실행하도록 설정합니다.
```bash
sudo systemctl enable docker
```

- docker는 항상 관리자권한으로 해야되니까 항상 sudo를 쳐줘야되는데 불편하니까, docker라는 그룹에 유저를 추가해줍니다.
```bash
sudo usermod -aG docker $USER
```

- 도커 상태 확인하기
```bash
# 실행중인 컨테이너 목록
docker ps

# 모든 컨테이너 목록. 정지, 멈춘것도 보여줌.
docker ps -a

# 이미지 목록 보기
docker images
```


## 도커로 여러가지 설치해서 실행해보기

### 도커로 NginX

- nginx 설치 하고 실행합니다.
```bash
# 이상태로 인스턴스 ip주소로 접근하면 nginx뜸
sudo docker run -p 80:80 nginx
```

- 옵션 `-p` 컴퓨터포트(서버포트):컨테이너포트
  - 서버(인스턴스)의 포드 80번을 열고 nginx컨테이너의 80포트를 열어서 연결함
  - 포트번호를 직접 설정하기 싫으면 대문자 `-P`해주면 됨

- NginX는 웹서버로 우리가 터미널을 끄더라고 계속 실행되서 외부의 접속을 처리해줘야 합니다.
- 하지만 위와 같이 실행시키면 터미널을 종료했을 때 nginx도 종료되서 접속이 불가능합니다.
- 그러면 -d옵션을 주면 됩니다. 
sudo docker run -p 80:80 -d nginx


- 로그확인 
  - docker ps 로 실행중인 docker의 name과 id를 확인할 수 있습니다.
  - `-a` 옵션으로 모든 docker를 볼수잇음

```bash
docker logs 이후 name 이나 id 입력
docker logs busy_bardeen

# -f 옵션을 하면 계속 로그창을 켜놓고 실시간으로 업데이트 되는것을 확인할 수 있습니다.
docker logs -f busy_bardeen
```

- 도커 멈추는 법
```bash
docker stop id 혹은 이름
```

> tip : 로그나 종료할때 id를 입력할때 아이디 전체를 입력하지 않고 앞부분만 입력해도 중복되는 id가 없으면 해당 아이디를 찾아서 실행해줍니다.

- 도커 시작
```bash
#정지한걸 다시 시작해줍니다.
docker start id 혹은 이름
```

- 도커 삭제
```bash
docker rm id나 이름
```

### docker hub

- docker 사용하면 자연스럽게 사용하는 곳으로
- 수많은 이미지를 업로드해놓은곳. git과 github관계
- https://hub.docker.com/


## jenkins 
- 자동 빌드 툴
- ci/cd 툴입니다.
- 스크립트를 작성해두고, 이벤트가 발생하면 자동으로 실행해서 배포할수있습니다

리눅스 크론탭 (crontab?)


### 도커로 MySQL

- mysql을 설치합니다.
```bash
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=1234 -d -p 3306:3306 mysql:latest
```
- `--name` 이름지정 (지정 안하면 랜덤이름 생성되버림)
- `-e` : 환경변수옵션
- 어떤 환경변수가 있는지 확인하고싶으면, docker hub 가서 다운받으려는 컨테이너를 확인해보면 됩니다.

- MySQL Docker 컨테이너 접속
  - 컨테이너 실행중일 때, 별도의 격리된 머신이 있다고 생각하면 됨.
  - 컨테이너 내부에 들어가서 명령을 내려야 할 상태일 때 exec 명령어와 마지막에 bash 터미널을 쓸거라고 알려줌

```bash
# mysql컨테이너에 접속해서 bash로 직접 명령어 치겠따
docker exec -it mysql-container bash
```

- 위에거 입력 후 db 실행 및 로그인합니다.
```bash
# 아래 입력 후 비밀번호 입력하면 접속됨
mysql -u root -p

#나갈때는 
exit
```

## Docker Compose
- 여러개의 컨테이너를 동시에 묶어서 실행 및 관리할 수 있는 도구

**컨테이너 실행하기**
```bash
docker compose up
```

**컨테이너 데몬(백그라운드모드)로 실행하기**
```bash
docker compose up -d
```

**로그 보기**
```bash
docker compose logs -f
```

**컨테이너 정지하기**
```bash
docker compose stop
```

**컨테이너 정지 및 삭제하기**
docker compose down


### 도커로 로켓챗 - docker compose로 실행하기

- 경로만들고 결로로 들어가줍니다.
```bash
mkdir rocketchat
cd rocketchat
```

- 만들어진거 다운. compose.yml 다운됩니다.
```bash
curl -L https://raw.githubusercontent.com/RocketChat/Docker.Official.Image/master/compose.yml -O

# 내용 확인해기~
cat compost.yml
```

- 백그라운드로 실행합니다. mongodb랑 rocketchat 설치 및 실행됩니다.
```bash
docker compose up -d

# 로 확인해보면 포트도 볼 수 있음
docker ps
```

- 멈추고 종료하는법
```bash
docker compose stop

docker compose down
```


> 컨테이너들이 너무 많이 운영되기 시작되면 하나씩 관리하기 너무 고통스러워집니다.
> 그래서 kubernetis(google꺼) 같은 컨테이너 관리 시스템이 필요합니다. k8s
> docker에서 만든 docker swarm?

### 좋은자료 공유
- 쿠머네티스.. 퍼플웍스 김충섭 서비큐라(https://subicura.com/)
  - https://subicura.com/k8s/?utm_source=subicura.com&utm_medium=referral&utm_campaign=blog

- https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html?utm_source=subicura.com&utm_medium=referral&utm_campaign=k8s


- T academy 강의사이트
  - https://tacademy.skplanet.com/live/player/listOnline.action


### 도커로 Portainer - docker compose로 실행하기
- 컨테이너를 모니터링 관리 하는 gui 툴 입니다.

- 경로 만들고 compose파일다운
```bash
mkdir portainer && cd portainer
git clone https://gist.github.com/93e03542d9178e93e3bc102bdbee97bc.git .
```

- 다운로드 항목 확인하고 내용물 확인해보기
```bash
# 목록확인
ls

# 파일내용 확인해보기 포트확인도할수있음
cat docker-compose.yml
```

- 다운 및 실행
```bash
docker compose up -d
```

- 로그확인
```bash
docker compose logs -f
```

- 방화벽에 9000번 포트 추가하기
- Portainer 접속하기 : ip:9000

## trefik

- 리버스 프록시 및 로드 밸런서 프로그램 입니다.

- 리버스 프록시
 - nginx가 그런 역할을 하기도 함
 - 서버 안에 여러 도커가있음. 웹서비스면 이 서버의 80 포트로 요청이 옴.
 - 그런데 서버에 여러 도커가 있는데 다 똑같이 80포트로열려있으면 구분이 불가능합니다.
 - 그런데 그 요청을 분류해서 주소를 보고 어디로 보내야할지 정하는 것.
 - 컨테이너를 올릴 때 라벨을 달아놓으면 리버스 프록시가 보고 요청을 보내줌.
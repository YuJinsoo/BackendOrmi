# GitHub 중급

도커강의
T 아카데미
https://tacademy.skplanet.com/live/player/onlineLectureDetail.action?seq=125


## Branch

- 추가로 개발하고 싶은 단위 개발을 위해 main과 분리해서 개발 후 한 번에 합치기(merge)위한 기능
- 연관성이 없는 서로 다른 모듈들을 동시에 개발할 수 있습니다.
- git에서 기본 브랜치는 main 입니다. git 저장소를 초기화할 때 자동으로 만들어집니다.

```shell
# 한번이라도 커밋한 후에 branch가 생성 가능합니다.
$ git branch Gary 

#이렇게 입력할 경우 main에서 파생되는 브랜치를 만듭니다.
$ git branch Gary main 
```

> 해당 책에서 나오는 예시에서 main 브랜치 또는 master 브랜치는 기본 브랜치를 의미합니다. master라는 단어가 노예제를 떠올리게 한다는 이유로 많은 코드에서 master 대신 main을 채택하고 있습니다.

```shell
git config --global init.defaultBranch main 
# 명령을 통해 git에서도 GitHub처럼 기본 브랜치를 main으로 사용할 수 있습니다.
```



### Branch 이동/변경, 파일복원

- checkout
    - 브랜치 변경 또는 작업 트리 파일 복원
    - 2.23에 도입된 switch, restore 도입됨
    - 사용할 브랜치 지정

```shell
# 사용할 브랜치 지정
$ git checkout Gary

#쉘 커맨드 창 맨 끝에  (main) 대신 (Gary)
```

- 새로운 내용 추가 및 커밋하기
```shell
$ echo 'hello branch' >> branch.txt # 파일생성
$ git status # 상태확인
$ git add branch.txt # 추가
$ git commit -m "개리 5" # 커밋
```


- 모든 컴밋을 그래프로 볼 수 있습니다.

```shell
# 모든 컴밋을 그래프로 볼 수 있습니다.
git log --all --decorate --oneline --graph
#출력내용
ABO@DESKTOP-C8VM12G MINGW64 ~/Desktop/binky (binky)
$ git log --all --decorate --oneline --graph
* cf59a3d (HEAD -> binky) 빙키1
| * b2b08b9 (origin/Gary) 개리5
|/
* 2024db2 (origin/main, origin/HEAD, main) initial commit
```


- 다른 사람 repo에 branch 개발 후 push 하면 에러가 발생하는데 이유는 upstream 브랜치를 설정하지 않았기 때문입니다.
`git push --set-upstream origin branch_name`
- 어느 원격 저장소의 어느 브랜치에 push 할 것인지 전달합니다.
- `git push` 할 때에는 이미 연결된 곳에 push 할 수 있지만, 원격 저장소에 해당 브랜치가 없는 경우에는 `git push -u origin <브랜치명>`을 실행해주어야 이후에 간단히 push 할 수 있습니다. `-u` 옵션이 `--set-upstream` 입니다.
- 여기서 origin은 키워드가 아닙니다. one, two등에 이름으로 할 수 있어요. 이는 여러 원격 저장소를 연결할 수 있기 때문입니다.
- 위 내용에 이어 main이 어느 원격 저장소(GitHub인지 GitLab인지 또는 그 외인지)의 main인지 알 수 없기 때문에 설정해주는 설정입니다.


### 브랜치 병합하기

- branch로 나누어 작업했던 것을 병합하는 명령어입니다.
```shell
$ git checkout main
$ git log
$ git merge binky
$ git log
```

- merge가 완료되었으면 push 까지 해주셔야 원격 저장소에 반영이 됩니다.
```shell
$ git push origin main
```
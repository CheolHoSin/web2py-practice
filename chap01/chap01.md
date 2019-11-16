# 개발 환경

### Install on Windows

버전은 무얼 쓰면 좋으냐고? 그냥 최신 버전을 쓰자.

범인인 우리가 트랜디하다고 느낄 수 있는 경험은 많지 않다. 버전이라도 최신 버전을 쓰면서 잠시나마 트랜디한 기분을 느껴보자.

- [Bitnami WAMP](https://bitnami.com/stack/wamp/installer)
- [Python3](https://www.python.org/)
  - **Add to Path** 체크. 직접 Path 등록하고 싶으면 체크 안해도 됨!

### Setup httpd.conf

1. Open a file `{apache_path}/conf/httpd.conf`
1. Insert below code in `<DocumentRoot>~</DocumentRoot>`
    ```
    <Files "*.py">
        Options ExecCGI
        AddHandler cgi-script .py
    </Files>
    ```
1. Restart Apache Server

### Test it!

1. Write `helloworld.py` into `{apache_path}/htdocs`

    **helloworld.py**
    ```
    #!python
    a = 3 + 4 + 5
    b = a / 3
    print("content-type: text/html; charset=utf-8\n")
    print(b)
    ```

1. Restart Apache Server

1. Open a browser and go to http://localhost:81/helloworld.py

### Trouble Shooting

```
[Sat Nov 16 18:54:55.567763 2019] [cgi:error] [pid 14876:tid 1256] (OS 2)������ ������ ã�� �� �����ϴ�.  : [client ::1:5276] couldn't create child process: 720002: 01.py
[Sat Nov 16 18:54:55.567763 2019] [cgi:error] [pid 14876:tid 1256] (OS 2)������ ������ ã�� �� �����ϴ�.  : [client ::1:5276] AH01223: couldn't spawn child process: D:/Bitnami/wampstack-7.3.11-0/apache2/htdocs/01.py
```

위와 같은 에러 발생 시 다음 방법을 시도

https://opentutorials.org/course/3256/19789#comment111691

> AH01223 에러 해결
> 
> 해결방안1 : 파이썬 재설치 ->helloworld.py폴더 내용중 해당 부분 수정 #!python -> 올경로/python.exe로 변경
> 
> 해결방안2 : 환경변수 Path에 파이썬 실행파일 등록 


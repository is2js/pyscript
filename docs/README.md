## CDN

- CDN

```javascript
<script defer src="https://pyscript.net/alpha/pyscript.js"></script>
```
- 로컬 프로젝트
  - [Pyscript_default](https://github.com/is2js/PyScript_default)



## PyScript 학습

- 아나콘다에서 만들었다.
- 참고 사이트1: [다빈치코딩](https://www.youtube.com/watch?v=BEho58_GsfM&list=PLmdU-G2KSEO9HKl_GQB0wVhLS36lpXCC-)
- 참고 사이트2: [외국튜토리얼](https://www.youtube.com/watch?v=MOPCdQNeW5w&list=PLpdmBGJ6ELUJ2ujkBcMQ3n0D2J2exAVTs&index=12)
- 참고 사이트3: [PWA로 만든 로컬프로젝트 분석](https://www.youtube.com/watch?v=lC2jUeDKv-s)
- 참고 사이트4: [github -> 배포](https://www.google.co.kr/search?q=how+to+deploy+pyscript&btnK=Google+%EA%B2%80%EC%83%89&sxsrf=ALeKk00ToVg3yYh-0orlXCMBxw9MK7-_WA%3A1622212766920&source=hp&ei=ngCxYK-tNMyUr7wPjs6IwAw&iflsig=AINFCbYAAAAAYLEOrl3cnuTzqMFj585J_VV49irBFpQC&oq=sdgothicneoa+&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEIcCEBQyBAgAEAoyBAgAEB4yBAgAEB4yBAgAEB5Q5ANY5ANgyAZoAHAAeACAAYcBiAGHAZIBAzAuMZgBAKABAqABAaoBB2d3cy13aXo&sclient=gws-wiz&ved=0ahUKEwiv9N-9zezwAhVMyosBHQ4nAsgQ4dUDCAc&uact=5#btnK=Google%20%EA%B2%80%EC%83%89&kpvalbx=_69DsYvm0K5LTmAWhwJ24Bg24) 
- 공식 홈페이지: https://pyscript.net/
- 데모 페이지: https://pyscript.net/examples/
- 



## 01_포켓몬데이터그리기

- github에서 pokemon csv 검색후 raw파일 url가져와서 사용함

  - https://raw.githubusercontent.com/KarlWithK/pokemon-csv/master/pokemon.csv

- `<py-env>`태그에 사용할 모듈을 `- pandas`형식으로 먼저 import해줘야한다.

- pyscript내에서는 url주소만으로 데이터를 사용할 수 없다.

  ![image-20220731181338065](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220731181338065.png)

- pyscript에서 출력은 `pyscript.write( '출력할 div영역의 id', 데이터(df))`을 이용한다.
  
  - **df는 `.to_html(classes="적용할 css 클래스(.)")`**형태로 **html로 변경 및 css를 입힌 데이터를 넘기면  이쁜 데이터가 넘어간다**.

### 복습

1. 로컬 파일은 `py-env`에 `paths:`에 명시한다
   - indent도 중요하다.
   - 태그안에 주석이 있으면 안된다.

#### data_frame.to_html 꾸미기

```python
data_frame.to_html(classes='df-style')
```



```css
<style>
    .df-style th, td{
        padding: 5px;
        border:1px solid silver;
    }
    .df-style tr:nth-child(even) {
        background: #e0e0e0;
    }
    .df-style tr:hover {
        background: #e2a3a3;
        cursor:pointer;
    }
</style>
```



1. **dataframe은 .to_html()로 string으로 만든 뒤, `pyscript.write('id', string변수)`로 출력한다**

   - 기본 출력하면 표가 없다.

   ```html
   <div id="df-output"></div>
   <py-script>
       import pandas as pd
   
       data_frame = pd.read_csv('pokemon.csv')
       pyscript.write('df-output', data_frame.to_html())
   </py-script>
   ```

   ![image-20220805161251087](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220805161251087.png)

2. **df.to_html에는 `classes=`를 줄 수 있다.**

   - **classes**에 css클래스를 만들고 나면  -> **바로 style태그를 만들어서 `.클래스 상세태그 {}`**를 만들어 정의해줘야한다.

     ![19c2eff8-0ea6-4292-984a-09307bf777d0](https://raw.githubusercontent.com/is3js/screenshots/main/19c2eff8-0ea6-4292-984a-09307bf777d0.gif)

     ![image-20220805161947479](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220805161947479.png)

     ![image-20220805161959567](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220805161959567.png)

     ![image-20220805162021129](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220805162021129.png)
     - **`td`는 table data의 모든 셀을 의미한다.**
     - **`tr`은 th + td들을 담고 있는 table row를 의미한다.**
       - **`th`는 `tr 속 table header 데이터 1개` **
       - **`td`는 `tr 속 table row 데이터 1개` **
     - **`표의 모든 셀을 터치`하려면 `th, td`를 2개를 다 선택하자.**

   - **보통 `tr`은 `:nth-child(even)`을 이용해 짝수만 background를 표시한다.**

     ![5894d2a5-a039-42c2-95a5-9b0370636d14](https://raw.githubusercontent.com/is3js/screenshots/main/5894d2a5-a039-42c2-95a5-9b0370636d14.gif)

     ![image-20220805162526478](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220805162526478.png)

     ![image-20220805162513023](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220805162513023.png)

   - **th, td의 셀이 아니라 `모든 요소를 선택`하려면 `tr`로 주면 된다. hover를 줄 땐 `tr:hover`를 바꿔주면 된다.**

     ![image-20220805162918590](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220805162918590.png)

     ![image-20220805162930086](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220805162930086.png)







#### 그래프를 띄우려면 plt에 그려놓고, pyscripte.write에 plt객체를 넣으면 된다.

![image-20220805163713920](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220805163713920.png)
![image-20220805163721502](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220805163721502.png)



#### plt 크기조절은 plt.gcf()를 통해 fig객체로 빼서 조절한다.

![image-20220805163942433](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220805163942433.png)

![image-20220805164010952](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220805164010952.png)





#### df.plot으로 그려도 plt객체에 입력되므로, 출력할 수 있다.

![image-20220805171959041](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220805171959041.png)

![image-20220805172336634](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220805172336634.png)



## 02_프로젝트 분석

- [참고영상](https://www.youtube.com/watch?v=lC2jUeDKv-s)

### 세팅

- 파이참으로 열기전에 **클론하고, 폴더에 진입**한 뒤

  - 가상환경 설치 및 진입후, 라이브러리 설치
  - **pycharm이 자동으로 생성해주는 것과 동일한 `venv`폴더를 이용해서 만든다.**

  ```python
  python -m venv venv
  
  .\venv\Scripts\activate
  
  pip install -r .\requirements.txt 
  ```

  

- **Pycharm flask프로젝트 `Run/Debug Configuration`설정해주기**

  - 명령어  `flask run`대신 **파이참으로 실행해준다.**
    1. terminal에서 생성한 가상환경을 pycharm이 인터프리터로 인식하도록 `settings > Project > Python interpreter` > `톱니 > add`해서 인식시켜준다.

       ![image-20220804181210182](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220804181210182.png)

    2. run부분에 Edit configuration에서 기본 설정을 삭제하고 `+ > flask`를 검색한다.

       ![image-20220804181310984](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220804181310984.png)

    3. **` target Type`: moduleName -> `target `: app (실행될 flask앱인 app.py)를 걸어준다.**

       - **`FLASK_DEBUG`를 true로서 체크해준다**

       ![image-20220804181427158](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220804181427158.png)

       - 설저된 후 run시키면
         ![image-20220804181605383](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220804181605383.png)

### 분석



1. **static폴더** 아래

   1. 일반적인 `css, js, images`이외에 `pyodide, pyscript, python`폴더가 따로 있다.

   2. `pyscript`폴더에 `css, js, py`가 따로 있다.

   3. `python`폴더에는 js대신 사용되는 함수로 구성된 `py`가 있다.

      ![image-20220804181918136](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220804181918136.png)

2. **template폴더** 아래

   1. 일반적인 index.html이 있다.

   2. **html 내부 header에는**

      1. `py-config`태그와 `py-env`태그를 걸어주었다.

         1. py-config에는 runtime관련 설정이 있다.
         2. py-env에는 정의한 python모듈들의 path가 걸려있다.

         ![image-20220804182215899](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220804182215899.png)

   3. **html body에서는**

      - 실행할 모듈을 body맨 마지막에 `py-script`태그로 걸어준다.

      ![image-20220804184155273](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220804184155273.png)

      - 실행되는 모듈은 맨마지막에 함수를 실행시킨다.

        ![image-20220804184834494](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220804184834494.png)

      - 나머지 모듈은 **실행모듈 client.py에서 import되어 사용**된다.

        ![image-20220804184933851](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220804184933851.png)





## 02_구구단



1. py-OnClick같은 **파이스크립트 전용함수**를 쓴다면
   1. py-script src에서 소스불러오기
   2. py-OnClick같은 메서드에서 사용하되 **메서드에는 e매개변수로 필수인자임**
   3. 출력하려면 Element('id')를 사용해서 write해줘야함.
2. **py-scrip내부에서 사용**하려면
   1. py-env에 메모리에 올리기
   2. py-script내부에서 from 올린모듈 import 메서드 형식으로 사용하기

### 복습



#### 바로 실행없는,pys-onClick의 event를 받는 전용함수 사용

1. e를 파라미터로 받는 함수를 py모듈에 정의한다

   ![image-20220810010901544](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220810010901544.png)

2. py-script의 src로 불러읽고 -> 그 밑으로 py-onClick등 파이스크립트전용함수에서 e파라미터를 받는 메서드를 연결한다.
   
   - 원래는 head 맨 아래에 걸어줘야하는 듯??
     ![image-20220810011026457](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220810011026457.png)

#### py-script태그 내부 import해서 사용

1. e파라미터 없이 python기본사용의 메서드로 정의한다. python파일은..
   ![image-20220810011053926](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220810011053926.png)

2. py-env에서 `로컬모듈`을 메모리에 올려준다.
   ![image-20220810011115400](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220810011115400.png)
3. py-script에서 from 모듈 import 메서드로 python처럼 사용한다.
   ![image-20220810011145569](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220810011145569.png)

## 03 구구단 pys-onClick + CSS





- 사적css추가 및 이미지 추가
- css는 link로 / 이미지는 main-box안에  `div.logo-circle`로 추가해준다



- css

  - body

    - `box-sizing: border-box;` : 박스의 기준을 테두리로 잡아서, 잡기힘든 컨텐츠기준을 초기화

    - margin, padding 0시작

    - 가로축(just) / 세로축(align) 가운데기준으로 시작 / 높이는 100vh=100%

      ```css
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      ```

      ![image-20220809104328142](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809104328142.png)

  - main-box

    ```css
    .main-box{
        box-shadow: 2px 4px 2px 4px bisque;
        border-radius:10px;
    
        width: 300px;
        height: 600px;
    
        text-align: center;
        padding: 20px 0;
    }
    ```

    

    - 그림자효과 x2px ypx 흐림2px 늘림4px

      ![image-20220809105154747](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809105154747.png)
      ![image-20220809105208585](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809105208585.png)

    - 둥근테두리 10px

      ![image-20220809105340798](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809105340798.png)

    - 너비300px, 높이600px

      ![image-20220809105431338](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809105431338.png)

    - 가운데정렬 및 패딩(위아래20px 좌우0px)

      - **가운데정렬할거면, 좌우패딩/마진 주지말고 위아래만 주자**

      ![image-20220809105551509](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809105551509.png)

  - heading-name

    ```css
    .heading-name{
        margin: 3px 0;
        font-size: 30px;
    
        background: linear-gradient(to right top, bisque, #b4977d);
        color:transparent;
        -webkit-background-clip: text;
    }
    ```

    - 위아래요소와의 마진 위아래3px 좌우0

    - 글자크기30

    - 백그라운드를 그라디언트로

      ![image-20220809110053925](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809110053925.png)

    - **글자색을 투명하게**

      ![image-20220809110242376](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809110242376.png)

    - **배경색을 text로 입히기(-webkit-background-clip: text)**

      ![image-20220809110350745](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809110350745.png)

  - logo-circle

    - 너비높이를 150px로 똑같게 주고, border(10px solid 색)을 그린다.
      ![image-20220809112933600](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809112933600.png)

    - border-radius를 50%로 주면 둥글게 된다.

      ![image-20220809113029232](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809113029232.png)

    - margin을 auto로 주면, 해당요소가 가운데로 간다

      ![image-20220809113304499](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809113304499.png)

    - position을 relative로 줘서 부모요소 main-box기준으로 위치시키게 한다

      ![image-20220809113504038](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809113504038.png)

    - 이미지의 삽입은 background-image: url("")로 준다.

      ![image-20220809113701545](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809113701545.png)

      - 기본적으로 왼쪽정렬? 되어있기 때문에 background-position:center; + -size: cover;로 바꿔줘야 딱맞게 가운데로 들어간다

        ![image-20220809113748923](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809113748923.png)

  - input

    ```css
    input {
        border: 3px solid bisque;
    
        width: 55%;
        height: 30px;
    
        padding: 5px 5px;
    
        font-size: 15px;
    }
    ```

    

    - 크기요소를 알려면 border부터 1px + solid +색 로 주고 시작하는게 좋다

      ![image-20220809115119841](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809115119841.png)

    - 가로가 부모에 의해 제한이 있다면 width를 %로 줄 수 있다.

      ![image-20220809115149761](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809115149761.png)

    - input은 placeholder를 보면서 padding을 줘서 안쪽요소를 확인할 수 있다.

      ![image-20220809115255955](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809115255955.png)

  - input::placeholder

    ```css
    input::placeholder {
        color: #8d7962;
        font-style: italic;
    }
    ```

    - input완성후에 `::placeholder`를 주어서 수정할 수 있다.

      ![image-20220809115509994](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809115509994.png)
      ![image-20220809115515972](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809115515972.png)

    

  - #btn `공통태그들은 id로 해주는 게 좋다?`

    ```css
    #btn{
        text-decoration: none;
        background: bisque;
        color: #5e5448;
    
        padding: 5px 8px;
    
        border-radius: 20px;
    
        box-shadow: 2px 2px 1px 1px #9a8974;
    }
    ```

    - 버튼같은 것은 기본스타일링을 제거하고 시작한다

    - background를 줄 것이면 굳이 border를 안그리고 시작해도 된다.

      ![image-20220809120925561](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809120925561.png)

    - **버튼은 글자는 고정상태에서 `padding을 통해 크기 조절`을 한다.**

      ![image-20220809120958493](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809120958493.png)

    - radius와 shadow를 준다.

      ![image-20220809121020615](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809121020615.png)

  - `#btn:hover`

    ```css
    #btn:hover{
        background: #5d5b57;
        color: #fff;
        font-weight: 600;
    }
    ```

    - 배경+글자색을 주고 + **font-weight로 진하게**표시하면 이쁘다

      ![image-20220809121657821](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809121657821.png)

  - #gugu_print

    ```css
    #gugu_print {
        width: 250px;
        border: 1px solid #ccc;
    
        /*margin: 10px;*/
        margin: 10px auto;
    
        border-radius: 10px 10px 0 0;
    
        padding: 0;
    
        text-align: center;
    }
    ```

    

    - 먼저 동적으로 채워질 list를 채워놓는다.

    - **동적으로 채워지는 곳은 높이를 모르니 width만 주고, border를 그린다.**

      ![image-20220809150542744](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809150542744.png)

    - **div를 가운데 정렬하기 위해 margin을 auto로 주지만, 맨 위에 위치한 것이 아니므로 `위아래는 10px로 직접 띄워주고, 좌우만 auto로줘서 가운데 정렬`한다**

      ![image-20220809150919587](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809150919587.png)

    - border-radius를 4개로 가르면, topleft부터 시계방향이므로 앞 2개만 주면, 위쪽만 radius가 적용된다.![image-20220809151003544](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809151003544.png)

    - 내부요소들은 list들로 꽉채울 것이기 때문에 padding을 0으로 준다

      ![image-20220809151039568](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809151039568.png)

    - 들어올 텍스트들을 가운데 정렬해준다.

      ![image-20220809151806756](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809151806756.png)

  - `li`

    - 각 li들은 div와 다르게 border를 먼저 그리는게 아니라 **background를 채워서 모양을 본다.**

      ![image-20220809152254605](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809152254605.png)

    - **border-top만 그려서** 나눠진 칸을 확인한다.

      ![image-20220809152322096](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809152322096.png)

    - 글자크기 /색/ 패딩을 준다

      ![image-20220809152351501](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809152351501.png)

  - `li:first-child`: list의 **첫번째요소만 제목으로서 처리**

    ```css
    li:first-child {
        background: #8d7962;
        color: white;
    
        border-radius: 10px 10px 0 0;
    
        border: none;
    }
    ```

    

    - li는 배경을 줘서 확인한다고 했다.

      ![image-20220809152521972](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809152521972.png)

    - 출력div의 위쪽border를 준상태니 똑같이 border-radius를 위쪽만 준다

      ![image-20220809152701354](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809152701354.png)

    - **첫줄의 border는 지워서, div의 border와 안겹치게 한다**

      ![image-20220809152741450](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809152741450.png)

  - `li:hover`

    ```css
    li:hover {
        background: #8d7962;
        color: white;
    }
    ```

    

    - tr, btn처럼 li 자식요소도 hover를 배경색으로 줄 수 있다.

    ![image-20220809153120411](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220809153120411.png)





### 사이트

https://www.youtube.com/channel/UCVnN37gEkdZ62mouxpN_3Mw/videos



### 복습

#### body css부터

- css는 link태그 + href="`/`루트시작이 아닌 `./`현재경로에서 찾아서 만들어주자.	

- body는 **폰트 + 마0패0 + 박스사이징: border-box;**부터 설정한다

  - **flex-box**로 만들고 **가운데 정렬하고, 높이를 100%(100vh)**로 준다.

  ```css
  @import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap");
  
  body {
      font-family: "Noto Sans KR", sans-serif;
      margin: 0;
      padding: 0;
      box-sizing: border-box;
  
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
  }
  ```



#### .main-box(전체 중앙 박스): 가로세로+(선or배경or)그림자(x,y,흐림,늘림)+곡선 -> text-align + padding

```css
.main-box {
    width: 300px;
    height: 600px;
    box-shadow: 2px 2px 5px 10px bisque;
    border-radius: 10px;

    text-align: center;
    padding: 20px;
}
```

#### h2.heading-name{제목}: 글자크기+배경-> 마진(상하 0) -> 배경제거후 꾸미기

```css
.heading-name {
    font-size: 30px;
    font-weight: bold;
    /*background: bisque;*/
    margin: 3px 0;

    background: linear-gradient(to right top, bisque, #a99a87);
    color:transparent;
    -webkit-background-clip: text;
}
```



#### 조작id가 들어가는 input#input-dan[placeholder=""] (인풋) + button#input-btn[pys-onClick="e메서드명"]{Click}

##### 인풋: 선 -> 가로세로 -> 글자크기 + 패딩 -> ::placeholder (글자)컬러+style

```css
#input-dan {
    border: 2px solid bisque;
    border-radius: 4px;

    width: 55%;
    height: 30px;

    padding: 5px 5px;
    font-size: 15px;
}

#input-dan::placeholder{
    color: #a99a87;
    font-style: italic;
}
```



##### 버튼: text-decoration:none; + 배경/그림자 + 곡선 -> padding(상하,좌우)으로 버튼크기조정 -> 글자색+크기 -> ::hover 배경 + 글자색 + 굵기

```css
#input_btn {
    text-decoration: none;
    background: burlywood;
    border-radius: 15px;
    box-shadow: 2px 2px 1px 1px bisque;

    color: white;
    padding: 5px 8px;

    font-size: 15px;
}

#input_btn:hover {
    background: gray;
    color: white;
    font-weight: bold;
}
```



#### 조작id가 들어가는 출력공간 #result-print -> 가로세로+선 -> margin 상하+auto(가운데정렬) -> 곡선 -> padding 0 for 꽉채운요소 + 글자가운데정렬

```css
#result_print {
    width: 250px;
    border: 1px solid #ccc;

    margin: 10px auto;

    padding: 0;

    text-align: center;

    border-radius: 10px;
}
```



#### [js를 대신하는 e메서드] 사용법

1. **body안에 가장 먼저**  `<py-script>`로 **pys-onClick에 쓸 메서드들을 모아둔 모듈을 메모리에** 올린다.

   ```html
   <body>
   	<py-script src="./gugudan_module.py"></py-script>
       <!-- html 태그 -->
   </body>
   
   ```

   

   ![image-20220819001723766](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220819001723766.png)



2. html근처 해당경로에 py모듈을 만든다.

   ![image-20220819001839290](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220819001839290.png)



3. 모듈내에서는 `event 파라미터 e`를 받는 모듈을 만든다.

   - **모듈 내에서는, html요소들을 Element()로 잡아서 사용할 수 있다.**
     - 빨간줄 뜨지만, 이미 html에는 읽어져있다.

   ![image-20220819002003971](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220819002003971.png)

   

4. **html태그내 `pys-onClick`속성으로 `모듈 속 e메서드`를 걸어준다.**

   ![image-20220819001937708](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220819001937708.png)





#### e메소드 속 문자열에 list태그를 넣기

1. 누적변수는 `= <ul>`로 초기화하고,  누적후 마지막에  `+= </ul>`닫는 태그를 누적해준다.

   ![image-20220819004200555](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220819004200555.png)

2. **ul의 첫list를 제목으로 쓸 거면 `<li> </li>`를 넣어서 초기화 해준다.**

   ![image-20220819004309227](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220819004309227.png)

3. **반복문 속 누적li들은 결과마다 `<br>`을 떼고 `<li> </li>`를 달아준다.**

   ![image-20220819004404549](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220819004404549.png)





#### 결과출력li태그 : line-style:none; + 배경 + 선border-top -> 글자크기 + 색 -> padding(상하 좌우)

```css
#result-print li {
    line-style: none;
    background: bisque;
    border-top: 1px solid #ffffff;

    color: #5e5448;
    font-size: 15px;

    padding: 1px 20px;
}
```

##### 첫li:first-child:제목으로서 다르게 처리: 배경 + 색 -> 바깥div와 같은 top곡선 + 바깥div를 위해 내 top선 가림 border:none

```css
#result-print li:first-child {
    background: #5d5b57;
    color: #ffffff;

    border-radius: 10px 10px 0 0;
    border:none;
}
```



##### li:hover   :  배경 + 색

```css
#result-print li:hover {
    background: #5d5b57;
    color: #ffffff;
}
```

##### 마지막li:last-child: 제목은 아니라서, bottom곡선만 똑같이 주기

```css
#result-print li:last-child {
    border-radius: 0 0 10px 10px;
}
```



#### div.logo-circle(배경으로 그림채운다): 가로세로+선+곡선50%-> margin:auto + 포지션relative -> background-image:url("")/position:center/size:cover

```css
.logo-circle {
    width: 150px;
    height: 150px;
    border: 5px solid bisque;
    border-radius: 50%;

    margin: auto;
    position: relative;

    background-image: url("./logo.png");
    background-position: center;
    background-size: cover;
}
```

### 엔터로 click누르기

1. calculator 모듈을 만든 곳에서, input 태그를 잡은 변수에다가 **.element.onkeypress = gugudan**을 같이 연결해준다.

   - input에 onclick뿐만 아니라 onkeypress도 연결되었다는 말

2. onkeypress는 **enter이외에 아무키나 눌러도 작동하게 되므로 에러를 포**함하고 있다.

   ![image-20220825130259125](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220825130259125.png)

   1.  enter만 인식하게 하려면 if enter의 keycode일때만 작동하도록 해야한다.
   2. **감싸주는 함수를 하나더 만들어서, if enter키일때만... gugudan함수를 실행하도록 포장한다**

3. **먼저 key_press함수를 작성하고, onkeypress에서 걸어주되, `e.keyCode`를 통해 `눌러지는 키의 code값을 확인`한다**

   ![image-20220825130357369](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220825130357369.png)

   - enter를입력하면 e.keyCode는  13이라는 아스키코드를 출력한다

     ![image-20220825130452334](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220825130452334.png)\

   - **key_press온 e.keyCode값이 13일때만 gugudan함수를 실행해주도록 하면된다.**

     - **on함수에서 on함수를 실행시킬 땐, 해당e코드를 인자로 그대로 넘겨주면 된다.**

     ![image-20220825130629583](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220825130629583.png)



#### 숫자 검증 by try~except with placerholder

![image-20220825132442418](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220825132442418.png)

1. 에러가 발생할 곳에 try로 감싼다
2. **placeholder로 에러문을 출력하기 위해서는**
   1. **input창을 빈칸으로 만들고**
   2. placholder 메세지를 수정하고
   3. **포커스를 input창으로 준다**
   4. **return통해, 아래과정은 안일어나게 만든다.**



## 05 이미지 합성

1. `h1`의 제목 텍스트를 pyscript.css 속성을 이용해서 설정할 수 있다.

   `h1.text-white.fold-bold.text-center.text-3xlg{이미지 합성 하기}`

2. id를 준 .card안에

   1. `.title{}`

   2. id를 준 div.my_image 2개의 공간을 생성한다.

      ```
      div#card1.card>div.title{첫번재 이미지}+div#my_image1.my_image
      ```

    3. 추가로 설명을 적을 `.features`와

    4. `input.btn` + type="file", id="file_upload1"로 구성하게 한다.

       ```
       div.features{이미지 파일을 올려주세요}
       input.btn[type="file"][id="file_upload1"]
       ```

3. id준 card를 3개로 복사해서 id값들을 바꿔준다.

4. 3번째 결과 카드는, 기존 input file을 지우고

   1. input#my_range아이디로 `type="range"` 민 ="0" 맥스="100"으로 준다.value="50"으로 가운데 위치시킨다.

   ```
   input#my_range[type="range",min="0",max="100",value="50"]
   ```

   2. 리스너를 달고 있는 btn을 추가한다.

   ```
   btn#btn1[pys-onClick="image_blend"]{Click Me!}
   ```

```html
<h1 class="text-white fold-bold text-center text-3xlg">이미지 합성 하기</h1>
<div id="card1" class="card">
    <div class="title">첫번쨰 이미지</div>
    <div id="my_image1" class="my_image"></div>
    <div class="features">이미지 파일을 올려주세요</div>
    <input type="file" class="btn" id="file_upload1">
</div>
<div id="card2" class="card">
    <div class="title">두번째 이미지</div>
    <div id="my_image2" class="my_image"></div>
    <div class="features">이미지 파일을 올려주세요</div>
    <input type="file" class="btn" id="file_upload2">
</div>
<div id="card3" class="card">
    <div class="title">결과 이미지</div>
    <div id="my_image3" class="my_image"></div>
    <div class="features">합성 결과를 보여줍니다</div>
    <input type="range" id="my_range" min="0" max="100" value="50">
    <button id="btn1" pys-onClick="image_blend">Click Me!</button>
</div>
```



### css꾸미기

- image_blend.css를 만들고 링크를 건다

1. body에 배경을 주고
2. .card에 배경 +box-shadow + 곡선 + 마진을 준다..

```css
body {
    background-color: #383838;
}

.card {
    background-color: #2b2a2a;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.4);
    border-radius: 5px;

    margin: 50px 20px 20px 20px;

    /*한줄로 만들기 전에 각각을 33% - @ 로 만들어놓기*/
    width: calc(33.3333% - 40px);
    padding: 20px;

    text-align: center;
    color: white;
    /*block요소들을 왼쪽정렬하며 한줄로 만들기*/
    float: left;
}

.title {
    font-size: 25px;
}

.my_image {
    margin: 50px 0;
}

/*이미지 들어갈 곳의 확장자로.. px을?*/
.my_image svg {
    width: 100px;
    height: 100px;
}

.features {
    margin: 10px 0;
    font-size: 14px;
}

/*input에 붙여준 btn속성*/
.btn {
    display: block;
}
/* 결과 버튼 */
button {
    align-items: center;
    background-color: cyan;
    border-radius: 20px;

    color: white;
    padding: 5px 10px;
    box-shadow: 2px 2px 1px 1px rgba(70, 244, 151, 0.65);
}

button:hover {
    color: purple;
    background-color: white;
    font-weight: 600;
}
```



### pyscript 작성

1. pillow를 갖다 쓰기 위해, head에  **import해서 쓸 모듈인**`py-env에  - Pillow`를 걸어준다

   - pyscript에 포함된 기본라이브러리는 `paths:`없이 걸어주면 된다.
   - 로컬모듈은 `paths: `아래 인덴트 걸어서 적어줘야한다.

   ```html
   <py-env>
       - Pillow
   </py-env>
   ```

2. 마찬가지로 head에 `py-script`로 **pys-onClick 등 이벤트메서드들로 쓸 모듈들은 `py-script에 src로 `걸어준다**

   - 먼저 경로에 모듈을 만들고, 아래와 같이 head에 걸어준다.

     ![image-20220822191851119](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220822191851119.png)

   ```html
   <py-script src="./image_blend.py"></py-script>
   ```





#### file타입 input을 눌렀을 때, 업로드 후 보여주는 부분 작성

1. pys-onChange가 없는 것 같다
2. python모듈을 onChange를 addEventListener("change", )로 걸어야하는데
3. js element에 html속 **pys-가 아니라 파이썬메서드를 html태그 생성후 + js이벤트리스너에 직접 걸 때는 `from pyodide import create_proxy`를 한번 씌워서 js 이벤트 리스너의 함수자리에** 걸어줘야한다.
4. **그렇다면, 모듈내에서 `(1)python모듈정의 -> (2) creat_proxy import -> (3) 모듈내 전역변수로 씌우기 -> (4) 모듈내 전역으로 html태그찾기 -> (4) 태그에 이벤트리스너걸기`의 과정을 모두 python모듈내에서 이루어져야한다.**
    - 검색해보니, pys-on이 존재하더라도 setAttribute로 동적으로 생성태그에 추가가안되는 것 같다. create_proxy에 씌워서 이벤트리스너로 add해줘야한다.



#### 2번째 file input(#file_upload2)에도 똑같은 리스너를 달려면?

1. 현재 이벤트리스너에 들어갈 메서드는 `이미지가 들어갈 공간의 id`를 찾아서 넣으므로, 2번째 file input에 적용안되는 상황이다.

    - img가 들어갈 공간의 #id를 파라미터로 빼고, 리스너 달때 e제외 새로운 인자로 id를 주면 될 것 같은데
    - **이벤트리스너로 넘어가는 메서드는 e이외에 파라미터를 가질 수 없다?!**

2. **이럴 때 이용하는 것이, `id로 찾지말고, 같은종류면 달고 있는 class로 찾기`이다.**

    1. #card1 .card
        1. #my_imadge1 .**my_lmage**
        2. input #file_upload1

    2. #card2 .card
        1. #my_imadge1 .**my_lmage**
        2. input #file_upload2

3. `e.target` (각각의 file input#fild_upload1,2,3..) -> `.parentNode` -> `.getElementsByClassName("공통 클래스") [0]` -> `.id`

    - **각각의 card에는 1개의 요소만 존재하지만, `ClassName으로 요소를 찾으면 복수라서 [0]`를 달아준다**

        - 기존
            ![image-20220824132815272](https://raw.githubusercontent.com/is2js/screenshots/main/image-20220824132815272.png)

        - id로 1개 요소가 아닌, 부모로 갔다가 공통class로 찾아서, 각각의 해당하는 요소를 찾게 만들기

            ![image-20220824133045997](https://raw.githubusercontent.com/is2js/screenshots/main/image-20220824133045997.png)

4. **추가로 다시 클릭했을 때, `추가할 빈공간의 자식들을 지우고, 거기에 추가`하도록 id가 아닌 태그로 받은 뒤, `첫번째 자식이 존재할때까지 계속 삭제`해서 자식이 존재안할때까지 삭제한다**

    ![image-20220824134039143](https://raw.githubusercontent.com/is2js/screenshots/main/image-20220824134039143.png)







#### 전역변수 dict에 2개이 그림 파일을 값으로 저장해놓고, 합성클릭시 blend하기

1. 필로우의 Image.open()으로 js파일객체를 그대로 쓰면 에러가난다
    1. `from PIL import Image` 모듈의 open을 써도 에러가난다
    2. **js파일객체 -> byte list로 바꾼 뒤 -**> python의 PIL에서 사용할 수 있다.

2. **js의 Uint8Array.new()를 이용해서, `인메모리 byte 스트림으로 변경`한 뒤, Image.open()에 넣어줘야한다.**

    1. html file객체를 **.arrayBuffer**()로 어레이퍼버를 만들고, 
    2. 버퍼를 **js용 Unit8Array**에 담아서, **js용 어레이버퍼**를 만든다.
    3. python의 내장 **bytearray**()를 통해 b''의 **바이트 배열**로 만든다.
    4. io의 **io.BytesIO()**를 이용해서, f = open()과 같은 역할로서 바이트배열 -> **인메모리 바이트 스트림**으로 만든다.
    5. 인메모리 바이트 스트림을 **PIL의 Image.open()으로 연다**

3. **비동기식으로 처리해야한다는 에러가 난다.**

    - .arrayBuffer()를 만들 때 `await` -> 메서드에는 `async`를 앞에 붙여줘야한다.

    ![image-20220824145405149](https://raw.githubusercontent.com/is2js/screenshots/main/image-20220824145405149.png)

4. **각 file input마다 `PIL이 Image.open()`으로 열어둔 이미지 정보를 `id를 key로하는 전역변수 map`에 저장해놓고, 나중에 합성할 때 꺼내 쓸 수 있게 한다.**

    ![image-20220824150738812](https://raw.githubusercontent.com/is2js/screenshots/main/image-20220824150738812.png)







#### dict에 저장된 이미지를 꺼내서 합성하기

1. 일단 합성 전에 이미지 크기를 통일 시킨다.

    1. 첫번째 사이즈대로 resize하기

2. slider값을 가져와서 / 100 후 0~1 ㄱ비율대로 합성하기

3. **jpg는 혼자 저장mode가 PIL RGBA -> png는 다 RGB mode**

    1. 각 이미지 dict에 저장 전에, .mode가 RGB(png)가 아니면 convert해주는 코드 추가

4. **.blend의 결과인 `PIL객체` -> `byte stream`-> ... -> 다시  `js용 File객체`로 변경해야한다.**

    1. byte steram을 담을 빈 io.ByteIO()를 만들고
    2. PIL객체.save() + foramt지정해서 byte steram으로 만들고
        1. **인메모리 파일이 io.BytesIO로 만든.. byte stream인가보다?!**
        2. 파일명을 저장하는 곳에 인메모리 빈 stream이 이용된다.
    3. byte steram에서 geValue()한 것을 Unit8Array로 만들고
    4. Unit8Array를 파일명 + 타입등으로  File객체로 만들어주면된다

5. 만들어진 js File객체를, 기존에img태그 만들어서 올리는 것처럼 복사해서 img태그를 append해준다.

    


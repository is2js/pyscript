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

    

## 06 틱택톡

- 2player까지 만들고 난 뒤 -> minmax알고리즘으로 1player vs computer가 가능하다
- 오목의 축소판이다.



### 3개의 파일부터 만들고, html에 걸어주기

- `tictactoe`html, css, py

  ![image-20220829114222236](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220829114222236.png)



### html 및 css, py 파일 만들기 세팅

1. 제일 바깥 공간 만들기

   - **pyscript의 css이용**

   `div.m-auto.text-center.font-bold.text-3xl`

2.  h1#header과 테이블#my_table 만들기

   `h1#header{Pyscript TicTacToe!}`

   1. **테이블을 html로 만드는게 좋으나, 학습을 위해 pyscript로 동적 생성할 예정 -> `table#my_table`로 제일 바깥 테이블태그만 만들어놓는다.**

   `table#my_table`

   

### pyscript 모듈에 e메서드이외에 init_function()로 동적 table + td마다 클릭리스너 달기

1. pyscript모듈에서는, **e함수이외에 `init_함수() 실행과 동시에 정의`해서, 홈페이지 시작시 작동할 모듈들도 정의할 수 있다.**
2. 최상단에 table태그를 잡아놓고 **init함수를 호출하면서 동시에 정의한다**
   1. row만큼 반복문을 돌면서 tr태그를 생성하고
   2. 내부에서 col만큼 반복문을 돌면서 td태그를 생성하되
      1. `td.id = `로 아이디를 부여하여, 클릭될 수 있게 한다.
         - `row * 열 수(구간별갯수) + col`을 이용하면 0부터 시작하는 값을 연속적으로 행렬을 채울 수 있다.
      2. 보이기용으로 O와 X를 집어넣고
      3. **생성된 각 td태그마다 addEventListener로 `click_cell` e함수를 달아준다.**
         - python모듈을 js문법에 이벤트리스너로 넣어줄 땐 **create_proxy()를 씌워서 넣어준다**
      4. td태그를 tr에 , tr태그는 table태그에 appendChild한다.

```python
from js import document
from pyodide import create_proxy

# 8. tr들을 달 table은 모듈내 전역변수로서 먼저 실행되게해서 잡아준다.
my_table = document.getElementById('my_table')


def click_cell(e):
    pass


def init_game():
    # 2. 3by3을 만들 기 위해 tr3개를 createElement한다.
    for i in range(3):
        tr = document.createElement('tr')
        # 3. 각 tr에다가 3개의 열을 td로 만들어준다.
        # -> 각각을 컨트롤하기 위해 td도 심어놔야한다. .id 로 id속성을 부여한다.
        for j in range(3):
            td = document.createElement('td')
            # 4. 이중반복문 내부에서는 row_index * 열수 + col_index로 0부터 연속적인 처리를 할 수 있다.
            # -> 2차원을 1차원으로 id를 0부터 부여한다.
            td.id = f'{i * 3 + j}'

            # 9. 내용확인용으로 id가 5보다 작은 것은 O 크면 X를 넣어준다.
            if int(td.id) < 5:
                td.innerHTML = 'O'
            else:
                td.innerHTML = 'X'

            # 5. 생성element는 addEventListener를 create_proxy()를 입혀서 python e함수를 배정한다
            # -> 각 td마다 작동할 이벤트listener를 달아준다.
            td.addEventListener('click', create_proxy(click_cell))
            # 6. row별 tr에  반복문속 td들을 append한다.
            tr.appendChild(td)
        # 7. td들이 달린 tr들을 table에 append한다.
        my_table.appendChild(tr)

# 1. e모듈 정의처럼, 미리 실행되어야할 함수들을 [정의 후 실행까지] 시킨다.
init_game()

```





### css 꾸미기

#### body: 배경+box-sizing기준+마0패0 -> flex -> 가운데정렬 , 높이도 가운데정렬+height:100vh로 내용물을 화면가운데로 몰기

```css
body {
    background-color: whitesmoke;
    box-sizing: border-box;
    margin: 0;
    padding: 0;

    display: flex;

    justify-content: center;

    align-items: center;
    height: 100vh;
}
```

#### table: 배경+좌우마진auto로 가운데정렬

```css
#my_table {
    border: 1px solid black;
    margin-left: auto;
    margin-right: auto;
}
```



#### td: 배경+보더(table과동일) -> 가로세로동일+margin조금 -> 글자크기 가로세로보다 조금작게 + 굵기 +  텍스트가운데정렬

```css
td {
    background-color: lightgoldenrodyellow;
    border: 1px solid black;

    width: 100px;
    height: 100px;
    margin: 1px;

    font-size: 80px;
    text-align: center;
    font-weight: bold;
}
```



### 2명의 turn체계 만들기(클릭마다 턴 돌아가기)

#### 클릭시 순서대로 player1이면 O, player2턴이면 X가 입력되도록 해야한다.

1. 어차피 1명이 먼저 출발이니, player1을 default값으로 선택하여 **turn변수(불린flag)를 전역변수로 선언**한다.

   ```python
   # 10. 턴을 위한 전역변수 설정 (각 플레이어turn마다 사용될 문자열들 + turn 불린flag변수)
   player1_mark = 'O'
   player2_mark = 'X'
   is_player1 = True # player1부터 True로 시작된다.
   ```

   

2. td의 클릭리스너(click_cell)은 **클릭시 `e.target.id`로 배정된 id를 받아오게 한다**

   - id를 알아와야 **찾아서 해당player의 text를 심을 수 있다.**

   ```python
   def click_cell(e):
       # 11. 클릭된 td의 id값을 받아온다. -> 셀의 클릭여부를 알고서, 클릭안된(방문안된) 것만 클릭되게 해야한다.
       # -> html로만 이루어진다면, class를 심어놓는 등의 작업을 할 수 있다.
       cell_id = int(e.target.id)
   ```

3. **html로 뿌려지는 행렬을 -> id는 1차원으로 관리**하는 중이므로 **`방문 상태배열`을 도입하고, 체킹하면서, `방문안한 cell만 클릭 + 현재turn의 문자열을 심어지도록` 해야한다**

   - 1차원으로 0부터 관리되는 id를 **방문배열 board을 도입한다.**

   ```python
   # 12. 2차원행렬의 id를 1차원으로 관리하여,
   #    -> 방문 상태배열을 선언해서 사용할 수 있다.(객체라면 각 셀마다 객체로 관리)
   board = [False] * 9
   
   def click_cell(e):
       # 11. 클릭된 td의 id값을 받아온다. -> 셀의 클릭여부를 알고서, 클릭안된(방문안된) 것만 클릭되게 해야한다.
       # -> html로만 이루어진다면, class를 심어놓는 등의 작업을 할 수 있다.
       cell_id = int(e.target.id)
       
       # 13. 방문안된 cell일 경우, 현재의 turn에 해당하는 텍스트를 심고, 턴을 바꿔야한다.
       if not board[cell_id]:
           mark_cell(cell_id, is_player1)
   ```

4. mark_cell을 통해, 현재td에 현재turn의 문자열을 입력하자

   ```python
   def mark_cell(cell_id, is_player1):
       # 14. 현재cell_id의 td를 찾아서 문자열을 turn에 맞게 심어주고, -> 방문체킹 + turn을 바꾼다.
       # -> f-string을 활용한다
       cell = document.getElementById(f'{cell_id}')
       cell.innerHTML = player1_mark if is_player1 else player2_mark
   
       # 15. 방문체킹하고 바뀐 턴을 바꿔준다.
       board[cell_id] = True
       # 16. 바뀐 값을 return하여 setter개념으로 바꿔줘야한다..
   ```

   

5. **턴을 바꾸려면, `전역변수를 갖다쓰지만 않고, 재할당`까지 해줘야하므로 `global`을 쓸 수 밖에 없는 상황이다.**

   ```python
   def change_turn():
       global is_player1
       is_player1 = not is_player1
   
   
   def click_cell(e):
       # 11. 클릭된 td의 id값을 받아온다. -> 셀의 클릭여부를 알고서, 클릭안된(방문안된) 것만 클릭되게 해야한다.
       # -> html로만 이루어진다면, class를 심어놓는 등의 작업을 할 수 있다.
       cell_id = int(e.target.id)
   
       # 13. 방문안된 cell일 경우, 현재의 turn에 해당하는 텍스트를 심고, 턴을 바꿔야한다.
       if not board[cell_id]:
           mark_cell(cell_id, is_player1)
           change_turn()
   ```

   





### 재실행을 위한 restart[다시하기]버튼 만들기 for 지속개발

- 다 클릭하고나서, table(행렬)과 매핑된 `방문 상태배열을 초기화`해야지 편하게 개발이 가능하다



#### css로 hover시 content밀어내기 & span 보이게하기

`button#restart.btn.btn-swap[pys-onClick="restart_game"]{다시하기}`

- hover애니메이션 효과를 위하 **.btn .btn-swap클래스 2개를 주었다.**

- context부분에 **span 진짜? 태그를 추가하여 hover시 나올 텍스트가 되게 한다**

  `다시하기<span>진짜?</span><`





`.btn`

```css
.btn {
    background: none;
    border:2px solid black;

    color: black;
    font-size: 35px;
    margin: 20px;
    padding: 20px 40px;

    width: 250px;
    height: 80px;

    cursor: pointer;
    position: relative;
}
```



![image-20220830000626075](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220830000626075.png)



`.btn-swap span`{}

- **span은 투명도0 -> hover시 1로 바뀌게 한다**

```css
.btn-swap span {
    position: absolute;
    top: 0;
    left: 0;
    /*  이렇게만 주면, span태그 글자가 버튼왼쪽위로 붙는다.*/

    padding: 20px 40px; /* 원래 버튼글자와 padding동일하게 주기*/
    width: 100%;

    opacity: 0; /* 글자가 투명도0으로 안보이게 한다 -> hover시만 보이게 해야한다*/
}

.btn-swap:hover span {
    opacity: 1;
}
```





`.btn-swap::before`

- hover시 기존콘텐트인 다시하기를 `hover시 width 0 -> 100%밀어내서 안보이게`한다

```css
/* 이제, hover겹치는 span을 위해
   ::before를 통해 content(다시하기) 앞에 width0%로 끼워넣은 것을 -> hover 시 100%를 차지하게 하여 밀어내버린다.
 */
.btn-swap::before {
    content: '';
    width: 0;
    height: 100%;

    position: absolute;
    top: 0;
    left: 0;
    background-color: cornflowerblue;
}

.btn-swap:hover::before {
    width: 100%;
}
```

![image-20220830002241566](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220830002241566.png)

![image-20220830002247558](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220830002247558.png)





#### css로 hover시 전환효과 주기

- span은 opacity를 0.5s, before는 width를 0.5s로 transition주면 된다.

![image-20220830003620396](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220830003620396.png)



### restart e함수 작성하기(상태변수 및 view)

1. py모듈에 init_game()위에 정의해주자
2. **상태관련 변수들을 모두 초기화한다**
   1. python - is_player1, board
   2. html - 각각의 id에 대한 cell



### turn을 view에 알려주기(click_cell할때마다 바뀐 turn텍스트 찍어주기)

1. turn을 알려줄 빈공간을 만든다.

   - ```
     div#print_turn.text-2xl
     ```

2. click_cell내부에서 작동할 python함수를 작성한다.

   1. 고정된 html원소를 찾는 것이므로 함수위에 전역으로 정의해준다.
   2. 현재의 turn을찍어주는 함수를 작성한다.

3. **`click_cell()`뿐만 아니라, `init_game()`에서도 호출하여 최초의 턴도 찍어준다.**

4. **뿐만 아니라 다시하기인 `restart_game()`에도 호출해야한다. 안하면 다시하기 누른 상태의 turn이 그대로 찍힌다.**

   - init_game()에서 view초기화이외에 **동적인 작업**은, 무조건 restart_game()에서도 해주자





### 클릭_셀마다 [turn 메세지 출력]이전에 [승자체크부터 먼저하기] -> check_win()

1. print_turn_message() 내부에서 **turn 출력 이전에 먼저 승자체크하고, 걸리면 turn대신 승자를 출력**하도록 해야한다.

   ```python
   # 18. turn을 찍어줄 공간을 찾고 -> 메서드를 작성한다.
   print_turn = document.getElementById('print_turn')
   def print_turn_message():
       turn_message = player1_mark if is_player1 else player2_mark
       # 23. 턴 변경 이전에, 승자체크를 해서, 승리한다면 turn 대신 's win으로 출력해줘야한다.
       check_win()
   
       print_turn.innerHTML = turn_message + '\'s turn'
   ```

2. **승리확인시 확인해야할 좌표들(1차원 id)을 `튜플 좌표 리스트`로 미리 전역변수로 선언해놓자.**

   - 확인시 해당좌표들에 같은 값이 들어있는지 확인해야한다.

   ```python
   win_list = [
       (0, 1, 2),  # 가로
       (3, 4, 5),
       (6, 7, 8),
       (0, 3, 6),  # 세로
       (1, 4, 7),
       (2, 5, 8),
       (0, 4, 8),  # 대각
       (2, 4, 6),
   ]
   ```

3. 이제 **board 상태배열 + 확인 튜플좌표 리스트 반복문** 을 통해서 승리하는지 확인한다.

   1. **3개의 원소를 확인**하는데, **첫번째가 빈칸이라면, 확인하지 않는다.**

   2. 해당좌표가 O든 X든  **3개 원소가 다 똑같은지 먼저 확인**한다. (누군가는 승리)

   3. **이제 board상태배열에서 누가 이긴상태인지 알아야하는데, `현재는 방문배열로서 True`로만 기록했었다.**

      - **board에 False -> 방문시 True가 아니라 `방문시 해당 marker`를 집어넣어놓고, `3원소가 같은 것이 누구인지 확인`해야할 필요가 있다.**

      ```python
      # board[cell_id] = True
      board[cell_id] = player1_mark if is_player1 else player2_mark
      ```

   4. **승리한 사람이 발견되면, winner뿐만 아니라 `True`의 `게임 종료여부`도 반환한다**

      - **그 이유는 `비긴 경우(종료, True)`이외에 `아직 게임안끝난 경우(False)`도 알려줘야하기 때문이다.**

   ```python
   def check_win():
       winner = '' # 31.
   
       # 25. 이제 **board 상태배열 + 확인 튜플좌표 리스트 반복문** 을 통해서 승리하는지 확인한다.
       # -> 튜플list는 반복문시 for인자에 한개씩 뽑아서 바로 쓸 수 있다.
       for x, y, z in win_list:
           # 26. 3개의 원소를 확인하는데, 첫번째가 빈칸이라면, 확인하지 않는다.
           if not board[x]:
               continue
           # 27. 해당좌표가 O든 X든 다 똑같은지 먼저 확인한다. (누군가는 승리)
           if board[x] == board[y] == board[y]:
               # 28. 누가 이겼는지 1개 원소로 확인한다. -> 'O' 또는 'X'를 넣어준 상태다.
               winner = board[x] # board[cell_id] = player1_mark if is_player1 else player2_mark
               # 30. 승자가 나오면 반복문 break를 걸어주고, 가변변수로서 위에는 None 대신 '' 빈문자열로 초기화
               #  -> 아래에서 if winner를 return한다.
               break
   
       if winner:
           # 32. 승자가 발견되었으면, winner뿐만 아니라 [승리여부인 True]도 같이 return해준다.
           return True, winner
   ```

4. **check_win()은 기본적으로 winner뿐만 아니라 `게임 끝났는지 여부`를 boolean으로 반환한다**

   1. 승리조건에 부합하는 경우 -> True(게임종료), winner
   2. **승리아닌데, board상태배열에 빈칸이 있는 경우 -> `False(게임진행중), ''`**
   3. **승리도 아니고, board에 빈칸이 없는 경우 -> `True(비김), 'Tie'`를 반환해준다**

   ```python
   # 32. 승자가 발견되었으면, winner뿐만 아니라 [승리여부인 True]도 같이 return해준다.
   if winner:
       return True, winner
   
   # 33. 승자를 못찾았다면, 아직 [게임이 안끝난 상태]거나 or [비긴 경우]다. (매번 체크된다)
   # => ( 승자 없는데 )  board상태배열에 빈칸(False)가 존재하면 -> 아직 안끝난 상태다.
   # => ( 승자 없는데 )  board상태배열에 빈칸(False)이 없으면  -> 비긴 경우다.
   if False in board:
       # 34. 아직 안끝났으면 False 및 winner에 빈문자열로 반환한다.
       return False, ''
   # 35. (승자없고, 남아있는 칸도 없다면) -> 비긴 경우다. -> 승자 자리에 Tie라고 반환해준다.
   return True, 'Tie'
   ```

   

5. 이제 다시 print_turn_message() 로 넘와서 `게임종료여부, 정보`를 반환받아서 다르게 출력하는 경우를 처리해준다.

   ```python
   def print_turn_message():
       # 23. 턴 변경 이전에, 승자체크를 해서, 승리한다면 turn 대신 's win으로 출력해줘야한다.
       is_end, winner = check_win()
       # 36. 종료되었으면 winner에는 'O' or 'X' (승리) vs  'Tie'(비김)의 2가지 경우가 있다.
       # -> 삼항연산자로 확인해서 그에 따라 's turn대신 맞는 문자열을 출력해준다.
       # -> 2가지 경우로 비교를 하는 것보다 Tie인지 아닌지로 판단하면 된다.
       if is_end:
           print_turn.innerHTML = f'{winner} Win !!' if winner != 'Tie' else 'Tie !!'
           return
       
       turn_message = player1_mark if is_player1 else player2_mark    
       print_turn.innerHTML = turn_message + '\'s turn'
   ```





### 승자데이터가 차게되면, 더이상 진행 게임안되게 하기

1. click_cell()이 가능한 경우는 아직 board[id]가 False상태일 때이다. -> **게임이 아직 안끝났을 때도 추가한다**

   ![image-20220830172738770](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220830172738770.png)

2. **그렇다면 `is_end는 global 전역상태변수`로 관리되어야한다**

   ![image-20220830172907432](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220830172907432.png)

   

3. **check_win()이 반환하는 값은, 전역상태변수를 업데이트해야한다.**

   ![image-20220830173002463](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220830173002463.png)



4. **restart_game 등에서는 `다시 초기화해줄 필요 없다`**
   - **check_win()은 `click_cell()내부에서 이미 클릭후 처음 작동`하므로**
     - **`restart_game(is_end==True)`->  `빈셀로 초기화` -> `내부 print_turn_message` -> `check_win()시 빈셀(html+board)로 업데이트` ->  `is_end == False로 업데이트`됨**
     - **즉, restart_game속  `board초기화 -> check_win()`으로 인해  자동으로 False상태가 되어있다.**

### 코드 수정(전역변수는 파라미터orReturn값으로 주지말자)

- 전역변수 is_player1을 mark_cell()**인자로 받지말고**, **global로 쓰되, return안하도록 수정**

  ```python
  # def mark_cell(cell_id, is_player1):
  # 40. 전역변수는 파라미터로 받지말고 return도 하지말자
  def mark_cell(cell_id):
      global is_player1
  ```



### 모드 설정을 위한 radio만들기(2player 기본 checked)

1. input radio들이 들어갈 div공간 만들기

   `div#radio.text-xl.font-light`

2. input으로 radio들을 만든다. type만 radio를, **각각의 radio들은 모두 같은name으로 1개의 데이터만 택1된다.**

   - name뿐만 아니라 id, value, pys-onClick값도 주는데 각각 다르게 준다.

   - **같은 부분은 아래와 같이 생성한다.**

     `input:radio[name='check-radio']`

   - **모드를 선택할때마다 `restart_game`이 실행되어야한다. `pys-onClick`으로 주자**

     ```html
     <input type="radio" name="check-radio" id="ai" value="ai" pys-onClick="restart_game"> 1 Player
     ```

3. 1개의 input을 복사한 뒤, id와value값만 다르게 준다.

   - **기본 체크되어있도록 태그끝에 `checked`를 준다.**

   ```html
   <input type="radio" name="check-radio" id="human" value="human" pys-onClick="restart_game" checked> 2 Player
   ```

4. **`모드를 결정하는 radio는 클릭시마다 restart`해줘야하는 것을 생각하자.**

```html
<div id="radio" class="text-xl font-light">
    <input type="radio" name="check-radio" id="ai" value="ai" pys-onClick="restart_game"> 1 Player
    <input type="radio" name="check-radio" id="human" value="human" pys-onClick="restart_game" checked> 2 Player
</div>
```



### 모드설정을 위한 모듈 수정

1. 2명의 player(O, X)에 대해, **1player선택시 -> player1 = human / player2 =ai를 담당하게 한하기 위해, mark를 human, ai변수에도 할당해준다.**

   ```python
   # 41. 1인용일 때, 각 mark를 human, ai에게도 배정한다.
   player1_mark = human = 'O'
   player2_mark = ai = 'X'
   ```

   

2. **radio에 체크되어있는 것을 확인하기 위해 , 2개의 input태그를 일단 가져와야한다.**

   - **가져온 radio태그는 `vs_ai.checked`를 통해 체크여부를 확인할 수 있다.**

   ```python
   # 42. radio에 체크되어있는 것을 확인하기 위해 , 2개의 input태그를 일단 가져와야한다.
   vs_ai = document.getElementById('ai')
   vs_human = document.getElementById('human')
   ```

   

3. **click_cell을 했을 때**

   1. 기존: 빈칸이면서 && 게임이 안끝났을 경우-> 마킹mark_cell + 턴 변경change_turn했었다.
   2. **변경: 빈칸 && 승자없을경우 -> 마킹mark_cell을 한 뒤 -> `턴을 바꿔야하는데`**
      1. **`현재 1인용으로서 as radio.checked` && `turn이 ai(is_player1=False)` && `게임안끝났다면`** -> **`change_turn대신 ai_turn으로 넘긴다.`**
   3. **not is_end를 2번 검사하게 되는데, `player1(human)`에 의해 게임이 먼저 종료될 수 있기 때문이다.**
      - 현재는 player1 mark_cell & change_turn 이후 **print전 게임종료확인 로직은 없는 상태다.**
      - **일단 나중에 수정하기로 하고, `ai_turn()으로 넘어오기 전에 게임 종료됬는지 확인검사 로직`만 넣어준다.**

   ```python
   def click_cell(e):
       # 11. 클릭된 td의 id값을 받아온다. -> 셀의 클릭여부를 알고서, 클릭안된(방문안된) 것만 클릭되게 해야한다.
       # -> html로만 이루어진다면, class를 심어놓는 등의 작업을 할 수 있다.
       cell_id = int(e.target.id)
   
       # 13. 방문안된 cell일 경우, 현재의 turn에 해당하는 텍스트를 심고, 턴을 바꿔야한다.
       # if not board[cell_id]:
       # 37. 방문안된cell이면서 && 게임이 안끝났을때만 클릭되게 한다.
       if not board[cell_id] and not is_end:
           mark_cell(cell_id)
           change_turn()
           # 42. 턴을 바꾼 뒤, player2 대신 ai의 턴(ai checkd & is_player1 False)이라면
           # -> 넘어가지 말고 직접 두도록 하게해야한다.
           # -> 추가로 게임이 종료된 상태가 아니여야한다.(player1에 turn에서 게임 종료될 수 있다)
           # => player1으로 print되기 전에 이미 승자여부 판단짓는 로직은 있다가 처리한다.
           if vs_ai.checked and not is_player1 and not is_end:
               ai_turn()
   
       # 20. 현재 바뀐 턴을, 알려주는 div에 찍어준다.(승자여부도 여기서 확인하는 중)
       print_turn_message()
   ```



### ai_turn()을 처리하기 with minimax 알고리즘

#### ai가 랜덤한 1개칸만 선택해서 mark_cell + change_turn 하게하고 테스트하기

1. mark_cell하고 change_turn은 항상 같이 움직여야한다. **통합 메서드 mark_cell_and_change_turn**을 만들어주고 mark_cell을 대체한다.

2. **현재 board에서 빈칸을 찾고, 1개를 랜덤하게 고른 뒤, 그 spot에 mark_cell_and_change_turn하게 해서 테스트한다.**

   ```python
   def ai_turn():
       # 43. ai가 두기 위해서는 빈셀부터 먼저 찾아야한다.
       # -> 빈셀들의 위치 를확인하기 위해서는, tuple()로 만들어준다.(변하지 않는 값)
       empty_spots = tuple(index for index, cell in enumerate(board) if not cell)
       # 44. 빈칸 중 랜덤하게 1칸만 가져온다.
       spot = random.choice(empty_spots)
       # 45. 랜덤한 빈칸 1개를 mark_cell로 칠해준다. -> 1 Player모드로 한번 두고, 랜덤으로 1개를 칠하는지 확인한다.
       mark_cell_and_change_turn(spot)
   ```

   

![image-20220901125550304](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220901125550304.png)

#### 테스트 후 랜덤한 1개 빈칸(spot)이 아니라, best spot을 찾는 알고리즘 적용하기

1. 기존 랜덤으로 고르는 것을 주석처리하고, 메서드로 반환하게 자리를 잡는다.

   ![image-20220901130537878](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220901130537878.png)

2. best_move()는 일단 **빈칸을 찾아, board의 상태 마킹만 한다.**

   - mark_cell()은  html마킹 + board마킹
   - **현재는 board만 마킹만 하면서, `마킹할때마다 매번 minimax(board, False)`로 score를 매번 확인한 뒤, `복구하면서, 택1의 score가 가장 높은 곳을 greedy로 탐색`한다.**

   ```python
   def best_move():
       best_score = float('-inf')
       spot = None
       for i, cell in enumerate(board):
           if not cell:
               # 45. 모든 빈셀을 찾을때마다 마킹해서 score를 계산한 뒤, 복구한다.
               board[i] = ai
               score = minimax(board, False)
               board[i] = False
               # 46. 만약 더 좋은 점수를 내었따면, 점수와 그 때의 원소를 저장한다.
               if best_score < score:
                   best_score = score
                   spot = i
       # 47. 찾은 best_score의 spot를 반환한다.
       return spot
   ```



#### 미니맥스 알고리즘 작성 개념

- backtracking의 한 부분이다.
- 컴퓨터가 이길 경우 1점
- 플레이어가 이길 경우 -1점
- 승자가 없는 경우 0점(비긴 경우)
  - 각 경우마다 남은턴수를 곱하면 더 좋은 모델이 된다.



1. player가 먼저 수를 두면 -> ai는 자신이 둘 수 있는 모든 경우의 수를 둔다.

   ![image-20220901132157568](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220901132157568.png)

2. 다음으로 ai는 player가 둘 수 있는 수도 모두 둔다.

   ![image-20220901134320205](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220901134320205.png)

3. **이 때, 컴퓨터는 `자신의 최선의 수인 max score`를 player turn에서는 `플레이어가 최선의 수를 둔 컴퓨터min score`를 만들게 한다.**





4. O의 차례라고 가정하자. -> 4 , 6, 9의 위치에 둘 수 있다. -> 아직 개임이 끝나진 않았다.

   ![image-20220901134524004](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220901134524004.png)

5. **결국 게임이 종료(승리, 패배, 비김)될 때까지 다 둔다.**

   1. 빠르게 이기는 것이 더 좋은 점수를 가지게 하기 위해, 남은턴수를 곱해줄 수 있다.
      1. 여기서는 다루지 않는다.

   ![image-20220901134704897](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220901134704897.png)



6. **마지막 수로 인해 결론이 난 부분에서는 `컴퓨터의max로서 1가지 경우 밖에 없으므로 점수를 그대로 올려주면서 백트래킹`한다.**

   ![image-20220901134821976](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220901134821976.png)

   

7. 그 전단계에서는 **`플레이어의 최선의수로인한 mini전략`으로서 `가장 점수가 낮은 것을 집계`하여 올려준다.**

   ![image-20220901134904015](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220901134904015.png)

   ![image-20220901134914592](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220901134914592.png)

8. 그 전단계는 컴퓨터turn으로 max를 올려준다.

   ![image-20220901134940328](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220901134940328.png)

9. **컴퓨터 입장에서는 4번을 두는 것이 가장 유리하다. 6, 9번은 player가 승리할 수 있어서 안좋은 전략이다.**

   ![image-20220901135100824](https://raw.githubusercontent.com/is3js/screenshots/main/image-20220901135100824.png)

   - 4번을 두게되면, 비기거나 이길 수 있어서 좋다.

10. 총 경우의 수는 9!로 엄청난 연산이 필요하다.

    - **그러므로 깊이를 정해서 일정 수준까지만 경우의수를 확인해야한다.**
    - **지금은 9번 깊이(9!)므로 다 한다.**
    - **여기에 알파베타알고리즘으로 필요없는 가지를 줄여 연산량을 줄일 수 도 있다.**
      - 여기도 생략





### 미니맥스알고리즘 작성

#### minimax(board상태배열, depth마다바뀌는turn을 알려주는 flag(boolean))

1. 결과적으로 humanTurn(flag-False)으로 게임에 대한 node가 시작되며, 최종적으로는 i에 ai가 둘 때 나타날 수 있는 경우의수를 다 고려한 뒤, best_score를 반환해줄것이다.

   - 모든 cell마다 best_score를 계산한 뒤, 그 best_socre를 만들어내는 i(spot)을 찾는 것이다.

   ```python
   def best_move():
       best_score = float('-inf')
       spot = None
       for i, cell in enumerate(board):
           if not cell:
               # 45. 모든 빈셀을 찾을때마다 마킹해서 score를 계산한 뒤, 복구한다.
               board[i] = ai
               score = minimax(board, False)
               board[i] = False
               # 46. 만약 더 좋은 점수를 내었따면, 점수와 그 때의 원소를 저장한다.
               if best_score < score:
                   best_score = score
                   spot = i
       # 47. 찾은 best_score의 spot를 반환한다.
       return spot
   ```

   

2. **minimax는 재귀로서 node를 뻗으며, depth마다 turn이 달라지는 업데이트변수를 파라미터로 가지고 있다.**

   ```python
   def minimax(is_ai_turn):
   ```

   

3. 종착역은 check_win()을 통해, 반환되는 is_end, winner 중 is_end가 True로 게임이 끝났을 때이다.

   - 종착역에서는 winner변수에 담긴 승자(O or X의 marker)에 따라 점수를 매핑하여 반환한다.

     - winner가 player1marker=  human = 'O'인 경우, -1점
     - player2_maker = ai = 'X'인 경우, 1점
     - 'Tie'로서 비긴 경우, 0점을 주게 한다.

   - **marker(winner)별 점수매핑은 dict로 한다.**

     ```python
     def minimax(is_ai_turn):
         # 48. 현재 ai가 놓은 상태에서 check_win()으로 승패부터 판단한다.
         # -> 가정이므로 전역변수 is_end대신 is_simulation_end로 대신 받는다.
         is_simulation_end, winner = check_win()
     
         # 49. 경기가 종료된 상태라면, dict score에 매핑된 점수를 반환해준다.
         if is_simulation_end:
             return scores[winner]
     ```

     ```python
     # 50. marker가 들어가 있는 변수로 매핑해준다. 컴터가 이기면 +1, 사람이기면 -1, 비기면0
     scores = {
         ai: 1,
         human: -1,
         'Tie': 0,
     }
     ```

     - **이렇게 결과 변수별, 매핑은 dict를 두고 한다.**

4. **depth별 2가지 양상으로 자식node들을 뻗어서, player별 다르게 자식node들을 뻗어야한다.**

   - 이 때, backtracking이라면, 상태배열을 깊은복사하는 파라미터로 들고 있지 않아도 된다.(원상복구)
   - **파라미터 속 depth별 player여부(is_ai_turn)을 확인**하여 **각각 다르게 자식node들을 뻗**어나간다.
     - **`현재 depth정보는 flag변수를 두어 알려준다.`**
   - 종착역을 제외한 현재재귀에서는 **자식node들값을 1개로 집계하여 반환하는데, ai는 max값을 가진 node를, human은 min값을 가진 node의  반환값을 1개로 집계하여 반환해줘야한다.**
     - ai_turn일때는... max알고리즘으로서, 자식node들이 반환해주는 score중 가장 높은 값을 선택한다.
     - human_turn(맨 처음 포함)일 때는, **`컴퓨터입장에서는 [human이 잘하여] 지거나 -1, 비기는 0 것을 고르도록`mini알고리즘을으로서**, 자식node들이 반환해주는 score중 가장 낮은 값을 선택하여 반환한다.
       - **각 자식들은 반대Flag로 넘겨서 자식들을 호출해야한다.**
   - **결국**

   ```python
   def minimax(is_ai_turn):
       # 48. 현재 ai가 놓은 상태에서 check_win()으로 승패부터 판단한다.
       # -> 가정이므로 전역변수 is_end대신 is_simulation_end로 대신 받는다.
       is_simulation_end, winner = check_win()
   
       # 49. 경기가 종료된 상태라면, dict score에 매핑된 점수를 반환해준다.
       if is_simulation_end:
           return scores[winner]
   
       # 51. default사람차례에 호출되어, False로 들어가있는 is_ai_turn이 True로 바뀐 경우
       # -> ai가 두는 것을 처리해야한다.
       # 일단 pass로 두고 human_turn일때를 처리한다.
       if is_ai_turn:
           # 54. 반대로 ai turn에서는, 종착역에서 반환하는 것중 max만 가진다.
           best_score = float('-inf')
           for i, cell in enumerate(board):
               if not cell:
                   board[i] = ai
                   score = minimax(False)  # turn은 담턴으로서, 반대로 돌려준다.
                   board[i] = False
                   best_score = max(best_score, score)
       else:
           best_score = float('inf')
           # 52. 사람의 턴에서는, 빈칸을 찾아돌면서, human marker를 둔체로 점수를 확인한다.
           # -> 여러 경우의 수를 재귀로 구현한다. 종착역은 겜 끝날때다.
           for i, cell in enumerate(board):
               if not cell:
                   board[i] = human
                   score = minimax(True)  # turn은 담턴으로서, 반대로 돌려준다.
                   board[i] = False
                   # 53. 종착역(게임 종료)에서 반환된 점수를 바탕으로 human이 이겼을 때, 가장 작은값을 찾는다.
                   best_score = min(best_score, score)
   
       # 55. boolean변경으로 매depth마다 서로 다르게 처리하여 반환된 best_score를 반환한다.
       # -> 종착역에서는 승자의node에서 1개만 점수만 반환되지만,
       # -> 그 직전엔 여러node들이 뻗어나가는 상황이며, 그 node들 중 best_score 1개로만 집계하여
       # -> 그 score값만 반환된다.(자식node들 집계를 greedy로 시행)
       # => 여러node의 집계를 반복문 + greedy로 구현한 best_score를 반환
       return best_score
   ```

   

5. **각 빈셀마다 ai가 놓을 때의 best_score를 반환하는데, 그것도 바깥에서 greedy를 통해 가장 높은 점수의 빈셀을 찾아서, 처리하게 하니 테스트를 해본다.** 

   - greedy로 시작해 계속 greedy로 진행된다.
   - **주체가 달라지는 것은 flag변수를 재귀에 달아서, detph마다 다르게 처리한다.**
   - **주체마다 자식들의 max를 뽑을지(ai), min을 뽑을지(human)다른 것이 자신의 처리다.**

   ```python
   def best_move():
       best_score = float('-inf')
       spot = None
       for i, cell in enumerate(board):
           if not cell:
               # 45. 모든 빈셀을 찾을때마다 마킹해서 score를 계산한 뒤, 복구한다.
               board[i] = ai
               score = minimax(False) # ai가 두고, human차례로서 해당depth는 human(컴퓨터는 mini)로 놓게 한다.
               board[i] = False
               # 46. 만약 더 좋은 점수를 내었따면, 점수와 그 때의 원소를 저장한다.
               if best_score < score:
                   best_score = score
                   spot = i
       # 47. 찾은 best_score의 spot를 반환한다.
       return spot
   ```

   

### 내가 A/S

#### ai가 연달아서 바로 두기 전에, 종료체크(check_win())까지 하고 진입하자. 만약, 종료되었으면 밑에 기본print_turn_message()가 알아서 해줄 것이다.

```python
# if vs_ai.checked and not is_player1 and not is_end:
#     ai_turn()
if not check_win()[0] and vs_ai.checked and not is_player1:
    ai_turn()
```


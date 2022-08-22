from js import document, window
from pyodide import create_proxy

def _upload_file_and_show(e):
    # 1. input태그(e.target)이 load를 마치면, e.target 엘리먼트 안에 files.item의 (n)번재로 존재한다.
    file = e.target.files.item(0)
    # 2. html에 img태그를 먼저 생성하고, 거기에 삽입해준다.
    # -> js모듈은 pyodide에서 제공하는 모듈로서 from js에서 import해서 쓴다.
    new_img = document.createElement('img')
    # 업로드된 이미지의 src는 window.URL.createObjectURL을 통해 file 객체에서 자신의 주소를 뽑아올 수 있다.
    new_img.src = window.URL.createObjectURL(file)

    # 5. 이미지가 심어진 이미지태그를 빈공간 div에 심어주자
    document.getElementById("my_image1").appendChild(new_img)


# 3. 업로드 이미지를 심어주는 함수를, file_upload1아이디를 가진  input태그에게 change 리스너를 걸어준다.
# -> html에서는 pys-onClick을 못걸어줬었다. 이렇게 거는 수 밖에 없다.
file_upload1 = document.getElementById("file_upload1")
file_upload1.addEventListener("change", create_proxy(_upload_file_and_show))

#  4. 여기까지 change 이벤트리스너를 걸어줘도 이미지가 안들어간다.
# -> 에러를 보면, pyodide의 create_proxy를 사용하라고 나온다.
# => 이벤트리스너에, 만든 이벤트모듈을 바로 걸지말고, create_proxy로 한번 씌운 것을 걸어줘야한다.


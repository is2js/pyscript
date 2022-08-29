from js import document, window, Uint8Array, File
from pyodide import create_proxy
from PIL import Image
import io

image_for_id = {}


async def _upload_file_and_show(e):
    # 1. input태그(e.target)이 load를 마치면, e.target 엘리먼트 안에 files.item의 (n)번재로 존재한다.
    file = e.target.files.item(0)
    # 2. html에 img태그를 먼저 생성하고, 거기에 삽입해준다.
    # -> js모듈은 pyodide에서 제공하는 모듈로서 from js에서 import해서 쓴다.
    new_img = document.createElement('img')
    # 업로드된 이미지의 src는 window.URL.createObjectURL을 통해 file 객체에서 자신의 주소를 뽑아올 수 있다.
    new_img.src = window.URL.createObjectURL(file)

    # 7. 각 요소마다 서로 다른id를 가진 공간을 찾을 때는, 자신만의 부모로 갔다가 class로 여러개를 찾는 척 [0]
    #    공통 클래스명으로 찾은 뒤 id를 뽑아낸다.
    my_image = e.target.parentNode.getElementsByClassName("my_image")[0]
    # 5. 이미지가 심어진 이미지태그를 빈공간 div에 심어주자
    # document.getElementById("my_image1").appendChild(new_img)
    # 8. 나는 다시 클릭할 시 기존에 넣어둔 자식들 다 지우고 다시 appendChild
    # -> 첫번째 자식이 없어질때까지 반복해서
    # my_image.removeChild()
    while my_image.firstChild:
        my_image.removeChild(my_image.firstChild);
    document.getElementById(my_image.id).appendChild(new_img)

    # 10. 각 이미지 파일객체를 전역변수에 담아놔야 합성할 수 있다.
    # - pillow의 Image모듈을 써서 열어본다
    # my_image = Image.open(file)
    # 11. js 파일을, 어레이버퍼 -> 바이트배열 -> 바이트스트림으로 만들어줘야 Image.open()에 사용할 수 있다.
    # 12. 어레이 버퍼를 만들 때, 비동기식으로 만들어야한다.
    array_buf_from_js = Uint8Array.new(await file.arrayBuffer())
    bytes_arr = bytearray(array_buf_from_js)
    bytes_stream = io.BytesIO(bytes_arr)

    img = Image.open(bytes_stream)

    # 16. 형식을 png가 아니면 png로 바꾸기
    # -> JPG지는 합성시 mode가 RGBA로 찍히고, png는 RGB로 찍히게 됨
    if not img.mode == 'RGB':
        img = img.convert('RGB')

    # 13. 전역dict에 각각의 image id로 저장하기
    image_for_id[my_image.id] = img


def image_blend(e):
    # 14. 첫번재 이미지로 크기 맞추기
    # -> 이미지 형식이 똑같아야한다...
    image_for_id['my_image2'] = image_for_id['my_image2'].resize(image_for_id['my_image1'].size)
    print(image_for_id)
    # 15. slider값을 가져와서 그 비율대로 합성하기
    slider = document.getElementById("my_range")
    value = int(slider.value) / 100 # blend함수는 0~1사이 값을원해서
    # print(value)
    blended_img = Image.blend(image_for_id['my_image1'], image_for_id['my_image2'], value)

    # 16. 합성결과는 open때 들어간 것 처럼 PIL객체며 -> bytes_stream을 만들기위해 빈 stream에 .save()를 통해 변환해준다.
    return_stream = io.BytesIO()
    blended_img.save(return_stream, format = "PNG") # 로컬파일과 동급인 인메모리파일 byte_stream
    # 16-2. stream의 값을 통해 -> 8비트배열 -> js 파일객체로 만든다
    return_image_file = File.new([Uint8Array.new(return_stream.getvalue())], "my_image3.png", {"type": "image/png"})
    # print(return_image_file)

    # 17. 만들어진 File객체를 img태그에 동봉해서 공간에 뿌려준다.
    new_img = document.createElement('img')
    new_img.src = window.URL.createObjectURL(return_image_file)
    my_image = e.target.parentNode.getElementsByClassName("my_image")[0]

    while my_image.firstChild:
        my_image.removeChild(my_image.firstChild);
    document.getElementById(my_image.id).appendChild(new_img)


# 3. 업로드 이미지를 심어주는 함수를, file_upload1아이디를 가진  input태그에게 change 리스너를 걸어준다.
# -> html에서는 pys-onClick을 못걸어줬었다. 이렇게 거는 수 밖에 없다.
file_upload1 = document.getElementById("file_upload1")
file_upload1.addEventListener("change", create_proxy(_upload_file_and_show))

#  4. 여기까지 change 이벤트리스너를 걸어줘도 이미지가 안들어간다.
# -> 에러를 보면, pyodide의 create_proxy를 사용하라고 나온다.
# => 이벤트리스너에, 만든 이벤트모듈을 바로 걸지말고, create_proxy로 한번 씌운 것을 걸어줘야한다.

# 6. 2번째 file_upload input에도 걸어주기
file_upload2 = document.getElementById("file_upload2")
file_upload2.addEventListener("change", create_proxy(_upload_file_and_show))

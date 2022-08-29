input_dan = Element('input-dan')


def calculator(e):
    try:
        n = int(input_dan.element.value)
    except:
        input_dan.element.value = ''
        input_dan.element.placeholder = '숫자만 입력가능!'

        input_dan.element.focus()
        return


    result = f'<ul> <li> {n}단 </li>'
    for i in range(1, 9 + 1):
        result += f'<li>{n} * {i} = {n * i}</li>'
    result += f'</ul>'

    Element('result-print').write(result)

def key_press(e):
    # print(e.keyCode)
    if e.keyCode == 13:
        calculator(e)

input_dan.element.onkeypress = key_press

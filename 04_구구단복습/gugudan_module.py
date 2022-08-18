input_dan = Element('input-dan')


def calculator(e):
    n = int(input_dan.element.value)
    # result = ''
    result = f'<ul> <li> {n}단 </li>'
    for i in range(1, 9 + 1):
        result += f'<li>{n} * {i} = {n * i}</li>'
    result += f'</ul>'

    Element('result-print').write(result)

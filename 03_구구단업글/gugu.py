# 불러와지는 소스내부에서 Element로 input태그를 잡아온다
input_dan = Element('input_dan')

def gugudan(e):
    # 내부에서는 메서드내부에서 전역변수인 input_dan을 html요소로서 쓴다.
    # .element.value 해야 값을 가져올 수 있다.
    n = int(input_dan.element.value)
    
    ## 각 요소들을 문자열<br>이 아니라 [전체문자열은 <ul>시작 </ul> ]종료한 뒤
    ## 각 line마다 <br> 대신 <li> ~ </li>이 들어오도록 해준다.
    ## gugu_result = ""
    gugu_result = f"<ul> <li>{n}단</li>"
    for i in range(1, 9 + 1):
        # gugu_result += f"{n} * {i} = {int(n * i)}<br>"
        gugu_result += f"<li>{n} * {i} = {int(n * i)}</li>"
        
    ##
    gugu_result += "</ul>"

    # 출력html을 잡아서 write해서 출력한다
    Element('gugu_print').write(gugu_result)

# input태그가 enter가 먹으려면, .element.onkeypress에도 함수객체를 걸어줘야한다
input_dan.element.onkeypress = gugudan




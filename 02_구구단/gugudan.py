def gugudan(e):
    result = Element('result-gugu')

    n = input("몇단을 출력할까요? ")
    gugu_result = ""
    for i in range(1, 9 + 1):
        # print(f"{n} * {i} = {int(n * i)}")
        # result.write(f"{n} * {i} = {int(n * i)}")
        gugu_result += f"{n} * {i} = {int(n * i)}<br>"

    # pyscript.write('result', gugu_result) # 사라질 예정
    result.write(gugu_result)




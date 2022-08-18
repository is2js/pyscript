def gugudan():

    element = Element("result")

    n = input("몇단을 출력할까요? ")
    for i in range(1, 9 + 1):
        print(f"{n} * {i} = {int(n * i)}")

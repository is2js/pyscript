from js import document
from pyodide import create_proxy

# 8. tr들을 달 table은 모듈내 전역변수로서 먼저 실행되게해서 잡아준다.
my_table = document.getElementById('my_table')

# 10. 턴을 위한 전역변수 설정 (각 플레이어turn마다 사용될 문자열들 + turn 불린flag변수)
player1_mark = 'O'
player2_mark = 'X'
is_player1 = True # player1부터 True로 시작된다.

# 12. 2차원행렬의 id를 1차원으로 관리하여,
#    -> 방문 상태배열을 선언해서 사용할 수 있다.(객체라면 각 셀마다 객체로 관리)
board = [False] * 9


def mark_cell(cell_id, is_player1):
    # 14. 현재cell_id의 td를 찾아서 문자열을 turn에 맞게 심어주고, -> 방문체킹 + turn을 바꾼다.
    # -> f-string을 활용한다
    cell = document.getElementById(f'{cell_id}')
    cell.innerHTML = player1_mark if is_player1 else player2_mark

    # 15. 방문체킹하고 바뀐 턴을 바꿔준다.
    board[cell_id] = True
    # 16. 바뀐 값을 return하여 setter개념으로 바꿔줘야한다..


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

            # # 9. 내용확인용으로 id가 5보다 작은 것은 O 크면 X를 넣어준다.
            # if int(td.id) < 5:
            #     td.innerHTML = 'O'
            # else:
            #     td.innerHTML = 'X'

            # 5. 생성element는 addEventListener를 create_proxy()를 입혀서 python e함수를 배정한다
            # -> 각 td마다 작동할 이벤트listener를 달아준다.
            td.addEventListener('click', create_proxy(click_cell))
            # 6. row별 tr에  반복문속 td들을 append한다.
            tr.appendChild(td)
        # 7. td들이 달린 tr들을 table에 append한다.
        my_table.appendChild(tr)

# 1. e모듈 정의처럼, 미리 실행되어야할 함수들을 [정의 후 실행까지] 시킨다.
init_game()

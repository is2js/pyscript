from js import document
from pyodide import create_proxy

# 8. tr들을 달 table은 모듈내 전역변수로서 먼저 실행되게해서 잡아준다.
my_table = document.getElementById('my_table')

# 10. 턴을 위한 전역변수 설정 (각 플레이어turn마다 사용될 문자열들 + turn 불린flag변수)
player1_mark = 'O'
player2_mark = 'X'
is_player1 = True  # player1부터 True로 시작된다.

# 12. 2차원행렬의 id를 1차원으로 관리하여,
#    -> 방문 상태배열을 선언해서 사용할 수 있다.(객체라면 각 셀마다 객체로 관리)
board = [False] * 9
# 24. 승리확인시 필요할 튜플 좌표들(1차원 id)을 list로 미리 보유해놓는다.
# -> 직접 승자check마다 선언해서 확인하는 것보다, [고정된 index쌍]는 미리 선언해놓는다.
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
# 38. 게임종료여부도 전역상태로 관리된다
is_end = False


def mark_cell(cell_id, is_player1):
    # 14. 현재cell_id의 td를 찾아서 문자열을 turn에 맞게 심어주고, -> 방문체킹 + turn을 바꾼다.
    # -> f-string을 활용한다
    cell = document.getElementById(f'{cell_id}')
    cell.innerHTML = player1_mark if is_player1 else player2_mark

    # 15. 방문체킹하고 바뀐 턴을 바꿔준다.
    # 29. 현재 board칸에 들어간 원소를 True가 아니라 직접적으로 player에 따라 입력한다.
    # board[cell_id] = True
    board[cell_id] = player1_mark if is_player1 else player2_mark
    # 16. 바뀐 값을 return하여 setter개념으로 바꿔줘야한다..


def change_turn():
    global is_player1
    is_player1 = not is_player1


def click_cell(e):
    # 11. 클릭된 td의 id값을 받아온다. -> 셀의 클릭여부를 알고서, 클릭안된(방문안된) 것만 클릭되게 해야한다.
    # -> html로만 이루어진다면, class를 심어놓는 등의 작업을 할 수 있다.
    cell_id = int(e.target.id)

    # 13. 방문안된 cell일 경우, 현재의 turn에 해당하는 텍스트를 심고, 턴을 바꿔야한다.
    # if not board[cell_id]:
    # 37. 방문안된cell이면서 && 게임이 안끝났을때만 클릭되게 한다.
    if not board[cell_id] and not is_end:
        mark_cell(cell_id, is_player1)
        change_turn()

    # 20. 현재 바뀐 턴을, 알려주는 div에 찍어준다.
    print_turn_message()


def restart_game(e):
    # 17. 기존 상태 변수들(is_player1, board)을 다 초기화한다.
    global is_player1
    is_player1 = True

    for i in range(len(board)):
        board[i] = False
        # 18. 화면도 초기화한다.
        cell = document.getElementById(f'{i}')
        cell.innerHTML = ''

    print_turn_message()  # 22. 다시할 때도, init_game()처럼 초기화된 turn이 찍혀야한다.


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

    print_turn_message()  # 21. 최초의 턴도 찍어준다.


# 18. turn을 찍어줄 공간을 찾고 -> 메서드를 작성한다.
print_turn = document.getElementById('print_turn')


def check_win():
    winner = '' # 31.

    # 25. 이제 **board 상태배열 + 확인 튜플좌표 리스트 반복문** 을 통해서 승리하는지 확인한다.
    # -> 튜플list는 반복문시 for인자에 한개씩 뽑아서 바로 쓸 수 있다.
    for x, y, z in win_list:
        # 26. 3개의 원소를 확인하는데, 첫번째가 빈칸이라면, 확인하지 않는다.
        if not board[x]:
            continue
        # 27. 해당좌표가 O든 X든 다 똑같은지 먼저 확인한다. (누군가는 승리)
        if board[x] == board[y] == board[z]:
            # 28. 누가 이겼는지 1개 원소로 확인한다. -> 'O' 또는 'X'를 넣어준 상태다.
            winner = board[x] # board[cell_id] = player1_mark if is_player1 else player2_mark
            # 30. 승자가 나오면 반복문 break를 걸어주고, 가변변수로서 위에는 None 대신 '' 빈문자열로 초기화
            #  -> 아래에서 if winner를 return한다.
            break

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


def print_turn_message():
    # 39. 게임종료여부는 전역으로 관리되어야한다
    global is_end

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


# 1. e모듈 정의처럼, 미리 실행되어야할 함수들을 [정의 후 실행까지] 시킨다.
init_game()

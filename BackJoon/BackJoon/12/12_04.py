N, M = map(int, input().split())
board = []
b_w = None

for _ in range(N):
    b_w = input()
    board.append([b_w])

print(board[0])




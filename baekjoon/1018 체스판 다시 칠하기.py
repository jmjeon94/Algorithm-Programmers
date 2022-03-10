import sys

n, m = 11, 12
chess = """BWWBWWBWWBWW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBWWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW"""
chess = chess.split()

def count(chess):
    cnt1 = 0
    for x in range(8):
        for y in range(8):
            if (y+x) % 2==0:
                if chess[y][x] == 'W':
                    cnt1+=1
            else:
                if chess[y][x] == 'B':
                    cnt1+=1
    cnt2 = 0
    for x in range(8):
        for y in range(8):
            if (y+x) % 2==0:
                if chess[y][x] == 'B':
                    cnt2+=1
            else:
                if chess[y][x] == 'W':
                    cnt2+=1

    return min(cnt1, cnt2)

ans = sys.maxsize
for i in range(n-7):
    for j in range(m-7):
        ans = min(count(list(map(lambda x: x[j:j+8], chess[i:i+8]))), ans)

print(ans)


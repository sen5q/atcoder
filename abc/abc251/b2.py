def solve():
    N, W = map(int, input().split())
    A = list(map(int, input().split())) + [0, 0]    #重さ0のおもり2個を追加することで対応
    good = [False] * (W + 1)

    for k in range(N + 2):  # 2個重さ0のおもりを追加したのでN+2です
        for j in range(k):
            for i in range(j):
                w = A[i] + A[j] + A[k]
                if w <= W:
                    good[w] = True
    return good.count(True)


print(solve())
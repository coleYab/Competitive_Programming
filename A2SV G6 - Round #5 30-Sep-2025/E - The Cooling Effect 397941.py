# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))

    ans = [float("inf")] * n
    fwd = [float("inf")] * n
    for idx, temp in zip(a, t):
        fwd[idx - 1] = temp
        ans[idx - 1] = temp

    for i in range(n):
        fw = i
        bw = n - i - 1
        if fw != 0:
            fwd[fw] = min(fwd[fw - 1] + 1, fwd[fw])
        if bw != n - 1:
            ans[bw] = min(ans[bw + 1] + 1, ans[bw])

    for i in range(n):
        ans[i] = min(fwd[i], ans[i])

    print(*ans)


if __name__ == "__main__":
    t = 1
    t = int(input().strip())
    for _ in range(t):
        a =  input()
        solve()
 
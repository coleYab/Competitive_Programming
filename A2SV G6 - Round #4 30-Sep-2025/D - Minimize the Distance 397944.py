# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    print(a[(n - 1) // 2])

if __name__ == "__main__":
    t = 1
    # t = int(input().strip()) =
    for _ in range(t):
        solve()

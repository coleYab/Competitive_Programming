# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

dic = {}
cnt = 1
for i in range(ord('a'), ord('z') + 1):
    for j in range(ord('a'), ord('z') + 1):
        if i == j: continue
        dic[chr(i) + chr(j)]= cnt
        cnt += 1

def solve():
    s = input()
    print(dic[s])

for _ in range(int(input())): solve()


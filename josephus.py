def jusephus(n, k):
    if n == 1:
        return 1
    if n > 1:
        return (jusephus(n-1, k) + k - 1) % n + 1

n, k = int(input()), int(input())
print(jusephus(n, k))
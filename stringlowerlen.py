inp=str(input())
n=int(len(inp))
a=list(inp)
count=0
for i in range(n):
    if inp[i] in inp[:i]:
        count=count+1

print(n-count)

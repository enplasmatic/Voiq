n = int(input())

for i in range(0,n):
    print((i%2)-1 + 4*n*i)
    i += n%(i+n)
    if i // 7:
        break

print(i)
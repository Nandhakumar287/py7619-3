n,k=map(int,input().split())
li=list(map(int,input().split()))[:n]
li.sort()
print(li[-k])

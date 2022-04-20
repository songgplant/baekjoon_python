N = int(input())
lists = list(map(int, input().split()))
lists.sort()
if len(lists) == 0 :
    print(N)
elif len(lists) == 1 :
    print(lists[0]**2)
else :
    print(lists[0]*lists[-1])
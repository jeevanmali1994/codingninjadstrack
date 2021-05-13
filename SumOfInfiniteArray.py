def sumInRanges(arr, n, queries, q):
    sum_array = []
    initial_sum = 0
    for num in arr:
        initial_sum += num
        sum_array.append(initial_sum)
    print(sum_array)
    return sum_array

cases = int(input())
for i in range(cases):
    n = int(input())
    arr = list(map(int,input().split()))
    q = int(input())
    queries = []
    for j in range(q):
        l,r = input().split()
        queries.append([int(l), int(r)])
    ans = sumInRanges(arr, n, queries, q)
    print(ans)


    

from sys import stdin

def binary_search(list, M):
    first, last = 0, len(list)
    max = 0
    while first < last:
        tree = 0.0
        mid = (first + last) // 2
        if last - 1 == first:
            start = first
            first = list[first]
            last = list[last]
            break
        for i in range(mid,len(list)):
            tree += list[i] - list[mid]
        if tree == M:
            return list[mid]
        if tree > M:
            max = list[mid]
            first = mid 
        else:
            last = mid
    while first <= last:
        tree = 0.0
        mid = (first + last) // 2
        if last - 1 == first:
            return max
        for i in range(start+1,len(list)):
            tree += list[i] - mid
        if tree == M:
            return mid
        if tree > M:
            max = mid
            first = mid
        else:
            last = mid 

N, M = map(int, stdin.readline().split()) 
tree_list = list(map(int, stdin.readline().split()))
tree_list.append(0)
tree_list.sort()

if len(tree_list) == 1:
    print(tree_list[0])
else : print(binary_search(tree_list,M))


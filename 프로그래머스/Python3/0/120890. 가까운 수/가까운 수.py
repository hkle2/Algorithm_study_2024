def solution(array, n):
    answer = 0
    array.append(n)
    array.sort()
    l = array.index(n)
    if l == 0:
        answer = array[1]
    elif l == len(array) - 1:
        answer = array[-2]
    else:
        if n - array[l-1] > array[l+1] - n:
            answer = array[l+1]
        else:
            answer = array[l-1]
    return answer
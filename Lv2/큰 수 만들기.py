def solution(number, k):

    j = 0
    for i in range(k):
        j-=1
        if j<0: j=0

        while j<len(number)-1:
            if number[j]<number[j+1]:
                number = number[:j] + number[j+1:]
                break
            j+=1
        else:
            number = number[:-1]

    return number

print(solution('1924', 2)) # 94

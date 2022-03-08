def solution(numbers):
    answer = []
    for n in numbers:
        if n%2==0:
            answer.append(n+1)
        else:
            b = list('0' + bin(int(n))[2:])
            i_zero = b[::-1].index('0')
            b[len(b) - i_zero -1] = '1'
            b[len(b) - i_zero] = '0'
            answer.append(int('0b'+''.join(b), 2))

    return answer

print(solution(list(range(10))))


"""
101
110

1
10
 11
101

100
101
0
1

 1111
10111

0111
1011

f(1) = 

01 10

11
100
 1111111111111111111111111111111
10111111111111111111111111111111

 11111111111110
 11111111111111
 
 11111101111111
 11111110111111
 
 11101111111111
 11111111111110
 
 11111110011111
 11111110101111
 
 11110110111111
 11110111111110

"""
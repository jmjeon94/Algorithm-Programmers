def solution(a, b):
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = 0
    for i in range(a-1):
        date += month[i]
    date += b

    return days[(date+4)%7]
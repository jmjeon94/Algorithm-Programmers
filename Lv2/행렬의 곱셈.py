def dot(arr1, arr2):

    return sum([a*b for a, b in zip(arr1, arr2)])

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            row.append(dot(arr1[i], [x[j] for x in arr2]))
        answer.append(row)

    return answer

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
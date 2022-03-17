def solution(cacheSize, cities):
    answer = 0

    cache = []
    for city in cities:
        city = city.lower()
        if not city in cache:
            cache.append(city)
            if len(cache) > cacheSize:
                cache.pop(0)
            answer += 5

        else:
            cache.remove(city)
            cache.append(city)
            answer += 1

    return answer


print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))

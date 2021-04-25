def sorting(fn):
    head = ''
    num = ''
    digitFlag = False
    for i, ch in enumerate(fn):

        if ch.isdigit():
            if not digitFlag: head = fn[:i]
            num += str(ch)
            digitFlag = True
            continue

        if digitFlag and (ch.isalpha() or ch=='.'):
            break

    return head.lower(), int(num)

def solution(files):
    return sorted(files, key=sorting)


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

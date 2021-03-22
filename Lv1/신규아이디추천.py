def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2 
    new_id = ''.join(list(filter(lambda x:x.isalnum() or x in ['-', '_', '.'], new_id)))
    # 3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # 4 
    if new_id[0]=='.':
        new_id = new_id[1:]
    if new_id[-1:]==['.']:
        new_id = new_id[:-1]
    # 5
    if len(new_id)==0:
        new_id = 'a'
    # 6
    new_id = new_id[:15]
    if new_id[-1]=='.':
        new_id = new_id[:-1]
    #7
    while len(new_id)<3:
        new_id += new_id[-1]
    
    return new_id

print(solution('=.=')) # aaa

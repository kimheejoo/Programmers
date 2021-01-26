# def solution(new_id):
#     import re
#     new_id = ''.join(re.findall('[a-z0-9-_.]',new_id.lower()))
#     while True:
#         new_id = new_id.replace('..','.')
#         if new_id.find("..") == -1: break
#     new_id = list(new_id)
#     if new_id[0] == '.': (new_id).pop(0)
#     if new_id:
#         if new_id[-1] == '.': (new_id).pop()
#     if not new_id: new_id.append('a')
#     if len(new_id)>=16:
#         new_id = new_id[:15]
#         if new_id[-1]=='.': new_id.pop()
#     if len(new_id)<=2:
#         last = new_id[-1]
#         while len(new_id)<3:
#             new_id.append(last)
    
#     return ''.join(new_id)

def solution(new_id):
    import re
    new_id = re.sub('[^a-z0-9\-_.]','',new_id.lower())
    new_id = re.sub('\.+','.',new_id)
    new_id = re.sub('^[.]|[.]$','',new_id)
    if not new_id: new_id = 'a'
    if len(new_id)>=16: new_id = new_id[:15]
    new_id = re.sub('[.]$','',new_id)
    if len(new_id)<=2:
        last = new_id[-1]
        while len(new_id)<3:
            new_id += last
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
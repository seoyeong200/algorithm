import re
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    print(new_id)
    
    characters = "-_."
    new_id = ''.join( x for x in new_id if x in characters or x.isalnum())
    print(new_id)

    print(new_id.count("."))
    i=0 
    tmp=''; print(i)
    while new_id[i]=='.':
        tmp+=new_id[i]
        i+=1
        print(tmp)
    new_id = new_id.replace(tmp,'.')
    print('new_id ', new_id)

    # for n in new_id:
    #     if n==".": 
          

    
    if new_id[0]=='.':
        new_id = new_id[1:]
    if new_id[-1]=='.':
        new_id = new_id[:-1]
    print("4단계 ",new_id)
            
    if new_id=='':
        new_id="a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1]=='.':
            new_id = new_id[:-1]
    if len(new_id)<=2:
        while len(new_id)<4:
            new_id+=new_id[-1]

    

    return new_id

solution(	"...!@BaT#*..y.abcdefghijklm")
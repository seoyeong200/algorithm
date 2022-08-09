'''
superaquatornado
uperaqu
raquator -> longest
aqua   -> shortest
atorna
ornado
4 8
'''

'''
abcdefghijklmnopqrstuvwxyz
겹치는 문자 하나도 없음
-1
abaaaba , 3
abaa
aaa -> shortest
aaba -> longest
3 4
'''



t = int(input())
game = []
for _ in range(t):
    st = input()
    k = int(input())
    game.append((st, k))



for g in game:
    W = g[0]; k = g[1]
    alphabet = {'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[],'h':[],'i':[],'j':[],'k':[],'l':[],'m':[],'n':[],'o':[],'p':[],'q':[],'r':[],'s':[],'t':[],'u':[],'v':[],'w':[],'x':[],'y':[],'z':[]}
    min = len(W)+1; max = 0
    for i in range(len(W)):
        alphabet[W[i]].append(i)
    for a in alphabet.keys():
        lst = alphabet[a]
        if len(lst) >= k:
            for i in range(len(lst)-k+1):
                seq_string_len = lst[i+k-1] - lst[i] + 1
                if min > seq_string_len:
                    min = seq_string_len
                if max < seq_string_len:
                    max = seq_string_len
    if min == len(W)+1 and max == 0:
        print(-1)
    else:
        print(min, max)










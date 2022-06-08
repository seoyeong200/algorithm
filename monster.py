inf = 999
class Player:
    def __init__(self, ex, attack, defense):
        self.rewards = {}
        self.ex = int(ex); self.attack = int(attack); self.defense = int(defense); 
        self.init_ex = int(ex); self.init_attack = int(attack); self.init_defense = int(defense)
    def result(self, name, reward, time):
        self.rewards[name] = [reward, time]
        
# monster를 굳이 클래스로 저장할 필요가 있을 까 . .        
class Monster:
    def __init__(self, name, reward, ex, attack, defense):
        self.name = name; self.reward = int(reward); self.ex = int(ex); 
        self.attack = int(attack); self.defense = int(defense)
    
        
def solution(character, monsters):
    answer = ''
    ex, attack, defense = character.split(" ")
    player = Player(ex, attack, defense)
    
    mon_lst = [0 for _ in range(len(monsters))]
    for i in range(len(monsters)):
        name, reward, ex, attack, defense = monsters[i].split(" ")
        mon_lst[i] = Monster(name, reward, ex, attack, defense)
    
    for m in mon_lst:
        breaking = 0; time = 0
        while True:
            time += 1
            print("플레이어 공격")
            if player.attack - m.defense > 0: 
                m.ex -= (player.attack - m.defense)
            if m.ex <= 0:
                print("monster 죽음")
                player.result(m.name, m.reward, time); break
                
            print("몬스터 공격")
            if m.attack - player.defense > 0: 
                player.ex -= (m.attack - player.defense)
            if player.ex <= 0:
                print("player 죽음")
                player.result(m.name, 0, inf); break
            else:
                player.ex = player.init_ex
                player.attack = player.init_attack
                player.defense = player.defense
            if breaking > 10: # 무한루프 임시확인
                print("infinte looping ");break
        print("round end", player.rewards)
    max = 0.0
    for mons in player.rewards:
        print(mons)
        if float(player.rewards[mons][0])/float(player.rewards[mons][1]) > max:
            answer = mons
    print(answer)
            
    return answer


character = "10 5 2"
monsters = ["Knight 3 10 10 3","Wizard 5 10 15 1","Beginner 1 1 15 1"]
solution(character, monsters)






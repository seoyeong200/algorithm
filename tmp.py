id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","muzi frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

report = list(set(report))
print(report)
user = {i:0 for i in id_list}
print(user)

for re in report:
    report, reported = re.split(" ")
    user[reported] += 1
print(user)

blocked = []
for u in user:
    if user[u] >= 2:
        user[u]



import sys
sound = sys.stdin.readline()

realduck = ["q","u","a","c","k"]
result = 0
visited = [False] * len(sound)

qindexs = []
for idx,value in enumerate(sound):
    if value == "q" and not visited[idx]:
        qindexs.append(idx)
print(qindexs)
for idx in qindexs:
    cnt = 0
    first = True
    for s in range(idx, len(sound)):
        if realduck[cnt] == sound[s] and not visited[s]:
            visited[s] = True
            print(sound[s])
            cnt += 1
            if sound[s] == "k":
                if first:
                    first = False
                    result += 1
                cnt = 0
                continue
    print(visited)


if result < 1 :
    print(-1)
else:
    print(result)
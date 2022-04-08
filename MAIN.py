def list(sumnumber):
    if sumnumber == 0:
        return []
    if sumnumber == 1:
        return [1]
    if sumnumber == 2:
        return [[1], [1, 1]]
    sumnumber -= 2
    rlist = [[1], [1, 1]]
    while sumnumber > 0:
        newlist = [1]
        for i in range(len(rlist[-1]) - 1):
            newlist.append(rlist[-1][i] + rlist[-1][i + 1])
        newlist.append(1)
        rlist.append(newlist)
        sumnumber-=1
    return rlist


a = list(4)
print(a)

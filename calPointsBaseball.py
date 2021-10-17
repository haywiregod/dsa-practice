def calPoints(ops) -> int:
    """
    :type ops: List[str] - List of operations
    :rtype: int - Sum of scores after performing all operations
    """
    result = 0
    scores = []
    l = len(ops)
    j = -1
    for i in range(l):
        print(i, j)
        print("scores", scores)
        if ops[i] == 'C':
            scores.pop()
            j = j-1
        elif ops[i] == 'D':
            scores.append(int(2*scores[j]))
            j = j+1
        elif ops[i] == '+':
            s = int(scores[j])+int(scores[j-1])
            scores.append(s)
        else:
            scores.append(int(ops[i]))
            j += 1

    
    return sum(scores)


if __name__ == '__main__':
    line = input()
    ops = line.strip().split()

    print(calPoints(ops))

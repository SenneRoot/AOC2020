

def runUntil(startData, stop):
        memory = dict()
        i = 1
        for s in startData[:-1]:
            memory[s] = i
            i += 1
        n = startData[-1]
        i += 1
        while i <= stop:
            if n not in memory:
                memory[n] = i - 1
                n = 0
            else:
                diff = i - 1 - memory[n]
                memory[n] = i - 1
                n = diff
            i += 1
        return n



if __name__ == "__main__":
    input = [0,20,7,16,1,18,15]
    
    print(runUntil(input, 2020))
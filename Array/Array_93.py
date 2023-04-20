a=int(input())
listn=[int(n) for n in input().split(" ",a-1)]
listwe=[int(we) for we in input().split(" ",a-1)]

class sortweight:
    def SortBasedOnWeight(self, nlist,welist):
        copywelist = welist.copy()
        output=[]
        copywelist.sort()
        for i in copywelist:
            if nlist[welist.index(i)] not in output:
                output.append(nlist[welist.index(i)])
        return output
sortwe = sortweight()
print(*sortwe.SortBasedOnWeight(listn,listwe))

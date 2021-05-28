
from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertex = 0
        self.addMatrix = defaultdict(list)
    def iniList(self):
            return []
    def AddEdges(self,v1,v2):
        self.addMatrix[v1].append(v2)
    def SortEdges(self):
        for key in self.addMatrix.keys():
            self.addMatrix[key].sort()
    def getTravelList(self,vertex,n):
        result = []
        def getTravelListHelper(vertex,i):
            result.append(vertex)
            print(vertex)
            print(i)
            i+=1
            j = 0
            if len(self.addMatrix[vertex]) != 0:
                next = self.addMatrix[vertex].pop(0)
                j = getTravelListHelper(next,i)
            return i+j
        i = getTravelListHelper(vertex,0)
        print(i)
        return result

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        G = Graph()
        for ticket in tickets:
            G.AddEdges(ticket[0],ticket[1])
        G.SortEdges()
        return G.getTravelList("JFK",len(tickets))


print(Solution().findItinerary(
    [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))

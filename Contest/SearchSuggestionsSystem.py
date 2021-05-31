class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        n = len(searchWord)
        result = [[] for i in range(n)]
        products.sort()
       # result[0] = self.searchKey(searchWord[0],products)
       # if len(result[0]) == 0:
       #     return result
        for i in range(n):
            result[i] = self.searchKey(searchWord[:i+1], products)
            if len(result[i]) == 0:
                return result
        return result
    def searchKey(self,target,checkList):
        search_result = []
        max_len = 0
        for items in checkList:
            if items.startswith(target):
                search_result.append(items)
                max_len+=1
            if max_len == 3:
                break
        return search_result

print(Solution().suggestedProducts(
    ["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))

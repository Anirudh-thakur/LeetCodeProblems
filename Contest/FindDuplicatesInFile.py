#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3747/

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        content_dict = dict()
        for path in paths:
            temp1 = path.split()
            for i in range(1,len(temp1)): 
                dir = temp1[0]
                temp2 = temp1[i]
                temp3 = temp2.split('(')
                dir = dir+"/"+temp3[0]
                content = temp3[1].replace(')',"")
                if content in content_dict.keys():
                    content_dict[content].append(dir)
                else:
                    content_dict[content] = [dir]
        result = []
        co = list(content_dict.keys())
        for cox in co:
            if content_dict[cox] != None:
                if len(content_dict[cox]) > 1:
                    result.append(content_dict[cox])
        return result

if __name__ == '__main__':
   paths = ["root/a 1.txt(abcd) 2.txt(efgh)",
            "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"]
   ObjS = Solution()
   result = ObjS.findDuplicate(paths)
   print(result)

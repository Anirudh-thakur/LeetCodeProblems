class Solution(object):
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = s.replace("(","")
        s = s.replace(")","")
        n = len(s)
        result = []
        i = 0
        j = 1
        while j < n:
            co1 = s[0 : i+1]
            co2 = s[j : n]
            if self.ValidInt(co1) and self.ValidInt(co2):
                addNew = "("+co1+", "+co2+")"
                result.append(addNew)
            co1_len = len(co1)
            co2_len = len(co2)
            if co1_len > 1 and co2_len == 1:
                dec = 1
                while dec < co1_len:
                    co1_dec = co1[0 : dec]+"."+co1[dec:co1_len]
                    if self.ValidDec(co1_dec) and self.ValidInt(co2):
                        addNew = "("+co1_dec+", "+co2+")"
                        result.append(addNew)
                    dec = dec+1
            elif co2_len > 1 and co1_len == 1:
                dec = 1
                while dec < co2_len:
                    co2_dec =  co2[0 : dec]+"."+co2[dec:co2_len]
                    if self.ValidDec(co2_dec) and self.ValidInt(co1):
                        addNew = "("+co1+", "+co2_dec+")"
                        result.append(addNew)
                    dec = dec + 1
            elif co1_len > 1 and co2_len > 1:
                for dec1 in range(1,co1_len):
                    for dec2 in range(1,co2_len):
                        co1_dec = co1[0 : dec1]+"."+co1[dec1:co1_len]
                        co2_dec = co2[0 : dec2]+"."+co2[dec2:co2_len]
                        if self.ValidDec(co1_dec) and self.ValidDec(co2_dec):
                            addNew = "("+co1_dec+", "+co2_dec+")"
                            result.append(addNew)
                dec = 1
                while dec < co1_len:
                    co1_dec = co1[0 : dec]+"."+co1[dec:co1_len]
                    if self.ValidDec(co1_dec) and self.ValidInt(co2):
                        addNew = "("+co1_dec+", "+co2+")"
                        result.append(addNew)
                    dec = dec+1
                dec = 1
                while dec < co2_len:
                    co2_dec =  co2[0 : dec]+"."+co2[dec:co2_len]
                    if self.ValidDec(co2_dec) and self.ValidInt(co1):
                        addNew = "("+co1+", "+co2_dec+")"
                        result.append(addNew)
                    dec = dec + 1
                
            i = i + 1
            j = j + 1
        #print(result)
        result_set = set(result)
        result = list(result_set)
        return result
    def ValidInt(self,check):
        l1 = len(check)
        l2 = len(str(int(check)))
        if l1 != l2:
            return False
        return True
    def ValidDec(self,check):
        l1 = len(check) 
        check_float = str(float(check))
        if l1 >= 7:
            return self.checkBigValidDec(check,l1)
        l2 = len(check_float)
 #       print("Check:"+str(check))
 #       print("length check:"+str(l1))
 #       print("Check Float:"+str(check_float))
 #       print("Length Integer check:"+str(l2))
        if l1 != l2:
            return False
        if(l2 >= 3 and check_float[l2-1] == '0' and check_float[l2-2] == '.'):
            return False
        return True
    def checkBigValidDec(self,check,n):
        if check[n-1] == '0':
            return False
        if check[0] == '0' and check[1] != '.':
            return False
        return True
if __name__ == '__main__':
    obj = Solution()
    result = obj.ambiguousCoordinates("(123)")
    print(result)
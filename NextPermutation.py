class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        dyn_string = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                      "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two"
                      , "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven"
                      , "twenty-eight", "twenty-nine", "thirty", "thirty-one", "thirty-two", "thirty-three"
                      , "thirty-four", "thirty-five", "thirty-six", "thirty-seven", "thirty-eight",
                      "thirty-nine", "forty", "forty-one", "forty-two", "forty-three", "forty-four",
                      "forty-five", "forty-six", "forty-seven", "forty-eight", "forty-nine", "fifty","fifty-one"
                      , "fifty-two", "fifty-three", "fifty-four", "fifty-five", "fifty-six", "fifty-seven",
                      "fifty-eight", "fifty-nine", "sixty", "sixty-one", "sixty-two", "sixty-three","sixty-four",
                      "sixty-five", "sixty-six", "sixty-seven", "sixty-eight", "sixty-nine", "seventy","seventy-one"
                      , "seventy-two", "seventy-three", "seventy-four", "seventy-five", "seventy-six", "seventy-seven",
                      "seventy-eight", "seventy-nine", "eighty", "eighty-one", "eighty-two", "eighty-three","eighty-four",
                      "eighty-five", "eighty-six", "eighty-seven", "eighty-eight", "eighty-nine", "ninety","ninety-one",
                      "ninety-two", "ninety-three", "ninety-four", "ninety-five", "ninety-six", "ninety-seven",
                      "ninety-eight", "ninety-nine", "hundred"]
        dyn_map = {"zero": 0 ,  "one": 1 , "two": 2, "three":3, "four": 4, "five":5, "six":6
                    ,"seven" : 7, "eight":8, "nine":9 , "ten":10, "eleven":11, "twelve":12,
                    "thirteen" : 13 , "fourteen":14 , "fifteen":15, "sixteen":16,  "seventeen":17, 
                    "eighteen": 18, "nineteen": 19, "twenty": 20,"twenty-one": 21,"twenty-two": 22,
                   "twenty-three": 23,"twenty-four": 24, "twenty-five": 25, "twenty-six": 26, "twenty-seven": 27,
                   "twenty-eight": 28, "twenty-nine": 29, "thirty": 30, "thirty-one": 31,"thirty-two": 32,
                   "thirty-three": 33,"thirty-four": 34,"thirty-five": 35,"thirty-six": 36,"thirty-seven": 37,
                   "thirty-eight": 38,"thirty-nine": 39,"forty": 40,"forty-one": 41,"forty-two": 42,"forty-three": 43,
                   "forty-four": 44,"forty-five": 45,"forty-six": 46,"forty-seven": 47,"forty-eight": 48,
                   "forty-nine": 49, "fifty": 50, "fifty-one": 51,"fifty-two": 52,"fifty-three": 53,"fifty-four": 54,
                   "fifty-five": 55,"fifty-six"	: 56,"fifty-seven": 57,"fifty-eight": 58,"fifty-nine": 59,
                   "sixty": 60,"sixty-one": 61, "sixty-two": 62,"sixty-three": 63,"sixty-four": 64,"sixty-five": 65,
                   "sixty-six": 66,"sixty-seven": 67,"sixty-eight": 68, "sixty-nine": 69,"seventy": 70,"seventy-one": 71,
                   "seventy-two": 72,"seventy-three": 73,"seventy-four": 74,"seventy-five": 75,"seventy-six": 76,"seventy-seven": 77,
                   "seventy-eight": 78, "seventy-nine": 79, "eighty": 80, "eighty-one": 81, "eighty-two": 82,"eighty-three": 83,
                   "eighty-four": 84,"eighty-five": 85,"eighty-six": 86,"eighty-seven": 87,"eighty-eight": 88,
                   "eighty-nine": 89,"ninety": 90,"ninety-one": 91,"ninety-two": 92,"ninety-three": 93,"ninety-four": 94,
                   "ninety-five": 95,"ninety-six": 96,"ninety-seven": 97,"ninety-eight": 98,"ninety-nine": 99,
                   "hundred": 100}
       # print(dyn_map["hundred"])
       # print(dyn_string[100])
        llist = []
        for x in nums:
            llist.append(dyn_string[x])
        llist.sort()
     #   print(llist)
        n = len(nums)
        for i in range(n):
            nums[i] = dyn_map[llist[i]]

        return nums
if __name__ == '__main__':
    nums = [1, 2, 3]
    obj = Solution()
    result = obj.nextPermutation(nums)
    print(result)
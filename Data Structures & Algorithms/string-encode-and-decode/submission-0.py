#approach for encode---> 
#1.loop through list of strs and get each string 
#2. take length of each string and take a special character and perform string concatenation.
#then join this to res we will get encode string 


##approach for decode--->(where input will be encoded string)
#1.Take a empty list and index at 0 position.
#2. perform character by character traversal (since input is a string)
#3. so at index 0 we will have integer and we will loop until we get special character this suggest then the next characters will be my output
#4.do it for all words 





class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += str(len(st)) + "@"+st
        return res




    def decode(self, s: str) -> List[str]:
        res = []
        index  = 0
        #perform character by character traversal
        while index<len(s):
            j = index # introduce new point where i---j will be word
            while s[j]!="@":  # its a special character then the next to this are words
                j+=1
            length = int(s[index:j])
            res.append(s[j+1:j+1+length])
            #next word
            index = j+1+length
        return res
        

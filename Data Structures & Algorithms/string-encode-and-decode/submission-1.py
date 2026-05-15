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
        for word in strs:
            res += str(len(word)) + "$" + word
        return res




    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!="$": #move j so that j stand at special symbol
                j+=1 
            length = int(s[i:j]) # bcoz i:j means we are getting number that tells me number of characters to take
            i = j + 1 #start index of word
            j = i + length #last index
            result.append(s[i:j])
            i=j # bcoz both started from 0 and same for next word both has to be started at same
        return result

        
        

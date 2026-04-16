class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        if endWord not in wordList:
            return 0
        queue = collections.deque()
        st = set(wordList)# to access in a constant time 
        st.add(beginWord)
        queue.append((beginWord,1))
        while queue:
            word , dist = queue.popleft()
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[0:i] + ch + word[i+1:]
                    if new_word == endWord:
                        return dist + 1
                    if new_word in st:
                        st.remove(new_word)
                        queue.append((new_word,dist+1))
        return 0
                    

        
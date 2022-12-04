#Program to sort characters by the frequency 
def frequencySort(self, s: str) -> str:
        uni = set(s)
        counter = []
        ans =''
        
        for i in uni:
            counter.append([i, s.count(i)])
            
        counter = sorted(counter, key=lambda x:x[1], reverse = True) 
        
        for i,j in counter:
            ans += i*j
            
        return ans 
        
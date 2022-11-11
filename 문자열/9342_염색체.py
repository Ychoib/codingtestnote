import re
N = int(input())

p = re.compile("[A-B]?A+F+C+[A-B]?$")
for i in range(N):
    print('Infected!' if p.match(input()) != None else 'Good')
    
        
    
    
    
    
            
        
        
# Gamblers-Ruin-Insurance-Example
*Gamblers Ruin is a statistical concept that demonstrates the fact that a gambler with finite wealth will eventually go broke against an opponent with infinite wealth, regardless of their betting system, even if there is a positive expected value on each bet.

import random
sim = 0
nruin = 0
nsims = 1000
while sim < nsims:
    sim += #winningamount    
    amount = #beginningamount    
    days = #daysuntilbroke    
    day = 0     
    while day < days:        
        day += 1        
        prob = random.random()        
        if prob > #probabilityofruin :               
            amount +=1        
        else:            
            amount -=1        
        if amount  == 0:            
            nruin += 1            
            break
print('Probability of ruin is', nruin/nsims)

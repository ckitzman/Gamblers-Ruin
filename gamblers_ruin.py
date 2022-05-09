#Gamblers Ruin is a statistical concept that demonstrates the fact that an entity with finite wealth will eventually go broke against an opponent(s) with infinite wealth, regardless of their betting system, even if there is a positive expected value on each bet.

import random sim = 0 nruin = 0 nsims = #numberofsimulations while sim < nsims: sim += 1
amount = #beginningamount
days = #days untilbroke
day = 0
while day < days:
day += 1
prob = random.random()
if prob > #probabilityofruin:
amount += #interestamount
else:
amount -= #claimammont
if amount == 0:
nruin += 1
break print('Probability of ruin is', nruin/nsims)
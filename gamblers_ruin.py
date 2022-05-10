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

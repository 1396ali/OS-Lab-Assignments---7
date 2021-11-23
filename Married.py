import random

boys = ['ali','reza','yasin','benyamin','mehrdad','sajjad','aidin','shahin']
girls = ['sara','zari','neda','homa','eli','goli','mary','mina']

res = []

for i in range(len(boys)):
    x = random.randint(0,len(boys)-1)
    y = random.randint(0,len(girls)-1)

    select_boys = boys[x]
    boys.remove(select_boys)
    
    select_girls = girls[y]
    girls.remove(select_girls)

    res.append(select_boys + " + " + select_girls)

print(res)

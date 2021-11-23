import random

boys = ['ali','reza','yasin','benyamin','mehrdad','sajjad','aidin','shahin']
girls = ['sara','zari','neda','homa','eli','goli','mary','mina']

res = []

for i in range(len(boys)):
    x = random.randint(0,len(boys)-1)
    y = random.randint(0,len(girls)-1)

    select_girls = girls[y]
    girls.remove(select_girls)
    
    select_boys = boys[x]
    boys.remove(select_boys)


    res.append(select_girls + " + " + select_boys)

print(res)

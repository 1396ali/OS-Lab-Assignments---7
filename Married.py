import random

boys = ['ali','reza','yasin','benyamin','mehrdad','sajjad','aidin','shahin']
girls = ['sara','zari','neda','homa','eli','goli','mary','mina']

res = []
i = 0

len_all = len(girls)

while i < len_all:
    x = random.randint(0,len(boys)-1)
    y = random.randint(0,len(girls)-1)

    select_boys = boys[x]
    select_girls = girls[y]

    res.append(select_boys + ' vs ' + select_girls)

    boys.remove(select_boys)
    girls.remove(select_girls)

    i += 1

for result in res:
    print(result)
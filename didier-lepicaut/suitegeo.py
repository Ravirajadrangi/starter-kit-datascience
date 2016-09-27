import matplotlib.pyplot as plt
u = 100
r = 2.5/100
n = range(11)
l = []


def f(x):
    for i in n:
        g = u*((1+r)**i)
        l.append(g)        
f(n)
print('\n')
print(l)

plt.title("suite")
plt.xlabel("i")
plt.ylabel("g")
plt.plot(l)

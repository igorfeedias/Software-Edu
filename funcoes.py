def somar (a,b):
    return a + b

def f(x):
    return x*x +1
y= f(3)
print ("O valor de y é", y)

#Funcao 1
def f(x):
    return x*x+2*x+5

def g(x):
    return x+4
y= f(5)
z= g(4)
k= int(input("Informe o valor de k:"))
x= f(g(k))
print ("o valor de f é", y)
print ("o valor de g é", z)
print ("o valor de x é", x)
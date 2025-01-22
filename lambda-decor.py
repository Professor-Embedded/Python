'''def cube(n):
    return n**3

print(cube(2))

f = lambda n:n**3
print(f(2))


l = lambda x : 'YES' if x%2 == 0 else 'NO'
print(l(10))
print(l(9))


def add(a,b):
    return a+b
    
print(add(2,4))

ans = lambda a,b: a+b
print(ans(2,4))


lst = [10, 2, 3, 4, 6]
result =list(filter(lambda x: x%2 ==0, lst))
print(result)




lst = [2,3,4,5]
result = list(map(lambda n: n*2, lst))
print(result)



from functools import reduce
lst = [2,3,4,5]

ans = reduce(lambda x,y:x+y, lst)
print(ans)



def decor(fun):
    def inner():
        result = fun()
        return result*2
    return inner

def num():
    return 5

result = decor(num)
print(result())



def decor(fun):
    def inner(n):
        result = fun(n)
        result += "How are you?"
        return result
    return inner


def hello(name):
    return "Hello" + name

ans = decor(hello("ashish"))
print(ans())

'''





















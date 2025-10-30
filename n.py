name='shiva'

print(name[2])

values=[2,4,65,7]
values.extend([4,6,8,9])
print(values)

print(min(values))
print(max(values))

values.sort()
print(values)

values[4]=47
print(values)

del values[2]
print(values)

a=10
b=a
print(id(a))
print(id(b))

print(type(a))

a=float(b)
print(type(a))

# mutable - list ,set,dict
# immutable - which cant chnage - int, string, tuple
#
def deco_fun(func):
    def swap(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return swap

@deco_fun
def sub(a,b):
    r=a-b
    return r
print(sub(2,4))


def count_up_to(n):
    count =1
    while count<=n:
        yield count
        count +=1

for num in count_up_to(10):
    print(num)

lst = [1,2,3]

it =iter(lst)

print(next(it))




for i in range(3, 20):
    for j in range (2,20):
        if i%j == 0:
            break
    if i==j:
        print(i)




a=[2,4,5,6]
b=[3,7,9,6]

list1 =[]
list2=[]

for i,j in zip(a,b):
        if i==j:
            list1.append(i)
            list2.append(j)

print(list1,list2)

l1=[2,3,5,8,7]
l2=sum(l1)
print(l2)
print(l1)
print('hello')



t1 = (1, 2, 3)
tw = 1, 2, 3
emprty_tuple = ()

not_tuple = (1) #just int 1
yes_tuple = (1,) #tuple with one element

t = (10, 20, 30, 40)
t[0] #10
t[-1] #40
t[1:3] #(20, 30)

t[0] = 100 #TypeError: 'tuple' object does not support item assignment

point = (3, 5)
x, y = point # x=3, y=5

a, b = 1, 2
a, b = b, a # a=2, b=1

#only methods: count() and index()

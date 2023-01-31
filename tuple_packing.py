# tuple packing
#x = 1, 2, 3, 4, 5
# print(x, type(x))

# tuple unpacking
#a, b, c = (1, 2, 3)
#print(a, b, c, type(a))

#def magic():
 #   return 1, 2, 3, 4

#z, x, c, v = magic()
#print(z, x, c, v)

x = 1
y = 2

magic = x, y

y, x = magic

print(x)
print(y)

a, b, *r = (1, 2, 3, 4, 5)
*a, b, r = (1, 2, 3, 4, 5)
a, *b, r = (1, 2, 3, 4, 5)
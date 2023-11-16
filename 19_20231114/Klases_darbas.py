#File open
file = open('test.txt', 'w')
file.write('Line 1\nline 2\nline 3')
file.close()


print("*"*40)
#With file open konstruktorius

with open('test.txt', 'rt') as file:
    print(file.read())

print("*"*40)

#Try file open konstruktorius
try:
    file = open('test.txt')
    a = file.read()
    print(a)
    print(type(a))
    print(a[7:12])
finally:
    file.close()




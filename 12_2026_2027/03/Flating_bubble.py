my_list=[1, 18, 7 ,48, 10, 14, 15]
n=len(my_list)

for i in range(n):
    didesnis=False
    print(my_list)
    for j in range(0, n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] =  my_list[j+1], my_list[j]
            didesnis=True
    if (didesnis==False):
        break

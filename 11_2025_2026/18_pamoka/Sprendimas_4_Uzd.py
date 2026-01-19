with open('Data.txt', 'r') as file:
    data = file.read().split("\n")

for i in range(len(data)):
    raides_eilueje = 0
    for item in data[i]:
        if item.isalpha():
            raides_eilueje+=1
    print(i+1, raides_eilueje)

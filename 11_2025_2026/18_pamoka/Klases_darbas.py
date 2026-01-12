#1
#Duotas sąrašas:
my_list = ["Daniel", "Kornėjus", "Augustas", "Maksim", "Natan", "Kajus", "dAniel", "danielius", "Austėja", "Marta", "Bernardas", "Emil"]
#Taikydami filter ir lambda funkcijas parašykite programną, kuri išrinktu tik moksleivius kurių vardai prasideda raidėmis "D", "d"

print(list(filter(lambda x: x.lower()[0] == "d", my_list)))

#2
#Duoti trys skaičių sąrašai
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

print("Original list:")
print(nums1)
print(nums2)
print(nums3)

#Raikydami map funkciją parašykite programą kuri sukurtų jnaują sąrašą, kurio elemtai būtų lygųs visų trijų sąršų elemntų sumai

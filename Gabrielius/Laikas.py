h, m, s = input("Įveskite laiką\n").split()

h=int(h)
m=int(m)
s=int(s)

print(h,m,s)

time_s=h*3600+m*60+s
print(time_s)

time_s-=5

h=time_s//3600
m=time_s%3600//60
s=time_s%60

print(h,m,s)

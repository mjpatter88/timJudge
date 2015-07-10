# acm.timus.ru
# 1785 Lost in Localization

num = int(input())

if(num >= 1 and num <= 4):
    print("few")
elif(num >= 5 and num <= 9):
    print("several")
elif(num >= 10 and num <= 19):
    print("pack")
elif(num >= 20 and num <= 49):
    print("lots")
elif(num >= 50 and num <= 99):
    print("horde")
elif(num >= 100 and num <= 249):
    print("throng")
elif(num >= 250 and num <= 499):
    print("swarm")
elif(num >= 500 and num <= 999):
    print("zounds")
elif(num >= 1000):
    print("legion")

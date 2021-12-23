var1 = 2
var2 = '''hello
this is raj
i am dying'''

for num in range(0,3):
    file = open(f"orders/file{num}.txt",'w')
    file.write(f"hello x{num}"+'\n'+str(var1)+'\n'+var2)
    file.close
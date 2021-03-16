'''
Program Animasi Console
By Nafis Handoko
'''

import os
def loadscreen(filesize,speed):
    loadtxt='|'
    loadnum=0
    while loadnum<=95:
        loadtxt+='|'*int(filesize/speed)
        loadnum+=1*(filesize/speed)
        os.system('cls')
        print('\n\n\n\t\t\t\t\t\tLOADING, PLEASE WAIT!')
        print('')
        print('\t'+loadtxt+'\n'+'\t'+loadtxt)
        print(loadnum)
        if loadnum>=100:print('COMPLETED!')
f=0
b=9
while True:
    os.system('color '+str(f)+str(b))
    loadscreen(200,20)
    f+=1
    b-=1
    if f>9 or b<0:
        f=0
        b=9


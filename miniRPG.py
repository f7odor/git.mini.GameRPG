import random
player=[1,1,1,1]
monster1=[1,1,1,1]
monster2=[1,1,1,1]
monster3=[1,1,1,1]
boss=[1,1,1,1]

def Player(stat):


    
    while stat >0:
        print()
        print("У вас осталось очков:")
        print(stat)
        print()
        
        print("Выберите куда распределить очки")
        print("HP  : 1")
        print("ATC : 2")
        print("ACC : 3")
        print("DEX : 4")
        x=int(input())
        if x==1:
            player[0]=player[0]+1
            stat=stat-1
            
        elif x==2:
            player[1]=player[1]+1
            stat=stat-1
        elif x==3:
            player[2]=player[2]+1
            stat=stat-1
        elif x==4:
            player[3]=player[3]+1
            stat=stat-1
        else:
            print("неправельный ввод")
            

    MinDMG=str(player[1]*3)
    MaxDMG=str(player[1]*4.5)
    fail=open("player.txt","w")
    reastr=('''MiDp='''+str(MinDMG)+'''
MaDp='''+str(MaxDMG)+'''
pAcc='''+str(player[2])+'''
pDex='''+str(player[3])+'''
pHP='''+str(player[0]*10))
    fail.write(reastr)
    fail.close()
    atc=player[0]
    print('''Ваш персонаж :
    DAMAGE='''+str(MinDMG)+"-"+str(MaxDMG)+'''
    ACCURACY='''+str(player[2])+'''
    EVASION='''+str(player[3])+'''
    Hit Points='''+str(player[0]*10))

def fight():
    statm=5
    stat=5
    global win
    win= False
    bossfight= False
    while bossfight!=True:
        end = False
        turn= True
        Player(stat)
        bossfight=enemy(statm)
        generation()
        mHP=MHP
        p1HP=PHP
        
        while end != True :
            
    
            if turn!= False:
                print()
                print("Ход игрока")
                input()
                if chanceP >= random.random():
                    print()
                    print("Игрок попадает и наносит урон в размере :")
                    hitP=random.uniform(minP,maxP)
                    print(hitP)
                    mHP=mHP-hitP
                    if mHP<= 0:
                        print()
                        print("Поздравляем вы выйграли ")
                        input()
                        statm=statm + 5
                        stat=5
                        win=True
                        end=True
                        
                    else :
                        print("осталось у HP монстра :")
                        print(MHP)
                        turn= False
                else:
                    print("Игроку не удалось попасть по монстру")
                    turn= False
            else :
                print()
                print("Ход монстра ")
                input()
                if chanceM >= random.random():
                    print()
                    print("Монстр попадает и наносит урон в размере :")
                    hitM=random.uniform(minM,maxM)
                    print(hitM)
                    p1HP=p1HP-hitM
                    if p1HP<=0:
                        print()
                        print("вы проиграли")
                        input()
                        win=False
                        end= True
                    else :
                        print("у вас осталось HP :")
                        print(PHP)
                        turn= True
                else:
                    print("Монстру не удалось попасть по вам")
                    turn= False
        

def generation():
    m=open("monster.txt", "r")
    
    global minM
    global maxM
    global MAcc
    global MDex
    global MHP

    global minP
    global maxP
    global PAcc
    global PDex
    global PHP

    global chanceP
    global chanceM
    
    MiDm=m.readline()
    MxDm=m.readline()
    m1Acc=m.readline()
    m1Dex=m.readline()
    m1HP=m.readline()
    minM=float(MiDm[5:])
    maxM=round(float(MxDm[5:]))
    MAcc=float(m1Acc[6:])
    MDex=float(m1Dex[6:])
    MHP=float(m1HP[5:])
    m.close()

    p=open("player.txt","r")
    MiDp=p.readline()
    MaDp=p.readline()
    pAcc=p.readline()
    pDex=p.readline()
    pHP=p.readline()
    minP=float(MiDp[5:])
    maxP=round(float(MaDp[5:]))
    PAcc=float(pAcc[5:])
    PDex=float(pDex[5:])
    PHP=float(pHP[4:])
    p.close()

    chanceP=PAcc/MDex
    chanceM=MAcc/PDex
    print("Шанс попадания игрока")
    print(chanceP)
    print("Шанс попадания монстра")
    print(chanceM)
    
def enemy(statm):
    global bossfight
    monster1=[1,1,1,1]
    monster2=[1,1,1,1]
    monster3=[1,1,1,1]
    boss=[1,1,1,1]
    monster=[]
    statm1=int(statm*0.8)
    statm2=statm
    statm3=int(statm*1.2)
    boss_stat= int(random.uniform(30,50))
    while boss_stat>0:
        x=int(random.uniform(1,5))
        if x==1:
            boss[0]=boss[0]+1
            boss_stat=boss_stat-1
        elif x==2:
            boss[1]=boss[1]+1
            boss_stat=boss_stat-1
        elif x==3:
            boss[2]=boss[2]+1
            boss_stat=boss_stat-1
        elif x==4:
            boss[3]=boss[3]+1
            boss_stat=boss_stat-1
    while statm1>0:
        x=int(random.uniform(1,5))
        if x==1:
            monster1[0]=monster1[0]+1
            statm1=statm1-1
        elif x==2:
            monster1[1]=monster1[1]+1
            statm1=statm1-1
        elif x==3:
            monster1[2]=monster1[2]+1
            statm1=statm1-1
        elif x==4:
            monster1[3]=monster1[3]+1
            statm1=statm1-1
    while statm2>0:
        x=int(random.uniform(1,5))
        if x==1:
            monster2[0]=monster2[0]+1
            statm2=statm2-1
        elif x==2:
            monster2[1]=monster2[1]+1
            statm2=statm2-1
        elif x==3:
            monster2[2]=monster2[2]+1
            statm2=statm2-1
        elif x==4:
            monster2[3]=monster2[3]+1
            statm2=statm2-1
    while statm3>0:
        x=int(random.uniform(1,5))
        if x==1:
            monster3[0]=monster3[0]+1
            statm3=statm3-1
        elif x==2:
            monster3[1]=monster3[1]+1
            statm3=statm3-1
        elif x==3:
            monster3[2]=monster3[2]+1
            statm3=statm3-1
        elif x==4:
            monster3[3]=monster3[3]+1
            statm3=statm3-1
    m1min=str(monster1[1]*3)
    m1max=str(monster1[1]*4.5)
    
    m2min=str(monster2[1]*3)
    m2max=str(monster2[1]*4.5)
    
    m3min=str(monster3[1]*3)
    m3max=str(monster3[1]*4.5)

    bossmin=str(boss[1]*3)
    bossmax=str(boss[1]*4.5)
    
    print()
    print("Выберите монстра:")
    print()
    print('''Monstr1:
    DAMAGE='''+str(m1min)+"-"+str(m1max)+'''
    ACCURACY='''+str(monster1[2])+'''
    EVASION='''+str(monster1[3])+'''
    Hit Points='''+str(monster1[0]*10))
    print()
    print('''Monstr2:
    DAMAGE='''+str(m2min)+"-"+str(m2max)+'''
    ACCURACY='''+str(monster2[2])+'''
    EVASION='''+str(monster2[3])+'''
    Hit Points='''+str(monster2[0]*10))
    print()
    print('''Monstr3:
    DAMAGE='''+str(m3min)+"-"+str(m3max)+'''
    ACCURACY='''+str(monster3[2])+'''
    EVASION='''+str(monster3[3])+'''
    Hit Points='''+str(monster3[0]*10))
    print()
    print('''BOSS:
    DAMAGE='''+str(bossmin)+"-"+str(bossmax)+'''
    ACCURACY='''+str(boss[2])+'''
    EVASION='''+str(boss[3])+'''
    Hit Points='''+str(boss[0]*10))
    m=int(input())
    if m==1:
        bossfight= False
        monster=monster1
        mmin=m1min
        mmax=m1max

    elif m==2:
        bossfight= False
        monster=monster2
        mmin=m2min
        mmax=m2max
    elif m==3:
        bossfight= False
        mmin=m3min
        mmax=m3max
        monster=monster3
    elif m==4:
        
        bossfight= True
        mmin=bossmin
        mmax=bossmax
        monster=boss

    else:
        print (" Nepravilnqj vvod")
    fail=open("monster.txt","w")
    reastr=('''MiDm='''+str(mmin)+'''
MxDm='''+str(mmax)+'''
m1Acc='''+str(monster[2])+'''
m1Dex='''+str(monster[3])+'''
m1HP='''+str(monster[0]*10))
    fail.write(reastr)
    fail.close()
    return bossfight






fight()

if win== True:
    print()
    print("Поздравляем вы прошли игру")
else:
    print()
    print("К сожалению вы проиграли")
input()

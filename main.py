# unbalanced game 승률 계산 프로그램
# import this file and use on interactive shell

player=input().split()
rule=1
rulestat={1:[2,1]}
stat={}
for i in player:
    stat[i]=[0,0,[],0]

def changerule():
    global rule, rulestat
    rule+=1
    rulestat[rule]=[2,1]
    
#ex) game(1,["지누","히도"])
def game(win,impo,weight=1):
    global player, stat, rule, rulestat
    for i in player:
        stat[i][0]+=weight
        if(i in impo):
            stat[i][1]+=win*weight
            stat[i][2].append([rule,1,win,weight])
        else:
            stat[i][1]+=(1-win)*weight
            stat[i][2].append([rule,0,win,weight])
    rulestat[rule][0]+=weight
    rulestat[rule][1]+=weight*win

def plus(name):
    global player, stat
    try:
        stat[name]
    except KeyError:
        stat[name]=[0,0,[],0]
    player.append(name)

def minus(name):
    global player
    player.pop(player.index(name))

def printresult():
    global stat, rulestat
    for i in stat:
        stat[i][3]=0
        for j in stat[i][2]:
            if(j[2]):
                stat[i][3]+=50/rulestat[j[0]][1]*rulestat[j[0]][0]*j[3]*(j[1]-0.5)*(j[2]-0.5)*4
            else:
                stat[i][3]+=50/(1-rulestat[j[0]][1]/rulestat[j[0]][0])*j[3]*(j[1]-0.5)*(j[2]-0.5)*4
    summ=0
    for i in stat:
        summ+=stat[i][3]
    summ/=len(stat)
    for i in stat:
        print(i," ",stat[i][0],"전 ",stat[i][1],"승  ",round(stat[i][3]-summ)/100,"승",sep='')

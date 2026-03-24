import random
import pandas as pd

k=0
players={'Player':['Me','Elani','Janjay','Filip','Martin'],
         'Score':[k,k,k,k,k]
         }
Player_Data=pd.DataFrame(players)
print(Player_Data)
l=0
Player_Data['values']=[l,l,l,l,l]
final=0
while True:
    z=0 
    x=0     #Find the Winner
    y=0     #4 Random number
    if Player_Data.loc[0,'Score']==-10:
        print('You lost \n you eliminated this game \n Bettel Luck next time')
        break
    elif final==1:
        print('You win this Game\nWe are so much proud of you')
        break
    you=int(input('Enter the number 1-100: '))
    Player_Data.loc[0,'values']=you
    lst=[you]
    if you<100:
        while y<Player_Data['Player'].count()-1:  
            num=random.randint(1,100);
            Player_Data.loc[y+1,'values']=num
            lst.append(num)
            y=y+1
        
        Total=(Player_Data['values'].sum())
        Part=(Player_Data['values'].count())     
        final=float((Total/Part)*0.8)
        lst.append(final)
        lst.sort()
        print(lst)

        while x<len(lst):
            if lst[x]==final:
                max=lst[x+1]-final
                min=final-lst[x-1]
                if max>min:
                    winner=lst[x-1]
                else:
                    winner=lst[x+1]    
            x=x+1
        while z<Player_Data['values'].count():
            if Player_Data.loc[z,'values']!=winner:
                Player_Data.loc[z,'Score']=Player_Data.loc[z,'Score']-1
                if Player_Data.loc[z,'Score']==-10:
                    print(f'Eliminated Player is \n{Player_Data.loc[z,'Player']}')
                    if Player_Data.loc[z,'Player']=='Me':
                        break
                    Player_Data.drop(z,axis=0,inplace=True)
                    Player_Data=Player_Data.reset_index(drop=True)
                    
                        
                    
            else:
                print(f'Winner this round {Player_Data.loc[z,'Player']} ')        
            z=z+1
        final=(Player_Data['Player'].count())    
        print(Player_Data)
        
    else:
        print('You entered out of range')        
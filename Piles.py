import random 

attempts =0 
piles ={'pile 1':10,'pile 2':10,'pile 3':10,'pile 4':10,'pile 5':10,'pile 6':10,'pile 7':10,'pile 8':10,'pile 9':10,'pile 10':10}
del_entries= []

# #####test#######
# for key in piles:
#     piles[key]-=1
#     print(piles[key])
#     if key == 'pile 1':
#         del_entries.append(key)
# for key in del_entries:
#     piles.pop(key)
# moved_coins= len(piles)
# print(piles)
# chosen_pile = f'pile {randint(1,len(piles)-1)}'
# print("randomly chosen_pile ="+str(chosen_pile))
# piles[chosen_pile]+=moved_coins  
# print(piles)
###################


empty_piles = 0 #stop when we have 9 empty piles and 1 pile with 100 coins


while empty_piles < 9:

    for key in piles:
        # At each turn you pick a coin from each pile(reduce the value of the piles by 1 for each round)
        piles[key]-=1
        print(piles)
  
    
    # and move it in a randomly selected pile
    chosen_pile = random.choice([k for k in piles])
    print(f'randomly chosen_pile ={chosen_pile}')
    piles[chosen_pile]+=len(piles) 
    print(piles)

    # delete the entries with empty value (when the pile has 0 coins)
    for key in piles:        
        if piles[key] == 0:
            empty_piles+=1
            del_entries.append(key)
            print(f'{key} is empty and number of ampty piles= {empty_piles}')

    for key in del_entries:
        piles.pop(key)
        del_entries=[] 


    attempts +=1
else:
   print(f'Game over \n the number of attempts = {attempts} \n the remining pile {piles}')
       

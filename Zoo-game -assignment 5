'''
Program     : Kids Zoo Game
Description : Has list of Animals and Hints, in order to add more animals just add more animal name and hints for the animal. Enjoy!!
Author      : Sandeep Joseph

Class: Zoo
       contains init class and guess_who_am_i(self) for naming the animals

'''


class zoo:
    def __init__(self, name):
        self.name = name
        
    def guess_who_am_i(self):
        userresponse = ''
        
        index = Animals.index(self.name)
        Hlen = len(hints[index])
        
        for r in range(0,Hlen):
            
            print(hints[index][r])
            print()
            userresponse = input('Who am I??  ')
                
            print('Your Guess',userresponse)

                    
            if userresponse.lower() == 'quit':
                print()
                print('Thank you')
                #return
                exit()
                    
            if  userresponse == self.name.lower():
                print()
                print('Congratulations! You got me in attempt : '+str(r+1)+' I am '+str(self.name))
                break
                
            else:
                print()
                print('You missed in clue ', r+1)
                if r == len(hints[index])-1:
                    print()
                    print('You missed in all '+str(r+1)+ ' attempts I am : ', self.name)
                    break
                
                    
                  
           

Animals   = ['elephant', 'tiger', 'lion', 'beer']

hints     = [
                ['I am the largest land-living mammal in the world',
                 'I have two trunks',
                 'My Name starts with e and ends with t'],
                
                ['I am the biggest cat',
                 'I come in black and white or orange and black',
                 'My Name starts with t and ends with r'],

                ['I am The king of Jungle',
                 'My color is golden yellow',
                 'My name starts with L and ends with n'],

                ['I am fat and black or brown and I love fish',
                 'I also comes in white color',
                 'My name starts with B and ends with R']
                
            ]


length = len(Animals)

for Animal in Animals:
    
    i = Animals.index(Animal)
    print()
    print('Animal Guessing Game -- Round :', i+1)
    print('-----------------------------------')
    print()
    print('I will give you three hints... Guess me who am I ??? Enter quit to Exit')
  
    Aobj = zoo(Animal)
    Aobj.guess_who_am_i()


	

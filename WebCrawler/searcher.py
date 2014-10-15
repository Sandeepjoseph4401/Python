import os
import fnmatch
import pickle
import shelve
from Weather import find_weather
from indexer import dict
from datetime import datetime

def search():
    userchoice = 'yes'
    word_ls    = []

    while(userchoice.lower() == 'yes'):
        data_list = shelve.open("file_content")
        
        
        query  =  input("\nPlease enter your search querry : ")
        query  =  query.strip(' ') 
        query  =  sorted(list(set(query.split(' '))))
        
        if ("or" in query) and ("and" not in query):
            print("\nOR Search as per user request on querry: "+str(query)+".......")
            query.remove("or")                          
            find_weather(query[0],query[1])
            time1 = datetime.now()
            for onebyone in query:
        
                word_ls.append(data_list[onebyone])
            #word_ls = list(set(word_ls))
            
            for onebyone1 in word_ls:
                    print (" Found at: ", onebyone1)
                    
            time2 = datetime.now()
            print("\nExecution Time  :"+str(time2.microsecond-time1.microsecond))


        elif(("and" in query) or (len(query) > 1)):
            print("\nAND or And/OR Search as per user request on querry: "+str(query)+".......")
            if "and" in query:      
                query.remove("and")
            if "or" in query:
                query.remove("or")
            find_weather(query[0],query[1])    
            time1 = datetime.now()    
            word_ls =  data_list[query[0]]
            
            for value1 in query[1:]:
                word_lst = data_list[value1]
                word_ls  = sorted(list(set(word_ls).intersection(word_ls)))
            for onebyone in word_ls:
                print(" Found at: ", onebyone)    
            
            time2 = datetime.now()
            print("\nExecution Time  :"+str(time2.microsecond-time1.microsecond))               

        else:
            print("\nSingle word Search as per user request on querry: "+str(query)+".......")
            time1 = datetime.now() 
            for words in data_list[query[0]]:
                print (" Found at: ", words)
            time2 = datetime.now()
            print("\nExecution Time  :"+str(time2.microsecond-time1.microsecond))

        print("\n\n************************************************************\n\n")   
        userchoice = input("\nThank you !!\n\nDo you want to perform another search(yes/no) : ")

    data_list.close()

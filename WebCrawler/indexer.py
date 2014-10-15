import shelve
import pickle
import os
import stat

'''def dict():
    Dict_Words = {}
    incerement = 0
    for item in data_list: 
        for word in item.split(' '):
            each_word = re.sub('^[^a-zA-z]*|[^a-zA-Z]*$','.', word)
            Dict_Words.setdefault(word,[]).append(incerement)
            Dict_Words[word] = list(set(Dict_Words[word]))
            Dict_Words[word].sort()
        incerement = incerement+1
'''

def dict():
    Dict_Words = {}
    incerement = 0
    shelvedata = shelve.open("file_content")
    files = ['rawdata.pickle','website.pickle']
    for file1 in files:  
        var1 = os.path.join(os.getcwd(),file1)
        file_raw = open(var1,'rb')
        content1 = pickle.load(file_raw)
        
        print(content1)
        for fpath, fcontent in content1:
            fcontent = fcontent.split(' ')
            for wordbyword in fcontent:
                #wordbyword =wordbyword.lower.rstrip("\'\"-\\,.:;!?")
                #fpath = str(fpath) + "\tModified time= " + str(mtime) + "\tSize= "+str(fsize)
                Dict_Words.setdefault(wordbyword,[]).append(fpath)
                Dict_Words[wordbyword] = list(set(Dict_Words[wordbyword]))

    for key, value in Dict_Words.items():
        shelvedata[key] = value
    file_raw.close()
    shelvedata.close()
            
                        
    

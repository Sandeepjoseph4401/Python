import os
import fnmatch
import pickle

filepath  = os.getcwd() + '/fortune1'
list1 = []
for dirpath, dirs, files in os.walk(filepath):
    for single_file in files:
        if (fnmatch.fnmatch(single_file,'*log') or fnmatch.fnmatch(single_file,'*txt')):
            dirpath1 = dirpath + "/" + single_file
            content = open(dirpath1,'r')
            content_read = content.read()
            tuple1 = (dirpath1, content_read)
            list1.append(tuple1)

var1 = os.path.join(os.getcwd(),'rawdata.pickle')
write  = open(var1,'wb')
pickle.dump(list1,write)
print("\n\n","====="*10,list1)

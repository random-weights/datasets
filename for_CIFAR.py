import numpy as np
import pickle


def unpickle(file):
    with open(file,'rb') as fh:
        dict = pickle.load(fh,encoding = "bytes")
    return dict


mydict = unpickle("test")
for key,value in mydict.items():
    print(key)


img_labels = mydict[b'fine_labels']

data = mydict[b'data']
new_dict = {'labels': img_labels,
            'img_arrays': data}

#writing new clean dictionary to new pickle
with open('test.pickle','wb') as fh:
    pickle.dump(new_dict,fh,protocol=pickle.HIGHEST_PROTOCOL)


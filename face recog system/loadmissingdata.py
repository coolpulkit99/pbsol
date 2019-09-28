import pickle
import sys
import os
import face_recognition
def loadmissinglist():
    f = open('facee.pckl', 'rb')
    obj = pickle.load(f)
    f.close()
    #check for new authorised users if any add to the list
    l=os.listdir("authorised")
    for i in l:
        if i not in obj.keys():
            known_image = face_recognition.load_image_file(str('authorised/')+str(i))
            biden_encoding = face_recognition.face_encodings(known_image)[0]
            obj[i]=biden_encoding
    newl=set(obj.keys())-set(l)
    for i in newl:
        obj.pop(i)
        
    #save the new authorised user list
    f = open('facee.pckl', 'wb')
    pickle.dump(obj, f)
    f.close()

    if(len(obj)<1):
        print("No 'Authorised Users' detected.Please add image of authorised user.")
        sys.exit(1)
    return obj 
    

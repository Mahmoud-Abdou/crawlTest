import pickle
import os.path
class file_manager:
    def __init__(self):

        return

    def read_visited(self,head,tail):
        try :
            f=open(str(head),"rb")
            mapp=pickle.load(f)
            f.close()
            return mapp[str(tail)]
        except Exception as e:
            return 0


    def write_visited(self,head,tail):
        try:
            f=open(str(head),"rb")
            mapp=pickle.load(f)
            f.close()
            f=open(str(head),"wb")
            mapp[str(tail)]=1
            pickle.dump(mapp,f)
            f.close()
            return
        except Exception as e:
            mapp={}
            f=open(str(head),"wb")
            mapp[str(tail)]=1
            pickle.dump(mapp,f)
        return



#print (file_manager.read_visited("asd","/t/a/w"))


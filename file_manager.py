import pickle
import os
import os.path
class file_manager:
    def __init__(self):
        return

    def read_visited(self,head,tail):
        #try :
        f=open(str(head),"rb")
        sz=os.path.getsize(str(head))
        if(sz>0):
            print("Sz = "+str(sz))
            print("head = "+str(head))
            mapp=pickle.load(f)
            x=mapp.get(str(tail),0)
            x+=1
            mapp[str(tail)]=x
            f.close()
            return x
        else:
            f.close()
            return 0
#        except EOFError:
#            if(tail=="https://en.wikipedia.org/wiki/Main_Page?tab=week"):
#                print("size = ")
#            return 0


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
        except EOFError:
            mapp={}
            f=open(str(head),"wb")
            mapp[str(tail)]=1
            pickle.dump(mapp,f)
            return



#print (file_manager.read_visited("asd","/t/a/w"))

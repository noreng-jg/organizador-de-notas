type_of_exceptions={}

try:
    f=open('../exceptions_lists','r')        
    type_of_exceptions['mobi']=f.readline().split(',')
    type_of_exceptions['pdf']=f.readline().split(',')

    for key in type_of_exceptions.keys():
        if '\n' in type_of_exceptions[key][-1]:
            type_of_exceptions[key][-1]=type_of_exceptions[key][-1].replace('\n','') 
    f.close()        
except IOError:
    pass

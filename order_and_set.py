from instantiation import create_instances
from make_txt import *

def order_by_title(_listofobjects):
    _innerlist=[]
    _outerdict={}
    list_of_titles=[]
    for each_object in _listofobjects:
        list_of_titles.append(each_object.title)
    no_duplicates=list(set(list_of_titles))
    for title_position_set in range(len(no_duplicates)):
        for title_position in range(len(_listofobjects)):
            if _listofobjects[title_position].title == no_duplicates[title_position_set]:
                _innerlist.append(_listofobjects[title_position])
        _outerdict[no_duplicates[title_position_set]]=_innerlist
        _innerlist=[]
    return _outerdict


def order_by_category(_dict):
    list_of_notes=[]
    list_of_highlights=[]
    for key in _dict.keys():
        for instance in _dict[key]:
            if 'Note' in instance.category:
                list_of_notes.append(instance)
            else: #it's a Highlight
                list_of_highlights.append(instance)
        _dict[key]={'Note': list_of_notes, 'Highlight':list_of_highlights}
        list_of_highlights=[]
        list_of_notes=[]
    return _dict


def print_time(_dict, _dictpast, _destiny):
    for key in _dict.keys():
        make_files(_destiny,_dictpast[key][-1])#takes the last instance
        for categorie in _dict[key]:
            if len(_dict[key][categorie]) != 0:
                category_time(_destiny,key, categorie)
            list_of_messages=[]
            for instancia in _dict[key][categorie]:
                list_of_messages.append(instancia.message)
            for message in list(set(list_of_messages)):
                write_stuff(_destiny,key,message)  
        


    

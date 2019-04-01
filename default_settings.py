#'My Clippings.txt'
# -*- coding: utf-8 -*-
from aux_functions import checkos

mynotes=''
the_lines=[]
separator='\r\n==========\r\n'
note_type={1:'Highlight', 2:'Bookmark', 3:'Note'}
lp=['destaque','marcador','nota']

#expanding portugues for tuple dictionary
for key in note_type.keys():
    note_type[key]=note_type[key],lp[key-1]

#make list with all the notes as global var 
def read(pathname):
    fileobj=open(pathname, 'r', encoding="utf-8")
    if checkos():
        note_list=fileobj.read().split(separator.replace('\r',''))
    else:
        note_list=fileobj.read().split(separator)
    return note_list


def return_lines(note_list):
    lines_list=[]   
    for note in note_list:
        #get first line of note list which is the Title in Kindle Format
        first_line=note.split('\n')[0]
        second_line=''.join(note.split('\n')[1:2])
        message=''.join(note.split('\n')[3:])
        args=[first_line, second_line, message]
        lines_list.append(args)
    
    return lines_list


from datetime_format import datetime_management
from category_format import category_management
from author_title_format import title_author_management
from default_settings import *


def general_management(note_list):
        atrributes_list=[]

        for note in return_lines(note_list)[:-1]:

                #Category substring and handling + bool bookmark
                _type=note[1].split('|')[0]
                category, temp_bool = category_management(note_type, _type)

                #Datetime substring
                dt=note[1].split('|')[-1]
                datetime_instance=datetime_management(dt)
                
                #Title and author
                title,author=title_author_management(note[0])
                
                #message
                message=note[2]

                #Getting everything together
                atrributes_list.append([title, datetime_instance, category, author, message, temp_bool])
        
        
        return atrributes_list
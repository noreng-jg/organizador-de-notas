from model_note import *
from general_format import general_management
from default_settings import the_lines

def create_instances(note_list):#instantiation logic
    instantiated_notes=[]

    for note in general_management(note_list):
        args,temp_bool=note[:-1], note[-1]
        if not temp_bool:#create an instance only if it's not a bookmark
            instantiated_notes.append(Note(*args))

    return instantiated_notes




# -*- coding: utf-8 -*-:
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from _codecs import decode
from aux_functions import title_gen_prob

def is_windows_path(_string):
    return '\\' in _string

def make_files(_destiny,obj):
    if not is_windows_path(_destiny):#linux
        _destiny+='/'+obj.title+'.txt'
    else:
        _destiny += '\\' + decode(obj.title, 'utf-8') + '.txt'

    f=open(_destiny, 'w')
    formatting=open(_destiny,'a+')
    formatting.write(obj.title+'\n')
    formatting.write('by '+ obj.author +'\n')
    formatting.write('Last time read ' + obj.datetimefield.ctime()+'\n\n')
    f.close()

def category_time(_destiny,title,_category):
    if is_windows_path(_destiny):
        _destiny += "\\" + title + '.txt'
    else:
        _destiny += "/" + title + '.txt'

    formatting=open(_destiny, 'a+')
    formatting.write('\n'+_category +'\n\n')
    formatting.close()
	
def next_actions(_destiny,_message):
    formatting = open(_destiny, 'a+')
    formatting.write('->' + _message + '\n')
    formatting.close()

def write_stuff(_destiny, title,_message):
    if is_windows_path(_destiny):
        _destiny += "\\" + title + '.txt'
        next_actions(_destiny, _message)
    else:
        _destiny += "/" + title + '.txt'
        next_actions(_destiny, _message)


from aux_functions import *
from default_settings import *
from getting_from_file import *
#Get the author names exception 
mobi_exceptions=[]
pdf_exceptions=[]

try:#some of the book titles got some bugs, because they have very difficult names that are difficult to 
#estabilish a pattern, so I've made an extra python file for me which handles those specific book titles
        fill_lists(type_of_exceptions['mobi'], type_of_exceptions['pdf'],mobi_exceptions, pdf_exceptions)

except KeyError:
       pass 

def itsapdf(_string):
    title_separator='-'
    _exception = ex_handling_name(pdf_exceptions, _string)
    if _exception:
        return clean_title_pdf(_exception,_string),_exception
        
    else:
        return _string.split(title_separator)[0], _string.split(title_separator)[1] #what is in the left,(_string.split(title_separator)[1]) #author in the right
        
def itsamobi(_string):
    #exception for a specific book I was reading...
        if ':' in _string:
            _string=_string.replace(':', '')
        if r'\u' in _string.encode('unicode-escape').decode('utf8','strict'):
            _string=title_gen_prob(_string.encode('unicode-escape').decode('utf8','strict').split('\\u')[1])
        return _string[:_string.find('(')], _string[_string.find('(')+1:_string.find(')')]

#Fill the author and title lists
def title_author_management(content):
        if content: #Sometimes there are empty notes in kindle file...
                if '(' and ')'  in content and not(count_numbers(content)>3) and ex_handling(mobi_exceptions, content):
                        return itsamobi(content)
                else:
                        return itsapdf(content)                        





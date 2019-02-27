import sys

def count_numbers(_string):
    count=0 #c way :P
    for letter in _string:
        if letter.isdigit():
            count+=1
    return count

def ex_handling(exception_list, _string):
        for item in exception_list:
                if item in _string:
                        return False
        return True 
#with the method below the above function is pratically useless...
def ex_handling_name(exception_list, _string):
        for author_name in exception_list:
                if author_name in _string:
                        return author_name
        return None 

def clean_title_pdf(author_name,_string):
        #remove trash from title
        idowntwantthis='-'
        clean_title=_string.replace(author_name, '').replace(idowntwantthis, '')
        
        # #check if there is whitespace in the beginning
        if clean_title[0].isspace():
                 return clean_title[1:]
        return clean_title

def find_2nd(string, substring):#S.O. help
   return string.find(substring, string.find(substring) + 1)

def fill_lists(_listmobi, _listpdf, lm_to_fill, lp_to_fill):
    for each in _listmobi:
        lm_to_fill.append(each)
    for each in _listpdf:
        lp_to_fill.append(each)   

def checkos():
        return sys.platform =='win32'


def remove_u(word):
    word_u = (word.encode('unicode-escape')).decode("utf-8", "strict")
        # print(True)
    if r'\u' in word_u:
        return word_u.split('\\u')[1]
    return word

def title_gen_prob(_string):
    selecting=''
    for char in _string:
        if char.isalpha() or char.isspace():
            selecting+=char
    return selecting

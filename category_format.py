def category_management(_typedictionary, _string):
    for key in _typedictionary.keys():
        for position in range(len(_typedictionary[key])):
            if _typedictionary[key][position] in _string.split('|')[0]:
                _type=_typedictionary[key][0]#Name category in english 
                if _type is 'Bookmark':
                    is_a_bookmark=True
                else:
                    is_a_bookmark=False
    return _type, is_a_bookmark



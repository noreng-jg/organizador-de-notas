from datetime import datetime
from dictionaries_portuguese import *

def datetime_management(dt):

    if not 'Added on' in dt:#Portuguese Format(it is dict time)

        dt=''.join([dt.replace(key, days_of_week[key]) for key in days_of_week.keys() if key in dt])
        dt=''.join([dt.replace(key, days_of_month[key]) for key in days_of_month.keys() if key in dt])
        if '\r' in dt:
            return datetime.strptime(dt, ' Adicionado: %A, %d de %B de %Y %H:%M:%S\r')
        else:
            return datetime.strptime(dt, ' Adicionado: %A, %d de %B de %Y %H:%M:%S')
    else:#English Format
        if '\r' in dt:
            return datetime.strptime(dt, ' Added on %A, %B %d, %Y %I:%M:%S %p\r')
        else:
            return datetime.strptime(dt, ' Added on %A, %B %d, %Y %I:%M:%S %p')   

        
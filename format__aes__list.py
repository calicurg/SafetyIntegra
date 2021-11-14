# -*- coding: cp1251 -*-

##aes__line = '''    Neutropenia	  26  (38.2%) / 64	  28  (41.8%) / 86	  32  (45.7%) / 83	  86  (42.0%) / 233
##    Anaemia	  21  (30.9%) / 57	  27  (40.3%) / 53	  22  (31.4%) / 45	  70  (34.1%) / 155
##    Thrombocytopenia	  18  (26.5%) / 44	  21  (31.3%) / 51	  17  (24.3%) / 34	  56  (27.3%) / 129
##    Leukopenia	   7  (10.3%) / 14	  14  (20.9%) / 32	   7  (10.0%) / 11	  28  (13.7%) / 57
##    Lymphopenia	   8  (11.8%) / 23	   9  (13.4%) / 17	   5   (7.1%) / 9	  22  (10.7%) / 49'''
##
##sl = aes__line.split('\n')

def Get__percent(cell):
    
    percent = cell.split('(')[1].split(')')[0]
    percent = percent.replace('.', ',')
    return percent
    
def Present__aes(aes__line):

    sl = aes__line.split('\n')    
    arr = []    
    for ls in sl:
        tsl = ls.split('\t')
        ae_sl = [Get__percent(si) for si in tsl[1:-1]]
        #ae_sl.insert(0, tsl[0])
        line = tsl[0].strip() + ' ('+ae_sl[0]+', '+ae_sl[1]+' и '+ae_sl[2]+')'
        arr.append(line)
        
    outline = ', '.join(arr) + ''' для группы Апагин 10 мг/кг, Апагин 15 мг/кг и плацебо, соответственно.'''
    
    return outline
    

def Start():
    
    aes__line = '''    Neutropenia	  26  (38.2%) / 64	  28  (41.8%) / 86	  32  (45.7%) / 83	  86  (42.0%) / 233
    Anaemia	  21  (30.9%) / 57	  27  (40.3%) / 53	  22  (31.4%) / 45	  70  (34.1%) / 155
    Thrombocytopenia	  18  (26.5%) / 44	  21  (31.3%) / 51	  17  (24.3%) / 34	  56  (27.3%) / 129
    Leukopenia	   7  (10.3%) / 14	  14  (20.9%) / 32	   7  (10.0%) / 11	  28  (13.7%) / 57
    Lymphopenia	   8  (11.8%) / 23	   9  (13.4%) / 17	   5   (7.1%) / 9	  22  (10.7%) / 49'''

    Present__aes(aes__line)        

#Start()
    

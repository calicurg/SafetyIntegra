# -*- coding: cp1251 -*-
import Template

dna = 'C:\\Il\\Apagin\\Results\\Safety\\AE__tables\\'
Accs = Template.Accs
Accs[2] = [] ## all AEs
Accs[3] = [] ## grade 1 AEs
Accs[4] = [] ## values - Ol sort
Accs[5] = [] ## AEsLI - print form

def Read__table__7_9():

    fna = dna + 'Table__7_9.txt'
    Template.fna = fna
    Template.Start()
    #Template.Head(0, 15)


def Read__table__7_8():

    #fna = dna + 'Table__7_2.txt'
    fna = dna + 'Table__7_8.txt'
    Template.fna = fna
    Template.Start()
    global rl
    rl = Template.Accs[0]
    #Template.Head(0, 15)



def float__to__str(float__value):

    lin = str(float__value)
    if '.' in lin:
        lin = lin.replace('.', ',')
        
    lin += '%'
    
    return lin
    

def AEs_LI(depth):

    Accs[5] = []
    for y in range(depth): ##10len(Accs[4])):
        sl = Accs[4][y]
        aes_sl = [float__to__str(si) for si in sl[:-1]]
        aes_sl.insert(0, sl[-1])
        line = aes_sl[0].lower() + ' (' + aes_sl[1] + ' в группе препарата Апагин 10 мг/кг, ' \
                                 + aes_sl[2] + ' в группе препарата Апагин 15 мг/кг и ' \
                                 + aes_sl[3] + ' в группе плацебо)'
        Accs[5].append(line)

    aes__line = ', '.join(Accs[5])
#    Template.Head(5, depth-1)

    print aes__line

    return aes__line
    

def value__to__float(lin_value):

    float__value = 0
    lin_value = lin_value.strip()
    if '%' in lin_value:
        lin_value = lin_value.replace('%', '')
        float__value = float(lin_value)
        #float__value = round(float__value, 2)
        
    return float__value
        

def Get__max__grade():

    Accs[4] = []    
    for y in range(len(Accs[3])):
        sl = Accs[3][y]
        #print sl #[1:]
        
######### -->> !!! splitting here will hide the grade!!!
        
        symptom = sl[0] ##.split('\t')[0]
        
######### <<-- !!! splitting here will hide the grade!!!
        
        values__li = [value__to__float(si) for si in sl[1:-1]]
        ol = values__li +[symptom]
#        print ol
        Accs[4].append(ol)

    Accs[4].sort()
    Accs[4].reverse()

#    Template.Head(4, 5)
    print 'Get__max__grade: done'

def AllGrades():

    Accs[3] = []
#    primer = 'Grade '+str(grade_inx)
    for y in range(len(Accs[2])):
        sl = Accs[2][y]
#        if primer in sl[0]:
#            print sl
        Accs[3].append(sl)
        
    print 'AllGrades : done'            
#    Template.Head(3, 10)       
    
    

def GetGrade(grade_inx):

    Accs[3] = []
    primer = 'Grade '+str(grade_inx)
    print primer
    for y in range(len(Accs[2])):
        sl = Accs[2][y]
        if primer in sl[0]:
#            print sl
            Accs[3].append(sl)
    print 'GetGrade ', grade_inx, ': done'            
#    Template.Head(3, 10)       
        

def GetPercent(fr):

    if fr == ' 0':
        percent = fr
    else:
        percent = fr.split('(')[1].split(')')[0]
    return percent

def GetPercentage(depth):

    Accs[2] = []
    for y in range(depth):
        ls = Accs[1][y]
        sl = ls.split(';')
        arr = [GetPercent(fr) for fr in sl[1:]]
        arr.insert(0, sl[0])
        Accs[2].append(arr)
                     
#    Template.Head(2, 10)       
    print 'GetPercentage: done'                    

def Get__raw__AEs():
    
    Accs[1] = []        
    for y in range(5, len(Template.Accs[0])):
        ls = Accs[0][y]
        if ls.startswith('    '):
            line = ls.replace('	  ', ';')
            line = line.strip()
            #print line
            Accs[1].append(line)
            
    #Template.Head(1, 5)
    print ': done'

def Start():

    Read__table__7_8()    
    Get__raw__AEs()
    GetPercentage(len(Accs[1]))
    GetGrade(3)
    Get__max__grade()
    AEs_LI(5)

#Start()    

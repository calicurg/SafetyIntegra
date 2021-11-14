# -*- coding: cp1251 -*-
import Template

Accs = Template.Accs
Accs[2] = []


def Read__table__7_2():
    dna = 'C:\\Il\\Apagin\\Results\\Safety\\AE__tables\\'
    fna = dna + 'Table__7_2.txt'
    #fna = dna + 'Table__7_8.txt'
    Template.fna = fna
    Template.Start()
    #Template.Head(0, 15)

    global rl
    
    rl = Template.Accs[0]

def GetSocPercentage(depth):

    for y in range(depth):
        ls = Accs[1][y]
        sl = ls.split(';')
        ol = [sl[0]]
        for x in range(1, 4):
            fr = sl[x].split('  ')[1]
            fr = fr.split(' /')[0]
            fr = fr.replace('(', '')
            fr = fr.replace(')', '')
            fr = fr.replace('.', ',')
            ol.append(fr)
            
        line = ol[0] + ' (' +ol[1] +' в группе препарата Апагин 10 мг/кг, ' \
                     +ol[2] +' в группе препарата Апагин 15 мг/кг, ' \
                     +ol[3] +' и  в группе плацебо)'
        
        Accs[2].append(line)
        print line
        
#    Template.Head(2, len(Accs[2]))
       
                    

def GetRawSocs():
    
    for y in range(5, len(Template.Accs[0])):
        ls = rl[y]
        if ls[0].isupper():
            line = ls.replace('	  ', ';')
            line = line.strip()
            #print line.strip()
            Accs[1].append(line)
            
    #Template.Head(1, 5)
    print 'GetRawSocs: done'

def Start():

    Read__table__7_2()        
    GetRawSocs()
    GetSocPercentage(7)
    
#Start()

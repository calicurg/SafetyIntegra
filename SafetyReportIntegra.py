# -*- coding: cp1251 -*-
import LightLinter as LL
import AE__grade__reader as AGR
import AETableReader     as AETR
import ae__rate__difference as ARDI
import format__aes__list as FAEL

TK = LL.TK
TKDI = LL.TKDI
Accs = AGR.Accs
Accs[6] = []

def Present__aes():

    aes__line = LL.TKDI['tx'][1].get('1.0', TK.END)
    aes__line = aes__line.encode('cp1251') 
    aes__line = aes__line.strip()
    target_line = FAEL.Present__aes(aes__line)
    target_line = target_line.decode('cp1251').encode('utf-8') 
    LL.TKDI['tx'][0].delete('1.0', TK.END)
    LL.TKDI['tx'][0].insert('1.0',    target_line) 
    

def Get__relatedeness__for__aes__list():

    aes__line = LL.TKDI['tx'][1].get()
    print aes__line

def Head():

    depth    = int(LL.TKDI['cb']['depth'].get())
    account  = int(LL.TKDI['cb']['accs'].get())
    AGR.Template.Head(account, depth)



def Get__rate__differences():

    for y in range(len(Accs[2])):
        
        sl = Accs[2][y]
        ls = '\t'.join(sl)
        ARDI.Get__differences(ls)
        


def AEs__placebo__only():

    Accs[4] = []
    for sl in AGR.Accs[2]:
        if sl[3] != ' 0' and sl[1] == ' 0' and sl[2] == ' 0' :
                Accs[4].append(sl)
                
                
    LL.TKDI['tx'][1].delete('1.0', TK.END)
    
    for sl in Accs[4]:
        #values__li = [str(si) for si in sl[:-1]]
        line = '\t'.join(sl[:-1])+'\n'
        LL.TKDI['tx'][1].insert(TK.END, line)   



def Prepare_table_7_2():

    AETR.Read__table__7_2()
    AGR.Get__raw__AEs()
    AGR.GetPercentage(len(AGR.Accs[1]))
            
    AGR.Template.Head(2, 10)
    LL.TKDI['tx'][1].delete('1.0', TK.END)

    arr = []
    for sl in Accs[2]:
        arr.append(sl)
        
#    arr.sort()
    for sl in arr:
        #values__li = [str(si) for si in sl[:-1]]
        line = '__'.join(sl[:-1])+'\n'
        LL.TKDI['tx'][1].insert(TK.END, line)    

    
    
    print 'Prepare_table_7_2: done'

def AEsLI__study__drug__only():

    Accs[5] = []
    for y in range(len(Accs[4])):
        sl = Accs[4][y]
##        aes_sl = [float__to__str(si) for si in sl[:-1]]
##        aes_sl.insert(0, sl[-1])
        line = sl[0].lower() + ' (' + sl[1] + ' в группе препарата Апагин 10 мг/кг, ' \
                                 + sl[2] + ' в группе препарата Апагин 15 мг/кг)'
        
        Accs[5].append(line)

    aes__line = ', '.join(Accs[5])
    aes__line = aes__line.decode('cp1251').encode('utf-8')
#    Template.Head(5, depth-1)

#    print aes__line
    LL.TKDI['tx'][0].delete('1.0', TK.END)
    LL.TKDI['tx'][0].insert('1.0', aes__line)

#    return aes__line

def AEs__study__drug__only():

    Accs[4] = []
    for sl in AGR.Accs[2]:
        if sl[3] == ' 0':
            if sl[1] != ' 0' and sl[2] != ' 0' :
                Accs[4].append(sl)
                
                
    LL.TKDI['tx'][1].delete('1.0', TK.END)
    
    for sl in Accs[4]:
        #values__li = [str(si) for si in sl[:-1]]
        line = '\t'.join(sl[:-1])+'\n'
        LL.TKDI['tx'][1].insert(TK.END, line)    


def Print__top__AEs():

    list_depth = int(LL.TKDI['cb']['depth'].get())
    array = AGR.Template.Head(4, list_depth)
    
    LL.TKDI['tx'][1].delete('1.0', TK.END)
    for sl in array:
        values__li = [str(si) for si in sl[:-1]]
        line = sl[-1]+'\t'+'\t'.join(values__li)+'\n'
        LL.TKDI['tx'][1].insert(TK.END, line)    
    
def AllGrades():

    AGR.AllGrades()

def GetGrade():

    grade_inx = int(TKDI['cb']['ae__grade'].get())
    AGR.GetGrade(grade_inx)

def Get_AEs_LI():
    
    AGR.Get__max__grade()
    list_depth = int(LL.TKDI['cb']['depth'].get())
    
    aes__line = AGR.AEs_LI(list_depth)
    aes__line = aes__line.decode('cp1251').encode('utf-8')

    LL.TKDI['tx'][0].delete('1.0', TK.END)
    LL.TKDI['tx'][0].insert(TK.END, aes__line)    
    

########################################################    

def Create__menu():

    LL.Create__menu()
##        TKDI['me'][0] = TK.Menu(TKDI['fr']['root'])
##    TKDI['me'][1] = TK.Menu(TKDI['me'][0])

    
    LL.TKDI['me'][1].add_command(label = 'Head', command = Head)
    LL.TKDI['me'][1].add_separator()
    LL.TKDI['me'][1].add_command(label = 'Prepare__table_7_8', command = Prepare__table_7_8)    
    LL.TKDI['me'][1].add_command(label = 'GetGrade', command = GetGrade)
    LL.TKDI['me'][1].add_command(label = 'AllGrades', command = AllGrades)    
    LL.TKDI['me'][1].add_command(label = 'Get_AEs_LI', command = Get_AEs_LI)
    LL.TKDI['me'][1].add_command(label = 'Print__top__AEs', command = Print__top__AEs)

    TKDI['me'][2] = TK.Menu(LL.TKDI['me'][0])
    LL.TKDI['me'][2].add_command(label = 'Prepare_table_7_2', command = Prepare_table_7_2)
    LL.TKDI['me'][2].add_command(label = 'AEs__study__drug__only', command = AEs__study__drug__only)
    LL.TKDI['me'][2].add_command(label = 'AEs__placebo__only', command = AEs__placebo__only)    
    LL.TKDI['me'][2].add_command(label = 'AEsLI__study__drug__only', command = AEsLI__study__drug__only)
    LL.TKDI['me'][2].add_separator()
    LL.TKDI['me'][2].add_command(label = 'Get__rate__differences', command = Get__rate__differences)

    LL.TKDI['me'][3] = TK.Menu(LL.TKDI['me'][0])
    LL.TKDI['me'][3].add_command(label = 'Prepare__table_7_9', command = Prepare__table_7_9)

    LL.TKDI['me'][4] = TK.Menu(LL.TKDI['me'][0])
    LL.TKDI['me'][4].add_command(label = 'Present__aes', command = Present__aes)

    
    TKDI['me'][0].add_cascade(label = 'Table_7_2', menu = TKDI['me'][2])
    TKDI['me'][0].add_cascade(label = 'Table_7_9', menu = TKDI['me'][3])
    TKDI['me'][0].add_cascade(label = '__AEs__', menu = TKDI['me'][4])
##
##    TKDI['fr']['root'].config(menu = TKDI['me'][0])
    
def CreateForms():

    LL.Create__root('Safety Integra')
    
    LL.Add__one__frame(0, 'root', 1, 1)
    LL.Add__one__frame(1, 'root', 2, 1)

    ######    frame 0   #####################
    
    LL.Add__cb('ae__grade', 0, 1, 1, 10, 'Arial 14')
    LL.TKDI['cb']['ae__grade']['values'] = range(1, 6)
    LL.TKDI['cb']['ae__grade'].set(1)

    LL.Add__cb('depth',     0, 2, 1, 10, 'Arial 14')
    LL.TKDI['cb']['depth']['values'] = range(1, 11)
    LL.TKDI['cb']['depth'].set(3)

    LL.Add__cb('accs',     0, 3, 1, 10, 'Arial 14')
    LL.TKDI['cb']['accs']['values'] = range(7)
    LL.TKDI['cb']['accs'].set(0)


    ######    frame 1  #####################

    LL.Add__tx(0, 1, 1, 1, 100, 15, 'white', 'blue',   'Courier 15 bold') 
    LL.Add__tx(1, 1, 2, 1, 100, 15, 'black', 'yellow', 'Courier 17 bold') 


    #########################################

    Create__menu()

def Prepare__table_7_9():

    AGR.Read__table__7_9()
    AGR.Get__raw__AEs()
    AGR.GetPercentage(len(AGR.Accs[1]))
    
    print 'Prepare__table_7_9: done'
    
def Prepare__table_7_8():

    AGR.Read__table__7_8()
    AGR.Get__raw__AEs()
    AGR.GetPercentage(len(AGR.Accs[1]))

    print 'Prepare__table_7_8: done'

def Start():
    
    CreateForms()
    
                   
    LL.TKDI['fr']['root'].mainloop()

Start()

    


    
    
    

    

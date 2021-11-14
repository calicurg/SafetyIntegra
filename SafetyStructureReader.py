import Template
import LightLinter as LL

Template.fna = 'C:\\Il\\Apagin\\Results\\Safety\\Amo__safety\\SafetyStructure__01.txt'
Template.Start()
#Template.Head(0, 3)

rl = Template.Accs[0]
Accs = Template.Accs

Accs[2] = [ [], [] ] ## paragraphs
TK = LL.TK

ParsDI = {}

def GetHeaders():

    header_inx = 0    
    for ls in rl:
        ls = ls.strip()
        if ls.startswith('15.'):
            header_inx = ls.split()[0]
            print header_inx
            #print ls
            Accs[1].append(ls)
            ParsDI[header_inx] = []
            #Accs[2].append([])
        else:
            if header_inx > 0:
                ParsDI[header_inx].append(ls)
            
           
def reflect__header(event):

    pair = LL.reflect__lx__in__entry('headers')
    inx = pair[0]
    si = pair[1]
    header_inx = si.split()[0]
    
    LL.TKDI['lx']['parphs'].delete(0, TK.END)

    parphs__li = ParsDI[header_inx] ##Accs[2][inx]
    if len(parphs__li) > 0:
        arr = [si.decode('cp1251').encode('utf-8') for si in parphs__li]
        LL.Fill__lx(arr, 'parphs')
    

def reflect__par(event):
    
    pair = LL.reflect__lx__in__entry('parphs')
    inx = pair[0]
    si = pair[1]
    LL.TKDI['tx'][0].delete('1.0', TK.END)
    LL.TKDI['tx'][0].insert(TK.END, si)
    
    
def CreateForms():

    LL.Create__root('Safety')
    LL.Add__one__frame(0, 'root', 1, 1) ### lxx
    LL.Add__one__frame(1, 'root', 2, 1) ##  txx

    LL.Add__lx('headers', 0, 1, 1, 50, 7, 'Arial 14')
    arr = [si.decode('cp1251').encode('utf-8') for si in Accs[1]]
    LL.Fill__lx(arr, 'headers')
    LL.TKDI['lx']['headers'].bind('<KeyRelease>', reflect__header)
    LL.TKDI['lx']['headers'].bind('<ButtonRelease>', reflect__header)
    
    LL.Add__lx('parphs', 0, 1, 2, 70, 7, 'Arial 14')
    LL.TKDI['lx']['parphs'].bind('<KeyRelease>', reflect__par)
    LL.TKDI['lx']['parphs'].bind('<ButtonRelease>', reflect__par)

    LL.Add__tx(0, 1, 1, 1, 120, 7, 'white', 'blue', 'Courier 16 bold')    
    
            
def Start():

    GetHeaders()
    CreateForms()
#    Template.Head(1, 3)

Start()    
    

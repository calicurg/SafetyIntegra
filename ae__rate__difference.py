#ls = 'Neutropenia	38.2%	41.8%	45.7%'

AEsDI = {}

def diff__1__vs__2(li):

    if li[1] == 0:
        diff = 0
    else:
        diff = (li[1] - li[2])/li[1]
	
    return diff

def diff__0__vs__2(li):

    if li[0] == 0:
        diff = 0
    else:
        diff = (li[0] - li[2])/li[0]
        
    return diff

def percent__to__float(perc_value):

    if perc_value[-1] == '%':
        value = perc_value[:-1]
        fl_value = float(value)
    else:
        fl_value = 0.0

    return fl_value


def Get__differences(ls):

    sl = ls.split('	')
    ae = sl[0]
    values_line = sl[1:]
##    print ae
##    print values_line

    values__li = [percent__to__float(si) for si in values_line]
    
    diff_0_2 = diff__0__vs__2(values__li)
    diff_1_2  = diff__1__vs__2(values__li)

    pair = [diff_0_2, diff_1_2]

    AEsDI[ae] = pair
    outline = ae +'__'+str(pair[0])+'__'+str(pair[1])+'__'+str(values_line[0])+'__'+str(values_line[1])+'__'+str(values_line[2])
    
    print outline
    return pair


def Start():
    
    ls = 'Neutropenia	38.2%	41.8%	45.7%'
    pair = Get__differences(ls)
#    print pair

#Start()
    

    

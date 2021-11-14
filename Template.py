
Accs = {0:[], ## raw lines of the first file
        1:[]
        }

fna = ''

def Open__rl():

    fi = open(fna, 'r')
    rl = fi.readlines()
    Accs[0] = rl
    print 'file with ', len(rl), 'lines is open'
    fi.close()



def Start():

    Open__rl()
    

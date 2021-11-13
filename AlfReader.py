fi = open('Entry__ALL_FILES.txt', 'r')
line = fi.read()
fi.close()

SentsLI = line.split('. ')
print len(SentsLI)

SE = {}
Refsi = {}
Reffrs = {}


DI = {}

DI[0] = line

Ol = []
FrOl = []




AntPoints = ['(', '[', '{']
PostPoints = [':', ';', ',', ')', ']', '}']

def WriteReffrs():

    fi = open('Reffrs.txt', 'w')
    for y in range(len(FrOl)):
        ol = FrOl[y]
        inci = ol[0]
        fr   = ol[1]

        if inci < 5:
            break

        fline = str(inci) +'\t'+fr+'\n'
        fi.write(fline)

    fi.close()
    print 'WriteReffrs: done'
    
   
def Get__frs():

    LIN = ''
    
    for seinx in SE.keys():
        astx = SE[seinx]['astx']
        wcls = ' '.join(astx) +' '
        LIN += wcls

    slfr = LIN.split('*')


    for fr in slfr:
        fr = fr.strip()
        sl = fr.split()
        if len(sl) == 1:
            continue
        
        if fr in Reffrs:
            Reffrs[fr] += 1
        else:
            Reffrs[fr] = 1
            
                
    for si, inci in Reffrs.items():
#        inci = v['inci']
        ol = [inci, si]
        FrOl.append(ol)

    FrOl.sort()
    FrOl.reverse()

    for y in range(20):
        ol = FrOl[y]
        print ol[0], ol[1]
    
    print 'Get__frs: done'        
        


def WCLAsterisks():

#    limit = 3
    limit = 2

    line = DI[0]
    
    SepsLI = []
    
    for si in Refsi.keys():
        if len(si) < limit:
            SepsLI.append(si)

    SepsLI += AntPoints
    SepsLI += PostPoints

    for seinx in SE.keys():
        ss = SE[seinx]['ss']
        astx = []
        
        for sinx in range(len(ss)):
            si = ss[sinx]
            if si in  SepsLI:
                si = '*'
                
            astx.append(si)
            
        SE[seinx]['astx'] = astx        
        
    print 'WCLAsterisks: done'
    

def RightPassage(si, steps):

    SeinxxLI = Refsi[si]['seinxx']
    SeinxxLI.sort()

    Reffrs.clear()
    if len(FrOl) > 0:
        for y in range(len(FrOl)):
            FrOl.pop(0)
            

    for pair in SeinxxLI:
        pos  = pair[0]
        seinx = pair[1]
        
        ss = SE[seinx]['ss']

        if steps == 0:
            end = len(ss)
        else:
            end = pos + steps
            if end > len(ss):
                end = len(ss)
                
        slfr = ss[pos:end]
        fr = ' '.join(slfr)
        
        #print fr
        

        if fr in Reffrs:
            Reffrs[fr] += 1
        else:
            Reffrs[fr] = 1

    for fr, inci in Reffrs.items():
        ol = [inci, fr]
        FrOl.append(ol)

    FrOl.sort()
    FrOl.reverse()

    for ol in FrOl:
        print ol


def HeadOl():

    for y in range(50):
        ol = Ol[y]
        inci = ol[0]
        if inci < 5:
            break
        
        print inci, '\t', ol[1]
    

def PrintOl():

    for ol in Ol:
        inci = ol[0]
        if inci < 5:
            break
        
        print inci, '\t', ol[1]

def FillRefsi():

    for seinx in range(len(SE)):
        ls = SE[seinx]['ls']        
        ss = ls.split()
        SE[seinx]['ss'] = ss

        for sinx in range(len(ss)):
            si = ss[sinx]
            if si in Refsi:
                Refsi[si]['inci'] += 1
                Refsi[si]['seinxx'].append([sinx, seinx])
            else:
                Refsi[si] = {'inci': 1, 'seinxx':[[sinx, seinx]]}

                
                
    for si, v in Refsi.items():
        inci = v['inci']
        ol = [inci, si]
        Ol.append(ol)

    Ol.sort()
    Ol.reverse()
    
    print 'FillRefsi: done'        

def ReplacePoints(ls):

    for point in AntPoints:
        if point in ls:
            spacer = point +' '
            ls = ls.replace(point, spacer)
            
    for point in PostPoints:
        if point in ls:
            spacer = ' '+point 
            ls = ls.replace(point, spacer)

    return ls




def FillSE():

    for seinx in range(len(SentsLI)):
        ls = SentsLI[seinx]
        SE[seinx] = {'raw':ls}
        try:
            ls = ls.lower()
            SE[seinx]['ls'] = ReplacePoints(ls)
        except:
            print ls

    print 'FillSE: done'



def Start():
    
    FillSE()
    FillRefsi()
    HeadOl()
#    WCLAsterisks()
#    Get__frs()
#    WriteReffrs()
            
Start()

class Page:
    def __init__(self, id):
        self.id = id
        self.counter = 0

def FIFO( fileName, pageref, pageframe ):
    frame = []
    pagefault = 0
    pagereplace = 0
    Fault = False
    for i in range( len( pageref ) ):
        if pageref[i] in frame:
            Fault = False
        # pagefault
        else:
            Fault = True
            pagefault = pagefault + 1
            # pagereplace
            if len( frame ) == pageframe:
                frame.pop()
                frame.insert( 0, pageref[i] )
                pagereplace = pagereplace + 1
            else:
                frame.insert( 0, pageref[i] )

        with open(fileName, 'a') as f:
            f.write( pageref[i] )
            f.write( '\t' )
            for k in range( len( frame ) ):
                f.write( frame[k] )
            if Fault == True:
                f.write( '\t' )
                f.write( 'F' )
            f.write( '\n' )

    with open(fileName, 'a') as f:
        f.write( 'Page Fault = ' )
        f.write( str(pagefault) )
        f.write( '  Page Replaces = ' )
        f.write( str(pagereplace) )
        f.write( '  Page Frames = ' )
        f.write( str(pageframe) )
        f.write( '\n\n' )

def LRU( fileName, pageref, pageframe ):
    frame = []
    pagefault = 0
    pagereplace = 0
    Fault = False
    for i in range( len( pageref ) ):
        if pageref[i] in frame:
            Fault = False
            frame.pop( frame.index( pageref[i] ) )
            frame.insert( 0, pageref[i] )
        # pagefault
        else:
            Fault = True
            pagefault = pagefault + 1
            # pagereplace
            if len( frame ) == pageframe:
                frame.pop()
                frame.insert( 0, pageref[i] )
                pagereplace = pagereplace + 1
            else:
                frame.insert( 0, pageref[i] )

        with open(fileName, 'a') as f:
            f.write( pageref[i] )
            f.write( '\t' )
            for k in range( len( frame ) ):
                f.write( frame[k] )
            if Fault == True:
                f.write( '\t' )
                f.write( 'F' )
            f.write( '\n' )

    with open(fileName, 'a') as f:
        f.write( 'Page Fault = ' )
        f.write( str(pagefault) )
        f.write( '  Page Replaces = ' )
        f.write( str(pagereplace) )
        f.write( '  Page Frames = ' )
        f.write( str(pageframe) )
        f.write( '\n\n' )

def FindPage( id,frame ):
    for i in range( len(frame) ):
        if frame[i].id == id:
            return i
    return -1

def FindLFU( frame ):
    min = len(frame) - 1
    for i in range( len(frame)-1, -1, -1 ):
        if ( frame[i].counter < frame[min].counter ):
            min = i
    return min

def LFU_LRU( fileName, pageref, pageframe ):
    frame = []
    pagefault = 0
    pagereplace = 0
    Fault = False
    for i in range( len( pageref ) ):
        index = FindPage( pageref[i],frame )
        if index != -1:
            Fault = False
            temp = frame[index]
            temp.counter = temp.counter + 1
            frame.pop( index )
            frame.insert( 0, temp )
        # pagefault
        else:
            Fault = True
            pagefault = pagefault + 1
            # pagereplace
            if len( frame ) == pageframe:
                min = FindLFU( frame )
                frame.pop(min)
                temp = Page( pageref[i] )
                temp.counter = temp.counter + 1
                frame.insert( 0, temp )
                pagereplace = pagereplace + 1
            else:
                temp = Page( pageref[i] )
                temp.counter = temp.counter + 1
                frame.insert( 0, temp )

        with open(fileName, 'a') as f:
            f.write( pageref[i] )
            f.write( '\t' )
            for k in range( len( frame ) ):
                f.write( frame[k].id )
            if Fault == True:
                f.write( '\t' )
                f.write( 'F' )
            f.write( '\n' )

    with open(fileName, 'a') as f:
        f.write( 'Page Fault = ' )
        f.write( str(pagefault) )
        f.write( '  Page Replaces = ' )
        f.write( str(pagereplace) )
        f.write( '  Page Frames = ' )
        f.write( str(pageframe) )
        f.write( '\n\n' )

def FindMFU( frame ):
    max = len(frame) - 1
    for i in range( len(frame)-1, -1, -1 ):
        if ( frame[i].counter > frame[max].counter ):
            max = i
    return max

def MFU_FIFO( fileName, pageref, pageframe ):
    frame = []
    pagefault = 0
    pagereplace = 0
    Fault = False
    for i in range( len( pageref ) ):
        index = FindPage( pageref[i],frame )
        if index != -1:
            Fault = False
            frame[index].counter = frame[index].counter + 1
        # pagefault
        else:
            Fault = True
            pagefault = pagefault + 1
            # pagereplace
            if len( frame ) == pageframe:
                max = FindMFU( frame )
                frame.pop(max)
                temp = Page( pageref[i] )
                temp.counter = temp.counter + 1
                frame.insert( 0, temp )
                pagereplace = pagereplace + 1
            else:
                temp = Page( pageref[i] )
                temp.counter = temp.counter + 1
                frame.insert( 0, temp )

        with open(fileName, 'a') as f:
            f.write( pageref[i] )
            f.write( '\t' )
            for k in range( len( frame ) ):
                f.write( frame[k].id )
            if Fault == True:
                f.write( '\t' )
                f.write( 'F' )
            f.write( '\n' )

    with open(fileName, 'a') as f:
        f.write( 'Page Fault = ' )
        f.write( str(pagefault) )
        f.write( '  Page Replaces = ' )
        f.write( str(pagereplace) )
        f.write( '  Page Frames = ' )
        f.write( str(pageframe) )
        f.write( '\n\n' )

def MFU_LRU( fileName, pageref, pageframe ):
    frame = []
    pagefault = 0
    pagereplace = 0
    Fault = False
    for i in range( len( pageref ) ):
        index = FindPage( pageref[i],frame )
        if index != -1:
            Fault = False
            temp = frame[index]
            temp.counter = temp.counter + 1
            frame.pop( index )
            frame.insert( 0, temp )
        # pagefault
        else:
            Fault = True
            pagefault = pagefault + 1
            # pagereplace
            if len( frame ) == pageframe:
                max = FindMFU( frame )
                frame.pop(max)
                temp = Page( pageref[i] )
                temp.counter = temp.counter + 1
                frame.insert( 0, temp )
                pagereplace = pagereplace + 1
            else:
                temp = Page( pageref[i] )
                temp.counter = temp.counter + 1
                frame.insert( 0, temp )

        with open(fileName, 'a') as f:
            f.write( pageref[i] )
            f.write( '\t' )
            for k in range( len( frame ) ):
                f.write( frame[k].id )
            if Fault == True:
                f.write( '\t' )
                f.write( 'F' )
            f.write( '\n' )

    with open(fileName, 'a') as f:
        f.write( 'Page Fault = ' )
        f.write( str(pagefault) )
        f.write( '  Page Replaces = ' )
        f.write( str(pagereplace) )
        f.write( '  Page Frames = ' )
        f.write( str(pageframe) )
        f.write( '\n' )

def Method1( name, pageref, pageframe ):
    fileName = "out_" + name
    with open(fileName, 'w') as f:
        f.write( '--------------FIFO-----------------------\n' )

    FIFO( fileName, pageref, pageframe )

def Method2( name, pageref, pageframe ):
    fileName = "out_" + name
    with open(fileName, 'w') as f:
        f.write( '--------------LRU-----------------------\n' )

    LRU( fileName, pageref, pageframe )

def Method3( name, pageref, pageframe ):
    fileName = "out_" + name
    with open(fileName, 'w') as f:
        f.write( '--------------Least Frequently Used LRU Page Replacement-----------------------\n' )

    LFU_LRU( fileName, pageref, pageframe )

def Method4( name, pageref, pageframe ):
    fileName = "out_" + name
    with open(fileName, 'w') as f:
        f.write( '--------------Most Frequently Used Page Replacement -----------------------\n' )

    MFU_FIFO( fileName, pageref, pageframe )

def Method5( name, pageref, pageframe ):
    fileName = "out_" + name
    with open(fileName, 'w') as f:
        f.write( '--------------Most Frequently Used LRU Page Replacement -----------------------\n' )

    MFU_LRU( fileName, pageref, pageframe )

def Method6( name, pageref, pageframe ):
    fileName = "out_" + name
    with open(fileName, 'w') as f:
        f.write( '--------------FIFO-----------------------\n' )

    FIFO( fileName, pageref, pageframe )

    with open(fileName, 'a') as f:
        f.write( '--------------LRU-----------------------\n' )

    LRU( fileName, pageref, int(pageframe) )

    with open(fileName, 'a') as f:
        f.write( '--------------Least Frequently Used LRU Page Replacement-----------------------\n' )

    LFU_LRU( fileName, pageref, pageframe )

    with open(fileName, 'a') as f:
        f.write( '--------------Most Frequently Used Page Replacement -----------------------\n' )

    MFU_FIFO( fileName, pageref, pageframe )

    with open(fileName, 'a') as f:
        f.write( '--------------Most Frequently Used LRU Page Replacement -----------------------\n' )

    MFU_LRU( fileName, pageref, pageframe )

if __name__ == '__main__':
    keep = True
    while keep:
        fileName = input( "請輸入檔案名稱:\n" )
        name = fileName + ".txt"
        f = None
        method = 0
        pageframe = -1
        try:
            f = open(name, 'r')
            first_line = f.readline()
            op = first_line.split()
            method = int(op[0])
            print(method)
            pageframe = int(op[1])
            print( pageframe )
            second_line = f.readline()
            pageref = second_line.strip()
            print( pageref )
        
            if ( method == 1 ):
                Method1( name, pageref, pageframe )
            elif ( method == 2 ):
                Method2( name, pageref, pageframe )
            elif ( method == 3 ):
                Method3( name, pageref, pageframe )
            elif ( method == 4 ):
                Method4( name, pageref, pageframe )
            elif ( method == 5 ):
                Method5( name, pageref, pageframe )
            elif ( method == 6 ):
                Method6( name, pageref, pageframe )

        except IOError:
            print('ERROR: can not found ' + name)
            if f:
                f.close()
        finally:
            if f:
                f.close()

        cmd = input( "繼續請輸入1\n" )
        if cmd == "1":
            keep = True

        else:
            keep = False
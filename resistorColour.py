"""

Code for Translating Resistor Values and Colours, by Steven M. Weld.
Available from https://github.com/arcweld/miscPython

Copyright 2016 Steven M. Weld.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

colourCode = {  # basic dictionary matching stripe colour with the value it represents.
	'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'gray': 8,
    'white': 9   
}
colours = {  # short cut values for single or two letter entries
    'br': 'brown',
    'r': 'red',
    'o': 'orange',
    'y': 'yellow',
    'v': 'violet',
    'w': 'white'
}

def col2num (colour): # given a colour, returns the value associated with that colour
    return colourCode[colour]
    
def col2res (a): # given a sequence of three colours, prints the resistance in ohms 
    print a
    num = [0, 0, 0]
    num[0] = colourCode[a[0]]
    num[1] = colourCode[a[1]]
    num[2] = colourCode[a[2]]
    print num, type(num[0])
    resVal = ( num[0]*10 + num[1] ) * 10 ** num[2]
    if (resVal >= 10**6):
        if (resVal % 10**6 == 0):
            print 'Resistor value is: %d ohms, or %dM' % (resVal, resVal/10**6)
        else: 
            print 'Resistor value is: %d ohms, or %d.%dM' % (resVal, resVal/10**6, (resVal % 10**6)/10**5)
    elif (resVal >= 10**3):
        if (resVal % 10**3 == 0):
            print 'Resistor value is: %d ohms, or %dK' % (resVal, resVal/1000)
        else:
            print 'Resistor value is: %d ohms, or %d.%dK' % (resVal, resVal/1000, (resVal % 1000)/100)
    else: 
        print 'Resistor value is: %d ohms' % (resVal)
        
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def num2col():
    colour = raw_input('What colour? ')
    if len(colour) < 1: 
        return 
    if len(colour) < 2:
        colour = colours[colour]
    try:
        print 'Value for %s is %d' % (colour, col2num(colour))
    except:
        print 'I do not understand the input.'

def stripes2res():
    stripes = ['','','']       
    for i in [0, 1, 2]:
        stripes[i] = raw_input("Stripe: ")
        if len(stripes[i]) < 1: 
            break 
        if len(stripes[i]) < 2: stripes[i] = colours[stripes[i]]
    print col2res(stripes), '\n'*2

#while ( True ):
#    choice = raw_input("What number? ")
#    if len(choice) < 1: break
#    print invert_dict(colourCode)[int(choice)]
#    
while ( True ):
    choice = raw_input("What would you like to do? ")
    if ( len(choice) == 0 ):
        break
    if ( choice == '1' ):
        stripes2res()
    if ( choice == '2' ):
        num2col()
    
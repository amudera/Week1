
def hanoi(n, start='peg1', destination='peg2',spare='peg3'):
    if n == 1:
        print("Move a disk from " + start + " to " + destination)
    if n> 1: 
        hanoi(n-1,start='peg1',spare='peg3',destination='peg2')
        print("Move a disk from " + start + " to " + destination)
        hanoi(n-1,spare='peg3',start='peg1',destination='peg2')

hanoi(5)
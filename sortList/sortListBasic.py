

if __name__ == '__main__':
    '''Create C list by addind A and B
        Sort new list without build in functions
    '''
    A = [1, 3, 4, 5, 6, 7, 7]
    B = [1, 2, 3, 8, 9, 5]

    C = A + B 

    moveitem = True

    while(moveitem):
        moveitem = False
        for i in range(len(C)-1):
            o1 = C[i]
            o2 = C[i+1]
            
            if o2 < o1:
                C[i] = o2
                C[i+1] = o1
                moveitem = True
    print(C)
            

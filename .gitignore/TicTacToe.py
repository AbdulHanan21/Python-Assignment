board = [0,1,2,3,4,5,6,7,8]
def show():
    print board[0],'|',board[1],'|',board[2]
    print '----------'
    print board[3],'|',board[4],'|',board[5]
    print '----------'
    print board[6],'|',board[7],'|',board[8]

def check():
    if board[0] == 'x' and board[1] == 'x' and board[2] == 'x' or board[0] == 'o' and board[1] == 'o' and board[2] == 'o':
        return True
    elif board[3] == 'x' and board[4] == 'x' and board[5] == 'x' or (board[3] == 'o' and board[4] == 'o' and board[5] == 'o'):
        return True
    elif board[6] == 'x' and board[7] == 'x' and board[8] == 'x' or board[6] == 'o' and board[7] == 'o' and board[8] == 'o':
        return True
    elif board[0] == 'x' and board[3] == 'x' and board[6] == 'x' or board[0] == 'o' and board[3] == 'o' and board[6] == 'o':
        return True
    elif board[1] == 'x' and board[4] == 'x' and board[7] == 'x' or board[1] == 'o' and board[4] == 'o' and board[7] == 'o':
        return True
    elif board[2] == 'x' and board[5] == 'x' and board[8] == 'x' or board[2] == 'o' and board[5] == 'o' and board[8] == 'o':
        return True
    elif board[0] == 'x' and board[4] == 'x' and board[8] == 'x' or board[0] == 'o' and board[4] == 'o' and board[8] == 'o':
        return True
    elif board[2] == 'x' and board[4] == 'x' and board[6] == 'x' or board[2] == 'o' and board[4] == 'o' and board[6] == 'o':
        return True
    else:
        return False

count = 0
activeUser = True
show()
while True:
    if count == 9:
        print 'Match is Drawn!!'
        break
    else:
        if activeUser == True:
            print 'First Person Turn:'
            input = raw_input("Enter spot:")
            input = int(input)
            count+=1
            activeUser = False
            if board[input] != 'x' and board[input] != 'o':
                board[input] = 'x'
                if check() == True:
                    show()
                    print 'Player 1 Has Won!!'
                    break
            else:
                print 'Spot is Already Taken!'
                count-=1
                while True:
                    input = raw_input('Choose Another Spot:')
                    input = int(input)
                    count+=1
                    if board[input] != 'x' and board[input] != 'o':
                        board[input] = 'x'
                        break
                    else:
                        print 'Spot is Already Taken!'
                        count-=1
            show()
        else:
            print 'Secod Person Turn:'
            input = raw_input("Enter Spot:")
            input = int(input)
            count+=1
            activeUser = True
            if board[input] != 'x' and board[input] != 'o':
                board[input] = 'o'
                if check() == True:
                    show()
                    print 'Player 2 Has Won!!'
                    break
            else:
                print 'Spot is Already Taken!'
                count-=1
                while True:
                    input = raw_input('Choose Another Spot:')
                    input = int(input)
                    count+=1
                    if board[input] != 'x' and board[input] != 'o':
                        board[input] = 'o'
                        break
                    else:
                        print 'Spot is Already Taken!'
                        count-=1
            show()

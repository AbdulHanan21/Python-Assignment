board = [0,1,2,3,4,5,6,7,8]
def show():
    print board[0],'|',board[1],'|',board[2]
    print '----------'
    print board[3],'|',board[4],'|',board[5]
    print '----------'
    print board[6],'|',board[7],'|',board[8]

#mapNumber
def m(x, y) :
    return 3*x + y

def check() :
    #check vertical and horizontal
    for x in range(3) :
        if board[m(x,0)] == board[m(x,1)] and board[m(x,1)] == board[m(x,2)] and board[m(x,0)] not in range(9) :
            return True
        if board[m(0,x)] == board[m(1,x)] and board[m(1,x)] == board[m(2,x)] and board[m(0,x)] not in range(9) :
            return True
    #check diagonals
    if board[m(0,0)] == board[m(1,1)] and board[m(1,1)] == board[m(2,2)] and board[m(0,0)] not in range(9) :
            return True
    if board[m(0,2)] == board[m(1,1)] and board[m(1,1)] == board[m(2,0)] and board[m(0,2)] not in range(9) :
            return True
    return False
        
count = 0
activeUser = True
show()
while True:
    if count == 9:
        print 'Match is Drawn!!'
        break
    else:
        if activeUser :
            print 'First Person Turn:'
            input = raw_input("Enter spot:")
            input = int(input)
            count+=1
            activeUser = False
            if board[input]  in range(9):
                board[input] = 'x'
                if check() :
                    show()
                    print 'Player 1 Has Won!!'
                    break
            else:
                print 'Spot is Already Taken!'
                count-=1
                while True:
                    input = int(raw_input('Choose Another Spot:'))
                    count+=1
                    if board[input]  in range(9):
                        board[input] = 'x'
                        break
                    else:
                        print 'Spot is Already Taken!'
                        count-=1
            show()
        else:
            print 'Secod Person Turn:'
            input = int(raw_input("Enter Spot:"))
            count+=1
            activeUser = True
            if board[input]  in range(9):
                board[input] = 'o'
                if check() :
                    show()
                    print 'Player 2 Has Won!!'
                    break
            else:
                print 'Spot is Already Taken!'
                count-=1
                while True:
                    input = int(raw_input('Choose Another Spot:'))
                    count+=1
                    if board[input] in range(9):
                        board[input] = 'o'
                        break
                    else:
                        print 'Spot is Already Taken!'
                        count-=1
            show()

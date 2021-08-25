#move_maker Jie Lyu 11/30
def move_maker(board,color):
    import copy
    result=[]
    template=copy.deepcopy(board)
    if color==1:
        for i in range(len(board)-1):
            for j in range(len(board)):
                if template[0][j]==2:
                    break
                if template[i][j]==1 and template[i+1][j]==0:
                    board[i][j]=0
                    board[i+1][j]=1
                    result.append(board)
                    board=copy.deepcopy(template)
                if template[i+1][j-1]==2 and j!=0 and template[i][j]==1:
                    board[i][j]=0
                    board[i+1][j-1]=1
                    result.append(board)
                    board=copy.deepcopy(template)
                if j+1<len(board) and template[i][j]==1 and template[i+1][j+1]==2:
                    board[i][j]=0
                    board[i+1][j+1]=1
                    result.append(board)
                    board=copy.deepcopy(template)
    if color==2:
        for i in range(len(board)):
            for j in range(len(board)):
                if template[len(board)-1][j]==1:
                    break
                if i>=1 and template[i][j]==2 and template[i-1][j]==0:
                    board[i][j]=0
                    board[i-1][j]=2
                    result.append(board)
                    board=copy.deepcopy(template)
                if j>=1 and i>=1 and template[i][j]==2 and template[i-1][j-1]==1:
                    board[i][j]=0
                    board[i-1][j-1]=2
                    result.append(board)
                    board=copy.deepcopy(template)
                if j+1<len(board) and i>=1 and template[i][j]==2 and template[i-1][j+1]==1:
                    board[i][j]=0
                    board[i-1][j+1]=2
                    result.append(board)
                    board=copy.deepcopy(template)
    return result
# move_chooser Jie Lyu 11/30 
def move_chooser(list_of_boards,color):
    import random
    import copy
    result=[]
    final_result=[]
    for i in range(len(list_of_boards)):       
        score=0
        opponent=0
        for j in range(len(list_of_boards[i])):
            for k in range(len(list_of_boards[i][j])):
                template=copy.deepcopy(list_of_boards[i])
                if list_of_boards[i][j][k]==color:
                        score+=1
                elif list_of_boards[i][j][k]!=color and list_of_boards[i][j][k]!=0:
                        opponent+=1
        if opponent==0:
            return list_of_boards[i]
        if color==1:
            if list_of_boards[i][len(list_of_boards[i])-1][k]==1:
                return list_of_boards[i]
            if move_maker(list_of_boards[i],2)==[]:
                list_of_boards[i]=copy.deepcopy(template)
                return list_of_boards[i]
        if color==2:
            if list_of_boards[i][0][k]==2:
                return list_of_boards[i]
            if move_maker(list_of_boards[i],1)==[]:
                list_of_boards[i]=copy.deepcopy(template)
                return list_of_boards[i]
        if score-opponent>0:
            list_of_boards[i]=copy.deepcopy(template)
            result.append(list_of_boards[i])
            final_result=list_of_boards[random.randint(0,len(result)-1)]
        elif score-opponent==0:
            list_of_boards[i]=copy.deepcopy(template)
            final_result=list_of_boards[random.randint(0,len(list_of_boards)-1)]
        else:
            list_of_boards[i]=copy.deepcopy(template)
            return list_of_boards[i]
    return final_result

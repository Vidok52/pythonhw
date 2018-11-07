import random
import copy

l0 = ["      |    a","b","c",'d',"e","f","g","h","i","j"]
l1 = ["========================================================="]
l2 = [" 1","|","*","*","*","*","*","*","*","*","*","*"]
l3 = [" 2","|","*","*","*","*","*","*","*","*","*","*"]
l4 = [" 3","|","*","*","*","*","*","*","*","*","*","*"]
l5 = [" 4","|","*","*","*","*","*","*","*","*","*","*"]
l6 = [" 5","|","*","*","*","*","*","*","*","*","*","*"]
l7 = [" 6","|","*","*","*","*","*","*","*","*","*","*"]
l8 = [" 7","|","*","*","*","*","*","*","*","*","*","*"]
l9 = [" 8","|","*","*","*","*","*","*","*","*","*","*"]
l10 = [" 9","|","*","*","*","*","*","*","*","*","*","*"]
l11 = ["10","|","*","*","*","*","*","*","*","*","*","*"]
Map = [l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11]

BattleMap = copy.deepcopy(Map)

def PrnField(arg1):
    for i in range(12):
        print(arg1[i])

def shooter():
    PrnField(BattleMap)
    checker = "Yes"
    def menu():
        print(
        """
        Welcome to the Battle Ship game:
        1. Make shot
        2. Show ship map
        3. Exit
        """ )
        answer = int(input("Please, select: "))
        return answer
       
    while checker != "No":
        answer = menu()
        status = "0"
        total = 0
        iter_ = 0
        if answer == 1:
            while status != "win":
                iter_ +=1
                shot_r = input("Row:")
                r = 0
                c = 0
                rang_e = ['a','b','c','d','e','f','g','h','i','j','1','2','3','4','5','6','7','8','9','10']
                while r != 'good':
                    for i in rang_e:
                        if shot_r == i:
                            r = "good"
                            break
                        else: r = "not good"
                    if r != 'good':
                        shot_r = input("You input wrong value, please try again:")
                shot_c = input("Column:")
                while c != 'good':
                    for i in rang_e:
                        if shot_c == i:
                            c = "good"
                            break
                        else: c = "not good"
                    if c != 'good':
                        shot_c = input("You input wrong value, please try again:")

        
                check = {"a":"2","b":"3","c":"4","d":"5","e":"6","f":"7","g":"8","h":"9","i":"10","j":"11"}

                for i in check:
                    if shot_r == i:
                        shot_r_l = check[i]
                        # print(shot_c)
                        charc = 1
                        break
                    else: charc =2
                
                if charc == 1:
                    shot_r = int(shot_r_l)
                else:
                    shot_r = int(shot_r)+1

                for i in check:
                    if shot_c == i:
                        shot_c_l = check[i]
                        # print(shot_c)
                        charc = 1
                        break
                    else: charc =2
                
                if charc == 1:
                    shot_c = int(shot_c_l)
                
                else:
                    shot_c = int(shot_c)+1
                
                while BattleMap[shot_r][shot_c] == "O" or BattleMap[shot_r][shot_c] == "X":
                    print("Dont waste bombs, this sector has already shot!")
                    shot_r = input("Please input line:")
                    shot_c = input("Please input column:")
                    
                    for i in check:
                        if shot_r == i:
                            shot_r_l = check[i]
                            charc = 1
                            break
                        else: charc =2
                
                    if charc == 1:
                        shot_r = int(shot_r_l)
                    else:
                        shot_r = int(shot_r)+1

                    for i in check:
                        if shot_c == i:
                            shot_c_l = check[i]
                            charc = 1
                            break
                        else: charc =2
                
                    if charc == 1:
                        shot_c = int(shot_c_l)
                
                    else:
                        shot_c = int(shot_c)+1
                    
     

                if Map[shot_r][shot_c] == "0":
                    print("Nice shot!")
                    BattleMap[shot_r][shot_c] = "X"
                    Map[shot_r][shot_c] = "X"
                    total += 1
                else:
                    print("You miss!")
                    BattleMap[shot_r][shot_c] = "O"
                PrnField(BattleMap)     
                if total == 20:
                    status = "win"
                else:
                    status = "Not win"
                                                       

            print("You win!")
            answer = input("Play again? Print 'Yes' if you are ready or 'No' if you want to close the game")
            while answer != "yes" or  answer != "No":
                answer = input("Play again? Print 'Yes' if you are ready or 'No' if you want to close the game")
    


        elif answer == 2:
            PrnField(Map)
        elif answer == 3:
            checker = "No"
            print("By, thanks for a game!")
        else: 
            checker = "Yes"
            print("Please, select only menu numbers!") 
    
def ShipTouching(A,B,paluba,direction,C,D):
    
    r = 0
    c = 0
    i = 1
    while i != (paluba+1):
        line = A + r
        column = B + c
        # print("Iteration:",i)
        # print("Line in cycle:",line)
        # print("Column in cycle:",column)
        # print("Paluba:",paluba)
        if line == 2 and column != 11 and column != 2:
            if Map[line][column] == "0"     or Map[line+1][column+1] == "0" \
                                            or Map[line+1][column] == "0" \
                                            or Map[line+1][column-1] == "0" \
                                            or Map[line][column+1] == "0" \
                                            or Map[line][column-1] == "0":
                                            status = "No"
                                            break
            else:
                status = "Yes"
                r += C
                c += D
                i += 1
                            
        elif line == 11 and column != 2 and column != 11:
            if Map[line][column] == "0"     or Map[line-1][column+1] == "0" \
                                            or Map[line-1][column] == "0" \
                                            or Map[line-1][column-1] == "0" \
                                            or Map[line][column+1] == "0" \
                                            or Map[line][column-1] == "0":
                                            status = "No"
                                            break
            else:
                status = "Yes"
                r += C
                c += D
                i += 1

        elif column == 2 and line != 11 and line != 2:
            if Map[line][column] == "0"     or Map[line+1][column+1] == "0" \
                                            or Map[line][column+1] == "0" \
                                            or Map[line-1][column+1] == "0" \
                                            or Map[line+1][column] == "0" \
                                            or Map[line-1][column] == "0":
                                            status = "No"
                                            break
            else:
                status = "Yes"
                r += C
                c += D
                i += 1
                            
        elif column == 11 and line != 2 and line != 11:
            if Map[line][column] == "0"     or Map[line+1][column-1] == "0" \
                                            or Map[line][column-1] == "0" \
                                            or Map[line-1][column-1] == "0" \
                                            or Map[line+1][column] == "0" \
                                            or Map[line-1][column] == "0":
                                            status = "No"
                                            break
            else:
                status = "Yes"
                r += C
                c += D
                i += 1

        elif line == 11 and column == 11:
            if Map[line][column] == "0"     or Map[line-1][column-1] == "0" \
                                            or Map[line][column-1] == "0" \
                                            or Map[line-1][column] == "0":
                                            status = "No"
                                            break
            else:
                status = "Yes"
                r += C
                c += D
                i += 1 

        elif line == 2 and column == 2:
            if Map[line][column] == "0"     or Map[line+1][column+1] == "0" \
                                            or Map[line][column+1] == "0" \
                                            or Map[line+1][column] == "0":
                                            status = "No"
                                            break
            else:
                status = "Yes"
                r += C
                c += D
                i += 1 

        elif line == 2 and column == 11:
            if Map[line][column] == "0"     or Map[line+1][column-1] == "0" \
                                            or Map[line][column-1] == "0" \
                                            or Map[line+1][column] == "0":
                                            status = "No"
                                            break
            else:
                status = "Yes"
                r += C
                c += D
                i += 1 

        elif line == 11 and column == 2:
            if Map[line][column] == "0"     or Map[line-1][column+1] == "0" \
                                            or Map[line][column+1] == "0" \
                                            or Map[line-1][column] == "0":
                                            status = "No"
                                            break
            else:
                status = "Yes"
                r += C
                c += D
                i += 1    
        else:
            if Map[line][column] == "0"     or Map[line-1][column+1] == "0" \
                                            or Map[line-1][column] == "0" \
                                            or Map[line-1][column-1] == "0" \
                                            or Map[line+1][column+1] == "0" \
                                            or Map[line+1][column] == "0" \
                                            or Map[line+1][column-1] == "0" \
                                            or Map[line][column-1] == "0" \
                                            or Map[line][column+1] == "0":
                                            status = "No"
                                            break
            else:
                status = "Yes"
                r += C
                c += D
                i += 1                                   
           
    return status


def ShipLocator(arg1):
    status = "No"    
    while status == "No":
        ship_r = random.randint(2,11)
        ship_c = random.randint(2,11)
        while Map[ship_r][ship_c] == "0":
            ship_r = random.randint(2,11)
            ship_c = random.randint(2,11)
    
        corrector = arg1
        if  ship_r <= corrector:
            line = 1
        elif ship_r >= 13 - corrector:
            line = -1
        else:
            line = 0

        if ship_c <= arg1:
            column = 1
        elif ship_c >= 13 - corrector:
            column = -1
        else:
            column = 0
    
        # print("line:",line,"column:",column)

        if line == 1 and column ==0:
            direction = 1
        elif line == -1 and column == 0:
            direction = 1
        elif line == 0 and column == 1:
            direction = 2
        elif line == 0 and column == -1:
            direction = 2
        elif line == 0 and column == 0:
            direction = random.randint(1,2)
            if direction == 1:
                line = random.choice([-1,1])
                column = 0
            else:
                column = random.choice([-1,1])
                line = 0
        else:
            cho = [line,column]
            what = random.choice(cho)
            if what == cho[0]:
                direction = 1
                line = cho[0]
                column = 0
            else:
                direction = 2
                column = cho[1]
                line = 0

            



        
        # if direction == 1:
        #     print("Ship will be built by horizontal :",direction)
        # elif direction == 2:
        #     print("Ship will be built by vertical :",direction)

        status = ShipTouching(ship_r,ship_c,arg1,direction,line,column)
         
    if direction == 1:
        Map[ship_r][ship_c] = "0"
        a = 1
        b = ship_r + line
        while a != arg1:
            Map[b][ship_c] = "0"
            b = b + line
            a += 1
    else:
        Map[ship_r][ship_c] = "0"
        a = 1
        c = ship_c + column
        while a != arg1:
            Map[ship_r][c] = "0"
            c = c + column
            a += 1

def ShipBuilder():
    ShipLocator(4)
    ShipLocator(3)
    ShipLocator(3)
    ShipLocator(2)
    ShipLocator(2)
    ShipLocator(2)
    ShipLocator(1)
    ShipLocator(1)
    ShipLocator(1)
    ShipLocator(1)
    
ShipBuilder()
# PrnField(Map)
shooter()
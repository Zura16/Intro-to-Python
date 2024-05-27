#defining basic functions that we will use in the code afterwards
def menu():
    print("Welcome to Pattern Print Shop. Please select from the following menu. ")
    print("\tA- To print a Rectangle Pattern")
    print("\tB- To print Pyramid Pattern")
    print("\tC- To print Diamond Pattern\n")
    print("\tQ- To quit")

    choice = input ()
    return choice
# Defining the rectangular shape
def rectangle():
    print("1- Solid Rectangle")
    print("2- Hollow Rectangle")
    print("0- Return to main menu")
    rec_choice = input()
    return rec_choice 
#Defining the Pyramid shape
def Pyramid():
    print("1- Half Pyramid")
    print("2- Full Pyramid")
    print("0- Return to main menu")
    pyramid_choice = input()
    return pyramid_choice

def full_pyramid():
    print("1- Full Pyramid")
    print("2- hollow full pyramid")
    print("3- hollow inverted pyramid")
    print("0- Return to main menu")
    full_pyramid_choice = input()
    return full_pyramid_choice

def half_pyramid():
    print("1- Half Pyramid")
    print("2- Inverted Half Pyramid")
    print("3- Hollow Inverted Half Pyramid")
    print("0- Return to main menu")
    half_pyramid_choice = input()
    return half_pyramid_choice

def symbol_half_pyramid():
    print("1- Symbol Half Pyramid")
    print("2- Number Half Pyramid")
    print("0- Return to main menu")
    symbol_half_pyramid = input()
    return symbol_half_pyramid

def symbol_inverted_half_pyramid():
    print("1- Symbol inverted half")
    print("2- number inverted half")
    print("0- Return to main menu")
    symbol_inverted_half_pyramid = input()
    return symbol_inverted_half_pyramid

def symbol_hollow_inverted_half_pyramid():
    print("1- Symbol hollow inverted half")
    print("2- Hollow half numbered pyramid")
    print("0- Return to main menu")
    symbol_hollow_inverted_half_pyramid = input()
    return symbol_hollow_inverted_half_pyramid
#definnig the diamond function
def diamond():
    print("1- Solid Diamond")
    print("2- Hollow Diamond")
    print("3- Half diamond")
    print("0- Return to main menu")
    diamond_choice = input()
    return diamond_choice

def valid(a,b):
    while a not in b:
        print("invalid input")
        a= input()
    return a


if __name__ == "__main__":
    for i in range(100):
        choice = menu()
        list = ("A", "B", "C", "Q")
        choice = valid(choice, list)

        if choice == "A":
            rec_choice = rectangle()
            rec_list = ("1", "2", "0")
            rec_choice = valid(rec_choice, rec_list)
            if rec_choice == '1':
                rows = int(input("Enter the number of rows: "))
                columns = int(input("Enter the number of columns: "))
                symbols = input("Enter the desired symbol: ")
                for i in range(rows):
                    for j in range(columns):
                        # Printing Pattern
                        print(symbols, end='  ')
                    print()
                    

            if rec_choice == '2':
                for q in range(1):
                    rows = int(input("Please Enter the Total Number of Rows  : "))
                    columns = int(input("Please Enter the Total Number of Columns  : "))
                    symbols = input("Enter the desired symbol: ")
                    print("Hollow Rectangle Star Pattern") 
                    for i in range(rows):
                        for j in range(columns):
                            if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
                                print(symbols, end = '  ')
                            else:
                                print(' ', end = '  ')
                        print()
                    break

            if rec_choice == "0":
                continue

        if choice == "B":
            pyramid_choice = Pyramid()
            pyramid_list = ("1", "2", "0")
            pyramid_choice = valid(pyramid_choice, pyramid_list)
            if pyramid_choice == '1':
                half_pyramid_choice = half_pyramid()
                half_pyramid_list = ("1", "2", "3", "0")
                half_pyramid_choice = valid(half_pyramid_choice, half_pyramid_list)
                if half_pyramid_choice == '1':
                    symbol_half_pyramid_choice = symbol_half_pyramid()
                    symbol_half_pyramid_list = ("1", "2", "0")
                    symbol_half_pyramid_choice = valid(symbol_half_pyramid_choice, symbol_half_pyramid_list)
                    if symbol_half_pyramid_choice == '1':
                        for i in range(1):
                            row = int(input("Enter the number of rows: "))
                            symbols = input("Enter the desired symbol: ")
                            print("")
                            for i in range(1, row + 1):
                                for j in range(1, i + 1):
                                    print(symbols, end = " ")
                                print("")
                            break 
                    if symbol_half_pyramid_choice == '2':
                        rows = int(input("Enter number of rows: "))
                        for i in range(rows):
                            for j in range(i+1):
                                print(j+1, end=" ")
                            print("\n")

                if half_pyramid_choice == '2':
                    symbol_inverted_half_pyramid_choice = symbol_inverted_half_pyramid()
                    symbol_inverted_half_pyramid_list = ("1", "2", "0")
                    symbol_inverted_half_pyramid_choice = valid(symbol_inverted_half_pyramid_choice, symbol_inverted_half_pyramid_list)
                    if symbol_inverted_half_pyramid_choice == '1':
                        for i in range(1):
                            rows = int(input("Enter number of rows: "))
                            symbols = input("Enter the desired symbol: ")
                            for i in range(rows, 0, -1):
                                for j in range(0, i):
                                    print(symbols," ", end="")    
                                print("\n")
                            break
                    if symbol_inverted_half_pyramid_choice == '2':
                        rows = int(input("Enter number of rows: "))
                        for i in range(rows, 0, -1):
                            for j in range(1, i+1):
                                print(j, end=" ")    
                            print("\n")

                if half_pyramid_choice == '3':
                    symbol_hollow_inverted_half_pyramid_choice = symbol_hollow_inverted_half_pyramid()
                    symbol_hollow_inverted_half_pyramid_list = ("1", "2", "0")
                    symbol_hollow_inverted_half_pyramid_choice = valid(symbol_hollow_inverted_half_pyramid_choice,symbol_hollow_inverted_half_pyramid_list)
                    if symbol_hollow_inverted_half_pyramid_choice == '1':
                        for i in range(1):
                            rows = int(input("Enter the number of rows: "))
                            symbols = input("Enter the desired symbol: ")
                            for i in range(rows, 0, -1):
                                if i == rows:
                                    print(rows * symbols)
                                elif 1 < i < rows:
                                        print(symbols + (i - 2) * ' ' + symbols)
                                else:
                                    print(symbols)
                    if symbol_hollow_inverted_half_pyramid_choice == '2':
                        n = int(input("Enter the number of rows: "))
                        for i in range(1, n+1):
                                for j in range(1, i+1):
                                    if(j == 1 or j == i or i == n):
                                        print(j,end=" ")
                                    else:
                                        print(" ",end=" ")
                                print()

            if pyramid_choice == '2':
                full_pyramid_choice = full_pyramid()
                full_pyramid_list = ("1", "2", "3", "0")
                full_pyramid_choice = valid(full_pyramid_choice,full_pyramid_list)
                if full_pyramid_choice == '1':
                    rows = int(input("Enter number of rows: "))
                    k = 0
                    count=0
                    count1=0
                    for i in range(1, rows+1):
                        for space in range(1, (rows-i)+1):
                            print("  ", end="")
                            count+=1   
                        while k!=((2*i)-1):
                            if count<=rows-1:
                                print(i+k, end=" ")
                                count+=1
                            else:
                                count1+=1
                                print(i+k-(2*count1), end=" ")
                            k += 1    
                        count1 = count = k = 0
                        print()
                if full_pyramid_choice == '2':
                    n = int(input("Enter the number of rows: "))
                    for i in range(1, n+1):
                        left_spaces = " " * (n-i)
                        if (i>2) and (i<n):
                            hollow_spaces = " " * (2*(i-2))
                            numbers = "1 "+ hollow_spaces + (str(i)+" ")
                            print(left_spaces+ numbers)
                        else: 
                            numbers = ""
                            for j in range(1,i+1):
                                numbers = numbers + (str(j)+ " ")
                            print(left_spaces + numbers)
                        print()   
                if full_pyramid_choice == '3':
                    n = int(input("Enter the number of lines: "))
                    for i in range(1,n+1):
                        for j in range(i,n+1):
                            if i==1:
                                print(j,end=" ")
                            elif j == i:
                                print(i,end=" ")
                            elif j == n:
                                print(n,end=" ")
                            else:
                                print(" ",end=" ")
                        print()
        if choice == "C":
            diamond_choice = diamond()
            diamond_list = ("1", "2", "3", "0")
            diamond_choice = valid(diamond_choice,diamond_list)
            if diamond_choice == '1':
                h = int(input("please enter diamond's height: "))
                symbols = input("Enter the desired symbol: ")
                for i in range(h):
                    print(" "*(h-i), symbols*(i*2+1))
                for i in range(h-2, -1, -1):
                    print(" "*(h-i), symbols*(i*2+1))
            if diamond_choice == '2':
                row = int(input('Enter number of row: '))
                symbols = input("Enter the desired symbol: ")
                for i in range(1, row+1):
                    for j in range(1,row-i+1):
                        print(" ", end="")
                    for j in range(1, 2*i):
                        if j==1 or j==2*i-1:
                            print(symbols, end="")
                        else:
                            print(" ", end="")
                    print()
                for i in range(row-1,0, -1):
                    for j in range(1,row-i+1):
                        print(" ", end="")
                    for j in range(1, 2*i):
                        if j==1 or j==2*i-1:
                            print(symbols, end="")
                        else:
                            print(" ", end="")
                    print()
            if diamond_choice == '3':
                n = int(input("Enter the number of rows: "))
                symbols = input("Enter the desired symbol: ")
                print("Pattern 1")
                for a1 in range (0,n):
                    for a2 in range (a1):
                        print(symbols, end="")
                    print()
                for a1 in range (n,0,-1):
                    for a2 in range (a1):
                        print(symbols, end="")
                    print()
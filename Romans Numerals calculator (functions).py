#Author:Maria Esteban
#Date:11/07/2022
#Purpose: convert two Roman Numerals to integers, perform an operation (+,-,*,/, ^) and give the result and remainder as an integer and as a Roman Numeral

def create_list(roman_num):
#parameter - roman_num is a string with valid Roman letters
#returns - a list with the values of the letters in order
#this function also checks for errors in the input
    my_list = []
    for i in range(len(roman_num)):
         if roman_num[i] == 'I':
          my_list.append(1)
         elif roman_num[i] == 'V':
          my_list.append(5)
         elif roman_num[i] == 'X':
          my_list.append(10)
         elif roman_num[i] == 'L':
          my_list.append(50)
         elif roman_num[i] == 'C':
          my_list.append(100)
         elif roman_num[i] == 'D':
          my_list.append(500)
         elif roman_num[i] == 'M':
          my_list.append(1000)
         else:  #if there is a letter that does not correspond to a value everything is erased from the list
          my_list=[] 
          break
    if 'IIII' in roman_num or 'VV' in roman_num or 'XXXX' in roman_num or 'LL' in roman_num or 'CCCC' in roman_num or 'DD' in roman_num or 'MMMM' in roman_num:
    #if a letter appears more times that it should everything is erased from the list as well
        my_list=[]
    return my_list

def get_value(my_list):
#parameter - my_list is a list with the values of the letters in order
#returns - value of the roman numeral
    val=0
    if len(my_list) == 1:
     my_list.append(0)
    #these if-statements evaluate the last number
    if my_list[-1] == 1:
        val += 1
    if my_list[-1] == 5 and my_list[-2] >= my_list[-1]:
        val += 5
    if my_list[-1] == 10 and my_list[-2] >= my_list[-1]:
        val += 10
    if my_list[-1] == 50 and my_list[-2] >= my_list[-1]:
        val += 50
    if my_list[-1] == 100 and my_list[-2] >= my_list[-1]:
        val += 100
    #substraction rule
    if my_list[-1] > my_list[-2]:
        val+=my_list[-1]-my_list[-2]
        my_list[-1]=0
        my_list[-2]=0
    #this evaluates the rest of the list
    for i in range(len(my_list)-1):
        if my_list[i]>= my_list[i+1]:
            val += my_list[i]
        if my_list[i] < my_list[i+1]:  
            val -= my_list[i]
    return val

def check_operator(operator):
#parameter - operator is a string 
#returns - a string with value 'right' if the operator is valid or value 'wrong' is operator is incorrect
    answer1=''
    if operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == '^':
        answer1='right'
    else:
        answer1='wrong'
    return answer1

def operations(operator, val1, val2):
#parameters - operator is a string with the operation user wants to do, val1 and val2 are integers that we got from converting the Roman Numerals
#returns - an integer result of performing the operation to val1 and val2
    digital_val = 0
    if operator == '+':
        digital_val = val1 + val2
    elif operator == '-':
        digital_val = val1 - val2
    elif operator == '*':
        digital_val = val1 * val2
    elif operator == '^':
        digital_val = val1 ** val2
    elif operator == '/':
        digital_val = val1 // val2
    return digital_val

def check_values(digital_val):
#parameter - digital val is a integer
#returns - a string saying 'right' if the integer is >0 and <4000 and 'wrong' otherwise
#this functions checks that the result of the operations is in the right interval so it can be represented in Roman numerals
    answer2=''
    if digital_val <= 0 or digital_val > 3999:
        answer2='wrong'
    else:
        answer2='right'
    return answer2

def integer_to_roman_num(value):
#parameter - value is an integer >0 and <4000
#returns - the value of the integer in Roman Numeral
    remainder = value
    M=CM=D=CD=C=L=X=V=I=XC=XL=IX=IV=0
#divides the value the maximum times it can by the maximum number it can and then goes to the next
    if value >=1000:
        M = value // 1000
        remainder = value % 1000
    if  remainder >= 900:
        CM = remainder // 900
        remainder %= 900
    if  remainder >= 500:
        D = remainder // 500
        remainder %= 500
    if  remainder >= 400:
        CD = remainder // 400
        remainder %= 400
    if  remainder >= 100:
        C = remainder // 100
        remainder %= 100
    if remainder >= 90:
        XC = remainder // 90
        remainder %= 90
    if remainder >= 50:
        L = remainder // 50
        remainder %= 50
    if remainder >= 40:
        XL = remainder // 40
        remainder %= 40
    if remainder >= 10:
        X = remainder // 10
        remainder %= 10
    if remainder >= 9:
        IX = remainder // 9
        remainder %= 9
    if remainder >= 5:
        V = remainder // 5
        remainder %= 5
    if remainder >= 4:
        IV = remainder // 4
        remainder %= 4
    if remainder >= 1:
        I = remainder // 1
        remainder %= 1
#puts the letter the times it has been divided by the value
    roman_val = ''
    for i in range(M):
        roman_val += 'M'
    for i in range(CM):
        roman_val += 'CM'
    for i in range(D):
        roman_val += 'D'
    for i in range(CD):
        roman_val += 'CD'
    for i in range(C):
        roman_val += 'C'
    for i in range(XC):
        roman_val += 'XC'
    for i in range(L):
        roman_val += 'L'
    for i in range(XL):
        roman_val += 'XL'
    for i in range(X):
        roman_val += 'X'
    for i in range(IX):
        roman_val += 'IX'
    for i in range(V):
        roman_val += 'V'
    for i in range(IV):
        roman_val += 'IV'
    for i in range(I):
        roman_val += 'I'
    return roman_val

user_response= 'Y'
while user_response == 'Y': #loop to continue or exit the program
    roman1 = input('Enter First Roman Number (no spaces): ').upper() #if the input is introduced in lower case is corrected to upper case
    list1=create_list(roman1)
    while len(list1) == 0: #if the lenght of the string if 0 is because the input entered has a problem so user needs to try another input
        print('Roman numeral not valid! Try again')
        roman1 = input('Enter First Roman Number (no spaces): ').upper()
        list1=create_list(roman1)
    val1 = get_value(create_list(roman1))
    print(f'Value of {roman1} : {val1}')
    
    roman2 = input('Enter Second Roman Number (no spaces): ').upper()
    list2=create_list(roman2)
    while len(list2) == 0:
        print('Roman numeral not valid! Try again')
        roman2 = input('Enter Second Roman Number (no spaces): ').upper()
        list2=create_list(roman2)
    val2 = get_value(create_list(roman2))
    print(f'Value of {roman2} : {val2}')

    operator = input('Operator: (+ - * / ^):')
    answer1=check_operator(operator)
    while answer1 == 'wrong': #if the operator is incorrect user is asked to introduced another operator
        print('Operator not valid! Try again.')
        operator = input('Operator: (+ - * / ^):')
        answer1=check_operator(operator)

    digital_val=operations(operator, val1, val2)
    answer2=check_values(digital_val)
    while answer2 == 'wrong': #if the result is outside the interval user is asked to introduce another operator
        print('This number cannot be represented in Roman numerals. Try other operator.')
        operator = input('Operator: (+ - * / ^):')
        answer1=check_operator(operator)
        while answer1 == 'wrong': 
                print('Operator not valid! Try again.')
                operator = input('Operator: (+ - * / ^):')
                answer1=check_operator(operator)
        digital_val=operations(operator, val1, val2)
        answer2=check_values(digital_val)
        
    roman_val=integer_to_roman_num(digital_val) #this if statements just print the digital and roman value and remainder
    if operator == '+':
        print(f'Digital sum is: {digital_val}')
        print(f'Roman sum is: {roman_val}')
    elif operator == '-':
        print(f'Digital substraction is: {digital_val}')
        print(f'Roman substraction is: {roman_val}')
    elif operator == '*':
        print(f'Digital multiplication is: {digital_val}')
        print(f'Roman multiplication is: {roman_val}')
    elif operator == '^':
        print(f'Digital result of {val1} raised to the power {val2}: {digital_val}')
        print(f'Roman result is: {digital-val}')
    elif operator == '/':
        digital_remainder= val1 % val2
        print(f'Digital quotient is: {digital_val} and the remainder is: {digital_remainder}')
        print(f'Roman quotient is: {roman_val} and the Roman remainder is: {integer_to_roman_num(digital_remainder)}')

    user_response=input('Continue (Y/N):') #asks the user if he wants to continuo or quit




#DICTONARIES FOR VARIOUS POSSIBILITIES
ones = {
    0 : 'zero ',
    1 : 'one ',
    2 : 'two ',
    3 : 'three ',
    4 : 'four ',
    5 : 'five ',
    6 : 'six ',
    7 : 'seven ',
    8 : 'eight ',
    9 : 'nine '
        }

prefix = {
    2 : 'twen',     # for -ty and -teen
    3 : 'thir',
    4 : 'four',
    5 : 'fif',
    6 : 'six',
    7 : 'seven',
    8 : 'eigh',
    9 : 'nin'
    }
    
suffix = {
    1 : 'thousand ',
    2 : 'lakh ',
    3 : 'crore '
    }


#FOR SINGLE NUMBERS
def once(num):
    return ones[num]


#FOR PAIR OF NUMBERS
def twice(n_10,n_1):
    if n_10 == 0 and n_1 == 0:
        return ""
    elif n_10 == 0:
        return once(n_1)
    elif n_10 == 1 and n_1 == 0:
        return "ten "
    elif n_10 == 1 and n_1 == 1:
        return "eleven "
    elif n_10 == 1 and n_1 == 2:
        return "twelve "
    elif n_10 == 1:
        return prefix[n_1]+"teen "
    elif n_10 == 2 and n_1 == 0:
        return prefix[n_10]+"ty "
    elif n_1 == 0:
        return prefix[n_10]+"ty "
    else:
        return prefix[n_10] + "ty " + once(n_1)
    
#IN ORDER TO MAKE A UNIFORM SYSTEM OF CONVERSION    
def convert_to_odds(num):
    numbers = ["0"]
    res = ""
    for digits in num:
        numbers.append(digits)
    for i in range(len(num)+1):
        res = res + numbers[i]
    return res
        
#MAIN PROGRAM
while True:
    try:    
        number = input('Enter number : ')
        if number == 'exit':
            break
        number = str(int(number))
        answer = ""
        l = len(number)
        if(l > 3):
            if(l%2 == 0):
                number = convert_to_odds(number)
                l = len(number)
            n = (len(number)-3)//2
            for f in range(0,(len(number)-3)//2):
                if int(number[2*f]) != 0 or int(number[2*f+1]) !=0:
                    answer = answer + twice(int(number[2*f]),int(number[2*f+1])) + suffix[n]
                    n-=1
        if l-3 < 0 or number[l-3] == 0:
            answer = answer + ""
        elif l != 1:
            if int(number[l-3]) != 0:
                answer = answer + once(int(number[l-3])) + "hundered "
        if(l == 1):
            number = convert_to_odds(number)
            l = len(number)
        answer= answer + twice(int(number[l-2]),int(number[l-1]))
        print (answer)
    except ValueError:
        print("Type only Natural numbers without spaces")
    except KeyError:
        print("Excced limits!")
    except IndexError:
        print("Type Something!")

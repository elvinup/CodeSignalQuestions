def decodeString(input):
    
    stack1 = []
    
    i = 0
    while i < len(input):
        if input[i] != ']':
            if ord(input[i]) >= 97 and ord(input[i]) <= 122:
                stack1.append(input[i])
            #Then this is a number
            else:
                print(i)
                digit = ''
                while input[i] != '[':
                    digit += input[i]
                    i += 1
                
                print(i)
                #print(digit)
                stack1.append(int(digit))
        else:
            tmp = ''
            while stack1[len(stack1)-1] != '[':
                tmp = stack1.pop() + tmp
            stack1.pop()
            mult = int(stack1.pop())
            newtmp = repeattmp(tmp, mult)
            print(newtmp)
            stack1.append(newtmp)
        
        i += 1
    output = ''
    print(stack1)
    while stack1:
        output = stack1.pop() + output
    return output
def repeattmp(string, mult):
    output = ''
    for i in range(mult):
        output += string
    return output

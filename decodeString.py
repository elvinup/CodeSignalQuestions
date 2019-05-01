def decodeString(input):
    
    stack1 = []
    
    i = 0
    while i < len(input):
        if input[i] != ']':
            if (ord(input[i]) >= 97 and ord(input[i]) <= 122) or input[i] == '[':
                stack1.append(input[i])
            #Then this is a number
            else:
                digit = ''
                while input[i] != '[':
                    digit += input[i]
                    i += 1
                stack1.append(digit)
                stack1.append(input[i])
        else:
            tmp = ''
            while stack1[len(stack1)-1] != '[':
                tmp = stack1.pop() + tmp
            stack1.pop()
            mult = int(stack1.pop())
            newtmp = repeattmp(tmp, mult)
            stack1.append(newtmp)
        
        i += 1
    output = ''
    while stack1:
        output = stack1.pop() + output
    return output

def repeattmp(string, mult):
    output = ''
    for i in range(mult):
        output += string
    return output

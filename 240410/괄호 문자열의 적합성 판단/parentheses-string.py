question = input()



def solve(question):
    arr = []
    for i in question:
        if i == '(':
            arr.append(i)

        elif i == ')':
            if len(arr) > 0:
                arr.pop()
            else:
                return "No"
        
    if len(arr) == 0:
        return "Yes"
    else:
        return "No"


print(solve(question))
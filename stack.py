class Stack:
    def __init__(self):
        self.stack = []         # list (empty)
        self.no = 0              # number of elements in the stack

    def push(self, n):
        self.stack.append(n)
        self.no += 1

    def emptylist(self):
        return self.no == 0

    def pop(self):
        if self.emptylist():
            print('Empty List')
        else:
            n = self.stack[-1]              # take the last element
            self.stack = self.stack[:-1]    # take all teh elements from the list except last one and make it new stack
            self.no -= 1
            return n


inp = input('Enter an Expression: ')
keys = inp.split()

valuestack = Stack()          #just created an empty values stack
operatorstack = Stack()           # new operators stack

for k in keys:
    if k == '(': pass         # do nothing  if token is left bracket
    elif k == ')':            # pop op from opstack, pop twice from val stack (one is right operand and one is left operand)
        right = valuestack.pop()      # do the arithmatic and push the result back to value stack
        left = valuestack.pop()
        oper = operatorstack.pop()
        if oper == '+': valuestack.push(left + right)
        if oper == '-': valuestack.push(left - right)
        if oper == '*': valuestack.push(left * right)
        if oper == '/': valuestack.push(left / right)
    elif k in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']: valuestack.push(int(k))
    elif k in ['+', '-', '*', '/']: operatorstack.push(k)
    elif k == '=': print(valuestack.pop())

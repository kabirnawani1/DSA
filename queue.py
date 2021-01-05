class Queue:
    def __init__(self):
        self.queue = []         # list (empty)
        self.no = 0              # number of elements in the queue

    def addqueue(self, n):
        self.queue.append(n)
        self.no += 1

    def emptylist(self):
        return self.no == 0

    def dequeue(self):
        if self.emptylist():
            print('Empty List')
        else:
            n = self.queue[0]              # take the last element
            self.queue = self.queue[1:]    # take all teh elements from the list except last one and make it new stack
            self.no -= 1
            return n


inp = input('Enter an Expression: ')
keys = inp.split()

valuequeue = Queue()          #just created an empty values stack
operatorqueue = Queue()           # new operators stack

for k in keys:
    if k == '(': pass         # do nothing  if token is left bracket
    elif k == ')':            # pop op from opstack, pop twice from val stack (one is right operand and one is left operand)
        right = valuequeue.dequeue()      # do the arithmatic and push the result back to value stack
        left = valuequeue.dequeue()
        oper = operatorqueue.dequeue()
        if oper == '+': valuequeue.addqueue(left + right)
        if oper == '-': valuequeue.addqueue(left - right)
        if oper == '*': valuequeue.addqueue(left * right)
        if oper == '/': valuequeue.addqueue(left / right)
    elif k in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']: valuequeue.addqueue(int(k))
    elif k in ['+', '-', '*', '/']: operatorqueue.addqueue(k)
    elif k == '=': print(valuequeue.dequeue())

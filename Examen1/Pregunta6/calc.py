import queue

class Node:
    ''' Class used to represent an evaluation tree '''
    value = ""
    value_type = 0
    left = None
    right = None

    def __init__ (self, **kwargs):
        if kwargs is not None:
            if 'val' in kwargs:
                self.value = kwargs['val']
            if 'left' in kwargs:
                self.left = kwargs['left']
            if 'right' in kwargs:
                self.right = kwargs['right']
            if 'type' in kwargs:
                self.value_type = kwargs['type']
        
class Evaluator:
    ''' Static class that contains necessary methods to evaluate and show an
        expression '''
    
    @classmethod
    def eval(cls, expr_type, expr):
        ''' Evaluation function 
            Takes an expresion and its type as input '''    
        stack = queue.LifoQueue()

        if expr_type: # Preffix notation
            for c in reversed(expr):
                if c == "+":
                    x = int(stack.get())
                    y = int(stack.get())
                    stack.put(str(x+y))
                elif c == "-":
                    x = int(stack.get())
                    y = int(stack.get())
                    stack.put(str(x-y))
                elif c == "*":
                    x = int(stack.get())
                    y = int(stack.get())
                    stack.put(str(x*y))
                elif c == "/":
                    x = int(stack.get())
                    y = int(stack.get())
                    stack.put(str(x//y))
                else:
                    stack.put(c)
        else: # Posfix notation
            for c in expr:
                if c == "+":
                    x = int(stack.get())
                    y = int(stack.get())
                    stack.put(str(x+y))
                elif c == "-":
                    x = int(stack.get())
                    y = int(stack.get())
                    stack.put(str(y-x))
                elif c == "*":
                    x = int(stack.get())
                    y = int(stack.get())
                    stack.put(str(x*y))
                elif c == "/":
                    x = int(stack.get())
                    y = int(stack.get())
                    stack.put(str(y//x))
                else:
                    stack.put(c)

        return stack.get()


    @classmethod
    def show (cls, expr_type, expr):
        ''' show function. Takes an expresion and its type. It builds an
            evaluation tree that will be used for printing the expresion '''
        
        stack = queue.LifoQueue()
        ops1 = ['+', '-']
        ops2 = ['*', '/']
        
        if expr_type: # Prefix notation
            for c in reversed(expr):
                if c in ops1:
                    x = stack.get()
                    y = stack.get()
                    new_node = Node(val = c, left = x, right = y, type = 0)
                    stack.put(new_node)
                elif c in ops2:
                    x = stack.get()
                    y = stack.get()
                    new_node = Node(val = c, left = x, right = y, type = 1)
                    stack.put(new_node)
                else:
                    new_node = Node(val = c, type = 2)
                    stack.put(new_node)
        else: # Posfix notation
            for c in expr:
                if c in ops1:
                    x = stack.get()
                    y = stack.get()
                    new_node = Node(val = c, left = y, right = x, type = 0)
                    stack.put(new_node)
                elif c in ops2:
                    x = stack.get()
                    y = stack.get()
                    new_node = Node(val = c, left = y, right = x, type = 1)
                    stack.put(new_node)
                else:
                    new_node = Node(val = c, type = 2)
                    stack.put(new_node)

        # Printing expresion
        Evaluator.print_expr(stack.get())
        print("")

    @classmethod
    def print_expr(cls, expr):
        ''' Method to transverse evaluation tree and print the expression '''
        if expr.left is None:
            print(expr.value, end=" ")
        else:
            if (expr.value_type == 1 and expr.left.value_type == 0):
                print('(', end=" ")
                Evaluator.print_expr(expr.left)
                print(')', end=" ")
            else:
                Evaluator.print_expr(expr.left)
            
            print(expr.value, end=" ")

            if (expr.value_type == 1 and expr.right.value_type < 2):
                print('(', end=" ")
                Evaluator.print_expr(expr.right)
                print(")", end=" ")
            else:
                Evaluator.print_expr(expr.right)

def loop ():
    ''' Main loop. Asking for input queries '''
    while (True):
        query = input()
        split_line = query.split(" ")

        if split_line[0] == "SALIR":
            break
        
        expr_type = (split_line[1] == "PRE")

        if split_line[0] == "EVAL":
            val = Evaluator.eval(expr_type, split_line[2:])
            print(val)
        else:
            expr = Evaluator.show(expr_type, split_line[2:])            

if __name__ == '__main__':
    loop()
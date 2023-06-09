# copyright anurag kumawat
# @anuragk16

from tkinter import messagebox

def eq_solver(eq_string = str()):
    eq_string = eq_string.replace("+"," +")
    eq_string = eq_string.replace("-"," -")
    eq_string = eq_string.replace("/"," / ")
    eq_string = eq_string.replace("*"," * ")
    eq_string.strip()
    
    lis = eq_string.split(" ")
    for i in range(0, lis.count("")):
        lis.pop(lis.index(""))
    
    for i in range(0,len(lis)):
        term = lis[i]
        if term[0] == "/" or term[0] == "*":
            pass
        else:
            if term[0] == "+" or term[0] == "-":
                pass
            else:
                lis[i] = "+"+term
    
    for l in range(0,lis.count("/")):
        try:
            if "/" in lis:
                op_index = lis.index("/")
                a = float(lis[op_index-1])
                b = float(lis[op_index+1])
                eq = a / b
                lis.pop(op_index-1)
                lis.pop(op_index-1)
                lis.pop(op_index-1)
                lis.insert(op_index-1, str(eq))
        except IndexError:
            if __name__ != "__main__":
                messagebox.showerror("Invalid equation:", "Invalid equation !!")
            return None
        except ZeroDivisionError:
            if __name__ != "__main__":
                messagebox.showerror("Division by zero", "Infinite : because you divide by zero")
            return None
        except ValueError:
            if __name__ != "__main__":
                messagebox.showerror("Check you equation", "You equation is invalid , don't use this /* or */ or alphabet")
            return None
    
    
    for l in range(0,lis.count("*")):
        try:
            if "*" in lis:
                op_index = lis.index("*")
                a = float(lis[op_index-1])
                b = float(lis[op_index+1])
                eq = a * b
                lis.pop(op_index-1)
                lis.pop(op_index-1)
                lis.pop(op_index-1)
                lis.insert(op_index-1, str(eq))
        except IndexError:
            if __name__ != "__main__":
                messagebox.showerror("Invalid equation:", "Invalid equation !!")
            return None
        except ValueError:
            if __name__ != "__main__":
                messagebox.showerror("Cheak you equation", "Your equation is invalid ,  don't use this /* or */ or alphabet")
        
            
    if len(lis) > 1:
        for i in range(0, len(lis)-1):
            lis[0] = float(lis[0]) + float(lis[1])
            lis.pop(1)
                    
    return lis[0]

    
if __name__ == "__main__":
    while True:
        a = str(input("Enter your mathmatical equation which have only : + , - , / , * :"))
        print(eq_solver(a))
        c = input("exit:")
        if c == "YES" or c == "yes" or c == "y" or c == "Y":
            break
        else:
            continue


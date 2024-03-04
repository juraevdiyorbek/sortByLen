def get_list(lst):
    new_lst = list((map(lambda x : str(x),lst)))
    new_lst.sort(key=lambda x : len(x))
    lst = list((map(lambda x : int(x),new_lst)))
    
    return lst

my_lst = list()
num = int(input("Enter the number : "))
for i in range(num):
    n = int(input(f"{i+1}-number: "))
    my_lst.append(n)
print(get_list(my_lst))

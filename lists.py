def get_list(lst):
    # avval stringga ozgartirdim listni ichidagilarni
    new_lst = list((map(lambda x : str(x),lst)))
    # keyin uzunlik boyicha sortladim
    new_lst.sort(key=lambda x : len(x))
    # ohirida yana int ga ogirib qoydim
    lst = list((map(lambda x : int(x),new_lst)))
    
    return lst
# funksiyani chaqirib uni ishlatdim
my_lst = list()
num = int(input("Enter the number : "))
for i in range(num):
    n = int(input(f"{i+1}-number: "))
    my_lst.append(n)
print(get_list(my_lst))

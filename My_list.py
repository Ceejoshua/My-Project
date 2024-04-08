My_list = []
My_list.append(10)
My_list.append(20)
My_list.append(30)
My_list.append(40)
print('My_list:', My_list)
My_list[1] = 15
print(My_list)
print('My_list:', My_list)
list = [50, 60, 70]
My_list.extend(list)
print(My_list)
print('My_list:', My_list)
My_list.remove(70)
print(My_list)
print('My_list:', My_list)
x = sorted(My_list)
print(x)
print(My_list[2])

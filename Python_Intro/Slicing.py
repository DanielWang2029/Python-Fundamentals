

# Slicing
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

#   list[start(included) : end(not included) : step]

print(None.value)

print(my_list[3:8])
print(my_list[-7:8])
print(my_list[3:-2])
print(my_list[-7:-2])

print(my_list[4:])
print(my_list[:7])

print(my_list[2:-1])
print(my_list[2:-1:1])
print(my_list[2:-1:2])
print(my_list[2:-1:-1])
print(my_list[-1:2:-1])
print(my_list[-1:2:-2])
print(my_list[-2:1:-2])
print(my_list[::-1])

url = 'www.baidu.com/zhidao'
print(url)
print(url[::-1])
print(url[-7:])
print(url[4:])
print(url[4:-7])
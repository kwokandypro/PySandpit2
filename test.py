my_list = [21, 2, 93]

def list_doubler(lst):
    doubled = []
    for num in lst:
        doubled.append(num*2)
    return doubled

az = list_doubler(my_list)

print(az)

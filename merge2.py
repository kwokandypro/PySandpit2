arr = [5, 3, 6, 2, 1, 4, 7]

results = []

if len(arr) % 2 == 1:
    while len(arr) > 0:
        ab = arr[0:int(len(arr) / 2)]
        del arr[0:int(len(arr) / 2)]
        ac = arr[0:]
        del arr[0:]

    while len(ab) > 0:
        ad = ab[0]
        del ab[0]
        ae = ab[0]
        del ab[0]
        af = ab[0]
        del ab[0]

    while len(ac) > 0:
        ag = ac[0]
        del ac[0]
        ah = ac[0]
        del ac[0]
        ai = ac[0]
        del ac[0]
        aj = ac[0]
        del ac[0]



while len(results) < 7:
    if not results:
        results.append([ad])
    else:
        for i in list(range(7)):
            if [ad] > results[i]  and ad not in  results:
                results.append(ad)
            elif [ae] > results[i]  and ae not in  results:
                results.append(ae)
            elif [af] > results[i]  and af not in  results:
                results.append(af)
            elif [aj] > results[i]  and aj not in  results:
                results.append(aj)  
            elif [ak] > results[i]  and ak not in  results:
                results.append(ak)
            elif [ah] > results[i]  and ah not in  results:
                results.append(af)
            elif [ai] > results[i]  and ai not in  results:
                results.append(af)


# print(results)
# 
# for i in list(range(3)):
#     if not results:
#         results.append(ad)
#     else:
#         print(i,results)
#         if ad > results[1]  and [ad] not in results:
#             results.append(ad)
# 
# 
# for i in list(range(5)):
#     if ad > results[0] and [ad] not in results:
#         print("pas")
#     else:
#         print("est")
# 
# import random
# 
# answer = random.randint(1,10)
# guess = ''
# while guess != answer:
#     guess = int(input('Guess a number: '))
# print('You win!')                    
# for i in list(range(3)):
#     if not results:
#         results.append(ad)
#     else:
#         print(i,results)
#         if ad > results[1]  and [ad] not in results:
#             results.append(ad)
# 

for i in list(range(5)):
    if ad > results[0] and [ad] not in results:
        print("pas")
    else:
        print("est")

import random

answer = random.randint(1,10)
guess = ''
while guess != answer:
    guess = int(input('Guess a number: '))
print('You win!')                    
for i in list(range(3)):
    if not results:
        results.append(ad)
    else:
        print(i,results)
        if ad > results[1]  and [ad] not in results:
            results.append(ad)


for i in list(range(5)):
    if ad > results[0] and [ad] not in results:
        print("pas")
    else:
        print("est")

import random

answer = random.randint(1,10)
guess = ''
while guess != answer:
    guess = int(input('Guess a number: '))
print('You win!')                    
for i in list(range(3)):
    if not results:
        results.append(ad)
    else:
        print(i,results)
        if ad > results[1]  and [ad] not in results:
            results.append(ad)

######################################





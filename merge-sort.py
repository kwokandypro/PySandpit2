#!/usr/bin/python3

# -*- coding: utf-8 -*-

# http://quiz.geeksforgeeks.org/merge-sort/


arr = [5, 3, 6, 2, 1, 4, 7]


def merge_sort(arr):
    results = []
    if len(arr) % 2 == 1:
        while len(arr) > 0:
            ab = arr[0:int(len(arr) / 2)]
            del arr[0:int(len(arr) / 2)]
            ac = arr[0:]
            del arr[0:]

        while len(ab) > 2:
            ad = ab[0:int(len(ab) / 2)]
            del ab[0:int(len(ab) / 2)]
            ae = ab[0:int(len(ab) / 2)]
            del ab[0:int(len(ab) / 2)]

        while len(ac) > 2:
            ah = ac[0:int(len(ac) / 2)]
            del ab[0:int(len(ac) / 2)]
            ai = ac[0:int(len(ac) / 2)]
            del ac[0:int(len(ac) / 2)]

        af = ab[0:1]
        aj = ac[0:1]
        ak = ac[1:2]

        if [ad] > [ae]:
            results.extend(ad)
            # ad.pop()
        else:
            results.extend(ae)

        if [ad] > [af]:
            results.append(ad)
            # ad.pop()
        else:
            results.append(af)

        if [ad] > [ah]:
            results.append(ad)
        else:
            results.append(ah)

        if [ad] > [ai]:
            results.append(ad)
        else:
            results.append(ai)

        if [ad] > [aj]:
            results.append(ad)
        else:
            results.append(aj)

        if [ad] > [ak]:
            results.append(ad)
        else:
            results.append(ak)

    print(results)

merge_sort(arr)


# def msort(x):
#     result = []
#     if len(x) < 2:
#         return x
#     mid = int(len(x)/2)
#     y = msort(x[:mid])
#     z = msort(x[mid:])
#     while (len(y) > 0) or (len(z) > 0):
#         if len(y) > 0 and len(z) > 0:
#             if y[0] > z[0]:
#                 result.append(z[0])
#                 z.pop(0)
#             else:
#                 result.append(y[0])
#                 y.pop(0)
#         elif len(z) > 0:
#             for i in z:
#                 result.append(i)
#                 z.pop(0)
#         else:
#             for i in y:
#                 result.append(i)
#                 y.pop(0)
#     return result

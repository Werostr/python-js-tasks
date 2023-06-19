import random

n = [1, 7, 9, 5, 4, 7, 4, 3]
# [9,7,7,5,4,4,3,1]
# [9,7,4,4,3,1,-5,-7]
k = 4


# n*log(n)
def córcia(n, k):
    n.sort(reverse=True)
    return n[k]


# córcia(n, k)


# k*n
def córcia2(n, k):
    for i in range(k):
        max_num = -100000
        for number in n:
            if number > max_num:
                max_num = number
        n.remove(max_num)
    return max_num


# print(córcia2(n, k))


# k*log(n)
def córcia3(n, k):
    pivot_index = random.randint(0, len(n) - 1)
    pivot = n[pivot_index]
    less = []
    more = []
    for i in range(len(n)):
        if i == pivot_index:
            continue
        if n[i] < pivot:
            less.append(n[i])
        else:
            more.append(n[i])
    print(less)
    print(more)
    if len(more) == k - 1:
        return pivot
    elif len(more) > k - 1:
        # n = more
        return córcia3(more, k)
    else:
        # n = less
        return córcia3(less, k - len(more) - 1)


print("wynik: ", córcia3(n, k))
# [1, 7, 9, 5, 4, 7, 4, 3]
# I
# pivot = 3
# less = [1]
# more = [7,9,5,4,7,4]
# [1], 3, [7,9,5,4,7,4]
# if len(more) == k-1 return pivot
# if len(more) > k-1 => n = more
# if len(more) < k-1 => n = less

# II
# pivot = 3
# less = [1]
# more = [7,9,5,4,7,4]
# [1], 3, [7,9,5,4,7,4]
# =>  n = [7,9,5,4,7,4]

# def córcia_quick_sort(n,k):

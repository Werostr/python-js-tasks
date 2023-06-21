from collections import Counter

shoes_number = int(input())
shoes_sizes = Counter(map(int, input().split()))
customers_number = int(input())

earned = 0

for i in range(customers_number):
    size, price = map(int, input().split())
    print(size)
    print(price)

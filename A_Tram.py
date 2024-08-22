# number of stations
n = int(input())
# keeping track of maximum passengers at any given time
max_passengers = 0
# how many passengers are right now in the tram
cur_passengers = 0
# input n stations a and b values
# a - no of ppl exit
# b - no of ppl entry
for _ in range(n):
    lst = list(map(int, input().rstrip().split()))
    a = lst[0]
    b = lst[1]
    # update the current passengers
    cur_passengers = cur_passengers - a + b
    # check if this value is greater than max passengers
    if cur_passengers > max_passengers:
        max_passengers = cur_passengers

print(max_passengers)

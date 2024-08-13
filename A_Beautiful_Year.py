year = input()
year_int = int(year)
year_int += 1
year = str(year_int)
lst = [i for i in year]

while len(set(lst)) != 4:
    year_int += 1
    year = str(year_int)
    lst = [i for i in year]

print(year)

st = input()
lower_count = 0
upper_count = 0

for i in st:
    if i.islower():
        lower_count += 1
    else:
        upper_count += 1

if lower_count >= upper_count:
    print(st.lower())

else:
    print(st.upper())
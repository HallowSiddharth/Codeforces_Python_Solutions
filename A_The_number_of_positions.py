"""
Already submitted, writing documentation
Logic:
1. Find out minimum position from a. This means Petyr's position can't be lesser than this.
2. Find out minimum position from b, Petyr's position can also not be lesser than this.
3. Find out maximum of those 2, since Petyr can have more in front of him, but can't have more from back of him.
4. This will give you Petyr's starting position.
5. n - this position will give you number of other positions Petyr can occupy.
6. add one to this, to include initial position and print it out .
"""


n, a, b = list(map(int, input().rstrip().split()))
min_pos_from_a = a + 1
min_pos_from_b = n - b
starting_pos = max(min_pos_from_a, min_pos_from_b)
print(n - starting_pos + 1)

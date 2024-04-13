n=int(input())
st=input()
st2=input()
answer_sum=0
for i in range(n):
    j=int(st[i])
    j1=int(st2[i])
    answer_sum+=min(abs(j-j1),9-(abs(j-j1))+1)
print(answer_sum)
n=int(input())
st=input()
st2='xxx'
ct=0
while st2 in st:
    ct+=st.count(st2)
    st2+='x'
    
print(ct)
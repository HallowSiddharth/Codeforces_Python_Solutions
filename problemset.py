# t=int(input())
# for i in range(t):
#     n=int(input())
#     lst=list(map(int,input().rstrip().split()))
#     lst2=list(lst)
#     lst2.sort()
#     max=lst2[-1]
#     if len(lst2)>1:
#         smax=lst2[-2]
#     else:
#         smax=max
#     for i in lst:
#         if i==max:
#             print(i-smax,end=" ")
#         else:
#             print(i-max,end=" ")
#     print()

#1722C - Word Game
#Correct Implementation, Time limit Exceeded
# t=int(input())
# for i in range(t):
#     n=int(input())
#     lst1=list(map(str,input().rstrip().split()))
#     lst2=list(map(str,input().rstrip().split()))
#     lst3=list(map(str,input().rstrip().split()))
#     d={1:[],2:[],3:[]}
#     c2={23:[],12:[],13:[]}
#     #c3=[]
#     for i in lst1:
#         d[1].append(i)
#     for i in lst2:
#         if i in d[1]:
#             d[1].remove(i)
#             c2[12].append(i)
#         else:
#             d[2].append(i)
#     for i in lst3:
#         if i in c2[12]:
#             c2[12].remove(i)
#             #c3.append(i)
#         elif i in d[1]:
#             d[1].remove(i)
#             c2[13].append(i)
#         elif i in d[2]:
#             d[2].remove(i)
#             c2[23].append(i)
#         else:
#             d[3].append(i)
#     pts={1:(len(d[1])*3)+(len(c2[12])*1)+(len(c2[13])*1),
#     2:(len(d[2])*3)+(len(c2[12])*1)+(len(c2[23])*1),
#     3:(len(d[3])*3)+(len(c2[13])*1)+(len(c2[23])*1)}
#     print(pts[1],pts[2],pts[3])
    

    
# t=int(input())
# for i in range(t):
#     n=int(input())
#     st=input()
#     found=False
#     if "R" not in st or "L" not in st:
#         print(-1)
#         found=True
#     for i in range(len(st)):
#         if i+1!= len(st) and (st[i]=="L" and st[i+1]=="R"):
#             print(i+1)
#             found=True
#             break
#     if found==False:
#         print(0)


# n=int(input())
# st=input()
# da=["0" for i in range(10)]

# for i in st:
#     if i=='L':
#         for j in range(len(da)):
#             if da[j]=='0':
#                 da[j]='1'
#                 break
#     elif i=='R':
#         for j in range(len(da)-1,-1,-1):
#             if da[j]=='0':
#                 da[j]='1' 
#                 break       
#     else:
#         da[int(i)]='0'
#     #print(da)
# print(''.join(da))

        
# t=int(input())
# for i in range(t):
#     n=int(input())
#     s=0
#     lst=list(map(int,input().rstrip().split()))
#     if len(set(lst))==1:
#         print("NO")
#     else:
#         print("YES")
#         for i in lst:
#             if i==s:
#                 lst.remove(i)
#                 lst.append(i)
#             else:
#                 s+=i
#         st=""
#         for i in lst:
#             st+=f"{i} "
#         print(st)

# st=input()
# print(st+st[-1::-1])

# t=int(input())
# for i in range(t):
#     n=int(input())
#     lst=list(map(int,input().rstrip().split()))
#     lst.sort()
#     l1=[lst[2*i] for i in range((len(lst)//2))]
#     l2=[lst[2*i+1] for i in range((len(lst)//2))]
#     m1=l1[len(l1)//2]
#     m2=l2[len(l2)//2]
#     print(abs(m1-m2))

# t=int(input())
# for i in range(t):
#     n=int(input())
#     print("9"*(n-1)+"8"*n)

# n,k=[int(i) for i in input().rstrip().split()]
# t=240
# t=t-k
# s=0
# for i in range(1,n+1):
#     a= t - (5*i)
#     if a<0:
#         break
#     else:
#         t=a
#         s+=1
# print(s)

# t=int(input())
# s=0
# for i in range(t):
#     n,k=[int(i) for i in input().rstrip().split()]
#     if k-n>=2:
#         s+=1
# print(s)
    
# n=int(input())
# arr=list(map(int,input().rstrip().split()))
# print(sum(arr)/n)

# n=int(input())
# for i in range(n):
#     a,b=[int(i) for i in input().rstrip().split()]
#     c=abs(b-a)
#     d=c//10
#     if a==b:
#         print(0)
#     elif c%10!=0:
#         print(d+1)
#     else:
#         print(d)

# t=int(input())
# for i in range(t):
#     n=int(input())
#     lst=list(map(int,input().rstrip().split()))
#     lst.sort(reverse=True)
#     i=len(lst)
#     try:
#         while i>1:
#             if lst[0]-lst[1]<=1:
#                 lst.pop(0)
#             else:
#                 break
#     except IndexError:
#         pass
#     if len(lst)==1:
#         print("YES")
#     else: print("NO")

#151A
# n, k, l, c, d, p, nl, np= [int(i) for i in input().rstrip().split()]  
# totalml=k*l
# drink=totalml//(n*nl)
# salt=p//(n*np)
# lime=(c*d)//n
# print(min(drink,salt,lime))


# n,m= [int(i) for i in input().rstrip().split()]  
# st=''
# for i in range(n):
#     lst=list(map(str,input().rstrip().split()))
#     st+=''.join(lst)      
# if 'C' in st or 'M' in st or 'Y' in st:
#     print("#Color")
# else:
#     print("#Black&White")


# n,k= [int(i) for i in input().rstrip().split()]  
# k=5-k
# lst=list(map(int,input().rstrip().split()))
# lst2=[]
# for i in lst:
#     if i<=k:
#         lst2.append(i)
# print(len(lst2)//3)


# n=int(input())
# d={'m':0,'c':0}
# for i in range(n):
#     m,c= [int(i) for i in input().rstrip().split()]  
#     if m>c:
#         d['m']+=1
#     elif c>m:
#         d['c']+=1

# if d['m']>d['c']:
#     print("Mishka")
# elif d['c']>d['m']:
#     print("Chris")
# else:
#     print("Friendship is magic!^^")

# t=int(input())
# for i in range(t):
#     n=int(input())
#     st=input()
#     st1=''
#     lst=[]
#     for i in range(n-1):
#         if st[i]=='1':
#             if lst[0]=='1':
#                 lst.pop(0)
#                 st+='-'
            
#     print(st1)

# t=int(input())
# for i in range(t):
#     n=int(input())
#     lst=list(map(int,input().rstrip().split()))
#     s=0
    
#     for i in range(len(lst)):
#         try:
#             if lst[i]%2==lst[i+1]%2:
#                 s+=1
#         except IndexError:
#             break
#     print(s)



# t=int(input())
# for i in range(t):
#     n=int(input())
#     m=1
#     for i in range(1,n+1):
#         m=(m*i)%1000000007
#     print((n*(n-1)%1000000007)*(m)%1000000007)


# t=int(input())
# for i in range(t):
#     n=int(input())
#     m=1
#     #factorial
#     for i in range(1,n+1):
#         m=(m*i)
#     print((n*(n-1)*(m))%1000000007)


# n=int(input())
# for i in range(n):
#     l=int(input())
#     st=input()
#     sign=''
#     current=int(st[0])
#     for i in range(len(st)-1):

#         if current==int(st[i+1]):

#             current=current-int(st[i+1])
#             if current<0:
#                 sign=sign+'+'
#             else:
#                 sign = sign + '-'


#         else:

#             current = current+int(st[i + 1])
#             if current<0:
#                 sign=sign+'-'
#             else:
#                 sign=sign+'+'


#     print(sign)
# t=int(input())
# for i in range(t):
#     n=int(input())
#     s=0
#     for i in range(1,(n//2)+1):
#         s+=i*8*i
#     print(s)


# y,w= [int(i) for i in input().rstrip().split()]  
# m=max(y,w)
# s=6-m+1
# g=6
# while True:
#     if s%2==0 and g%2==0:
#         #print(f"{s//2}/{g//2}")
#         s,g=s//2,g//2
#     elif s%3==0 and g%3==0:
#         #print(f"{s//3}/{g//3}")
#         s,g=s//3,g//3
#     else:
#         break
# print(f"{s}/{g}")

# t=int(input())
# for i in range(t):
#     lst=list(map(int,input().rstrip().split()))
#     a=lst[0]
#     b=lst[1]
#     c=lst[2]
#     n=lst[3]
#     ma=max(a,b,c)
#     n-=((ma-a)+(ma-b)+(ma-c))
#     if n%3==0 and n>=0:
#         print("YES")
#     else:
#         print("NO")


# t=int(input())
# for i in range(t):
#     n=int(input())
#     lst=list(map(int,input().rstrip().split()))
#     lsto=[]
#     lste=[]
#     a,b,c=None,None,None
#     for i in range(len(lst)):
#         if lst[i]%2==0:
#             lste.append([i+1,lst[i]])
#         else:
#             lsto.append([i+1,lst[i]])

#         if len(lste)>=2 and len(lsto)>=1:
#             a,b,c=lste[0][0],lste[1][0],lsto[0][0]
#             break
#         elif len(lsto)>=3:
#             a,b,c=lsto[0][0],lsto[1][0],lsto[2][0]
#             break
#     if a!=None:
#         print("YES")
#         print(a,b,c)
#     else:
#         print("NO")

# t=int(input())
# for i in range(t):
#     n,m=[int(i) for i in input().rstrip().split()]  
#     lst=list(map(int,input().rstrip().split()))
#     c=list(map(int,input().rstrip().split()))
#     c.sort(reverse=True)
#     d={}
#     tables=[]
#     for i in lst:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     sl=list(d.values())
#     sl.sort(reverse=True)
#     for i in c:
#         try:
#             if sl[0]>=i:
#                 tables.append(i)
#                 sl[0]-=i
#                 sl.sort(reverse=True)

#             else:
#                 tables.append(sl[0])
#                 sl.pop(0)
#         except IndexError:
#             break

#     print(sum(tables))


# t=int(input())
# for i in range(t):
#     st='314159265358979323846264338327'
#     st2=input()
#     s=0
#     for i in range(len(st2)):
#         if st2[i]==st[i]:
#             s+=1
#         else:
#             break
#     print(s)


# t=int(input())
# for i in range(t):
#     n,s,r=[int(i) for i in input().rstrip().split()] 
#     arr=[]
#     a1=s-r
#     arr.append(a1)
#     b=r//(n-1)
#     c=r%(n-1)
#     d=a1-c
#     for i in range(n-1):
#         b1=b
#         if c!=0:
#             b1+=1
#             c-=1
#         arr.append(b1)
#     st=' '.join([str(i) for i in arr])
#     print(st)

#     n,s,r=[int(i) for i in input().rstrip().split()] 
#     lst= list(map(int,input().rstrip().split()))

# n,m=[int(i) for i in input().rstrip().split()]
# lst=list(map(int,input().rstrip().split()))
# s=0
# for i in range(len(lst)):
#     if i==0:
#         s+=lst[i]-1
        
#     elif m < lst[i]-lst[i-1] or lst[i]<lst[i-1]:
#         s+=m

#     else:
#         s+=lst[i]-lst[i-1]
    

# print(s)

# n,m=[int(i) for i in input().rstrip().split()]
# i=n+1
# np=None
# while True:
#     found=True
#     for j in range(2,(i//2)+1): 
#         if i%j==0:
#             found=False
#     if found==True:
#         np=i
#         break
#     else:
#         i=i+1
# if np==m:
#     print("YES")
# else:
#     print("NO")

# t=int(input())
# for i in range(t):
#     st=input()
#     if st in 'codeforces':
#         print("YES")
#     else:
#         print('NO')

# t=int(input())
# for i in range(t):
#     found=False
#     n=int(input())
#     st=input()
#     t=[0,0]
#     for i in range(n):
#         if st[i]=='U':
#             t[1]+=1
#         elif st[i]=='R':
#             t[0]+=1
#         elif st[i]=='D':
#             t[1]-=1
#         elif st[i]=='L':
#             t[0]-=1
#         if t==[1,1]:
#             found=True
#             print("YES")
#             break
#     if found!=True:
#         print("NO")

# t=int(input())
# for i in range(t):
#     n=int(input())
#     st=input()
#     s=0
#     if st=='':
#         print(0)
#     else:
#         while len(st)!=0:
#             if st[0]!=st[-1]:
#                 st=st[1:-1]
#                 s+=1
#             else:
#                 break
#         print(len(st))

# t=int(input())
# for i in range(t):
#     n=int(input())
#     lst=list(map(int,input().rstrip().split()))
#     s=0
#     for i in range(len(lst)):
#         try:
#             if lst[i]>=0 and lst[i+1]>=0:
#                 s+=lst[i]
#             elif lst[i]<0 and lst[i+1]<0:
#                 s+=-lst[i]
#                 lst[i+1]=-lst[i+1]
#             elif lst[i]>=0 and lst[i+1]<=0 and abs(lst[i+1])>abs(lst[i]):
#                 s+=-lst[i]
#                 lst[i+1]=-lst[i+1]
#             elif lst[i]>=0 and lst[i+1]<=0 and abs(lst[i+1])<=abs(lst[i]):
#                 s+=lst[i]
#             elif lst[i]<=0 and lst[i+1]>=0 and abs(lst[i+1])>abs(lst[i]):
#                 s+=lst[i]
#             elif lst[i]<=0 and lst[i+1]>=0 and abs(lst[i+1])<=abs(lst[i]):
#                 s+=-lst[i]
#                 lst[i+1]=-lst[i+1]
#         except IndexError:
#             s+=lst[i]
#     print(s)
        
# t=int(input())
# for i in range(t):
#     n,q=list(map(int,input().rstrip().split()))
#     lst=list(map(int,input().rstrip().split()))
#     for j in range(q):
#         st=input()
#         lst2=st.split()
#         if lst2[0]=='1':
#             for i in range(int(lst2[1])-1,int(lst2[2])):
#                 s=0
#                 for k in str(lst[i]):
#                     s+=int(k)
#                 lst[i]=s

           
#         else:
#             print(lst[int(lst2[1])-1])

# lst=list(map(int,input().rstrip().split()))
# lst.sort()
# print(lst[2]- lst[0])

# n,k=list(map(int,input().rstrip().split()))
# lst=list(map(int,input().rstrip().split()))
# k_s=lst[k-1]
# s=0
# for i in lst:
#     if i>= k_s and i>0:
#         s+=1
# print(s)

# n,h=list(map(int,input().rstrip().split()))
# lst=list(map(int,input().rstrip().split()))
# s=0
# for i in lst:
#     if i>h:
#         s+=2
#     else:
#         s+=1
# print(s)

# n=int(input())
# for i in range(n):
#     st=input()
#     lst=[i for i in 'abcdefghijklmnopqrstuvwxyz']
#     l2=[i for i in st]
#     found=False
#     l2=list(set(l2))
#     if len(l2)!=len(st):
#         print("No")
#     else:
#         for i in range(1,len(l2)-1):
#             currind=lst.index(l2[i])
#             nextind=lst.index(l2[i+1])
#             prevind=lst.index(l2[i-1])
#             if abs(currind-nextind)==1 or abs(currind-prevind)==1:
#                 found=True
#         if found:
#             print("Yes")
#         else:
#             print("No")

# s1=input()
# s2=input()
# s3=input()
# ind1=[i for i in range(1,27)]
# d={j:i for (j,i) in zip(s1,ind1)}
# d2={i:k for (i,k) in zip(ind1,s2)}
# s=''
# for z in s3:
#     if z.isdigit():
#         s+=z
#     elif z.isupper():
#         l=z.lower()
#         ind=d[l]
#         s+=d2[ind].upper()
#     else:
#         ind=d[z]
#         s+=d2[ind]
# print(s)


# st=input()
# answer="YES"
# for i in st:
#     if i not in ['1','7']:
#         answer="NO"
# print(answer)
# l=[
# 7,
# 4,
# 47,
# 74,
# 477,
# 744,
# 747,
# 474,
# 447,
# 774]
# n=int(input())
# answer='NO'
# for i in l:
#     if n%i==0:
#         answer='YES'
# print(answer)

# n=int(input())
# lst=list(map(int,input().rstrip().split()))
# s=sum(lst)/2
# lst.sort(reverse=True)
# t=0
# val=0
# for i in lst:
#     if val<=s:
#         val+=i
#         t+=1
# print(t)
# import math
# n,k=list(map(int,input().rstrip().split()))
# g=math.ceil(n/2)
# if g>=k:
#     print((2*k)-1)
# else:
#     print(2*(k-g))

# st=input()
# s=['H','Q','9']
# ans='NO'
# for i in s:
#     if i in st:
#         ans='YES'
# print(ans)

# n=int(input())
# lst=list(map(int,input().rstrip().split()))
# lst.sort()
# lst=[str(i) for i in lst]
# print(' '.join(lst))

# a=int(input())
# b=int(input())
# c=int(input())
# res=[]
# res.append(a+(b*c))
# res.append(a*(b+c))
# res.append((a+b)*c)
# res.append((a*b)+c)
# res.append(a*b*c)
# res.append(a+b+c)
# print(max(res))

# a,b=list(map(int,input().rstrip().split()))
# lst=list(map(int,input().rstrip().split()))
# lst.sort(reverse=True)
# mix=lst[0]-lst[a-1]
# for i in range(b-a+1):
#     A=lst[i]
#     B=lst[i+a-1]
#     if A-B < mix:
#         mix=A-B
# print(mix)

# import math
# n=int(input())
# lst=list(map(int,input().rstrip().split()))
# d={1:0,2:0,3:0,4:0}
# for i in lst:
#     d[i]+=1

# s=0
# s+=d[4]
# d[4]=0
# r=0
# if d[2]%2==0:
#     s+=d[2]/2
# else:
#     s+=d[2]//2
#     r=2
# d[2]=0
# s+=d[3]
# d[1]-=d[3]
# d[3]=0

# if d[1]<0:
#     d[1]=0
# rem = r+d[1]
# s+=math.ceil(rem/4)
# print(int(s))

# def swap(lst,ind1,ind2):
#     lst[ind1],lst[ind2]=lst[ind2],lst[ind1]

# n=int(input())
# lst=list(map(int,input().rstrip().split()))
# mi=lst[0]
# ma=lst[0]
# minind=0
# maxind=0
# for i in range(len(lst)):
#     if lst[i]>ma:
#         ma=lst[i]
#         maxind=i
#     if lst[i]<=mi:
#         mi=lst[i]
#         minind=i



# spare=0
# if minind<maxind:
#     spare=-1

# minind=len(lst)-1-minind
# print(minind+maxind+spare)

# n,t=list(map(int,input().rstrip().split()))
# st=input()
# lst=[i for i in st]
# lst2=[]
# for i in range(t):
#     i=1
#     while i<n:
#         if lst[i-1]=='B' and lst[i]=='G':
#             lst[i-1],lst[i]=lst[i],lst[i-1]
#             i+=1
#         i+=1 
# print(''.join(lst))

n=int(input())
# a=list(map(int,input().split()))
a=[]
for i in range(n):
	x=int(input())
	a.append(x)
arr=[]
ss=set()
for i in a:
	ss.add(i)
for i in ss:
	arr.append(i)
d={}
for i in range(len(a)):
	if a[i] in d:
		d[a[i]]+=1
	else:
		d[a[i]]=1
ans=0
for i in range(len(arr)):
	for j in range(i+1,len(arr)):
		for k in range(j+1,len(arr)):
			cc=0
			ss=arr[i]+arr[j]+arr[k]
			if ss%arr[i]==0:
				cc+=1
			if ss%arr[j]==0:
				cc+=1
			if ss%arr[k]==0:
				cc+=1
			if cc==1:
				ans+=(d[arr[i]]*d[arr[j]]*d[arr[k]])
for i in range(len(arr)):
	if d[arr[i]]<2:
		continue 
	for j in range(len(arr)):
		if i==j:
			continue
		ss=(2*arr[i])+arr[j]
		if ss%arr[i]!=0 and ss%arr[j]==0:
			temp=(d[arr[i]]*(d[arr[i]]-1))//2 
			temp=temp*d[arr[j]]
			ans+=temp
print(6*ans)
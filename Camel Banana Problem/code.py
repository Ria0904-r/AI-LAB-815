totban=int(input(&#39;Enter no. of bananas at starting &#39;))
dis=int(input(&#39;Enter distance you want to cover &#39;))
load_capacity=int(input(&#39;Enter max load capacity of your
camel &#39;))
lose=0
start=total
for i in range(dis):
while start&gt;0:
start=start-load_capacity

if start==1:
lose=lose-1

lose=lose+2

lose=lose-1
start=total-lose
if start==0:
break
print(start)

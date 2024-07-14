prices =[100, 180, 260, 310, 40, 535, 695]
print(prices)
# prices.sort()
l=[]
for i in range(1,len(prices)):        
       if(prices[i]>prices[i-1]):
            l.append((prices[i]-prices[i-1]))
            print(l)
       else:
           continue
            
# l.sort()
print(l)
print(sum(l))
print(prices)
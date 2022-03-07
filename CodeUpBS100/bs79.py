x = int(input())
sum = 0;
for i in range(1,x+1):
  sum += i
  if(sum < x):
    continue;
  else:
    print(i)
    break;
    
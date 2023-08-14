high=int(input("Enter the size of List: "))
li=[]
print("Enter Elements: ")
for i in range(0,high):
  el=int(input())
  li.append(el)
print("List has: ",end='')
for i in li:
  print(i,end=', ')
search=int(input("\nEnter the Element to be searched: "))
low=0
mid=(high+low)//2 
while low<=high:
    if search==li[mid]:
      print("Element Present at index:",mid)
      break
    elif search<li[mid]:
      high=mid-1
      mid=(high+low)//2
    elif search>li[mid]:
      low=mid+1
      mid=(high+low)//2
    else:
      print("Element not found!")

  
  

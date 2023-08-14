size=int(input("Enter the size of List: "))
li=[]
print("Enter Elements: ")
for i in range(0,size):
  el=int(input())
  li.append(el)
print("Array has: ",end='')
for i in li:
  print(i,end=', ')
search=int(input("\nEnter the Element to be searched: "))
print("Element is at index: ",end='')
for i in range(size):
  if search==li[i]:
    print(i,end=', ')
  

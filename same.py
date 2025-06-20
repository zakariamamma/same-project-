wafin akhoya le3ziz twehechtek bzaaaaf chof bghit readme file dyal had lcode import time

print(30*"-")
tasks = ["wakeup","clean your face","drink coffee"]
print("\033[32myour task list\033[0m ")
print()

time.sleep(1.25)

for i in tasks:
  print(i)
  print(30*"-")
  time.sleep(3/2)

print()
adding = input("add your new task >>> ")
print()
time.sleep(5/4)
tasks.append(adding)

print("\033[32mupdated list \033[0m")
print()
time.sleep(2)

for i in tasks:
  print(i)
  print(30*"-")
  time.sleep(3/2)

indixing_num = int(input("which index do you want to update? >>> "))
time.sleep(2)
print()

indixing = input("enter your new task >>> ")
tasks[indixing_num -1] = indixing
print()

time.sleep(2)
print("\033[32mupdated list\033[0m")
print()
time.sleep(1.25)

for i in tasks:
  print(i)
  time.sleep(3/2)
  print(30*"-")

print()
# changed this line to ask for index
removing_index = int(input("enter the index of the task to remove >>> "))
tasks.pop(removing_index - 1) # changed this line to remove by index
time.sleep(2)
print()

print("\033[32mfinal list\033[0m")
print()
time.sleep(1.25)

for i in tasks:
  print(i)
  time.sleep(3/2)
  print(30*"_")

print("enjoy for your day, always im here to help you ")
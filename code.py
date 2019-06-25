```
print('Hello Welcome To The Carnival! \nWe need to gather some information about you before we can give you your ticket')

user_name = input('What Is your name? ')

ages = {1:"1-7",2:"8-14",3:"15-64",4:"65-99",5:"99-120"}
q = ages

def user_age():
  age = int(input('Please Enter Your age '))
  x = age
  if x == q[1] or x == q[5]:
     print("free")
  if x == q[2] or x == q[4]:
      print("$6")
  if x == q[3]:
          print("$10")
  if x < q[1] or x > q[5]:
        print('Pick A Age between 1 and 120')
        return


user_age()
#the below line is prompting the user to pick a ticket between 1 & 100
def user_ticket_number():
  min_num = 1
  mi = min_num
  max_num = 100
  ma = max_num

  ticket = int(input("Please Pick A Ticket Number between 1 and 100 "))
  t = int(ticket)
  while t < mi or t > ma:
   print("Please Choose Another Number")
  if t > mi or t < ma:
    print(t)
    return
print(user_ticket_number())

def print_it():
    print('Hello ' + user_name + ' it looks like your ticket price is ' + str(user_age()) + '')

print(print_it())

```

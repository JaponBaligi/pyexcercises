print("<ep 14>")

#loops

#while loop
a = 1
while a == 1:
    print("oops")
#do not run pls

a = 1

while a < 10:
    a += 1
    print(a)
#this much safer because program knows where it can stop

while True:
    question = input("To exit program,press q: ")

    if question == "q":
        print("closing...")
        break#this breaks loop, says the python "bro stop"
    else:
        print("why are you trying to stay?!")

#for loop

allowed_chars = "0123456789+-/*= "
print("""
Simple calculator.

Operators:

    +   add
    -   substract
    *   multiply
    /   divide
Simply type your process to calculate(eg. 23*22)
""")

while True:
    data = input("Process: ")
    if data == "q":
        print("closing...")
        break

    for s in data:#this line telling "look for s variable in data(s variable usually defined in loop)"
        if s not in allowed_chars:#this is the defined part of s
            print("are trying something else?!")
            quit()

    process = eval(data)

    print(process)
#in this example, we can see that the user only allowed some characters that defined before -this prevents some safety issues- 

for i in range(0, 10):
    print(i)
#range() function allows showing represent numbers in a certain range, usage:range(first_number, last_number)



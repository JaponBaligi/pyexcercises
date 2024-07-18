#eval() and exec() function

print("""
Simple Calculator.

Operators:

    + add
    - subtract
    *   multiply
    /   divide
Type the action you want to perform and ENTER
Press the key. (For example, the numbers 23 and 46
after typing 23 * 46 to multiply
Press ENTER.)

""")

data = input("Process: ")
operation= eval(data)

print(operation)




d1 = """

In Python, there is a function called print() to print output to the screen.
We use the function. You can use this function like this:

>>> print("Hello World")

Şimdi de aynı kodu siz yazın!

>>> """

entry = input(d1)

exec(entry)

d2 = """

As you can see, the print() function calls itself
It prints the values ​​given as parameters to the screen.

Thus, we have completed our first lesson. Now one
We can move on to our next lesson."""

print(d2)

#basically eval() evaluates 'a' Python expression and returns the result, 
#exec() is used to dynamically execute Python code. This code can span multiple lines and can include any Python statements.


#if statement

number = int(input("Enter a number: "))

if number > 10:
    print("This number greater than 10")

if number < 10:
    print("This number less than 10")

if number == 10:
    print("Your number is 10")

#elif statement

age = int(input("Your age: "))

if age == 18:
    print("18 is good!")

elif age < 0:
    print(":D")

elif age < 18:
    print("young blood!")

elif age > 18:
    print("you are starting to going end!")

#else statement

soru = input("Tell me a fruit:")

if soru == "apple":
    print("yes, apple is a fruit...")

elif soru == "cherry":
    print("yes, cherry is a fruit...")

elif soru == "peach":
    print("yes, peach is a fruit...")

else:
    print(soru, "is really a fruit?")



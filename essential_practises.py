print("<ep 05:01>")
print("'printing exercises with characters'")

print("Lorem ipsum is simply dummy text")

print("Lorem"+"ipsum"+ "is"+"simply"+"dummy"+"text")

print('Lorem ipsum is simply dummy text')

print('Lorem'+''+'ipsum'+''+'is'+''+'simply'+''+'dummy'+''+'text')

print("Lorem" "ipsum" "is" "simply" "dummy" "text")

print('Lorem'+'ipsum'+'is'+'simply'+'dummy'+'text')

print("")#blank string

print(" ")#string with blank char

print(type("Lorem"))#checking variable type with type() function

print("abo"*3)#multiplying string with numbers(integers)

a = 3 
print("aboabo"*a)#defining a variable to integer and multiplying it with a string

print("<ep 05:02>")
print("printing exercises with numbers(integers)")

print(23)
#it works because 23 is an integer -->
#but when you try print(Lorem ipsum is simply dummy text) you'll get an error message because python thinks you are trying to print variables such as "lorem" "ipsum"...
print(2.5)#also works with floats

print(10+2j)#also works with complex numbers

print(5 + 7)

print (32 * 35)

print (7 / 2)

print (42 - 13)

print("do not forget")
print(12345,"is an integer")
print("12345"+" "+"is a string")
#you can also check this with type() function
print(type(12345))
print(type("12345"))

print("23"+"65")#if you try to do this math you will get two strings merge, not two integers addition result


print("<ep 05:03")
print("variables")

b = 5 #is defining a variable, referring b is 5 as an integer
print(b)
print(b * 50)
print(b / 5)

pi = 3.14
print(pi + b )

username = "JaponBaligi"
password = "1a2b3c4d"

print(len(username))#the len() function shows us our string's length
print(len(password))

length_of_password = len(password)
print(type(length_of_password))# we can see our password's type 



print("<ep 06:01>")

print("usage of print()(ironically)")

print('hmm')
print("hmm")
print("""hmm""")
#they are all same but different important usages
print("İstanbul'un """"hava"""" tahmini")
#in this example if we try using ' or triple " for print() function, it will not work properly because -->
#python cannot decide which is the starting or ending statement of the string quotes.

#sep usage
print("https://","www.","google.","com",sep=" ")#in this example sep parameter places blank character every element
print("https://","www.","google.","com",sep="")#is same because default definition of sep parameter is blank character
print("a","s","m","m",sep=".")#in this example sep parameter places dot every element

#end parameter usage (\n)
print("bir\niki\nüç")
print("bir","iki","üç",sep="\n")#you can also combine end parameter with sep parameter like this, result will be same with the first example

#file usage
dosya = open("deneme.txt","w")
print("sum lorem ipsum",file=dosya)
dosya.close()
#there will be no output of this code because it's not monitorized



#flush usage
f = open("kisisel_bilgiler.txt","w")
print("hi there!", file=f,flush=True)
#simply flush gives you opportunity to the save your content on a file without close the file(default is false, thats why we close the folder without typing flush=False)
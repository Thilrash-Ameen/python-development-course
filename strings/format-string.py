age = 24
txt = "My name is Thilrash, I'm {}"
print(txt.format(age))

quantity = 3
itemno = 100
price = 150.25
myorder = "I want {} pieces of item {} for {} rupees"
print(myorder.format(quantity,itemno,price))

myorder = "I want {2} pieces of item {1} for {0} rupees"
print(myorder.format(quantity,itemno,price))
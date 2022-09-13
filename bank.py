greeting=input("Say something to greet the customer:")
g=greeting.capitalize().strip()
if(g=="Hello"):
    m=0
elif(g[0]=="Hello"):
    m=0
elif(g[0]=="H"):
    m=20
else:
    m=100

print("You must pay $" + str(m) + " to customer")

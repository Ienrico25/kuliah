bad_chars = ["a", "i", "u", "e", "o","A", "I", "U", "E", "O"]

x = input("Tulis sesuatu:")

for i in bad_chars:
    x = x.replace(i, "")
    
print(str(x))

s="Honesty is the best policy"
words=s.split("") 
newwords=[word[::-1] for word in words]
newsentence=" ".join(newwords)
print("Reversed String:") 
print(newsentence)
print(len(newwords))

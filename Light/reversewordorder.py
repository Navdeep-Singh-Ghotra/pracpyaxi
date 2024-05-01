def reversewordorder(str):
              words = str.split()
              words.reverse()
              return " ".join(words)

inp = input("enter a sentence : ")
result = reversewordorder(inp)
print(result)
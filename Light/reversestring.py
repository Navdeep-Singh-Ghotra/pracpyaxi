str = input('input string')
def reversestring(str):
              reverse = ''
              for char in str:
                      reverse = char + reverse
              return reverse

def reverserec(str):
        if len(str) == 0:
                return str
        else:
                return reverserec(str[1:]) + str[0]
#result = reversestring(str)
result = reverserec(str)
print(result)

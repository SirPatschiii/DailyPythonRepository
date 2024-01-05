def invertString(input):
    output = input[::-1]
    return output;

text = input("Geben Sie ein Wort ein: ")
print("Ihr invertiertes Wort lautet: " + invertString(text))
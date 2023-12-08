def calcPercent(num, percent):
    return num * (percent / 100)

num = input("Geben Sie bitte eine Zahl ein: ")
percent = input("Geben Sie bitte nun Ihre Prozenzzahl ein: ")

num = float(num)
percent = float(percent)

print(str(percent) + "% von " + str(num) + " sind " + str(calcPercent(num, percent)))

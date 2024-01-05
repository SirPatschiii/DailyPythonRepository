def main():
    secondsIn = input("Geben Sie eine Anzahl an Sekunden ein: ")
    x = int(secondsIn)
    days = x // 60 // 60 // 24
    x = x - days * 60 * 60 * 24

    hours = x // 60 // 60
    x = x - hours * 60 * 60

    minutes = x // 60
    x = x - minutes * 60

    print("Das entspricht " + str(days) + " Tagen, " + str(hours) + " Stunden, " + str(minutes) + " Minuten und " + str(x) + " Sekunden.")

if __name__ == "__main__":
    main()

def main():
    list_of_transactions = []

    # type = True -> sale
    transaction1 = {
        "type": True,
        "amount": 100,
        "date": "2024.01.15"
    }

    transaction2 = {
        "type": True,
        "amount": 250,
        "date": "2024.01.13"
    }

    transaction3 = {
        "type": False,
        "amount": 50,
        "date": "2024.01.15"
    }

    transaction4 = {
        "type": False,
        "amount": 150,
        "date": "2024.01.14"
    }

    transaction5 = {
        "type": False,
        "amount": 150,
        "date": "2024.01.14"
    }

    list_of_transactions.append(transaction1)
    list_of_transactions.append(transaction2)
    list_of_transactions.append(transaction3)
    list_of_transactions.append(transaction4)
    list_of_transactions.append(transaction5)

    income = 0
    expense = 0

    for e in list_of_transactions:
        if e["date"] == "2024.01.14":
            print(e)
            print()
        if e["type"] is True:
            income += e["amount"]
        else:
            expense += e["amount"]

    print(f"Overall income: {income}")
    print(f"Overall expense: {expense}")
    print()

    if income > expense:
        print("Your wallet looks fine!")
    else:
        print("You should decrease your expenses")


if __name__ == '__main__':
    main()

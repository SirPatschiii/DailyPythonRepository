def m_and(a, b):
    if a and b:
        return 1
    else:
        return 0


def m_or(a, b):
    if a or b:
        return 1
    else:
        return 0


def m_not(a, b):
    if a == 0 and b == 0:
        return "1 1"
    if a == 0 and b == 1:
        return "1 0"
    if a == 1 and b == 0:
        return "0 1"
    if a == 1 and b == 1:
        return "0 0"


def m_nand(a, b):
    if m_and(a, b):
        return 0
    else:
        return 1


def m_nor(a, b):
    if not a and not b:
        return 1
    else:
        return 0


def m_xor(a, b):
    if a == b:
        return 0
    else:
        return 1


def m_xnor(a, b):
    if a == b:
        return 1
    else:
        return 0


def main():
    print("Die Wahrheitstabelle für AND lautet:")
    print("0 0 = " + str(m_and(0, 0)))
    print("0 1 = " + str(m_and(0, 1)))
    print("1 0 = " + str(m_and(1, 0)))
    print("1 1 = " + str(m_and(1, 1)))

    print("Die Wahrheitstabelle für OR lautet:")
    print("0 0 = " + str(m_or(0, 0)))
    print("0 1 = " + str(m_or(0, 1)))
    print("1 0 = " + str(m_or(1, 0)))
    print("1 1 = " + str(m_or(1, 1)))

    print("Die Wahrheitstabelle für NOT lautet:")
    print("0 0 = " + str(m_not(0, 0)))
    print("0 1 = " + str(m_not(0, 1)))
    print("1 0 = " + str(m_not(1, 0)))
    print("1 1 = " + str(m_not(1, 1)))

    print("Die Wahrheitstabelle für NAND lautet:")
    print("0 0 = " + str(m_nand(0, 0)))
    print("0 1 = " + str(m_nand(0, 1)))
    print("1 0 = " + str(m_nand(1, 0)))
    print("1 1 = " + str(m_nand(1, 1)))

    print("Die Wahrheitstabelle für NOR lautet:")
    print("0 0 = " + str(m_nor(0, 0)))
    print("0 1 = " + str(m_nor(0, 1)))
    print("1 0 = " + str(m_nor(1, 0)))
    print("1 1 = " + str(m_nor(1, 1)))

    print("Die Wahrheitstabelle für XOR lautet:")
    print("0 0 = " + str(m_xor(0, 0)))
    print("0 1 = " + str(m_xor(0, 1)))
    print("1 0 = " + str(m_xor(1, 0)))
    print("1 1 = " + str(m_xor(1, 1)))

    print("Die Wahrheitstabelle für XNOR lautet:")
    print("0 0 = " + str(m_xnor(0, 0)))
    print("0 1 = " + str(m_xnor(0, 1)))
    print("1 0 = " + str(m_xnor(1, 0)))
    print("1 1 = " + str(m_xnor(1, 1)))


if __name__ == '__main__':
    main()

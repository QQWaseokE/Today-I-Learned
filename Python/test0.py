def number(a):

    str_list = list(a)

    n = len(str_list)

    sum = 0

    for i in range(0, n):
        if str_list[i] == "A" or str_list[i] == "B" or str_list[i] == "C":
            str_list[i] = 3
        elif str_list[i] == "D" or str_list[i] == "E" or str_list[i] == "F":
            str_list[i] = 4
        elif str_list[i] == "G" or str_list[i] == "H" or str_list[i] == "I":
            str_list[i] = 5
        elif str_list[i] == "J" or str_list[i] == "K" or str_list[i] == "L":
            str_list[i] = 6
        elif str_list[i] == "M" or str_list[i] == "N" or str_list[i] == "O":
            str_list[i] = 7
        elif (
            str_list[i] == "P"
            or str_list[i] == "Q"
            or str_list[i] == "R"
            or str_list[i] == "S"
        ):
            str_list[i] = 8
        elif str_list[i] == "T" or str_list[i] == "U" or str_list[i] == "V":
            str_list[i] = 9
        elif str_list[i] == "W" or "X" or str_list[i] == "Y" or str_list[i] == "Z":
            str_list[i] = 10

        sum = sum + str_list[i]

    print(sum)


str = input()
number(str)

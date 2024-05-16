def palindrome(s):
    str_list = []

    for x in s:
        if x.isalpha():
            str_list.append(x.lower())

    while str_list:
        n = len(str_list)

        if n == 1 or n == 0:
            return True
        else:
            if str_list.pop(0) != str_list.pop():
                return False


print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))

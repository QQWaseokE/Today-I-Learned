def find_name(a):
    name_dict = {39: "Justin", 14: "John", 67: "Mike", 105: "Summer"}

    if a in name_dict:
        return name_dict[a]

    else:
        return "?"

    # for name in a:
    #     if name in name_dict:
    #         name_dict[name] += 1
    #     else:
    #         name_dict[name] = 1

    # result = set()
    # for name in name_dict:
    #     if name_dict[name] >= 2:
    #         result.add(name)

    # return result


n = int(input())
print(find_name(n))

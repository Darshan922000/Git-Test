def make_situation(n):
    h = ""
    for i in range(n):
        h += " "
        h += "\""
        h += "#" * (i + 1)
        h += "\""

    return h


n = int(input("Enter any number for #: "))
print(make_situation(n))
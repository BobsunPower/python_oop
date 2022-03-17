def outer():
    x = "local"

    def inner():
        nonlocal x  # fixed
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x  # fixed
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


x = "global"
print(x)
outer()
print(x)

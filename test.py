def test(x):
    if x > 20:
        return
    if x % 2 == 0:
        print(f"Even number recusive call: {x}")
        x = x * 2 + 1
        # test(x * 2 + 1)
        test(x)
    else:
        print(f"Odd number recusive call: {x}")
        x = x + 1
        # test(x + 1)
        test(x)

    print(f"Value of x = {x}")
    print(type(x))


if __name__ == "__main__":
    test(0)
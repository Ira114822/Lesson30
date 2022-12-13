def third():
    # print("hello!!!")
    try:
        print("begin third")
        n = int(input())

        if n == 1:
            5 / 0
        elif n == 2:
            int("eoip")  # value Error
        else:
            # a + b  # NameError
            raise NameError(1, 2, 3, 4, 5, 6, 877, "gdfgdf", "dfgdfhdfhd")
        print("hello")
    except BaseException as exc:
        print("exception was handled:", exc)


    except (ZeroDivisionError, ValueError, NameError) as exc:
        print("exception was handled:")
        print(exc)
        print(repr(exc))
        print(exc.args)
        print(exc.args[1])
    # except (ZeroDivisionError, ValueError, NameError):
    #     print("exception was handled...")
    # except ZeroDivisionError:
    #     print("exception ZeroDivisionError was handled...")
    # except ValueError:
    #     print("exception ValueError was handled...")
    # except NameError:
    #     print("exception NameError was handled...")

    print("end third function")


def second():
    print("begin second")
    third()
    print("End second")


def first():
    print("begin first")
    second()
    print("End first")


def main():
    print("begin main")
    first()
    print("End main")


main()

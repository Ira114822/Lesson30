def third():
    # print("hello!!!")
    try:
        [1,2,3][10]
      # иерархия; сначало более специализированные
    except IndexError:
        print("exception IndexError was handled")
    except KeyError:
        print("exception KeyError was handled")
    except LookupError:
        print("exception LookupError was handled")
    except Exception:
        print("exception Exception was handled")
    except BaseException:
        print("exception BaseException was handled")
    except:
        print("exception was handled")


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

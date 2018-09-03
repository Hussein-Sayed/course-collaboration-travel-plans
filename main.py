def view_students():
    while True:
        view_ask = input("to view all students type 'view all' to view specific student type 'view one' to exit type"
                         " 'exit'" + "\n")
        if view_ask == "view one":
            while True:
                found = False
                with open("data.txt", "r") as view_stu:
                    search_for = input("please enter user mail, to exit type 'exit'" + "\n")
                    while True:
                        data = view_stu.readline()
                        if search_for in data:
                            print(data)
                            found = True
                        if not data:
                            break
                        elif search_for == "exit":
                            break
                    if search_for == "exit":
                        break
                    elif not found:
                        print("user not found")
        elif view_ask == "view all":
            with open("data.txt") as view_stu:
                while True:
                    data = view_stu.readline()
                    print(data)
                    if not data:
                        break
        elif view_ask == "exit":
            break
        else:
            print("wrong input!")

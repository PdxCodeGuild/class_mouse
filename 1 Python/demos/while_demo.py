

# i = 0
# while i < 10:
#     i += 1
#     print(i)

while True:
    print("Starting the while true")
    yes_no = input("Enter a yes or no: ")
    while yes_no != "yes" and yes_no != "no":
        yes_no = input("Enter a yes or no: ")
        if yes_no == "dog":
            break

    else:
        print("You did it!!!")



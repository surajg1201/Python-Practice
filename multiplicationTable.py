
def display_multiplication_table(num):

    for i in range(1, 11):

        print(num, "x", i, "=", num*i)

        print()


num = int(input("Enter the num to get table: "))
print()


display_multiplication_table(num)

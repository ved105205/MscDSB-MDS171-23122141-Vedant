def get_insight(file_name, second_file):
    with open(file_name + ".txt", "r") as booking_file:
        print(f"Total Order Till Date: {booking_file.read()}")
    with open(second_file + ".txt", "r") as price_file:
        print(f"Total Price Till Date: {price_file.read()}")


def to_booking(
    name, price, phone_number, type, total_guest, date, check_out_date, file_name
):
    with open("total_booking.txt", "r") as total_orders:
        total_order = int(total_orders.read())

    with open("total_price.txt", "r") as total_prices:
        total_price = float(total_prices.read())

    total_order += 1
    total_price_booking = price

    total_price += total_price_booking

    with open("total_booking.txt", "w") as order:
        order.write(str(total_order))

    with open("total_price.txt", "w") as total_prices:
        total_prices.write(str(total_price))

    with open(file_name + ".txt", "a+") as file:
        # total_order = 0

        file.write(f"Total Booking Till Date: {total_order}\n")
        file.write(f"Total Price from Orders to Date: {total_price}\n")
        file.write("---------------------------------\n")
        file.write(f"Guest Name: {name}\n")
        file.write(f"Phone Number: {phone_number}\n")
        file.write(f"Room Type: {type}\n")
        file.write(f"Room Price: {price}\n")

        file.write(f"Total Guest: {total_guest}\n")
        file.write(f"check-in-date: {date}\n")
        file.write(f"check-out-date: {check_out_date}\n")
        file.write(f"Total price For This Order: {total_price_booking}\n")
        file.write("---------------------------------\n")
        print("Your Order is Created Successfully")


def main():
    print("1. Create New Order          2.  get Insight")
    print("3. exit")
    while True:
        user_choice = int(input("Enter Your Choice (1-3): "))

        if user_choice == 1:
            name = input("Customer Name: ")
            phone_number = int(input("Customer Phone Number: "))
            type = str(input("Room Type: "))
            price = float(input("Room Price: "))
            guest = int(input("Total Guest: "))
            check_in_date = str(input("Check-In Date: "))
            check_out_date = str(input("Check-Out Date: "))
            to_booking(
                name,
                price,
                phone_number,
                type,
                guest,
                check_in_date,
                check_out_date,
                "booking",
            )
        elif user_choice == 2:
            get_insight("total_booking", "total_price")
        elif user_choice == 3:
            print("Exitting.....")
            break
        else:
            print("Invalid choice.")
    # except ValueError:
    #     print(ValueError)


main()

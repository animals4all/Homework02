def print_report(day, file_name):
    day_num = "Day" + " " + str(day)
    day_num = day_num.upper()
    print day_num
    the_file = open(file_name, "r")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]
        
        delivery_info = "Delivered " + count + " " + melon + "s for total of $" + amount
        delivery_info = delivery_info.upper()
        print delivery_info
    the_file.close()

def main():
    files = ("um-deliveries-20140519.txt", "um-deliveries-20140520.txt", "um-deliveries-20140521.txt")
    day = 0
    for file_name in files:
        day += 1
        print_report(day, file_name)


if __name__ == "__main__":
    main()

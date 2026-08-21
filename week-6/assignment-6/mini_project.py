numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


def find_min(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


def find_max(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


def search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1


def bubble_sort(numbers):
    sorted_numbers = numbers.copy()

    for i in range(len(sorted_numbers)):
        for j in range(0, len(sorted_numbers) - 1 - i):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = (
                    sorted_numbers[j + 1],
                    sorted_numbers[j],
                )

    return sorted_numbers


def show_menu():
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    return input("Choose an option (1-5): ")


def main():
    while True:
        choice = show_menu()

        if choice == "1":
            minimum = find_min(numbers)
            print(f"Minimum: {minimum}")

        elif choice == "2":
            maximum = find_max(numbers)
            print(f"Maximum: {maximum}")

        elif choice == "3":
            target = int(input("Enter a number to search for: "))
            index = search(numbers, target)

            if index != -1:
                print(f"Found at index {index}")
            else:
                print("Not found")

        elif choice == "4":
            sorted_numbers = bubble_sort(numbers)
            print(f"Sorted list: {sorted_numbers}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-5.")


main()
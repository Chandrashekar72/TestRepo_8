from datetime import datetime

def calculate_age(dob):
    today = datetime.today()
    age = today.year - dob.year

    # If birthday hasn't occurred yet this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age


def main():
    print("=== Age Calculator ===")
    dob_input = input("Enter your Date of Birth (DD-MM-YYYY): ")

    try:
        dob = datetime.strptime(dob_input, "%d-%m-%Y")
        age = calculate_age(dob)
        print(f"Your age is: {age} years")
    except ValueError:
        print("Invalid date format. Please enter in DD-MM-YYYY format.")

if __name__ == "__main__":
    main()

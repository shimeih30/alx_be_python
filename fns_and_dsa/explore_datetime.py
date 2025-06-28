from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Save current datetime
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))  # Formatted output

def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)  # Save future date
        print("Future date:", future_date.strftime("%Y-%m-%d"))  # Formatted output
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()

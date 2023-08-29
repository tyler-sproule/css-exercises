def generate_email(date, day, start_time, end_time, location):
    subject = "Interpreter Request Details"
    body = f"We have received your request for {day}, {date} from {start_time} to {end_time} at {location}\n\nThank you!"

    return f"Subject: {subject}\n\n{body}"

def main():
    print("Paste the input here (press Enter twice after the last line):\n")

    input_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        input_lines.append(line)

    date = input_lines[0].split(': ')[1]
    day = input_lines[1].split(': ')[1]
    start_time = input_lines[2].split(': ')[1]
    end_time = input_lines[3].split(': ')[1]

    # Skip a line
    location_line = input()

    location = location_line.split(': ')[1]

    email_content = generate_email(date, day, start_time, end_time, location)
    print("\nGenerated email content:\n")
    print(email_content)

if __name__ == "__main__":
    main()
def convert_time_range_with_minutes_to_24_hour(time_range):
    # Split the range into start and end times
    start_time, _, end_time = time_range.partition(" to ")

    # Helper function to convert individual times
    def convert_to_24_hour_with_minutes(time_12_hour):
        # Split time into hour, minutes, and meridian
        time, meridian = time_12_hour.split()
        hour, minutes = map(int, time.split(":")) if ":" in time else (int(time), 0)

        # Convert to 24-hour format
        if meridian == "AM":
            if hour == 12:  # 12 AM is 00:00
                hour = 0
        elif meridian == "PM":
            if hour != 12:  # Add 12 to PM times, except for 12 PM
                hour += 12

        # Return formatted time
        return f"{hour:02}:{minutes:02}"

    # Convert both start and end times
    start_24_hour = convert_to_24_hour_with_minutes(start_time)
    end_24_hour = convert_to_24_hour_with_minutes(end_time)

    # Return the range in 24-hour format
    return f"{start_24_hour} to {end_24_hour}"

# Example usage
time_range = "9:30 AM to 5:15 PM"
print("24-hour format:", convert_time_range_with_minutes_to_24_hour(time_range))

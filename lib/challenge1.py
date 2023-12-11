# function for converting time
def convert_12hrs_to_24hrs(hour, minute, period):
    # conditinal statement

    if period == "am" and hour == 12:
        hour = 0
    elif period == "pm" and hour != 12:
        hour += 12

    return f"{hour:02d}{minute:02d}"


result = convert_12hrs_to_24hrs(1, 30, "am")
print(result)

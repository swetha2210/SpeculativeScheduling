from datetime import datetime

# Convert the timestamp to a datetime object
timestamp = 1577836800.0
dt_object = datetime.utcfromtimestamp(timestamp)

# Format the datetime object as a string
formatted_date_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')

print(formatted_date_time)

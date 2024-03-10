
flight_connections = [
('Amsterdam', 'Dublin', 100), ('Amsterdam', 'Rome', 140), ('Rome', 'Warsaw', 130),
('Minsk', 'Prague', 95), ('Stockholm', 'Rome', 190), ('Copenhagen', 'Paris', 120),
('Madrid', 'Rome', 135), ('Lisbon', 'Rome', 170), ('Dublin', 'Rome', 170),]


# Variables to store total flight time and count of routes to Rome
total_flight_time = 0
routes_to_rome = 0
 
# Loop through each flight connection
for connection in flight_connections:
    city_from, city_to, time = connection  
    if city_to == 'Rome':
        total_flight_time = total_flight_time + time
        routes_to_rome = routes_to_rome + 1

# Calculate average flight time
if routes_to_rome > 0:
    average_flight_time = total_flight_time / routes_to_rome
else:
    average_flight_time = 0

# Print the output
print("Routes to Rome:", routes_to_rome)
print("Average flight time to Rome:", average_flight_time, "minutes")



#connection = city_from, city_to, time ---- This syntax is used for packing multiple values into a tuple.
#Here, city_from, city_to, and time are individual variables, and connection becomes a tuple containing 
#these variables. This is commonly used when you want to group related variables together into a tuple, 
#especially if you intend to pass them around as a single unit.

#city_from, city_to, time = connection ---- This syntax is used for unpacking the elements of a tuple
#connection into individual variables city_from, city_to, and time. 
#It assumes that connection is a tuple containing three elements, 
#and it assigns each element of the tuple to its corresponding variable. 
#This is commonly used when you know the structure of the tuple and want to access its elements separately.

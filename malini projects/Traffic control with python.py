import time

def control_traffic_light(traffic_light, color, duration):
    print(f"Traffic Light ({traffic_light}): {color}")
    time.sleep(duration)

def simulate_traffic_control():
    while True:
        # Traffic light for North-South direction
        control_traffic_light("North-South", "Green", 5)
        control_traffic_light("North-South", "Yellow", 2)
        control_traffic_light("North-South", "Red", 5)

        # Traffic light for East-West direction
        control_traffic_light("East-West", "Red", 2)  # Add a brief delay for safety
        control_traffic_light("East-West", "Green", 5)
        control_traffic_light("East-West", "Yellow", 2)

# Run the simulation
simulate_traffic_control()

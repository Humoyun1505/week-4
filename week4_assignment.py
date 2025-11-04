def calculate_room_revenue(room_type, nights_booked, season):
    rate = 0
    if room_type == "suite" or room_type == "SUITE":
        if season == "low" or season == "LOW":
            rate = 150
        elif season == "regular" or season == "REGULAR":
            rate = 225
        elif season == "peak" or season == "PEAK":
            rate = 350
    elif room_type == "deluxe" or room_type == "DELUXE":
        if season == "low" or season == "LOW":
            rate = 100
        elif season == "regular" or season == "REGULAR":
            rate = 160
        elif season == "peak" or season == "PEAK":
            rate = 240
    elif room_type == "standard" or room_type == "STANDARD":
        if season == "low" or season == "LOW":
            rate = 60
        elif season == "regular" or season == "REGULAR":
            rate = 95
        elif season == "peak" or season == "PEAK":
            rate = 140
    return rate * nights_booked
def calculate_booking_rate(hotel_years, baseline_rooms, booked_rooms):
    expected_bookings = 1000 + (hotel_years * 100)
    room_capacity = expected_bookings - baseline_rooms
    booking_percentage = ((booked_rooms - baseline_rooms) / room_capacity) * 100
    return round(booking_percentage, 1)
def determine_occupancy_level(booking_percent):
    if booking_percent < 50:
        return "Under Capacity"
    elif 50 <= booking_percent < 60:
        return "Fair Occupancy"
    elif 60 <= booking_percent < 70:
        return "Good Occupancy"
    elif 70 <= booking_percent < 85:
        return "Excellent Occupancy"
    else:
        return "Full Capacity"
def calculate_net_income(revenue, nights, occupancy_level):
    base_income = revenue * 0.05 + nights * 2
    if occupancy_level == "Under Capacity":
        level_factor = 0.5
    elif occupancy_level == "Fair Occupancy":
        level_factor = 1.0
    elif occupancy_level == "Good Occupancy":
        level_factor = 1.2
    elif occupancy_level == "Excellent Occupancy":
        level_factor = 1.5
    else:
        level_factor = 1.8
    return round(base_income * level_factor, 1)
def needs_discount_offer(operating_days, total_nights, avg_booking):
    if operating_days >= 6 and avg_booking < 50:
        return True
    if total_nights < 100 and avg_booking < 60:
        return True
    if operating_days >= 4 and avg_booking < 40:
        return True
    return False
def generate_booking_analysis(guest_name, room_type, nights, season, hotel_years, baseline_rooms, booked_rooms, operating_days):
    revenue = calculate_room_revenue(room_type, nights, season)
    booking_rate = calculate_booking_rate(hotel_years, baseline_rooms, booked_rooms)
    occupancy_level = determine_occupancy_level(booking_rate)
    net_income = calculate_net_income(revenue, nights, occupancy_level)
    discount_needed = needs_discount_offer(operating_days, nights, booking_rate)
    print("========================================")
    print(f"Booking Analysis for: {guest_name}")
    print("----------------------------------------")
    print(f"Room Type: {room_type}")
    print(f"Nights Booked: {nights}")
    print(f"Season: {season}")
    print(f"Room Revenue: ${revenue}")
    print("Booking Analysis:")
    print(f"  Experience: {hotel_years} years, Baseline: {baseline_rooms}, Booked Rooms: {booked_rooms}")
    print(f"  Booking Rate: {booking_rate}%")
    print(f"  Occupancy Level: {occupancy_level}")
    print(f"Net Income: ${net_income}")
    print(f"Operating Days: {operating_days}")
    print(f"Discount Offer Needed: {'Yes' if discount_needed else 'No'}")
    print()
print("HOTEL BOOKING ANALYTICS")
print("========================================")
generate_booking_analysis("Harrison", "suite", 45, "peak", 3, 800, 1150, 3)
generate_booking_analysis("Madison", "deluxe", 60, "regular", 5, 900, 1300, 5)
generate_booking_analysis("Logan", "standard", 30, "low", 8, 850, 950, 7)
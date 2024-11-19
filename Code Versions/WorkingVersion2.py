from datetime import datetime

# Sample dataset with all locations
locations = {
    "A": [
        {"name": "HealthPlus Clinic", "service": "Cardiology", "rating": 4.5, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 3},
        {"name": "Wellness Care Clinic", "service": "Dermatology", "rating": 4.2, "hours": {"start": "8 AM", "end": "4 PM"}, "distance": 5},
    ],
    "B": [
        {"name": "CureWell Clinic", "service": "Pediatrics", "rating": 3.8, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 2},
        {"name": "Healing Touch Clinic", "service": "Orthopedics", "rating": 4.1, "hours": {"start": "10 AM", "end": "5 PM"}, "distance": 8},
    ],
    "C": [
        {"name": "CardioMed Clinic", "service": "Cardiology", "rating": 4.0, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 7},
        {"name": "Family Care Clinic", "service": "Pediatrics", "rating": 4.6, "hours": {"start": "8 AM", "end": "5 PM"}, "distance": 10},
    ],
    "D": [
        {"name": "City Wellness Clinic", "service": "General Practice", "rating": 4.3, "hours": {"start": "9 AM", "end": "4 PM"}, "distance": 4},
        {"name": "SkinCare Clinic", "service": "Dermatology", "rating": 4.7, "hours": {"start": "10 AM", "end": "5 PM"}, "distance": 12},
    ],
    "E": [
        {"name": "Health Horizon Clinic", "service": "General Practice", "rating": 4.8, "hours": {"start": "9 AM", "end": "3 PM"}, "distance": 1},
        {"name": "OrthoFlex Clinic", "service": "Orthopedics", "rating": 3.9, "hours": {"start": "8 AM", "end": "6 PM"}, "distance": 6},
    ],
    "F": [
        {"name": "Healthy Heart Clinic", "service": "Cardiology", "rating": 4.4, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 9},
        {"name": "Pediatric Care Clinic", "service": "Pediatrics", "rating": 4.5, "hours": {"start": "8 AM", "end": "5 PM"}, "distance": 3},
    ],
    "G": [
        {"name": "Medicare Clinic", "service": "General Practice", "rating": 4.1, "hours": {"start": "10 AM", "end": "5 PM"}, "distance": 2},
        {"name": "Dermatology Plus", "service": "Dermatology", "rating": 4.6, "hours": {"start": "9 AM", "end": "4 PM"}, "distance": 7},
    ],
    "H": [
        {"name": "Orthopedic Care Center", "service": "Orthopedics", "rating": 4.2, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 6},
        {"name": "Complete Care Clinic", "service": "Pediatrics", "rating": 3.9, "hours": {"start": "10 AM", "end": "6 PM"}, "distance": 5},
    ],
    "I": [
        {"name": "SuperMed Clinic", "service": "General Practice", "rating": 4.7, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 8},
        {"name": "SkinFirst Clinic", "service": "Dermatology", "rating": 4.5, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 3},
    ],
    "J": [
        {"name": "CardioPlus Clinic", "service": "Cardiology", "rating": 4.8, "hours": {"start": "8 AM", "end": "4 PM"}, "distance": 4},
        {"name": "WellCare Clinic", "service": "Pediatrics", "rating": 4.3, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 10},
    ],
}

# Function to convert time to 24-hour format for comparison
def convert_to_24hr_format(time_str):
    try:
        return datetime.strptime(time_str, '%I %p').time()
    except ValueError:
        return None

# Main function
def health_resource_locator():
    print("Welcome to the Health Resource Locator!")
    
    # Get user inputs
    user_location = input("Enter your current location (A-J): ").upper()
    budget = input("Enter your maximum budget (or press Enter to skip): ")
    service = input("Enter the service you need (or press Enter to skip): ").lower()
    distance = input("Enter maximum distance (in km, or press Enter to skip): ")
    rating = input("Enter the minimum rating (out of 5, or press Enter to skip): ")
    visit_time = input("Enter the hour of visit (e.g., 9 AM, 2 PM): ").lower()

    # Handle missing inputs
    budget = float(budget) if budget else None
    distance = float(distance) if distance else None
    rating = float(rating) if rating else None
    visit_time_24hr = convert_to_24hr_format(visit_time)

    # Filter clinics based on user input
    matching_clinics = []
    
    for clinic in locations.get(user_location, []):
        # Check service
        if service and service not in clinic["service"].lower():
            continue
        
        # Check rating
        if rating and clinic["rating"] < rating:
            continue
        
        # Check distance
        if distance and clinic["distance"] > distance:
            continue
        
        # Check time of visit
        if visit_time_24hr:
            clinic_open_time = convert_to_24hr_format(clinic["hours"]["start"])
            clinic_close_time = convert_to_24hr_format(clinic["hours"]["end"])
            if not (clinic_open_time <= visit_time_24hr <= clinic_close_time):
                continue
        
        # Add to results
        matching_clinics.append(clinic)

    # Output results
    if matching_clinics:
        print("\nMatching Clinics:")
        for clinic in matching_clinics:
            print(f"{clinic['name']} - {clinic['service']} - Rating: {clinic['rating']} - Distance: {clinic['distance']} km")
    else:
        print("\nNo clinics match your criteria.")

# Run the program
health_resource_locator()

import folium
from datetime import datetime
from geopy.distance import geodesic

# Actual locations (A-J) and clinic coordinates for Pune (with real-world examples)
coordinates = {
    "A": (18.5204, 73.8567),  # Pune city center
    "B": (18.5333, 73.8700),  # Kothrud
    "C": (18.5200, 73.8200),  # Koregaon Park
    "D": (18.5333, 73.8311),  # Viman Nagar
    "E": (18.4721, 73.8268),  # Hadapsar
    "F": (18.4785, 73.9126),  # Magarpatta
    "G": (18.4565, 73.8686),  # Baner
    "H": (18.5522, 73.8933),  # Wakad
    "I": (18.6500, 73.8400),  # Pune University
    "J": (18.4640, 73.8702),  # Kharadi
}

# Actual clinic coordinates in Pune (names, coordinates, services, and ratings)
clinic_coordinates = {
    "A": [
        {"name": "Jehangir Hospital", "service": "General Practice", "rating": 4.7, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 5, "location": (18.5207, 73.8560)},
        {"name": "Sahyadri Speciality Hospital", "service": "Orthopedics", "rating": 4.5, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 6, "location": (18.5282, 73.8575)},
        {"name": "Ruby Hall Clinic", "service": "Cardiology", "rating": 4.6, "hours": {"start": "9 AM", "end": "7 PM"}, "distance": 4, "location": (18.5203, 73.8540)},
        {"name": "Bayside Hospital", "service": "Dermatology", "rating": 4.4, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 5, "location": (18.5215, 73.8565)},
    ],
    "B": [
        {"name": "Deenanath Mangeshkar Hospital", "service": "Cardiology", "rating": 4.8, "hours": {"start": "8 AM", "end": "6 PM"}, "distance": 7, "location": (18.5286, 73.8641)},
        {"name": "Sahydri Multi-Specialty Hospital", "service": "Pediatrics", "rating": 4.3, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 5, "location": (18.5351, 73.8694)},
        {"name": "KEM Hospital", "service": "General Practice", "rating": 4.5, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 6, "location": (18.5285, 73.8617)},
        {"name": "Kothrud Hospital", "service": "Orthopedics", "rating": 4.3, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 8, "location": (18.5400, 73.8695)},
    ],
    "C": [
        {"name": "Ruby Hall Clinic", "service": "General Practice", "rating": 4.6, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 3, "location": (18.5213, 73.8196)},
        {"name": "Koregaon Park Hospital", "service": "Orthopedics", "rating": 4.2, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 4, "location": (18.5220, 73.8215)},
        {"name": "Serene Care Clinic", "service": "Pediatrics", "rating": 4.0, "hours": {"start": "8 AM", "end": "6 PM"}, "distance": 3, "location": (18.5230, 73.8225)},
        {"name": "St. Mary’s Hospital", "service": "Dermatology", "rating": 4.4, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 5, "location": (18.5235, 73.8202)},
    ],
    "D": [
        {"name": "Columbia Asia Hospital", "service": "Orthopedics", "rating": 4.3, "hours": {"start": "9 AM", "end": "7 PM"}, "distance": 6, "location": (18.5355, 73.8300)},
        {"name": "Cloudnine Hospital", "service": "Pediatrics", "rating": 4.8, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 5, "location": (18.5300, 73.8325)},
        {"name": "Pune Care Clinic", "service": "General Practice", "rating": 4.5, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 5, "location": (18.5342, 73.8285)},
        {"name": "Medica Super Specialty Hospital", "service": "Cardiology", "rating": 4.2, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 7, "location": (18.5320, 73.8311)},
    ],
    "E": [
        {"name": "Sanas Hospital", "service": "Dermatology", "rating": 4.4, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 5, "location": (18.4735, 73.8275)},
        {"name": "Noble Hospital", "service": "Orthopedics", "rating": 4.7, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 4, "location": (18.4745, 73.8280)},
        {"name": "Life Care Hospital", "service": "General Practice", "rating": 4.5, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 3, "location": (18.4750, 73.8295)},
        {"name": "Spandan Heart Hospital", "service": "Cardiology", "rating": 4.2, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 6, "location": (18.4765, 73.8310)},
    ],
    "F": [
        {"name": "Mangeshkar Hospital", "service": "Cardiology", "rating": 4.5, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 8, "location": (18.4800, 73.9120)},
        {"name": "Magarpatta Heart Clinic", "service": "General Practice", "rating": 4.6, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 5, "location": (18.4812, 73.9135)},
        {"name": "Care Clinic", "service": "Pediatrics", "rating": 4.4, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 7, "location": (18.4825, 73.9142)},
        {"name": "Healing Hands Clinic", "service": "Orthopedics", "rating": 4.3, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 6, "location": (18.4802, 73.9125)},
    ],
    "G": [
        {"name": "Kundali Hospital", "service": "Pediatrics", "rating": 4.2, "hours": {"start": "10 AM", "end": "5 PM"}, "distance": 4, "location": (18.4590, 73.8695)},
        {"name": "Baner Heart Clinic", "service": "Cardiology", "rating": 4.6, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 5, "location": (18.4578, 73.8710)},
        {"name": "Orthospecialty Hospital", "service": "Orthopedics", "rating": 4.3, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 6, "location": (18.4595, 73.8730)},
        {"name": "Baner Super Care Clinic", "service": "Dermatology", "rating": 4.5, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 7, "location": (18.4592, 73.8697)},
    ],
    "H": [
        {"name": "Noble Hospital", "service": "General Practice", "rating": 4.7, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 7, "location": (18.5535, 73.8950)},
        {"name": "Wakad Heart Clinic", "service": "Cardiology", "rating": 4.6, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 5, "location": (18.5540, 73.8960)},
        {"name": "LifeCare Hospital", "service": "Orthopedics", "rating": 4.3, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 8, "location": (18.5552, 73.8970)},
        {"name": "Healing Hands", "service": "General Practice", "rating": 4.5, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 6, "location": (18.5545, 73.8985)},
    ],
    "I": [
        {"name": "BJP Hospital", "service": "Orthopedics", "rating": 4.5, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 5, "location": (18.6525, 73.8402)},
        {"name": "Pune University Clinic", "service": "Cardiology", "rating": 4.4, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 4, "location": (18.6530, 73.8395)},
        {"name": "Research Clinic", "service": "Dermatology", "rating": 4.7, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 5, "location": (18.6505, 73.8385)},
        {"name": "Life Clinic", "service": "General Practice", "rating": 4.3, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 6, "location": (18.6500, 73.8405)},
    ],
    "J": [
        {"name": "Kharadi Hospital", "service": "Cardiology", "rating": 4.6, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 6, "location": (18.4655, 73.8715)},
        {"name": "Tech Care Hospital", "service": "General Practice", "rating": 4.4, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 5, "location": (18.4640, 73.8725)},
        {"name": "Life Plus Clinic", "service": "Orthopedics", "rating": 4.3, "hours": {"start": "9 AM", "end": "6 PM"}, "distance": 4, "location": (18.4670, 73.8730)},
        {"name": "Kharadi Heart Clinic", "service": "Cardiology", "rating": 4.6, "hours": {"start": "9 AM", "end": "5 PM"}, "distance": 7, "location": (18.4630, 73.8700)},
    ],
}

# Function to convert time to 24-hour format for comparison
def convert_to_24hr_format(time_str):
    try:
        return datetime.strptime(time_str, '%I %p').time()
    except ValueError:
        return None

# Function to calculate the distance between two locations using geopy
def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).km

# Main function to handle user input and display the results
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

    # Create a Folium map centered on the user's location
    user_coords = coordinates.get(user_location)
    if user_coords:
        m = folium.Map(location=user_coords, zoom_start=12)

        # Mark the user's location in green with a larger icon to avoid overlap
        folium.Marker(user_coords, popup="Your Location", icon=folium.Icon(color='green', icon_size=(20, 20))).add_to(m)

        # Filter clinics based on user input
        matching_clinics = []

        for clinic in clinic_coordinates.get(user_location, []):
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
            
            # Add matching clinic to results
            matching_clinics.append(clinic)

            # Create map marker with larger text box for info
            info_html = f'''
            <h3>{clinic["name"]}</h3>
            <p><strong>Service:</strong> {clinic["service"]}</p>
            <p><strong>Rating:</strong> {clinic["rating"]}/5</p>
            <p><strong>Distance:</strong> {clinic["distance"]} km</p>
            <p><strong>Hours:</strong> {clinic["hours"]["start"]} to {clinic["hours"]["end"]}</p>
            '''
            popup = folium.Popup(info_html, max_width=500)
            folium.Marker(clinic["location"], popup=popup).add_to(m)

            # Draw a clear line to the shortlisted clinic
            folium.PolyLine([user_coords, clinic["location"]], color="blue", weight=3, opacity=1).add_to(m)

        # Check if any clinics match
        if matching_clinics:
            print("\nShortlisted Clinics:")
            for clinic in matching_clinics:
                print(f"{clinic['name']} - {clinic['service']} - Rating: {clinic['rating']}/5 - Distance: {clinic['distance']} km")

        # Save the map to an HTML file
        map_file = 'health_locator_map.html'
        m.save(map_file)
        print(f"\nMap has been saved to '{map_file}'.")
    else:
        print("Invalid location. Please enter a valid location from A-J.")

# Run the health resource locator
health_resource_locator()

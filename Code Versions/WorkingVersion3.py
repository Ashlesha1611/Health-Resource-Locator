from datetime import datetime

distances = {
    'A': {'B': 5, 'C': 8, 'D': 7, 'E': 10, 'F': 15, 'G': 12, 'H': 18, 'I': 13, 'J': 11},
    'B': {'A': 5, 'C': 5, 'D': 6, 'E': 9, 'F': 13, 'G': 11, 'H': 17, 'I': 12, 'J': 10},
    'C': {'A': 8, 'B': 5, 'D': 7, 'E': 8, 'F': 14, 'G': 11, 'H': 16, 'I': 12, 'J': 9},
    'D': {'A': 7, 'B': 6, 'C': 7, 'E': 6, 'F': 13, 'G': 10, 'H': 15, 'I': 11, 'J': 10},
    'E': {'A': 10, 'B': 9, 'C': 8, 'D': 6, 'F': 11, 'G': 7, 'H': 13, 'I': 9, 'J': 8},
    'F': {'A': 15, 'B': 13, 'C': 14, 'D': 13, 'E': 11, 'G': 9, 'H': 20, 'I': 17, 'J': 16},
    'G': {'A': 12, 'B': 11, 'C': 11, 'D': 10, 'E': 7, 'F': 9, 'H': 16, 'I': 10, 'J': 8},
    'H': {'A': 18, 'B': 17, 'C': 16, 'D': 15, 'E': 13, 'F': 20, 'G': 16, 'I': 14, 'J': 12},
    'I': {'A': 13, 'B': 12, 'C': 12, 'D': 11, 'E': 9, 'F': 17, 'G': 10, 'H': 14, 'J': 8},
    'J': {'A': 11, 'B': 10, 'C': 9, 'D': 10, 'E': 8, 'F': 16, 'G': 8, 'H': 12, 'I': 8}
}

places = {
    'A': [
        {"name": "Green Valley Clinic", "services": ["General Medicine", "Dentistry"], "cost": 2000, "rating": 4.5, "hours": "8 AM - 8 PM"},
        {"name": "Sunrise Health Center", "services": ["Orthopedics", "Dermatology"], "cost": 2500, "rating": 4.3, "hours": "9 AM - 9 PM"},
        {"name": "Apex Pharmacy", "services": ["Prescription Medicines", "Immunizations"], "cost": 500, "rating": 4.7, "hours": "8 AM - 10 PM"},
        {"name": "Alpha Diagnostics", "services": ["Blood Tests", "MRI Scans"], "cost": 3000, "rating": 4.6, "hours": "7 AM - 8 PM"},
    ],
    'B': [
        {"name": "Blue Cross Clinic", "services": ["Pediatrics", "General Medicine"], "cost": 1800, "rating": 4.2, "hours": "8 AM - 8 PM"},
        {"name": "Healing Hands", "services": ["Gynecology", "Physiotherapy"], "cost": 3000, "rating": 4.6, "hours": "9 AM - 7 PM"},
        {"name": "Wellness Pharmacy", "services": ["Health Supplements", "Medication Refills"], "cost": 400, "rating": 4.7, "hours": "8 AM - 10 PM"},
        {"name": "Prime Diagnostics", "services": ["X-ray", "Ultrasound"], "cost": 2500, "rating": 4.4, "hours": "7 AM - 7 PM"},
    ],
    'C': [
        {"name": "Care First Clinic", "services": ["Cardiology", "Dermatology"], "cost": 1500, "rating": 4.1, "hours": "8 AM - 8 PM"},
        {"name": "Wellness Center", "services": ["General Medicine", "Dentistry"], "cost": 2000, "rating": 4.3, "hours": "9 AM - 9 PM"},
        {"name": "CityMed Pharmacy", "services": ["OTC Medicines", "Vaccinations"], "cost": 600, "rating": 4.6, "hours": "8 AM - 10 PM"},
        {"name": "QuickCheck Diagnostics", "services": ["COVID-19 Tests", "ECG"], "cost": 2000, "rating": 4.5, "hours": "7 AM - 7 PM"},
        {"name": "Flex Rehab", "services": ["Physiotherapy", "Neurological Rehabilitation"], "cost": 3400, "rating": 4.7, "hours": "8 AM - 6 PM"},
    ],
    'D': [
        {"name": "City Health Hub", "services": ["Orthopedics", "General Medicine"], "cost": 1800, "rating": 4.2, "hours": "8 AM - 8 PM"},
        {"name": "Advanced Care Clinic", "services": ["Cardiology", "Dermatology"], "cost": 1400, "rating": 4.3, "hours": "9 AM - 7 PM"},
        {"name": "HealthHub Pharmacy", "services": ["Compounding", "Health Check Supplies"], "cost": 700, "rating": 4.6, "hours": "8 AM - 10 PM"},
        {"name": "Precision Diagnostics", "services": ["CT Scans", "Allergy Testing"], "cost": 3500, "rating": 4.7, "hours": "7 AM - 7 PM"},
        {"name": "Vital Rehab", "services": ["Cardiac Rehabilitation", "Addiction Recovery"], "cost": 4000, "rating": 4.8, "hours": "8 AM - 6 PM"},
    ],
    'E': [
        {"name": "Eastside Care", "services": ["Gynecology", "General Medicine"], "cost": 2300, "rating": 4.3, "hours": "8 AM - 8 PM"},
        {"name": "MediPlus", "services": ["Dermatology", "Cardiology"], "cost": 3200, "rating": 4.5, "hours": "9 AM - 9 PM"},
        {"name": "EastPharma", "services": ["Vaccinations", "Prescription Medicines"], "cost": 800, "rating": 4.7, "hours": "8 AM - 10 PM"},
        {"name": "SmartDiagnostics", "services": ["Pathology Tests", "Bone Density Scans"], "cost": 4000, "rating": 4.6, "hours": "7 AM - 8 PM"},
        {"name": "Revive Rehab", "services": ["Speech Therapy", "Physical Therapy"], "cost": 3700, "rating": 4.8, "hours": "8 AM - 6 PM"},
    ],
    'F': [
        {"name": "Central Clinic", "services": ["Pediatrics", "General Medicine"], "cost": 2200, "rating": 4.4, "hours": "8 AM - 8 PM"},
        {"name": "Healing Touch Clinic", "services": ["Orthopedics", "Cardiology"], "cost": 2800, "rating": 4.6, "hours": "9 AM - 9 PM"},
        {"name": "HealthyPharma", "services": ["OTC Medicines", "Compounding"], "cost": 900, "rating": 4.7, "hours": "8 AM - 10 PM"},
        {"name": "MedTech Diagnostics", "services": ["Blood Tests", "Cancer Screening"], "cost": 4200, "rating": 4.5, "hours": "7 AM - 7 PM"},
        {"name": "TheraCare Rehab", "services": ["Neurological Rehabilitation", "Physical Therapy"], "cost": 4000, "rating": 4.8, "hours": "8 AM - 6 PM"},
    ],
    'G': [
        {"name": "Green Valley Clinic", "services": ["Cardiology", "General Medicine"], "cost": 2100, " rating": 4.4, "hours": "8 AM - 6 PM"},
        {"name": "Life Care Center", "services": ["Pediatrics", "Dermatology"], "cost": 2400, "rating": 4.3, "hours": "9 AM - 5 PM"},
        {"name": "PharmaGreen", "services": ["Vaccinations", "Prescription Medicines"], "cost": 700, "rating": 4.6, "hours": "9 AM - 9 PM"},
        {"name": "UltraDiagnostics", "services": ["MRI Scans", "CT Scans"], "cost": 4000, "rating": 4.7, "hours": "7 AM - 8 PM"},
    ],
    'H': [
        {"name": "Sunrise Clinic", "services": ["Orthopedics", "Gynecology"], "cost": 2600, "rating": 4.2, "hours": "8 AM - 4 PM"},
        {"name": "Complete Health Center", "services": ["Cardiology", "General Medicine"], "cost": 1900, "rating": 4.1, "hours": "7 AM - 5 PM"},
        {"name": "MediAid Pharmacy", "services": ["OTC Medicines", "First Aid Supplies"], "cost": 500, "rating": 4.3, "hours": "8 AM - 8 PM"},
    ],
    'I': [
        {"name": "Care Health Clinic", "services": ["Cardiology", "General Medicine"], "cost": 2700, "rating": 4.3, "hours": "9 AM - 7 PM"},
        {"name": "Healthy Life Center", "services": ["Orthopedics", "Pediatrics"], "cost": 2300, "rating": 4.4, "hours": "8 AM - 6 PM"},
        {"name": "HealthFirst Pharmacy", "services": ["Medication Refills", "Vaccinations"], "cost": 800, "rating": 4.5, "hours": "10 AM - 9 PM"},
    ],
    'J': [
        {"name": "Medical Hub", "services": ["Dentistry", "General Medicine"], "cost": 1500, "rating": 4.1, "hours": "9 AM - 5 PM"},
        {"name": "Heart Care Clinic", "services": ["Cardiology", "General Medicine"], "cost": 2000, "rating": 4.2, "hours": "7 AM - 5 PM"},
        {"name": "MediQuick Pharmacy", "services": ["Prescription Medicines", "Immunizations"], "cost": 600, "rating": 4.4, "hours": "10 AM - 8 PM"},
        {"name": "HealthLine Diagnostics", "services": ["Ultrasound", "Bone Density Scans"], "cost": 3200, "rating": 4.6, "hours": "7 AM - 7 PM"},
    ],
}

# Dijkstra's Algorithm to find the shortest path from the current location
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = {node: False for node in graph}
    path = {}
    unvisited_nodes = list(graph.keys())
    
    while unvisited_nodes:
        min_node = None
        for node in unvisited_nodes:
            if min_node is None:
                min_node = node
            elif distances[node] < distances[min_node]:
                min_node = node
        
        for neighbor, weight in graph[min_node].items():
            if not visited[neighbor]:
                new_dist = distances[min_node] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    path[neighbor] = min_node
        
        visited[min_node] = True
        unvisited_nodes.remove(min_node)
    
    return distances

# Check if the clinic is open at the desired time
def is_clinic_open(clinic_hours, visit_time):
    open_time, close_time = clinic_hours.split(" - ")
    open_time = datetime.strptime(open_time, "%I %p")
    close_time = datetime.strptime(close_time, "%I %p")
    return open_time <= visit_time <= close_time

# Filter clinics based on user criteria
def filter_clinics(places, reachable_places, max_cost=None, service=None, min_rating=None, visit_time=None):
    results = []
    service = service.lower() if service else None
    
    for place in reachable_places:
        if place in places:
            for clinic in places[place]:
                clinic_services = [ s.lower() for s in clinic["services"]]
                if (max_cost is None or clinic["cost"] <= max_cost) and \
                   (service is None or service in clinic_services) and \
                   (min_rating is None or clinic["rating"] >= min_rating):
                    clinic["distance"] = reachable_places[place]
                    if visit_time:
                        clinic_open_status = is_clinic_open(clinic["hours"], visit_time)
                        clinic["status"] = "Open" if clinic_open_status else "Closed"
                    results.append(clinic)
    return results

# Display the filtered results
def display_clinics(filtered_clinics):
    if not filtered_clinics:
        print("No clinics match your criteria.")
    else:
        for clinic in filtered_clinics:
            print(f"Name: {clinic['name']}")
            print(f"Services: {', '.join(clinic['services'])}")
            print(f"Cost: {clinic['cost']}")
            print(f"Hours: {clinic['hours']}")
            print(f"Rating: {clinic['rating']}")
            print(f"Distance: {clinic['distance']} km")
            print(f"Status: {clinic.get('status', 'N/A')}")
            print("------------------------------")

# Main program
def main():
    print("Welcome to the Health Resource Locator!")
    user_location = input("Enter your current location (A-J): ").upper()
    if user_location not in distances:
        print("Invalid location. Exiting program.")
        return
    
    reachable_places = dijkstra(distances, user_location)
    
    try:
        max_cost = int(input("Enter your maximum budget (or press Enter to skip): ") or 0)
    except ValueError:
        max_cost = None
    
    # Extract all unique services from the places dictionary
    all_services = set()
    for city, facilities in places.items():
        for facility in facilities:
            all_services.update(facility["services"])

    # Display services and take input
    print("Available services:")
    for idx, service in enumerate(sorted(all_services), 1):
        print(f"{idx}. {service}")
    
    try:
        selected_service_index = int(input("Enter the number corresponding to the service you are looking for: "))
        selected_service = sorted(all_services)[selected_service_index - 1]
        print(f"You selected: {selected_service}")
    except (IndexError, ValueError):
        print("Invalid service selection. Proceeding without a specific service filter.")
        selected_service = None

    # Get maximum distance
    try:
        max_distance = float(input("Enter maximum distance (in km, or press Enter to skip): ") or float('inf'))
        if max_distance < 0:
            raise ValueError("Distance cannot be negative.")
    except ValueError:
        print("Invalid input for distance. Defaulting to no distance limit.")
        max_distance = float('inf')
    
    # Get minimum rating
    try:
        min_rating = float(input("Enter minimum rating (0-5, or press Enter to skip): ") or 0)
        if not (0 <= min_rating <= 5):
            raise ValueError("Rating must be between 0 and 5.")
    except ValueError:
        print("Invalid input for rating. Defaulting to 0.")
        min_rating = 0

    # Get visit time
    visit_time_input = input("Enter your desired visit time (e.g., '10 AM', '2 PM'): ")
    try:
        visit_time = datetime.strptime(visit_time_input, "%I %p")
    except ValueError:
        print("Invalid time format. Proceeding without time filter.")
        visit_time = None
    
    # Filter reachable places by distance
    reachable_places = {place: dist for place, dist in reachable_places.items() if dist <= max_distance}
    
    # Filter clinics based on criteria
    filtered_clinics = filter_clinics(
        places,
        reachable_places,
        max_cost=max_cost,
        service=selected_service,
        min_rating=min_rating,
        visit_time=visit_time
    )
    
    # Display filtered clinics
    print("\n--- Results ---")
    display_clinics(filtered_clinics)

if __name__ == "__main__":
    main()

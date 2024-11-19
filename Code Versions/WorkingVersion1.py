# Define the updated graph where every place is connected to every other place
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

# Clinic data (updated)
places = {
    'A': [
        {"name": "Green Valley Clinic", "services": ["General Medicine", "Dentistry"], "cost": 2000},
        {"name": "Sunrise Health Center", "services": ["Orthopedics", "Dermatology"], "cost": 2500}
    ],
    'B': [
        {"name": "Blue Cross Clinic", "services": ["Pediatrics", "General Medicine"], "cost": 1800},
        {"name": "Healing Hands", "services": ["Gynecology", "Physiotherapy"], "cost": 3000}
    ],
    'C': [
        {"name": "Care First Clinic", "services": ["Cardiology", "Dermatology"], "cost": 1500},
        {"name": "Wellness Center", "services": ["General Medicine", "Dentistry"], "cost": 2000}
    ],
    'D': [
        {"name": "City Health Hub", "services": ["Orthopedics", "General Medicine"], "cost": 1800},
        {"name": "Advanced Care Clinic", "services": ["Cardiology", "Dermatology"], "cost": 1400}
    ],
    'E': [
        {"name": "Eastside Care", "services": ["Gynecology", "General Medicine"], "cost": 2300},
        {"name": "MediPlus", "services": ["Dermatology", "Cardiology"], "cost": 3200}
    ],
    'F': [
        {"name": "Central Clinic", "services": ["Pediatrics", "General Medicine"], "cost": 2200},
        {"name": "Healing Touch Clinic", "services": ["Orthopedics", "Cardiology"], "cost": 2800}
    ],
    'G': [
        {"name": "Green Valley Clinic", "services": ["Cardiology", "General Medicine"], "cost": 2100},
        {"name": "Life Care Center", "services": ["Pediatrics", "Dermatology"], "cost": 2400}
    ],
    'H': [
        {"name": "Sunrise Clinic", "services": ["Orthopedics", "Gynecology"], "cost": 2600},
        {"name": "Complete Health Center", "services": ["Cardiology", "General Medicine"], "cost": 1900}
    ],
    'I': [
        {"name": "Care Health Clinic", "services": ["Cardiology", "General Medicine"], "cost": 2700},
        {"name": "Healthy Life Center", "services": ["Orthopedics", "Pediatrics"], "cost": 2300}
    ],
    'J': [
        {"name": "Medical Hub", "services": ["Dentistry", "General Medicine"], "cost": 1500},
        {"name": "Heart Care Clinic", "services": ["Cardiology", "General Medicine"], "cost": 2000}
    ]
}

# Dijkstra's Algorithm to find the shortest path from the current location
def dijkstra(graph, start):
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = {node: False for node in graph}
    path = {}

    # Initialize unvisited nodes
    unvisited_nodes = list(graph.keys())
    
    while unvisited_nodes:
        # Find the node with the smallest distance
        min_node = None
        for node in unvisited_nodes:
            if min_node is None:
                min_node = node
            elif distances[node] < distances[min_node]:
                min_node = node
        
        # Check the neighbors of the current node
        for neighbor, weight in graph[min_node].items():
            if not visited[neighbor]:
                new_dist = distances[min_node] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    path[neighbor] = min_node
        
        visited[min_node] = True
        unvisited_nodes.remove(min_node)

    return distances

# Filter clinics based on user criteria (updated for case insensitivity)
def filter_clinics(places, reachable_places, max_cost=None, service=None):
    results = []
    service = service.lower() if service else None  # Make user input lowercase for case-insensitivity
    
    for place in reachable_places:
        if place in places:
            for clinic in places[place]:
                # Normalize the service names to lowercase and compare with the user input
                clinic_services = [s.lower() for s in clinic["services"]]
                
                if (max_cost is None or clinic["cost"] <= max_cost) and \
                   (service is None or service in clinic_services):
                    clinic["distance"] = reachable_places[place]
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
            print(f"Distance: {clinic['distance']} km")
            print("------------------------------")

# Main program
def main():
    print("Welcome to the Health Resource Locator!")
    
    # Step 1: Get user location
    user_location = input("Enter your current location (A-J): ").upper()
    if user_location not in distances:
        print("Invalid location. Exiting program.")
        return
    
    # Step 2: Calculate distances
    reachable_places = dijkstra(distances, user_location)
    
    # Step 3: Get user preferences
    try:
        max_cost = int(input("Enter your maximum budget (or press Enter to skip): ") or 0)
    except ValueError:
        max_cost = None
    service = input("Enter a service you need (or press Enter to skip): ").strip()
    max_distance = float(input("Enter maximum distance (in km, or press Enter to skip): ") or float('inf'))
    
    # Filter reachable places by max distance
    reachable_places = {place: dist for place, dist in reachable_places.items() if dist <= max_distance}
    
    # Step 4: Filter clinics based on preferences
    filtered_clinics = filter_clinics(places, reachable_places, max_cost if max_cost else None, 
                                      service if service else None)
    
    # Step 5: Display results
    print("\n--- Results ---")
    display_clinics(filtered_clinics)

if __name__ == "__main__":
    main()

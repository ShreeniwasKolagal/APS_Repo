import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Define the graph
G = nx.DiGraph()

# Add nodes
nodes = ['SuperSource', 'AirportA', 'AirportB', 'StationC', 'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'Venue']
G.add_nodes_from(nodes)

# Add edges with capacities
def add_edges(G):
    edges = [
        ('SuperSource', 'AirportA', 1000),
        ('SuperSource', 'AirportB', 1000),
        ('SuperSource', 'StationC', 1000),
        ('AirportA', 'J1', 30),
        ('AirportB', 'J1', 25),
        ('StationC', 'J2', 20),
        ('J1', 'J3', 35),
        ('J2', 'J3', 15),
        ('J3', 'J4', 25),
        ('J3', 'J6', 10),
        ('J4', 'Venue', 15),
        ('Venue', 'J5', 20),
        ('J5', 'J6', 10),
        ('J5', 'Venue', 40)
    ]

    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity, current_load=0)

add_edges(G)

# Step 2: Initialize people at entry points
people_at = {node: 0 for node in nodes}
people_at['AirportA'] = 1000
people_at['AirportB'] = 1000
people_at['StationC'] = 1000

# Step 3: Movement simulation with night restrictions and emergency doubling
def simulate_movement(G, people_at, hours=10, night_start_hour=6, emergency_hour=5, night_blocked_edges=None):
    history = []

    if night_blocked_edges is None:
        night_blocked_edges = [('AirportA', 'J1'), ('AirportB', 'J1')]

    for hour in range(hours):
        new_people_at = people_at.copy()
        moved_this_hour = 0

        # Emergency crowd doubling
        if hour == emergency_hour:
            print("Emergency! Doubling crowds at entry points!")
            new_people_at['AirportA'] *= 2
            new_people_at['AirportB'] *= 2
            new_people_at['StationC'] *= 2

        for node in people_at:
            outgoing_edges = list(G.out_edges(node, data=True))
            if not outgoing_edges:
                continue

            people_to_move = people_at[node]
            if people_to_move == 0:
                continue

            for u, v, data in outgoing_edges:
                # Night time restrictions
                if hour >= night_start_hour and (u, v) in night_blocked_edges:
                    continue

                capacity = data['capacity']

                move_count = min(capacity, people_to_move)

                if move_count > 0:
                    new_people_at[u] -= move_count
                    new_people_at[v] += move_count
                    moved_this_hour += move_count

        people_at = new_people_at
        history.append((hour, people_at.copy(), moved_this_hour))

        print(f"Hour {hour+1}: {moved_this_hour} people moved.")

    return history

# Step 4: Plotting (Optional)
def plot_graph(G):
    pos = nx.spring_layout(G, seed=42)
    capacities = nx.get_edge_attributes(G, 'capacity')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=capacities)
    plt.show()

# Step 5: Analytics
def plot_analytics(history):
    hours = [h[0] for h in history]
    people_at_venue = [h[1]['Venue'] for h in history]
    moved = [h[2] for h in history]

    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    plt.plot(hours, people_at_venue, marker='o')
    plt.title('People at Venue Over Time')
    plt.xlabel('Hour')
    plt.ylabel('People at Venue')

    plt.subplot(1,2,2)
    plt.plot(hours, moved, marker='x', color='red')
    plt.title('People Moved Each Hour')
    plt.xlabel('Hour')
    plt.ylabel('People Moved')

    plt.tight_layout()
    plt.show()

# Step 6: Run everything
plot_graph(G)
history = simulate_movement(G, people_at, hours=12)
plot_analytics(history)

# Step 7: Final People Distribution
final_state = history[-1][1]
print("\nFinal People Distribution:")
for node, count in final_state.items():
    print(f"{node}: {count} people")

# Step 8: Detect bottlenecks
def detect_bottlenecks(final_state, threshold=100):
    print("\nBottleneck nodes (more than", threshold, "waiting people):")
    for node, people in final_state.items():
        if people > threshold and node not in ['Venue']:
            print(f"- {node}: {people} people stuck!")

detect_bottlenecks(final_state)
import math
import sys
from collections import defaultdict, deque
import heapq


def to_radians(deg):
    return deg * math.pi / 180

def distance_on_sphere(lat1, lon1, lat2, lon2):
    
    R = 6371.0  
    phi1, phi2 = to_radians(lat1), to_radians(lat2)
    delta_phi = to_radians(lat2 - lat1)
    delta_lambda = to_radians(lon2 - lon1)
    
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def calculate_angle(A, B):
    dot_product = sum(a * b for a, b in zip(A, B))
    norm_A = math.sqrt(sum(a ** 2 for a in A))
    norm_B = math.sqrt(sum(b ** 2 for b in B))
    return math.acos(dot_product / (norm_A * norm_B))

def absolute_curvature(points):
    
    n = len(points)
    total_ac = 0
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        p3 = points[(i + 2) % n]
        
      
        A = [p2[j] - p1[j] for j in range(3)]
        B = [p3[j] - p2[j] for j in range(3)]
        
       
        angle = calculate_angle(A, B)
        total_ac += abs(angle)
    
    return total_ac / (2 * math.pi)


def read_input():
    n = int(input())
    nodes = {}
    for _ in range(n):
        node_id, lat, lon = input().split()
        nodes[int(node_id)] = (float(lat), float(lon))

    m = int(input())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    t = int(input())
    users = []
    for _ in range(t):
        user_id, lat, lon = input().split()
        users.append((int(user_id), float(lat), float(lon)))

    return nodes, edges, users


def build_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def find_cycles(graph):
    visited = set()
    cycles = []

    def bfs_cycle(node):
        queue = deque([(node, [node])])
        while queue:
            current, path = queue.popleft()
            for neighbor in graph[current]:
                if neighbor == path[0] and len(path) > 2:
                    cycles.append(path)
                elif neighbor not in path:
                    queue.append((neighbor, path + [neighbor]))

    for node in graph:
        if node not in visited:
            bfs_cycle(node)
            visited.add(node)
    
    return cycles


def assign_users_to_polygons(users, cycles, nodes):
    user_assignments = [[] for _ in range(len(cycles))]
    for user_id, lat, lon in users:
        min_dist = float('inf')
        assigned_polygon = -1
        for i, cycle in enumerate(cycles):
            
            cycle_coords = [nodes[node] for node in cycle]
            center_lat = sum(coord[0] for coord in cycle_coords) / len(cycle_coords)
            center_lon = sum(coord[1] for coord in cycle_coords) / len(cycle_coords)
            dist = distance_on_sphere(lat, lon, center_lat, center_lon)
            if dist < min_dist:
                min_dist = dist
                assigned_polygon = i
        user_assignments[assigned_polygon].append(user_id)
    return user_assignments

def main():
   
    nodes, edges, users = read_input()
    
    
    graph = build_graph(edges)
    
    
    cycles = find_cycles(graph)
    
 
    user_assignments = assign_users_to_polygons(users, cycles, nodes)
    
   
    print(len(cycles))
    for i, cycle in enumerate(cycles):
        print(len(cycle))
        print(" ".join(map(str, cycle)))
        print(len(user_assignments[i]))
        print(" ".join(map(str, user_assignments[i])))

if __name__ == "__main__":
    main()

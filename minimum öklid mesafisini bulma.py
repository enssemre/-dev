import math

def euclidean_distance(point1, point2):
    return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))

points=[]
for i in range(2):
    x = float(input(f"{i+1}. noktanin x koordinatini girin: "))
    y = float(input(f"{i+1}. noktanin y koordinatini girin: "))
    points.append((x, y))
distance = euclidean_distance(points[0], points[1])
print(f"İki nokta arasindaki Öklid mesafesi: {distance:.2f}")
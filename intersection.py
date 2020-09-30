import shapely
from shapely.geometry import LineString, Point

# [(318, 3), (318, 722), (636, 722), (636, 6)]
# [(2, 241), (959, 242), (963, 484), (0, 484)]
A = (960,0)
B = (0, 720)

#line 2
C = (0, 0)
D = (960, 720)

line1 = LineString([A, B])
line2 = LineString([C, D])

int_pt = line1.intersection(line2)
point_of_intersection = int_pt.x, int_pt.y

print(point_of_intersection)
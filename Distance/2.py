# DISTANCE FORMULA
# Euclidean Distance
# Euclidean Distance is the most commonly used distance formula. To find the Euclidean distance between two points, we first calculate the squared distance between each dimension. If we add up all of these squared differences and take the square root, we’ve computed the Euclidean distance.

def euclidean_distance(pt1, pt2):
  distance = 0
  for i in range(len(pt1)):
    distance += (pt1[i]-pt2[i]) ** 2

  return distance**(1/2)

print(euclidean_distance([1,2],[4,0]))
print(euclidean_distance([5,4,3],[1,7,9]))
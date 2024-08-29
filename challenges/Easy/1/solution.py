from math import sqrt

def check_if_points_is_legit(points):
    if points is None or not isinstance(points, list) or points == []:
        raise ValueError("The parameter 'points' has to be a valid list, filled with tuples of numbers.")
    
    for point in points:
        if isinstance(point, tuple) and len(point) == 2:
            if not all(isinstance(i, (int, float)) for i in point):
                raise ValueError("The parameter points is a list, but it's not legit, check the input.")

    
def compute_steps_to_go_through_all_points(points):
    """
    Args:
        points_list (list): [(x1, y1), (x2, y2), ...]
    """
    check_if_points_is_legit(points)
     
    current_point = None
    steps_through_all_points = 0

    for next_point in points:
        if current_point is None or current_point == next_point:
            current_point = next_point
            continue
        
        x_current_point, y_current_point = current_point
        x_next_point, y_next_point = next_point
    
        distance_between_x = abs(x_current_point - x_next_point)
        distance_between_y = abs(y_current_point - y_next_point)
            
        if x_current_point == x_next_point:
            steps_through_all_points += distance_between_y
        elif y_current_point == y_next_point:
            steps_through_all_points += distance_between_x
        else: # diagonal path
            """
            This is tricky: to determine the maximum steps you can take along the
            diagonal, take the smaller of the two distances: 
            max_diagonal_steps = min(distance_between_x, distance_between_y).
            The remaining steps on the non-diagonal axis would be the difference 
            between the greater distance and max_diagonal_steps, but in the end,
            the total number of steps required is simply the greater of the two distances.
            This means the additional calculations are unnecessary.
            """
            steps_through_all_points += max(distance_between_x, distance_between_y)
        
        current_point = next_point
            
     
    return steps_through_all_points


input_str = input("Enter a list of points in the format [(x1, y1), (x2, y2), ...]: ")
points = eval(input_str)
necessary_steps = compute_steps_to_go_through_all_points(points)
print(f"The number of necessary steps to go through all points is {necessary_steps}")
        
    
    
    
    
    


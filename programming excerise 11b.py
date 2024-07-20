import math

def calculate_hypotenuse(angle_degrees, adjacent_length):
    """
    Calculate the length of the hypotenuse of a right triangle given an angle and the adjacent side length.

    :param angle_degrees: The nearest angle in degrees.
    :param adjacent_length: The length of the adjacent side.
    :return: The length of the hypotenuse.
    """
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate the hypotenuse using the cosine of the angle
    hypotenuse_length = adjacent_length / math.cos(angle_radians)

    return hypotenuse_length

# Example usage:
angle = 30  # nearest angle in degrees
adjacent = 10  # length of the adjacent side
hypotenuse = calculate_hypotenuse(angle, adjacent)
print(f"The length of the hypotenuse is: {hypotenuse:.2f}")

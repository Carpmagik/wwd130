import math

print("Welcome to the Velocity Calulator. Please enter the following: ")

mass = float(input("Mass:"))
gravity = float(input("Gravity: "))
time = float(input("Time: "))
density = float(input("Density (km/g^3, 1.3 for air, 1000 for water): "))
cross_area = float(input("Cross Sectional Area: "))
drag = float(input("0.5 for sphere, 1.1 for cylinder: "))

c = (1 / 2) * (density) * (cross_area) * (drag)

mathe = math.sqrt(mass * gravity / c) * (1 - math.exp((-math.sqrt(mass * gravity * c) / mass) * time))


print(f"The inner value of c is : {c:.3f}")
print(f"The velocity after {time} seconds is: {mathe:.3f} m/s")
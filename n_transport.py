import math as m
import random as r
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')

lambda_a = 20 # Absorption mean free path.
lambda_s = 0.5 # Scattering mean free path.

sigma_a = 1/lambda_a # Absorption macroscopic cross section.
sigma_s = 1/lambda_s # Scattering macroscopic cross section.

sigma_t = sigma_a + sigma_s # Total cross section.

lambda_t = 1/sigma_t # Total mean free path.

nparticles = 100

average = 0

# For n neutrons:

for i in range(nparticles):
    
    is_absorbed = 0
    
    # Start at origin.
    x = 0
    y = 0
    z = 0
    
    ncollisions = 0
    
    while is_absorbed == 0:
        # Initialize distance for neutron to travel.
        s = -lambda_t * m.log(r.random())
        
        # Initialize random direction: [-pi, pi] for theta, [0, 2pi] for phi.
        theta = m.asin(-1 + 2 * r.random())
        phi = 2 * m.pi * r.random()
        
        # Convert distance into steps in x, y, z.
        # Neutrons travel out spherically.
        dx = s * m.cos(theta) * m.cos(phi)
        dy = s * m.cos(theta) * m.sin(phi)
        dz = s * m.sin(theta)
        
        # Increment coordinates.
        x = x + dx
        y = y + dy
        z = z + dz
        
        ncollisions += 1
        
        # sigma_a / sigma_t is what proportion of the total macroscopic x section is absorption.
        # If the random number is less than this ratio, the neutron is absorbed.
        if r.random() < sigma_a / sigma_t:
            print("Number of collsions to absorption: ")
            print(ncollisions)
            is_absorbed = 1 # End program for neutron.
            ax.scatter(x, y, z) # Plot neutron final position before absorption.
            distance = m.sqrt(x ** 2 + y ** 2 + z ** 2)
            average += distance
    
average = average/nparticles

print("Average distance travelled: ")
print(average)

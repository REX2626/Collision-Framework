# Collision Framework

# TODO:

Add multile collisions touching at the same time

Add rotation
Check for collision by using pixel masks?
Find a way to work out when they will collide

Collisions will make moments, which will rotate a square
The moment will occur wherever the square touches the other square

Improve stability, fix any edge cases

Improve performance if possible

# Done:

Add basic pygame display

Add basic square objects

Make square objects move around, bouncing off walls

Make positions and velocities be fractions instead of floats (built in fractions or self made)

Make time move forward until there is a collision, then do the collision
To do the collision: swap the velocities of the objects

Add multiple collisions per frame

Add multiple collision at same the time

## Potential:

Make a soft body square, 4 corners are the points
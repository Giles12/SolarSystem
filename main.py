from ursina import *
import numpy as np

def update():
    global t
    t = t + 0.0005
    angle = np.pi * 40 / 180  # Convert degrees to radians

    # Mercury orbit
    radius_1 =1
    Mercury.x = np.cos(t) * radius_1
    Mercury.z = np.sin(t) * radius_1

    # Venus orbit
    radius_2 = 1.4
    Venus.x = np.cos(t + angle) * radius_2
    Venus.z = np.sin(t + angle) * radius_2

    # Earth orbit
    radius_3 = 1.8
    Earth.x = np.cos(t + angle * 2) * radius_3
    Earth.z = np.sin(t + angle * 2) * radius_3

    # Mars orbit
    radius_4 = 2.2
    Mars.x = np.cos(t + angle * 3) * radius_4
    Mars.z = np.sin(t + angle * 3) * radius_4

    # Jupiter orbit
    radius_5 = 2.6
    Jupiter.x = np.cos(t + angle * 4) * radius_5
    Jupiter.z = np.sin(t + angle * 4) * radius_5

    # Saturn orbit
    radius_6 = 3
    Saturn.x = np.cos(t + angle * 5) * radius_6
    Saturn.z = np.sin(t + angle * 5) * radius_6

    # Uranus orbit
    radius_7 = 3.4
    Uranus.x = np.cos(t + angle * 6) * radius_7
    Uranus.z = np.sin(t + angle * 6) * radius_7

    # Neptune orbit
    radius_8 = 3.8
    Neptune.x = np.cos(t + angle * 7) * radius_8
    Neptune.z = np.sin(t + angle * 7) * radius_8

# Create the Ursina app
app = Ursina()

# Sun and planet entities
sun = Entity(model="sphere", color=color.yellow, scale=1.5)
Mercury = Entity(model="sphere", color=color.gray, scale=0.2)
Venus = Entity(model="sphere", color=color.orange, scale=0.3)
Earth = Entity(model="sphere", color=color.blue, scale=0.4)
Mars = Entity(model="sphere", color=color.violet, scale=0.3)
Jupiter = Entity(model="sphere", color=color.red, scale=0.6)
Saturn = Entity(model="sphere", color=color.white, scale=0.5)
Neptune = Entity(model="sphere", color=color.cyan, scale=0.5)
Uranus = Entity(model="sphere", color=color.gold, scale=0.5)

# Initialize time for orbits
t = -np.pi

editor_camera = EditorCamera()

# Register the update function
app.run()

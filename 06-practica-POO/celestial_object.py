import pygame

class CelestialObject:
   def __init__(self, image_path, mass, distance=0, orbit_speed=0):
      self.image_path = image_path
      self.distance = distance
      self.orbit_speed = orbit_speed
      self.mass = mass
   
   def draw(self):
      pass
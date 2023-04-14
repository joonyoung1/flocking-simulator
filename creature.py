from vector import Vector
from random import normalvariate, randint
from const import *


class Creature:
    def __init__(self, x, y):
        self.pos = Vector(x, y)
        self.velocity = Vector(normalvariate(0, 1), normalvariate(0, 1))
    
    def update(self, others, obstacles, foods, factors):
        alignment = Vector(0, 0)
        cohesion = Vector(0, 0)
        separation = Vector(0, 0)

        near_count = 0
        separation_count = 0
        for other in others:
            if other == self:
                continue
        
            dist = self.distance(other)
            if dist > factors['View Range']:
                continue
            
            near_count += 1
            alignment += other.velocity
            cohesion += other.pos - self.pos

            if dist <= factors['Avoid Range']:
                separation_count += 1
                separation += (self.pos - other.pos).normalize() * (factors['Avoid Range'] - dist)
        
        if near_count > 0:
            alignment /= near_count
            cohesion /= near_count
        if separation_count > 0:
            separation /= separation_count

        self.velocity += alignment * factors['Alignment']
        self.velocity += cohesion * factors['Cohesion']
        self.velocity += separation * factors['Separation']

        avoidance = Vector(0, 0)
        avoid_count = 0
        for obstacle in obstacles:
            dist = self.distance(obstacle)
            if dist > factors['View Range']:
                continue

            avoid_count += 1
            avoidance += (self.pos - obstacle.pos).normalize() * (factors['View Range'] - dist)
        if avoid_count > 0:
            avoidance /= avoid_count
        self.velocity += avoidance * factors['Avoidance']

        seaking = Vector(0, 0)
        food_count = 0
        for food in foods:
            dist = self.distance(food)
            if dist > factors['View Range']:
                continue
            
            food_count += 1
            seaking += (food.pos - self.pos)
            if dist < 15:
                food.pos.x = randint(0, SCREEN_WIDTH)
                food.pos.y = randint(0, SCREEN_HEIGHT)
        if food_count > 0:
            seaking /= food_count
        self.velocity += seaking * factors['Seeking']

        self.velocity.normalize()
        self.velocity *= factors['Max Speed']

        self.pos += self.velocity

        if self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH
        elif self.pos.x > SCREEN_WIDTH:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = SCREEN_HEIGHT
        elif self.pos.y > SCREEN_HEIGHT:
            self.pos.y = 0

    def distance(self, other):
        return ((self.pos.x - other.pos.x)**2 + (self.pos.y - other.pos.y)**2)**0.5
    
    def body_points(self):
        dx = self.velocity.x
        dy = self.velocity.y

        m = (dx*dx + dy*dy)**0.5
        dx, dy = (dx / m * CREATURE_SIZE, dy / m * CREATURE_SIZE) if m > 0 else (1, 0)

        pts = [(-0.5, -0.866), (-0.5, 0.866), (2.0, 0.0)]
        pts = [(self.pos.x + p[0] * dx + p[1] * dy, self.pos.y + p[0] * dy - p[1] * dx) for p in pts]
        return pts

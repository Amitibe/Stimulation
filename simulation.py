import os
os.system("pip install pygame")
os.system("pip install matplotlib")
import pygame
import random
import time
import matplotlib.pyplot as plt
import classes
from classes import *

# Initialize Pygame and setup constents
pygame.init()
BORDER_X_SIZE =1000
BORDER_Y_SIZE = 800
WANT_HUNTERS = True
NUMBER_OF_FOOD = 50
NUMBER_OF_CREATURES = 20
NUMBER_OF_HUNTERS = 2 

# Set the screen size and caption
size = (BORDER_X_SIZE, BORDER_Y_SIZE)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Evolution Simulation")
bg_color = (255, 255, 255)
min_speed = 0.01
max_speed = 50
def get_color(speed):
    if 0 < speed <= 1:
        return (41,189,24)
    if 1 < speed <= 2:
        return (33,165,213)
    if 2 < speed <= 3:
        return (87,33,213)
    if 3 < speed <= 5:
        return (236,36,229)
def check_collision(creature, food):
    distance = ((creature.get_x() - food.get_x()) ** 2 + (creature.get_y() - food.get_y()) ** 2) ** 0.5
    if distance <= creature.get_radius() + food.get_radius():
        return True
    else:
        return False

#create a list of creatures
alive_c = []
for i in range(NUMBER_OF_CREATURES):
    c = creature(random.randint(0,100000))
    c.set_x(random.randint(0,BORDER_X_SIZE))
    c.set_y(random.randint(0,BORDER_Y_SIZE))
    c.set_color((0, 254, 0))
    c.set_y_dr(random.uniform(-3,3))
    c.set_x_dr(random.randint(-3,3))
    c.set_radius(random.randint(12, 18))
    c.set_speed(20/c.get_radius())
    alive_c.append(c)
alive_h = []
if WANT_HUNTERS:
    for i in range(NUMBER_OF_HUNTERS):
        c = hunter(random.randint(0,100000))
        c.set_x(random.randint(0,BORDER_X_SIZE))
        c.set_y(random.randint(0,BORDER_Y_SIZE))
        c.set_color((0, 0, 0))
        c.set_radius(random.randint(12,18))
        c.set_y_dr(random.uniform(-3,3))
        c.set_x_dr(random.randint(-3,3))
        c.set_speed(15/c.get_radius())
        alive_h.append(c)
list_of_food = []
list_of_speed = [[None]]
list_of_radui = [[None]]
list_of_Pchance = [[None]]
running = True
count = 0
all_dead = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    life = True
    if count ==20 or all_dead == True:
        break
    for i in range(NUMBER_OF_FOOD):
        f = classes.food()
        f.set_y(random.randint(0, BORDER_Y_SIZE))
        f.set_x(random.randint(0, BORDER_X_SIZE))
        list_of_food.append(f)
    starttime = time.time()
    while life:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(bg_color)
        for food in list_of_food:
            pygame.draw.circle(screen, food.get_color(), (food.get_x(), food.get_y()), food.get_radius())
        for creature in alive_c:
            creature.set_x((creature.get_x()+creature.get_xdr()*creature.get_speed()))
            creature.set_y((creature.get_y()+creature.get_ydr()*creature.get_speed()))
            if creature.get_x() < 0 or creature.get_x() > BORDER_X_SIZE:
                creature.set_x_dr(-creature.get_xdr())
            if creature.get_y() < 0 or creature.get_y() > BORDER_Y_SIZE:
                creature.set_y_dr(-creature.get_ydr())
            pygame.draw.circle(screen, creature.get_color(), (creature.get_x(), creature.get_y()), creature.get_radius())
            for food in list_of_food:
                if check_collision(creature, food):
                    list_of_food.remove(food)
                    creature.set_hunger(creature.get_hunger() +1)
        for hunter in alive_h:
            hunter.set_x(hunter.get_x()+hunter.get_xdr()*hunter.get_speed())
            hunter.set_y(hunter.get_y()+hunter.get_ydr()*hunter.get_speed())
            if hunter.get_x() < 0 or hunter.get_x() > BORDER_X_SIZE:
                hunter.set_x_dr(-hunter.get_xdr())
            if hunter.get_y() < 0 or hunter.get_y() > BORDER_Y_SIZE:
                hunter.set_y_dr(-hunter.get_ydr())
            pygame.draw.circle(screen, hunter.get_color(),(hunter.get_x(),hunter.get_y()),hunter.get_radius())
            for creature in alive_c:
                numb = random.randint(0,100)
                chance_of_dying = 100 - creature.get_protection_chance()
                if check_collision(hunter,creature) and hunter.get_radius()>creature.get_radius() and numb < chance_of_dying:
                    alive_c.remove(creature)
                    hunter.set_hunger(hunter.get_hunger()+1)
        if len(list_of_food) == 0:
            life = False
        if len(alive_c) == 0 and len(alive_h) == 0:
            all_dead = True
            print("all dead")
            break
        if time.time()-starttime >10:
            print("was stuck, continuing")
            list_of_food.clear()
            break
        pygame.display.update()
    print(f"day {count} : {len(alive_c)}")
    list_of_speed.append([None])
    list_of_radui.append([None])
    list_of_Pchance.append([None])
    removelst_c = []
    shouldrepoduce =[]
    huntershouldrepreduce = []
    removelst_h = []
    for hunter in alive_h:
        if hunter.get_hunger() == 0:
            removelst_h.append(hunter)
        elif hunter.get_hunger() >=2:
            huntershouldrepreduce.append(hunter)
        else:
            hunter.set_hunger(0)
    for creature in alive_c:
        list_of_radui[count].append(creature.get_radius())
        list_of_Pchance[count].append(creature.get_protection_chance())
        list_of_speed[count].append(creature.get_speed())
        if creature.get_hunger() == 0:
            removelst_c.append(creature)
        elif creature.get_hunger() >= 2:
            shouldrepoduce.append(creature)
        else:
            creature.set_hunger(0)

    for o in removelst_c:
        alive_c.remove(o)
    for o in removelst_h:
        alive_h.remove(o)
    for hunter in huntershouldrepreduce:
        c = classes.hunter(hunter.get_name()+1)
        c.set_x(hunter.get_x())
        c.set_y(hunter.get_y())
        c.set_y_dr(random.uniform(-1, 1))
        c.set_x_dr(random.randint(-1, 1))
        r = hunter.get_radius() * random.uniform(0.5, 1.5)
        c.set_radius(r)
        c.set_speed(15/r)
        alive_h.append(c)
        hunter.set_hunger(0)
    for creature in shouldrepoduce:
        c = classes.creature(creature.get_name() + 1)
        c.set_x(creature.get_x())
        c.set_y(creature.get_y())
        c.set_y_dr(random.uniform(-3, 3))
        c.set_x_dr(random.randint(-3, 3))
        c.set_protection_chance(creature.get_protection_chance() + random.randint(-10,10))
        r = creature.get_radius()*random.uniform(0.5,1.5)
        if r <=4:
            r = 4
        c.set_radius(r)
        c.set_speed(20/c.get_radius())
        c.set_color(get_color(creature.get_speed()))
        alive_c.append(c)
        creature.set_hunger(0)

    count = count + 1

del list_of_speed[-1]
del list_of_radui[-1]
del list_of_Pchance[-1]
for i in list_of_Pchance:
    del i[0]
    print(f"{i})", end=" ")
print()
for i in list_of_speed:
    del i[0]
    print(len(i), end=" ")
print()
for i in list_of_radui:
    del i[0]
    print(len(i), end=" ")
xix = []
for i in range(len(list_of_speed)):
    xix.append(i)
avrerage_size = []
average_speed =[]
avrerage_pchance =[]
sum =0
try:
    for b in list_of_speed:
        sum = 0
        for g in b:
          sum +=g
        average_speed.append(sum / len(b))
    for b in list_of_radui:
        sum=0
        for g in b:
            sum +=g
        avrerage_size.append(sum/len(b))
    for b in list_of_Pchance:
        sum = 0
        for g in b:
            sum +=g
        avrerage_pchance.append(sum/len(b))
    print()
    print(len(xix))
    print(len(avrerage_pchance))
    plt.plot(xix,avrerage_pchance)
    plt.show()
    plt.plot(xix, average_speed, label="Speed")
    plt.plot(xix, avrerage_size, label="Size ")
    plt.title("Size and Speed over generations")
    plt.ylabel("Speed")
    plt.xlabel("gen")
    plt.legend()
    plt.show()
    plt.stackplot(xix, avrerage_size, average_speed, colors=["blue", "red"])
    plt.title("Speed and size over generations plot")
    plt.show()
    plt.plot(avrerage_size, average_speed)
    plt.title("Speed over Size")
    plt.ylabel("Speed")
    plt.xlabel("Size")
    plt.show()
except:
    print("everyone died")


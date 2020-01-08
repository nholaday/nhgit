from sys import exit

class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass


class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        print "You enter the Central Corridor"
        room = raw_input("> ")
        return room

    select = enter("hi")
    if "Laser" in select:
        LaserWeaponArmory()

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_next):
        pass

    def opening_scene(self):
        pass


#a_map = Map('central_corridor')
#a_game = Engine(a_map)
#a_game.play()
#

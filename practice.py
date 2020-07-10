class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'


class Bike:
    def noise(self):
        return 'On your left'

    def pedal(self):
        return 'Pedaling!'


class Loud:
    def noise(self):
        return super().noise().upper()
        # super() delegates to the next class on the MRO


class LoudDog(Loud, Dog):
    '''
    MRO:
    (<class '__main__.LoudDog'>,
    <class '__main__.Loud'>,
    <class '__main__.Dog'>,
    <class 'object'>)
    '''
    pass


class LoudBike(Loud, Bike):
    pass


misty = Dog()
chari = Bike()
yapper = LoudDog()
print(yapper.noise())
print(LoudDog.__mro__)
print(Loud.__dict__)


'''
for cls in LoudDog.__mro__:
    if 'noise' in cls.__dict__:
        if super():
            continue
        else:
            break
'''

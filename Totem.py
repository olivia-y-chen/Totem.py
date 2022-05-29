"""
Created on 9/10/2021

@author: Olivia Chen
"""
import random

if __name__ == '__main__':
    """print("\nfixed totem\n")

    totem_fixed()

    print("\nself totem\n")

    totem_selfie()

    print("\nrandom totem\n")

    totem_random()"""

def part_hair_balding():
    """Returns a string that is balding hair and forehead"""
    a = r" |||||      ||||| " + "\n"
    a += r" ================ "
    return a

def part_hair_long():
    """Returns a string that is long straight hair"""
    a = r" |||||||||||||||| " + "\n"
    a += r" |||||||||||||||| " + "\n"
    a += r" |||||||||||||||| "
    return a

def part_hair_curvy():
    """Returns a string that is curvy hair"""
    a = r" (((((((((((((((( " + "\n"
    a += r" )))))))))))))))) " + "\n"
    a += r" (((((((((((((((( "
    return a

def part_nose_nostrils():
    """Returns a string that has large nostrils"""
    a = r" |      ||      | " + "\n"
    a += r" |     (OO)     | "
    return a

def part_nose_pointy():
    """Returns a string that has pointy nose"""
    a = r" |       |      | " + "\n"
    a += r" |       >      | "
    return a

def part_nose_round():
    """Returns a strung that has round nose"""
    a = r" |      |       | " + "\n"
    a += r" |      _)      | "
    return a

def part_mouth_open():
    """Returns a string that is an open mouth with a chin"""
    a =  r" |      __      | " + "\n"
    a += r" |     (__)     | " + "\n"
    a += r"  \            /  " + "\n"
    a += r"   \__________/   "
    return a

def part_mouth_frown():
    """Returns a string that is a frowny mouth with a chin"""
    a = r" |      __      | " + "\n"
    a += r" |     /  \     | " + "\n"
    a += r"  \            /  " + "\n"
    a += r"   \__________/   "
    return a

def part_mouth_smile():
    """Returns a string that is a smiley mouth with a chin"""
    a = r" |              | " + "\n"
    a += r" |     \__/     | " + "\n"
    a += r"  \            /  " + "\n"
    a += r"   \__________/   "
    return a

def part_eyes_tired():
    """Returns a string that are tired eyes"""
    a = r" |              | " + "\n"
    a += r" |  O       O   | " + "\n"
    a += r" | _/        \_ | "
    return a

def part_eyes_large():
    """Returns a string that are large eyes"""
    a = r" |   _      _   | " + "\n"
    a += r" |  ( )    ( )  | " + "\n"
    a += r" |   ^      ^   | "
    return a

def part_eyes_squinty():
    """Returns a string that are squinty eyes"""
    a = r" |              | " + "\n"
    a += r" |  \>      </  | " + "\n"
    a += r" |              | "
    return a

def selfie_band():
    """Returns netID within a band"""
    a = r" #--------------# " + "\n"
    a += r" |oyc4      oyc4| " + "\n"
    a += r" #--------------# "
    return a

def old_head():
    """Print a head that looks old with tired eyes, and open mouth, large nose, and balding hair"""
    print(part_hair_balding())
    print(part_eyes_tired())
    print(part_nose_nostrils())
    print(part_mouth_open())
    return

def angry_head():
    """Print a head that looks angry with long hair, angry eyes, frowny mouth, and pointh nose"""
    print(part_hair_long())
    print(part_eyes_squinty())
    print(part_nose_pointy())
    print(part_mouth_frown())
    return

def happy_head():
    """Print a head that looks happy with curly hair, large eyes, round nose, and smiley mouth"""
    print(part_hair_curvy())
    print(part_eyes_large())
    print(part_nose_round())
    print(part_mouth_smile())
    return

def totem_fixed():
    happy_face()
    angry_head()
    old_head()
    return

def head_with_hair(hairfunc):
    """Print a head with tired eyes, round nose, open mouth, but with a hair specified by hairfunc"""
    print(hairfunc())
    print(part_eyes_tired())
    print(part_nose_round())
    print(part_mouth_open())
    return

def head_with_nose(nosefunc):
    """Print a head with curly hair, large eyes, and a smiley face, but with a nose specified by nosefunc"""
    print(part_hair_curvy())
    print(part_eyes_large())
    print(nosefunc())
    print(part_mouth_smile())
    return

def head_with_eyes_mouth(eyefunc, mouthfunc):
    """Print a head with curly hair and pointy nose, but with eyes specified by eyefunc and a mouth specified by mouthfunc"""
    print(part_hair_curvy())
    print(eyefunc())
    print(part_nose_pointy())
    print(mouthfunc())
    return

def selfie(nosefunc, mouthfunc):
    """totem_selfie helper function that has curly hair and large eyes and a selfie band, but with a mouth specified by mouthfunc and a nose specified by nosefunc"""
    print(part_hair_curvy())
    print(selfie_band())
    print(part_eyes_large())
    print(nosefunc())
    print(mouthfunc())
    return

def totem_selfie():
    """Print a totem pole with selfie bands"""
    selfie(part_nose_pointy, part_mouth_open)
    selfie(part_nose_round, part_mouth_smile)
    selfie(part_nose_nostrils, part_mouth_frown)
    return

def head_random():
    """Print a head with randomly chosen features"""
    eyeList = [part_eyes_large, part_eyes_tired, part_eyes_squinty]
    noseList = [part_nose_nostrils, part_nose_pointy, part_nose_round]
    mouthList = [part_mouth_open, part_mouth_frown, part_mouth_smile]
    hairList = [part_hair_curvy, part_hair_balding, part_hair_long]
    w = eyeList[random.randint(0,2)]
    x = mouthList[random.randint(0,2)]
    y = hairList[random.randint(0,2)]
    z = noseList[random.randint(0,2)]
    head_with_hair(y)
    head_with_nose(z)
    head_with_eyes_mouth(w, x)
    return

def totem_random():
    """Print three random heads using head_random()"""
    head_random()
    head_random()
    head_random()
    return

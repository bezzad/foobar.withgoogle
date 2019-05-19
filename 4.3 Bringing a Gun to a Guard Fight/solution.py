# It have to be the one problem a raytracing engineer faced one day in his life and
# never forgot. Gosh it took me so much time to figure this one out, easily the hardest
# for me in this whole set of challenges. Basically you are in a room of given dimension
# and can shoot a laser beam that reflects on walls and you need to figure out exactly
# in which directions you can shoot so that it gets to your ennemy, given a max distance
# and your position. For that one problem I made a huge essay on how it works in the
# comments which I’m going to post below:
#
# The first thing you had to realize in order to solve this challenge is that you
# could simply mirror the room and check if the beam gets where you want. Let me
# show you:
# In our case let us make a room of dimension [3,2], with the position of the
# target at [1,2]. For the sake of simplicity let us imagine the beam is shot at
# [1,2] and so we are trying to shot ourselves. We get something like this:
#               -----
#               |*xx|
#               |xxx|
#               -----
# If we shoot with a vector of [1,0], aka straight ahead, we will get this result:
#               -----
#               |*~~|
#               |xxx|
#               -----
# We can see that the beam gets back to you directly, thanks to the reflection,
# and that the goal is achieved! But there is another way to do that:
#               ----- -----
#               |*~~| |~~*|
#               |xxx| |xxx|
#               ----- -----
# We can here realize that, by putting a mirror version of the room where the beam
# gets, we can make a straight line instead of calculating the reflection and see
# that it gets to our original target, [1,2], being ourselves!
# The good thing with that is that it also allows us to determine the distance
# needed by the beam to get through, and thus we can mirror the rooms up to the
# maximum distance easily.

# The next thing to realize was that room mirrors in a pattern, see the below
# diagram:
#               -----
#               |*xx|
#               |xxx|
#               -----
#      [...]    -----   [...]
#               |xxx|
#               |*xx|
#               -----
#   ----- ----- ----- ----- -----
#   |*xx| |xx*| |*xx| |xx*| |*xx|
#   |xxx| |xxx| |xxx| |xxx| |xxx|
#   ----- ----- ----- ----- -----
#               -----
#               |xxx|
#               |*xx|
#               -----
#      [...]    -----   [...]
#               |*xx|
#               |xxx|
#               -----
# x always repeats in the same way, and so does y
# Thus we need to figure out how to calculate how to mirror one room twice and we
# can make an entire atlas of mirrored rooms!
# In our case though the function below only calculates the mirrors of the point
# of coordinates node across an atlas of length (distance*2)^2

# Sooo the hard part about this was figuring out about the mirroring of the room.
# I was talking with a friend and when I told him about a specific thing that the
# problem stated on the rooms, that if you shoot in the corner it reflects perfectly
# we both had an Eureka moment: “Wait, isn’t the room reflection symmetric to itself?”
# and then I looked up some 2D plane mirroring(which leaded to a ton of maths I didn’t
# need actually and so I had to figure out a 1D transform on my own) and then just verify
# the angles and ensure the distance of the guard is before yourself.

import math

def mirror_atlas(node, dimensions, distance):
    node_mirrored = []
    for i in range(len(node)):
        points = []
        for j in range(-(distance//dimensions[i])-1, (distance//dimensions[i]+2)):
            points.append(get_mirror(j, node[i], dimensions[i]))
        node_mirrored.append(points)
    return node_mirrored


def get_mirror(mirror, coordinates, dimensions):
    res = coordinates
    mirror_rotation = [2*coordinates, 2*(dimensions-coordinates)]
    if(mirror < 0):
        for i in range(mirror, 0):
            res -= mirror_rotation[(i+1) % 2]
    else:
        for i in range(mirror, 0, -1):
            res += mirror_rotation[i % 2]
    return res


def solution(dimensions, your_position, guard_position, distance):
    mirrored = [mirror_atlas(your_position, dimensions,
                             distance), mirror_atlas(guard_position, dimensions, distance)]
    res = set()
    angles_dist = {}
    for i in range(0, len(mirrored)):
        for j in mirrored[i][0]:
            for k in mirrored[i][1]:
                beam = math.atan2((your_position[1]-k), (your_position[0]-j))
                l = math.sqrt((your_position[0]-j)**2 + (your_position[1]-k)**2)
                if [j, k] != your_position and distance >= l:
                    if((beam in angles_dist and angles_dist[beam] > l) or beam not in angles_dist):
                        if i == 0:
                            angles_dist[beam] = l
                        else:
                            angles_dist[beam] = l
                            res.add(beam)
    return len(res)

# ======================= Test Case ==========================================
if __name__ == "__main__":
    tests = [
        [
            [3, 2],
            [1, 1],
            [2, 1],
            400
        ],
    ]

    results = [0 for x in range(len(tests))]
    answers = [6, 16, 935, 2789, 2000000000, 23, 256, 141031256]
    timingsSum = [0 for x in range(len(tests))]
    testRuns = 10

    for j in range(1, testRuns + 1):
        print("Testing round: " + str(j))
        for i in range(len(tests)):
            results[i] = solution(tests[i][0], tests[i][1], tests[i][2], tests[i][3])

    for i, t in enumerate(timingsSum):
        print("Test " + str(i + 1) + " runtime: " + str(t/testRuns))

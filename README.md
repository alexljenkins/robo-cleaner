# Cleaner

### Problem Statement:
I'm way too 'busy' to vacuum my apartment

### Solution:
Build a vacuum cleaner that can do it for me!


###Solution Stages:
1. Visually display an agent moving over each available square in a KNOWN space.
2. Place the agent in an unknown map and get it to discover the entire space.
3. Place the agent randomly in the space and get it to quickly determine where
    it is in the KNOWN house by overlapping visited tiles to the map.
4. From any random location on the KNOWN map. Get the agent to calculate the
    shortest method to visit every available tile. Favoring room-by-room solving.
    (Requires 'room' recognition/definitions and a pathfinder/mapfinder.
5. Allow the agent to be curious in a known space. Thereby allowing it to
    experiment/attempt to travel to previously known 'object' tiles.
    Might use a gradient by saving each vacuum layout creating probabilities
    of a tile being free to vacuum or containing an object in it.
6. Optimize the discovery phase
7. Reduce the pixel size to allow for curves etc. increasing the 'cleaned'
    tiles per step.

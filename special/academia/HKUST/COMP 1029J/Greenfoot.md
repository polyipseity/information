---
aliases:
  - Greenfoot
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029J/Greenfoot
  - language/in/English
---

# Greenfoot

## installation

Follow the instructions on {@{<https://greenfoot.org/>}@}.

## usage

Explore the user interface yourself.

## documentation

### `Actor`

See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html>.

- `Actor` :@: `Actor()`: Remember to add to the world using `World#addObject`. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#%3Cinit%3E()>.
- `getObjectsInRange` :@: `<A> List<A> getObjectsInRange(int radius, Class<A> cls)`: `radius` in cells. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#getObjectsInRange(int,java.lang.Class)>.
- `getRotation` :@: `int getRotation()`: [0, 359]. 0 is east. Increase is clockwise. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#getRotation()>.
- `getX` :@: `int getX()`: See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#getX()>.
- `getY` :@: `int getY()`: See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#getY()>.
- `move` :@: `void move(int distance)`: `distance` in cells. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#move(int)>.
- `setRotation` :@: `void setRotation(int rotation)`: `rotation` is in [0, 359]. 0 is east. Increase is clockwise. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#setRotation(int)>.
- `turn` :@: `void turn(int amount)`: `amount` in degree. Positive is clockwise. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#turn(int)>.

### `Greenfoot`

See <https://www.greenfoot.org/files/javadoc/greenfoot/Greenfoot.html>.

- `getRandomNumber` :@: `static int getRandomNumber(int limit)`: [0, limit). See <https://www.greenfoot.org/files/javadoc/greenfoot/Greenfoot.html#getRandomNumber(int)>.
- `isKeyDown` :@: `static boolean isKeyDown(String keyName)`: See <https://www.greenfoot.org/files/javadoc/greenfoot/Greenfoot.html#isKeyDown(java.lang.String)>.

### `World`

See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html>.

- `World` :@: `World(int worldWidth, int worldHeight, int cellSize[, boolean unbounded = false])`: See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#%3Cinit%3E(int,int,int,boolean)>.
- `addObject` :@: `void addObject(Actor object, int x, int y)`: See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#addObject(greenfoot.Actor,int,int)>.
- `getHeight` :@: `int getHeight()`: In cells. See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#getHeight()>.
- `getObjects` :@: `<A> List<A> getObjects(Class<A> cls)`: See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#getObjects(java.lang.Class)>.
- `getWidth` :@: `int getWidth()`: In cells. See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#getWidth()>.

## see also

- [general/Greenfoot](../../../../general/Greenfoot.md)

---
aliases:
  - Greenfoot
tags:
  - flashcard/special/academia/HKUST/COMP_1029J/Greenfoot
  - language/in/English
---

# Greenfoot

## installation

Follow the instructions on {{<https://greenfoot.org/>}}. <!--SR:!2024-11-30,233,330-->

## usage

Explore the user interface yourself.

## documentation

### `Actor`

See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html>.

- `Actor` :: `Actor()`: Remember to add to the world using `World#addObject`. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#%3Cinit%3E()>. <!--SR:!2024-04-26,65,310-->
- `getObjectsInRange` :: `<A> List<A> getObjectsInRange(int radius, Class<A> cls)`: `radius` in cells. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#getObjectsInRange(int,java.lang.Class)>. <!--SR:!2024-09-28,176,310-->
- `getRotation` :: `int getRotation()`: [0, 359]. 0 is east. Increase is clockwise. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#getRotation()>. <!--SR:!2024-04-28,68,310-->
- `getX` :: `int getX()`: See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#getX()>. <!--SR:!2024-04-28,67,310-->
- `getY` :: `int getY()`: See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#getY()>. <!--SR:!2024-04-27,66,310-->
- `move` :: `void move(int distance)`: `distance` in cells. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#move(int)>. <!--SR:!2024-04-18,60,310-->
- `setRotation` :: `void setRotation(int rotation)`: `rotation` is in [0, 359]. 0 is east. Increase is clockwise. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#setRotation(int)>. <!--SR:!2024-06-28,101,290-->
- `turn` :: `void turn(int amount)`: `amount` in degree. Positive is clockwise. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#turn(int)>. <!--SR:!2024-08-01,118,290-->

### `Greenfoot`

See <https://www.greenfoot.org/files/javadoc/greenfoot/Greenfoot.html>.

- `getRandomNumber` :: `static int getRandomNumber(int limit)`: [0, limit). See <https://www.greenfoot.org/files/javadoc/greenfoot/Greenfoot.html#getRandomNumber(int)>. <!--SR:!2024-09-12,157,310-->
- `isKeyDown` :: `static boolean isKeyDown(String keyName)`: See <https://www.greenfoot.org/files/javadoc/greenfoot/Greenfoot.html#isKeyDown(java.lang.String)>. <!--SR:!2024-04-23,63,310-->

### `World`

See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html>.

- `World` :: `World(int worldWidth, int worldHeight, int cellSize[, boolean unbounded = false])`: See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#%3Cinit%3E(int,int,int,boolean)>. <!--SR:!2024-07-28,114,290-->
- `addObject` :: `void addObject(Actor object, int x, int y)`: See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#addObject(greenfoot.Actor,int,int)>. <!--SR:!2024-07-29,115,290-->
- `getHeight` :: `int getHeight()`: In cells. See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#getHeight()>. <!--SR:!2024-04-19,60,310-->
- `getObjects` :: `<A> List<A> getObjects(Class<A> cls)`: See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#getObjects(java.lang.Class)>. <!--SR:!2024-04-26,66,310-->
- `getWidth` :: `int getWidth()`: In cells. See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#getWidth()>. <!--SR:!2024-04-15,56,310-->

## see also

- [general/Greenfoot](../../../../general/Greenfoot.md)

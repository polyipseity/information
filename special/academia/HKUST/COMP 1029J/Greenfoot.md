---
aliases:
  - Greenfoot
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029J/Greenfoot
  - language/in/English
---

# Greenfoot

## installation

Follow the instructions on {@{<https://greenfoot.org/>}@}. <!--SR:!2027-10-26,1060,350-->

## usage

Explore the user interface yourself.

## documentation

### `Actor`

See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html>.

- `Actor` :@: `Actor()`: Remember to add to the world using `World#addObject`. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#%3Cinit%3E()>. <!--SR:!2028-07-13,1261,350-->
- `getObjectsInRange` :@: `<A> List<A> getObjectsInRange(int radius, Class<A> cls)`: `radius` in cells. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#getObjectsInRange(int,java.lang.Class)>. <!--SR:!2026-10-24,754,330-->
- `getRotation` :@: `int getRotation()`: [0, 359]. 0 is east. Increase is clockwise. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#getRotation()>. <!--SR:!2028-12-09,1383,350-->
- `getX` :@: `int getX()`: See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#getX()>. <!--SR:!2028-11-11,1359,350-->
- `getY` :@: `int getY()`: See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#getY()>. <!--SR:!2028-08-05,1280,350-->
- `move` :@: `void move(int distance)`: `distance` in cells. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#move(int)>. <!--SR:!2028-03-10,1166,350-->
- `setRotation` :@: `void setRotation(int rotation)`: `rotation` is in [0, 359]. 0 is east. Increase is clockwise. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#setRotation(int)>. <!--SR:!2025-08-08,406,310-->
- `turn` :@: `void turn(int amount)`: `amount` in degree. Positive is clockwise. See <https://www.greenfoot.org/files/javadoc/greenfoot/Actor.html#turn(int)>. <!--SR:!2025-07-08,341,290-->

### `Greenfoot`

See <https://www.greenfoot.org/files/javadoc/greenfoot/Greenfoot.html>.

- `getRandomNumber` :@: `static int getRandomNumber(int limit)`: [0, limit). See <https://www.greenfoot.org/files/javadoc/greenfoot/Greenfoot.html#getRandomNumber(int)>. <!--SR:!2026-01-11,486,310-->
- `isKeyDown` :@: `static boolean isKeyDown(String keyName)`: See <https://www.greenfoot.org/files/javadoc/greenfoot/Greenfoot.html#isKeyDown(java.lang.String)>. <!--SR:!2026-07-22,620,310-->

### `World`

See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html>.

- `World` :@: `World(int worldWidth, int worldHeight, int cellSize[, boolean unbounded = false])`: See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#%3Cinit%3E(int,int,int,boolean)>. <!--SR:!2025-06-23,330,290-->
- `addObject` :@: `void addObject(Actor object, int x, int y)`: See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#addObject(greenfoot.Actor,int,int)>. <!--SR:!2025-11-03,462,310-->
- `getHeight` :@: `int getHeight()`: In cells. See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#getHeight()>. <!--SR:!2028-03-21,1174,350-->
- `getObjects` :@: `<A> List<A> getObjects(Class<A> cls)`: See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#getObjects(java.lang.Class)>. <!--SR:!2027-04-25,886,330-->
- `getWidth` :@: `int getWidth()`: In cells. See <https://www.greenfoot.org/files/javadoc/greenfoot/World.html#getWidth()>. <!--SR:!2028-01-08,1117,350-->

## see also

- [general/Greenfoot](../../../../general/Greenfoot.md)

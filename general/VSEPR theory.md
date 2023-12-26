---
aliases:
  - VSEPR theory
  - valence shell electron pair repulsion theory
tags:
  - flashcards/general/VSEPR_theory
  - languages/in/English
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# VSEPR theory

## AXE method

The [electron pairs](electron%20pair.md) of the central [atom](atom.md) can be {{represented by AX<sub>n</sub>E<sub>m</sub>, where A is the central atom, X are the [ligands](ligand.md), and E are the [_lone_ electron pairs](lone%20pair.md)}}. The steric number is {{the sum of the numbers of X and E}}. <!--SR:!2025-03-31,523,290!2024-04-13,291,330-->

### main-group elements

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen.gen import markdown_sanitizer
e = __env__
return await memorize_table(
  e.cwf_sects('2900', '8daf'),
  ('AXE', '[shape](molecular%20geometry.md)', 'ideal bond angle(s)', 'example(s)',),
  (
    ('AX<sub>2</sub>E<sub>0</sub>', '[linear](linear%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX2E0-3D-balls.png)', '180°', '[CO<sub>2</sub>](carbon%20dioxide.md)',),
    ('AX<sub>2</sub>E<sub>1</sub>', '[bent](bent%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX2E1-3D-balls.png)', '120°', '[SO<sub>2</sub>](sulfur%20dioxide.md)'),
    ('AX<sub>2</sub>E<sub>2</sub>', '[bent](bent%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX2E2-3D-balls.png)', '~109.5°', '[H<sub>2</sub>O](water.md)'),
    ('AX<sub>2</sub>E<sub>3</sub>', '[linear](linear%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX2E3-3D-balls.png)', '180°', '[XeF<sub>2</sub>](xenon%20difluoride.md)'),
    ('AX<sub>3</sub>E<sub>0</sub>', '[trigonal planar](trigonal%20planar%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX3E0-3D-balls.png)', '120°', '[BF<sub>3</sub>](boron%20trifluoride.md)'),
    ('AX<sub>3</sub>E<sub>1</sub>', '[trigonal pyramidal](trigonal%20pyramidal%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX3E1-3D-balls.png)', '~109.5°', '[NH<sub>3</sub>](ammonia.md)'),
    ('AX<sub>3</sub>E<sub>2</sub>', '[T-shaped](T-shaped%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX3E2-3D-balls.png)', '90°, 180°', '[ClF<sub>3</sub>](chlorine%20trifluoride.md)'),
    ('AX<sub>4</sub>E<sub>0</sub>', '[tetrahedral](tetrahedral%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX4E0-3D-balls.png)', '~109.5°', '[CH<sub>4</sub>](methane.md)'),
    ('AX<sub>4</sub>E<sub>1</sub>', '[seesaw/disphenoidal](seesaw%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX4E1-3D-balls.png)', '90°, 120°, 180°', '[SF<sub>4</sub>](sulfur%20tetrafluoride.md)'),
    ('AX<sub>4</sub>E<sub>2</sub>', '[square planar](square%20planar%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX4E2-3D-balls.png)', '90°', '[XeF<sub>4</sub>](xenon%20tetrafluoride.md)'),
    ('AX<sub>5</sub>E<sub>0</sub>', '[trigonal bipyramidal](trigonal%20bipyramidal%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/Trigonal-bipyramidal-3D-balls.png)', '90°, 120°', '[PCl<sub>5</sub>](phosphorous%20pentachloride.md)'),
    ('AX<sub>5</sub>E<sub>1</sub>', '[square pyramidal](square%20pyramidal%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX5E1-3D-balls.png)', '90°', '[BrF<sub>5</sub>](bromine%20pentafluoride.md)'),
    ('AX<sub>5</sub>E<sub>2</sub>', '[pentagonal planar](pentagonal%20planar%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX5E2-3D-balls.png)', '72°', 'XeF<sub>5</sub><sup>-</sup>'),
    ('AX<sub>6</sub>E<sub>0</sub>', '[octahedral](octahedral%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX6E0-3D-balls.png)', '90°', '[SF<sub>6</sub>](sulfur%20hexafluoride.md)'),
    ('AX<sub>6</sub>E<sub>1</sub>', '[pentagonal pyramidal](pentagonal%20pyramidal%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX6E1-3D-balls.png)', '72°, 90°', 'XeOF<sub>5</sub><sup>-</sup>'),
    ('AX<sub>7</sub>E<sub>0</sub>', '[pentagonal bipyramidal](pentagonal%20bipyramidal%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX7E0-3D-balls.png)', '72°, 90°', '[IF<sub>7</sub>](iodine%20heptafluoride.md)'),
    ('AX<sub>8</sub>E<sub>0</sub>', '[square antiprismatic](square%20antiprismatic%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX8E0-3D-balls.png)', '', 'XeF<sub>8</sub><sup>2-</sup>'),
    ('AX<sub>9</sub>E<sub>0</sub>', '[tricapped trigonal antiprismatic](tricapped%20trigonal%20antiprismatic%20molecular%20geometry.md)', '![{}](../archives/Wikimedia%20Commons/AX9E0-3D-balls.png)', '', 'ReH<sub>9</sub><sup>2-</sup>'),
  ),
  lambda datum: map(cloze, (*datum[:1], f'{datum[1]}<br/>{datum[2].format(markdown_sanitizer(datum[1]))}', *datum[3:],)),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2900"--><!-- The following content is generated at 2023-03-26T17:23:22.932532+08:00. Any edits will be overridden! -->

> | AXE | [shape](molecular%20geometry.md) | ideal bond angle(s) | example(s) |
> |-|-|-|-|
> | {{AX<sub>2</sub>E<sub>0</sub>}} | {{[linear](linear%20molecular%20geometry.md)<br/>![linear](../archives/Wikimedia%20Commons/AX2E0-3D-balls.png)}} | {{180°}} | {{[CO<sub>2</sub>](carbon%20dioxide.md)}} |
> | {{AX<sub>2</sub>E<sub>1</sub>}} | {{[bent](bent%20molecular%20geometry.md)<br/>![bent](../archives/Wikimedia%20Commons/AX2E1-3D-balls.png)}} | {{120°}} | {{[SO<sub>2</sub>](sulfur%20dioxide.md)}} |
> | {{AX<sub>2</sub>E<sub>2</sub>}} | {{[bent](bent%20molecular%20geometry.md)<br/>![bent](../archives/Wikimedia%20Commons/AX2E2-3D-balls.png)}} | {{~109.5°}} | {{[H<sub>2</sub>O](water.md)}} |
> | {{AX<sub>2</sub>E<sub>3</sub>}} | {{[linear](linear%20molecular%20geometry.md)<br/>![linear](../archives/Wikimedia%20Commons/AX2E3-3D-balls.png)}} | {{180°}} | {{[XeF<sub>2</sub>](xenon%20difluoride.md)}} |
> | {{AX<sub>3</sub>E<sub>0</sub>}} | {{[trigonal planar](trigonal%20planar%20molecular%20geometry.md)<br/>![trigonal planar](../archives/Wikimedia%20Commons/AX3E0-3D-balls.png)}} | {{120°}} | {{[BF<sub>3</sub>](boron%20trifluoride.md)}} |
> | {{AX<sub>3</sub>E<sub>1</sub>}} | {{[trigonal pyramidal](trigonal%20pyramidal%20molecular%20geometry.md)<br/>![trigonal pyramidal](../archives/Wikimedia%20Commons/AX3E1-3D-balls.png)}} | {{~109.5°}} | {{[NH<sub>3</sub>](ammonia.md)}} |
> | {{AX<sub>3</sub>E<sub>2</sub>}} | {{[T-shaped](T-shaped%20molecular%20geometry.md)<br/>![T-shaped](../archives/Wikimedia%20Commons/AX3E2-3D-balls.png)}} | {{90°, 180°}} | {{[ClF<sub>3</sub>](chlorine%20trifluoride.md)}} |
> | {{AX<sub>4</sub>E<sub>0</sub>}} | {{[tetrahedral](tetrahedral%20molecular%20geometry.md)<br/>![tetrahedral](../archives/Wikimedia%20Commons/AX4E0-3D-balls.png)}} | {{~109.5°}} | {{[CH<sub>4</sub>](methane.md)}} |
> | {{AX<sub>4</sub>E<sub>1</sub>}} | {{[seesaw/disphenoidal](seesaw%20molecular%20geometry.md)<br/>![seesaw/disphenoidal](../archives/Wikimedia%20Commons/AX4E1-3D-balls.png)}} | {{90°, 120°, 180°}} | {{[SF<sub>4</sub>](sulfur%20tetrafluoride.md)}} |
> | {{AX<sub>4</sub>E<sub>2</sub>}} | {{[square planar](square%20planar%20molecular%20geometry.md)<br/>![square planar](../archives/Wikimedia%20Commons/AX4E2-3D-balls.png)}} | {{90°}} | {{[XeF<sub>4</sub>](xenon%20tetrafluoride.md)}} |
> | {{AX<sub>5</sub>E<sub>0</sub>}} | {{[trigonal bipyramidal](trigonal%20bipyramidal%20molecular%20geometry.md)<br/>![trigonal bipyramidal](../archives/Wikimedia%20Commons/Trigonal-bipyramidal-3D-balls.png)}} | {{90°, 120°}} | {{[PCl<sub>5</sub>](phosphorous%20pentachloride.md)}} |
> | {{AX<sub>5</sub>E<sub>1</sub>}} | {{[square pyramidal](square%20pyramidal%20molecular%20geometry.md)<br/>![square pyramidal](../archives/Wikimedia%20Commons/AX5E1-3D-balls.png)}} | {{90°}} | {{[BrF<sub>5</sub>](bromine%20pentafluoride.md)}} |
> | {{AX<sub>5</sub>E<sub>2</sub>}} | {{[pentagonal planar](pentagonal%20planar%20molecular%20geometry.md)<br/>![pentagonal planar](../archives/Wikimedia%20Commons/AX5E2-3D-balls.png)}} | {{72°}} | {{XeF<sub>5</sub><sup>-</sup>}} |
> | {{AX<sub>6</sub>E<sub>0</sub>}} | {{[octahedral](octahedral%20molecular%20geometry.md)<br/>![octahedral](../archives/Wikimedia%20Commons/AX6E0-3D-balls.png)}} | {{90°}} | {{[SF<sub>6</sub>](sulfur%20hexafluoride.md)}} |
> | {{AX<sub>6</sub>E<sub>1</sub>}} | {{[pentagonal pyramidal](pentagonal%20pyramidal%20molecular%20geometry.md)<br/>![pentagonal pyramidal](../archives/Wikimedia%20Commons/AX6E1-3D-balls.png)}} | {{72°, 90°}} | {{XeOF<sub>5</sub><sup>-</sup>}} |
> | {{AX<sub>7</sub>E<sub>0</sub>}} | {{[pentagonal bipyramidal](pentagonal%20bipyramidal%20molecular%20geometry.md)<br/>![pentagonal bipyramidal](../archives/Wikimedia%20Commons/AX7E0-3D-balls.png)}} | {{72°, 90°}} | {{[IF<sub>7</sub>](iodine%20heptafluoride.md)}} |
> | {{AX<sub>8</sub>E<sub>0</sub>}} | {{[square antiprismatic](square%20antiprismatic%20molecular%20geometry.md)<br/>![square antiprismatic](../archives/Wikimedia%20Commons/AX8E0-3D-balls.png)}} |  | {{XeF<sub>8</sub><sup>2-</sup>}} |
> | {{AX<sub>9</sub>E<sub>0</sub>}} | {{[tricapped trigonal antiprismatic](tricapped%20trigonal%20antiprismatic%20molecular%20geometry.md)<br/>![tricapped trigonal antiprismatic](../archives/Wikimedia%20Commons/AX9E0-3D-balls.png)}} |  | {{ReH<sub>9</sub><sup>2-</sup>}} | <!--SR:!2024-01-07,214,330!2024-05-01,304,330!2024-01-20,223,330!2024-03-10,265,330!2024-03-25,274,330!2024-02-26,252,330!2025-10-16,707,330!2024-04-08,214,230!2024-05-08,311,330!2023-12-29,193,310!2024-02-29,255,330!2024-05-03,306,330!2024-01-21,224,330!2024-03-13,222,270!2024-04-06,286,330!2024-02-19,189,230!2024-05-25,323,330!2025-01-25,454,310!2024-03-11,265,330!2025-06-17,560,310!2024-01-22,225,330!2024-02-25,251,330!2024-01-11,200,290!2024-04-27,204,230!2024-05-29,327,330!2025-10-04,694,330!2023-12-28,192,310!2024-03-04,179,230!2024-03-12,266,330!2024-08-07,373,330!2024-05-12,315,330!2025-04-16,551,310!2024-04-13,291,330!2024-01-29,121,250!2024-11-11,431,310!2024-01-02,12,150!2024-03-29,278,330!2024-08-31,383,310!2024-03-22,271,330!2024-02-20,204,270!2024-05-02,305,330!2026-03-02,810,330!2024-03-24,273,330!2024-05-26,278,290!2024-03-13,267,330!2024-03-12,221,270!2024-03-11,266,330!2024-02-11,52,150!2024-03-08,263,330!2025-01-13,431,290!2024-03-28,277,330!2024-02-17,115,190!2024-02-25,251,330!2026-05-04,861,330!2024-04-08,288,330!2025-04-23,523,310!2024-02-06,238,330!2024-12-08,458,310!2024-03-27,276,330!2024-05-27,279,250!2024-02-07,239,330!2024-01-27,229,330!2024-05-05,308,330!2024-01-17,54,210!2024-04-05,285,330!2024-01-09,168,270!2023-12-27,162,250!2024-02-28,254,330!2024-01-18,48,190!2024-06-23,290,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="8daf"--><!-- The following content is generated at 2023-03-26T16:22:57.607537+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←AX<sub>2</sub>E<sub>0</sub> <!--SR:!2024-03-30,279,330!2024-05-07,310,330-->
2. AX<sub>2</sub>E<sub>0</sub>→:::←AX<sub>2</sub>E<sub>1</sub> <!--SR:!2024-02-27,253,330!2024-05-09,312,330-->
3. AX<sub>2</sub>E<sub>1</sub>→:::←AX<sub>2</sub>E<sub>2</sub> <!--SR:!2024-04-03,283,330!2024-03-09,264,330-->
4. AX<sub>2</sub>E<sub>2</sub>→:::←AX<sub>2</sub>E<sub>3</sub> <!--SR:!2024-03-23,272,330!2024-03-12,267,330-->
5. AX<sub>2</sub>E<sub>3</sub>→:::←AX<sub>3</sub>E<sub>0</sub> <!--SR:!2024-02-05,238,330!2024-04-17,187,290-->
6. AX<sub>3</sub>E<sub>0</sub>→:::←AX<sub>3</sub>E<sub>1</sub> <!--SR:!2024-02-26,252,330!2024-04-02,282,330-->
7. AX<sub>3</sub>E<sub>1</sub>→:::←AX<sub>3</sub>E<sub>2</sub> <!--SR:!2024-04-07,287,330!2024-05-26,324,330-->
8. AX<sub>3</sub>E<sub>2</sub>→:::←AX<sub>4</sub>E<sub>0</sub> <!--SR:!2024-01-31,36,230!2024-02-29,75,290-->
9. AX<sub>4</sub>E<sub>0</sub>→:::←AX<sub>4</sub>E<sub>1</sub> <!--SR:!2024-05-04,307,330!2024-05-27,325,330-->
10. AX<sub>4</sub>E<sub>1</sub>→:::←AX<sub>4</sub>E<sub>2</sub> <!--SR:!2024-05-06,309,330!2024-04-26,299,330-->
11. AX<sub>4</sub>E<sub>2</sub>→:::←AX<sub>5</sub>E<sub>0</sub> <!--SR:!2024-01-23,226,330!2024-04-24,297,330-->
12. AX<sub>5</sub>E<sub>0</sub>→:::←AX<sub>5</sub>E<sub>1</sub> <!--SR:!2024-03-13,268,330!2024-03-31,280,330-->
13. AX<sub>5</sub>E<sub>1</sub>→:::←AX<sub>5</sub>E<sub>2</sub> <!--SR:!2024-05-28,326,330!2024-04-04,284,330-->
14. AX<sub>5</sub>E<sub>2</sub>→:::←AX<sub>6</sub>E<sub>0</sub> <!--SR:!2024-04-14,292,330!2024-02-23,249,330-->
15. AX<sub>6</sub>E<sub>0</sub>→:::←AX<sub>6</sub>E<sub>1</sub> <!--SR:!2024-08-29,355,290!2024-04-23,296,330-->
16. AX<sub>6</sub>E<sub>1</sub>→:::←AX<sub>7</sub>E<sub>0</sub> <!--SR:!2024-01-01,202,310!2024-05-13,249,270-->
17. AX<sub>7</sub>E<sub>0</sub>→:::←AX<sub>8</sub>E<sub>0</sub> <!--SR:!2024-05-24,322,330!2024-01-16,78,290-->
18. AX<sub>8</sub>E<sub>0</sub>→:::←AX<sub>9</sub>E<sub>0</sub> <!--SR:!2024-02-24,250,330!2024-03-26,275,330-->
19. AX<sub>9</sub>E<sub>0</sub>→:::←_(end)_ <!--SR:!2024-04-25,298,330!2024-01-24,227,330-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

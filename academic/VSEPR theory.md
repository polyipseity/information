---
aliases: ['VSEPR theory', 'valence shell electron pair repulsion theory',]
---

#academic/chemistry #flashcards/academic/Vv/VSEPR_theory

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../utility.py.md
```
%%

# VSEPR theory

## AXE method

The [electron pairs](electron%20pair.md) of the central [atom](atom.md) can be {{represented by AX<sub>n</sub>E<sub>m</sub>, where A is the central atom, X are the [ligands](ligand.md), and E are the [_lone_ electron pairs](lone%20pair.md)}}. The steric number is {{the sum of the numbers of X and E}}. <!--SR:!2023-04-07,3,250!2023-04-07,4,270-->

### main-group elements

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen.gen import markdown_sanitizer
e = __env__
return await memorize_table(
	(e.cwf_section('2900'), e.cwf_section('8daf'),),
	('AXE', '[shape](molecular%20geometry.md)', 'ideal bond angle(s)', 'example(s)',),
	(
		('AX<sub>2</sub>E<sub>0</sub>', '[linear](linear%20molecular%20geometry.md)', '![{}](../attachments/AX2E0-3D-balls.png)', '180°', '[CO<sub>2</sub>](carbon%20dioxide.md)',),
		('AX<sub>2</sub>E<sub>1</sub>', '[bent](bent%20molecular%20geometry.md)', '![{}](../attachments/AX2E1-3D-balls.png)', '120°', '[SO<sub>2</sub>](sulfur%20dioxide.md)'),
		('AX<sub>2</sub>E<sub>2</sub>', '[bent](bent%20molecular%20geometry.md)', '![{}](../attachments/AX2E2-3D-balls.png)', '~109.5°', '[H<sub>2</sub>O](water.md)'),
		('AX<sub>2</sub>E<sub>3</sub>', '[linear](linear%20molecular%20geometry.md)', '![{}](../attachments/AX2E3-3D-balls.png)', '180°', '[XeF<sub>2</sub>](xenon%20difluoride.md)'),
		('AX<sub>3</sub>E<sub>0</sub>', '[trigonal planar](trigonal%20planar%20molecular%20geometry.md)', '![{}](../attachments/AX3E0-3D-balls.png)', '120°', '[BF<sub>3</sub>](boron%20trifluoride.md)'),
		('AX<sub>3</sub>E<sub>1</sub>', '[trigonal pyramidal](trigonal%20pyramidal%20molecular%20geometry.md)', '![{}](../attachments/AX3E1-3D-balls.png)', '~109.5°', '[NH<sub>3</sub>](ammonia.md)'),
		('AX<sub>3</sub>E<sub>2</sub>', '[T-shaped](T-shaped%20molecular%20geometry.md)', '![{}](../attachments/AX3E2-3D-balls.png)', '90°, 180°', '[ClF<sub>3</sub>](chlorine%20trifluoride.md)'),
		('AX<sub>4</sub>E<sub>0</sub>', '[tetrahedral](tetrahedral%20molecular%20geometry.md)', '![{}](../attachments/AX4E0-3D-balls.png)', '~109.5°', '[CH<sub>4</sub>](methane.md)'),
		('AX<sub>4</sub>E<sub>1</sub>', '[seesaw/disphenoidal](seesaw%20molecular%20geometry.md)', '![{}](../attachments/AX4E1-3D-balls.png)', '90°, 120°, 180°', '[SF<sub>4</sub>](sulfur%20tetrafluoride.md)'),
		('AX<sub>4</sub>E<sub>2</sub>', '[square planar](square%20planar%20molecular%20geometry.md)', '![{}](../attachments/AX4E2-3D-balls.png)', '90°', '[XeF<sub>4</sub>](xenon%20tetrafluoride.md)'),
		('AX<sub>5</sub>E<sub>0</sub>', '[trigonal bipyramidal](trigonal%20bipyramidal%20molecular%20geometry.md)', '![{}](../attachments/Trigonal-bipyramidal-3D-balls.png)', '90°, 120°', '[PCl<sub>5</sub>](phosphorous%20pentachloride.md)'),
		('AX<sub>5</sub>E<sub>1</sub>', '[square pyramidal](square%20pyramidal%20molecular%20geometry.md)', '![{}](../attachments/AX5E1-3D-balls.png)', '90°', '[BrF<sub>5</sub>](bromine%20pentafluoride.md)'),
		('AX<sub>5</sub>E<sub>2</sub>', '[pentagonal planar](pentagonal%20planar%20molecular%20geometry.md)', '![{}](../attachments/AX5E2-3D-balls.png)', '72°', 'XeF<sub>5</sub><sup>-</sup>'),
		('AX<sub>6</sub>E<sub>0</sub>', '[octahedral](octahedral%20molecular%20geometry.md)', '![{}](../attachments/AX6E0-3D-balls.png)', '90°', '[SF<sub>6</sub>](sulfur%20hexafluoride.md)'),
		('AX<sub>6</sub>E<sub>1</sub>', '[pentagonal pyramidal](pentagonal%20pyramidal%20molecular%20geometry.md)', '![{}](../attachments/AX6E1-3D-balls.png)', '72°, 90°', 'XeOF<sub>5</sub><sup>-</sup>'),
		('AX<sub>7</sub>E<sub>0</sub>', '[pentagonal bipyramidal](pentagonal%20bipyramidal%20molecular%20geometry.md)', '![{}](../attachments/AX7E0-3D-balls.png)', '72°, 90°', '[IF<sub>7</sub>](iodine%20heptafluoride.md)'),
		('AX<sub>8</sub>E<sub>0</sub>', '[square antiprismatic](square%20antiprismatic%20molecular%20geometry.md)', '![{}](../attachments/AX8E0-3D-balls.png)', '', 'XeF<sub>8</sub><sup>2-</sup>'),
		('AX<sub>9</sub>E<sub>0</sub>', '[tricapped trigonal antiprismatic](tricapped%20trigonal%20antiprismatic%20molecular%20geometry.md)', '![{}](../attachments/AX9E0-3D-balls.png)', '', 'ReH<sub>9</sub><sup>2-</sup>'),
	),
	lambda datum: map(cloze, (*datum[:1], f'{datum[1]}<br/>{datum[2].format(markdown_sanitizer(datum[1]))}', *datum[3:],)),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2900"--><!-- The following content is generated at 2023-03-26T17:23:22.932532+08:00. Any edits will be overridden! -->

> | AXE | [shape](molecular%20geometry.md) | ideal bond angle(s) | example(s) |
> |-|-|-|-|
> | {{AX<sub>2</sub>E<sub>0</sub>}} | {{[linear](linear%20molecular%20geometry.md)<br/>![linear](../attachments/AX2E0-3D-balls.png)}} | {{180°}} | {{[CO<sub>2</sub>](carbon%20dioxide.md)}} |
> | {{AX<sub>2</sub>E<sub>1</sub>}} | {{[bent](bent%20molecular%20geometry.md)<br/>![bent](../attachments/AX2E1-3D-balls.png)}} | {{120°}} | {{[SO<sub>2</sub>](sulfur%20dioxide.md)}} |
> | {{AX<sub>2</sub>E<sub>2</sub>}} | {{[bent](bent%20molecular%20geometry.md)<br/>![bent](../attachments/AX2E2-3D-balls.png)}} | {{~109.5°}} | {{[H<sub>2</sub>O](water.md)}} |
> | {{AX<sub>2</sub>E<sub>3</sub>}} | {{[linear](linear%20molecular%20geometry.md)<br/>![linear](../attachments/AX2E3-3D-balls.png)}} | {{180°}} | {{[XeF<sub>2</sub>](xenon%20difluoride.md)}} |
> | {{AX<sub>3</sub>E<sub>0</sub>}} | {{[trigonal planar](trigonal%20planar%20molecular%20geometry.md)<br/>![trigonal planar](../attachments/AX3E0-3D-balls.png)}} | {{120°}} | {{[BF<sub>3</sub>](boron%20trifluoride.md)}} |
> | {{AX<sub>3</sub>E<sub>1</sub>}} | {{[trigonal pyramidal](trigonal%20pyramidal%20molecular%20geometry.md)<br/>![trigonal pyramidal](../attachments/AX3E1-3D-balls.png)}} | {{~109.5°}} | {{[NH<sub>3</sub>](ammonia.md)}} |
> | {{AX<sub>3</sub>E<sub>2</sub>}} | {{[T-shaped](T-shaped%20molecular%20geometry.md)<br/>![T-shaped](../attachments/AX3E2-3D-balls.png)}} | {{90°, 180°}} | {{[ClF<sub>3</sub>](chlorine%20trifluoride.md)}} |
> | {{AX<sub>4</sub>E<sub>0</sub>}} | {{[tetrahedral](tetrahedral%20molecular%20geometry.md)<br/>![tetrahedral](../attachments/AX4E0-3D-balls.png)}} | {{~109.5°}} | {{[CH<sub>4</sub>](methane.md)}} |
> | {{AX<sub>4</sub>E<sub>1</sub>}} | {{[seesaw/disphenoidal](seesaw%20molecular%20geometry.md)<br/>![seesaw/disphenoidal](../attachments/AX4E1-3D-balls.png)}} | {{90°, 120°, 180°}} | {{[SF<sub>4</sub>](sulfur%20tetrafluoride.md)}} |
> | {{AX<sub>4</sub>E<sub>2</sub>}} | {{[square planar](square%20planar%20molecular%20geometry.md)<br/>![square planar](../attachments/AX4E2-3D-balls.png)}} | {{90°}} | {{[XeF<sub>4</sub>](xenon%20tetrafluoride.md)}} |
> | {{AX<sub>5</sub>E<sub>0</sub>}} | {{[trigonal bipyramidal](trigonal%20bipyramidal%20molecular%20geometry.md)<br/>![trigonal bipyramidal](../attachments/Trigonal-bipyramidal-3D-balls.png)}} | {{90°, 120°}} | {{[PCl<sub>5</sub>](phosphorous%20pentachloride.md)}} |
> | {{AX<sub>5</sub>E<sub>1</sub>}} | {{[square pyramidal](square%20pyramidal%20molecular%20geometry.md)<br/>![square pyramidal](../attachments/AX5E1-3D-balls.png)}} | {{90°}} | {{[BrF<sub>5</sub>](bromine%20pentafluoride.md)}} |
> | {{AX<sub>5</sub>E<sub>2</sub>}} | {{[pentagonal planar](pentagonal%20planar%20molecular%20geometry.md)<br/>![pentagonal planar](../attachments/AX5E2-3D-balls.png)}} | {{72°}} | {{XeF<sub>5</sub><sup>-</sup>}} |
> | {{AX<sub>6</sub>E<sub>0</sub>}} | {{[octahedral](octahedral%20molecular%20geometry.md)<br/>![octahedral](../attachments/AX6E0-3D-balls.png)}} | {{90°}} | {{[SF<sub>6</sub>](sulfur%20hexafluoride.md)}} |
> | {{AX<sub>6</sub>E<sub>1</sub>}} | {{[pentagonal pyramidal](pentagonal%20pyramidal%20molecular%20geometry.md)<br/>![pentagonal pyramidal](../attachments/AX6E1-3D-balls.png)}} | {{72°, 90°}} | {{XeOF<sub>5</sub><sup>-</sup>}} |
> | {{AX<sub>7</sub>E<sub>0</sub>}} | {{[pentagonal bipyramidal](pentagonal%20bipyramidal%20molecular%20geometry.md)<br/>![pentagonal bipyramidal](../attachments/AX7E0-3D-balls.png)}} | {{72°, 90°}} | {{[IF<sub>7</sub>](iodine%20heptafluoride.md)}} |
> | {{AX<sub>8</sub>E<sub>0</sub>}} | {{[square antiprismatic](square%20antiprismatic%20molecular%20geometry.md)<br/>![square antiprismatic](../attachments/AX8E0-3D-balls.png)}} |  | {{XeF<sub>8</sub><sup>2-</sup>}} |
> | {{AX<sub>9</sub>E<sub>0</sub>}} | {{[tricapped trigonal antiprismatic](tricapped%20trigonal%20antiprismatic%20molecular%20geometry.md)<br/>![tricapped trigonal antiprismatic](../attachments/AX9E0-3D-balls.png)}} |  | {{ReH<sub>9</sub><sup>2-</sup>}} | <!--SR:!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,3,250!2023-04-07,4,270!2023-04-07,3,250!2023-04-07,4,270!2023-04-07,3,250!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,3,250!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,3,250!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-06,1,190!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,3,250!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-08,3,230!2023-04-07,4,270!2023-04-07,3,250!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,3,250!2023-04-07,4,270!2023-04-08,3,230!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,4,270!2023-04-07,3,250!2023-04-07,4,270!2023-04-07,3,250!2023-04-08,3,230!2023-04-07,4,270!2023-04-08,3,230!2023-04-08,3,230-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="8daf"--><!-- The following content is generated at 2023-03-26T16:22:57.607537+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←AX<sub>2</sub>E<sub>0</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
2. AX<sub>2</sub>E<sub>0</sub>→:::←AX<sub>2</sub>E<sub>1</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
3. AX<sub>2</sub>E<sub>1</sub>→:::←AX<sub>2</sub>E<sub>2</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
4. AX<sub>2</sub>E<sub>2</sub>→:::←AX<sub>2</sub>E<sub>3</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
5. AX<sub>2</sub>E<sub>3</sub>→:::←AX<sub>3</sub>E<sub>0</sub> <!--SR:!2023-04-07,4,270!2023-04-07,3,250-->
6. AX<sub>3</sub>E<sub>0</sub>→:::←AX<sub>3</sub>E<sub>1</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
7. AX<sub>3</sub>E<sub>1</sub>→:::←AX<sub>3</sub>E<sub>2</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
8. AX<sub>3</sub>E<sub>2</sub>→:::←AX<sub>4</sub>E<sub>0</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
9. AX<sub>4</sub>E<sub>0</sub>→:::←AX<sub>4</sub>E<sub>1</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
10. AX<sub>4</sub>E<sub>1</sub>→:::←AX<sub>4</sub>E<sub>2</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
11. AX<sub>4</sub>E<sub>2</sub>→:::←AX<sub>5</sub>E<sub>0</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
12. AX<sub>5</sub>E<sub>0</sub>→:::←AX<sub>5</sub>E<sub>1</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
13. AX<sub>5</sub>E<sub>1</sub>→:::←AX<sub>5</sub>E<sub>2</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
14. AX<sub>5</sub>E<sub>2</sub>→:::←AX<sub>6</sub>E<sub>0</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
15. AX<sub>6</sub>E<sub>0</sub>→:::←AX<sub>6</sub>E<sub>1</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
16. AX<sub>6</sub>E<sub>1</sub>→:::←AX<sub>7</sub>E<sub>0</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
17. AX<sub>7</sub>E<sub>0</sub>→:::←AX<sub>8</sub>E<sub>0</sub> <!--SR:!2023-04-07,4,270!2023-04-07,3,250-->
18. AX<sub>8</sub>E<sub>0</sub>→:::←AX<sub>9</sub>E<sub>0</sub> <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->
19. AX<sub>9</sub>E<sub>0</sub>→:::←_(end)_ <!--SR:!2023-04-07,4,270!2023-04-07,4,270-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

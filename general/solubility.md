---
aliases:
  - insolubilities
  - insolubility
  - insoluble
  - solubilities
  - solubility
  - soluble
tags:
  - flashcards/general/solubility
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# solubility

__Solubility__ is {{the ability of a [solute](solution%20(chemistry).md) to form a [solution](solution%20(chemistry).md) with a [solvent](solvent.md)}}. <!--SR:!2023-12-31,142,232-->

It is measured as {{the [concentration](concentration.md) of the solute in a saturated solution, in which no more solute can be [dissolved](solvation.md)}}. <!--SR:!2025-01-09,467,292-->

## solubility of ionic compounds in water

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
from pytextgen import gen, read, util
import typing
soluble = R'<span style="color\: green;">soluble</span>'
insoluble = R'<span style="color\: red;">insoluble</span>'
data: typing.Mapping[str, typing.Mapping[str, str]] = {
  'group I compounds': {
    'general solubility': soluble,
    'exception(s)': 'Li<sub>3</sub>PO<sub>4</sub>',
  },
  'NH<sub>4</sub><sup>+</sup> compounds': {
    'general solubility': soluble,
    'exception(s)': '_(none)_',
  },
  'nitrates': {
    'general solubility': soluble,
    'exception(s)': '_(none)_',
  },
  'acetates (ethanoates)': {
    'general solubility': soluble,
    'exception(s)': 'Ag<sup>+</sup> compounds',
  },
  'chlorides': {
    'general solubility': soluble,
    'exception(s)': 'Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds',
  },
  'bromides': {
    'general solubility': soluble,
    'exception(s)': 'Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds',
  },
  'iodides': {
    'general solubility': soluble,
    'exception(s)': 'Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, Hg<sub>2</sub><sup>2+</sup>, and Hg<sup>2+</sup> compounds',
  },
  'sulfates': {
    'general solubility': soluble,
    'exception(s)': 'Ag<sup>+</sup>, Pb<sup>2+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Ca<sup>2+</sup> compounds',
  },
  'carbonates': {
    'general solubility': insoluble,
    'exception(s)': 'group I, NH<sub>4</sub><sup>+</sup>, and UO<sub>2</sub><sup>2+</sup> compounds',
  },
  'sulfites': {
    'general solubility': insoluble,
    'exception(s)': 'group I and NH<sub>4</sub><sup>+</sup> compounds',
  },
  'phosphates': {
    'general solubility': insoluble,
    'exception(s)': 'group I and NH<sub>4</sub><sup>+</sup> compounds (excluding Li<sup>+</sup>)',
  },
  'hydroxides': {
    'general solubility': insoluble,
    'exception(s)': 'group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds ([Ca(OH)<sub>2</sub>](calcium%20hydroxide.md) is poorly soluble)',
  },
  'oxides': {
    'general solubility': insoluble,
    'exception(s)': 'group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds',
  },
  'sulfides': {
    'general solubility': insoluble,
    'exception(s)': 'group I, group II, and NH<sub>4</sub><sup>+</sup> compounds',
  },
}
text: gen.TextCode = gen.maps_to_code(data)
return (
  util.Result(
    location=__env__.cwf_sect('901862'),
    text=gen.cloze_text(text,
      states=await read.read_flashcard_states(__env__.cwf_sect('901862')),
    ),
  ),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="901862"--><!-- The following content is generated at 2023-10-11T09:22:26.343630+08:00. Any edits will be overridden! -->

> group I compounds
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Li<sub>3</sub>PO<sub>4</sub>}} <!--SR:!2025-05-11,700,230!2024-09-14,365,210-->

> NH<sub>4</sub><sup>+</sup> compounds
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{_(none)_}} <!--SR:!2026-03-15,1012,282!2024-01-21,324,289-->

> nitrates
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{_(none)_}} <!--SR:!2025-10-17,822,236!2024-07-15,454,289-->

> acetates (ethanoates)
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup> compounds}} <!--SR:!2024-10-17,551,242!2024-03-22,329,230-->

> chlorides
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds}} <!--SR:!2025-05-13,773,268!2024-01-10,280,190-->

> bromides
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds}} <!--SR:!2026-11-12,1147,266!2025-01-13,492,190-->

> iodides
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, Hg<sub>2</sub><sup>2+</sup>, and Hg<sup>2+</sup> compounds}} <!--SR:!2026-07-21,1056,262!2024-07-23,412,210-->

> sulfates
> - general solubility: {{<span style="color: green;">soluble</span>}}
> - exception(s): {{Ag<sup>+</sup>, Pb<sup>2+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Ca<sup>2+</sup> compounds}} <!--SR:!2025-06-27,797,261!2024-08-26,388,230-->

> carbonates
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, NH<sub>4</sub><sup>+</sup>, and UO<sub>2</sub><sup>2+</sup> compounds}} <!--SR:!2025-12-14,813,248!2023-11-27,122,230-->

> sulfites
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I and NH<sub>4</sub><sup>+</sup> compounds}} <!--SR:!2024-07-26,415,206!2024-02-07,260,210-->

> phosphates
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I and NH<sub>4</sub><sup>+</sup> compounds (excluding Li<sup>+</sup>)}} <!--SR:!2024-06-04,460,230!2024-01-08,211,210-->

> hydroxides
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds ([Ca(OH)<sub>2</sub>](calcium%20hydroxide.md) is poorly soluble)}} <!--SR:!2025-04-08,628,230!2024-11-09,427,230-->

> oxides
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds}} <!--SR:!2025-01-01,660,250!2023-12-10,28,130-->

> sulfides
> - general solubility: {{<span style="color: red;">insoluble</span>}}
> - exception(s): {{group I, group II, and NH<sub>4</sub><sup>+</sup> compounds}} <!--SR:!2024-07-12,486,238!2024-09-05,415,210-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### examples

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
insoluble = '<span style="color: red;">insoluble</span>'
reacts = '<span style="color: violet;">reacts</span>'
slightly_soluble = '<span style="color: yellow;">slightly soluble</span>'
soluble = '<span style="color: green;">soluble</span>'
return await memorize_map(
  e.cwf_sects("059f", "b92d", None,),
  {
    "[ammonium carbonate](ammonium%20carbonate.md)": soluble,
    "[ammonium chloride](ammonium%20chloride.md)": soluble,
    "[ammonium hydroxide](ammonia%20solution.md)": soluble,
    "[ammonium phosphate](ammonium%20phosphate.md)": soluble,
    "[ammonium sulfide](ammonium%20sulfide.md)": reacts,
    "[ammonium sulfite](ammonium%20sulfite.md)": soluble,
    "[barium hydroxide](barium%20hydroxide.md)": soluble,
    "[barium oxide](barium%20oxide.md)": reacts,
    "[barium sulfate](barium%20sulfate.md)": insoluble,
    "[calcium hydroxide](calcium%20hydroxide.md)": slightly_soluble,
    "[calcium oxide](calcium%20oxide.md)": reacts,
    "[calcium sulfate](calcium%20sulfate.md)": slightly_soluble,
    "[calcium sulfide](calcium%20sulfide.md)": reacts,
    "[calcium sulfite](calcium%20sulfite.md)": insoluble,
    "[copper(I) bromide](copper(I)%20bromide.md)": insoluble,
    "[copper(I) chloride](copper(I)%20chloride.md)": insoluble,
    "[copper(I) iodide](copper(I)%20iodide.md)": insoluble,
    "[copper(II) bromide](copper(II)%20bromide.md)": soluble,
    "[copper(II) carbonate](copper(II)%20carbonate.md)": insoluble,
    "[copper(II) chloride](copper(II)%20chloride.md)": soluble,
    "[copper(II) ethanoate](copper(II)%20ethanoate.md)": soluble,
    "[copper(II) hydroxide](copper(II)%20hydroxide.md)": insoluble,
    "[copper(II) iodide](copper(II)%20iodide.md)": soluble,
    "[copper(II) oxide](copper(II)%20oxide.md)": insoluble,
    "[copper(II) phosphate](copper(II)%20phosphate.md)": insoluble,
    "[copper(II) sulfate](copper(II)%20sulfate.md)": soluble,
    "[copper(II) sulfide](copper(II)%20sulfide.md)": insoluble,
    "[lead(II) bromide](lead(II)%20bromide.md)": slightly_soluble,
    "[lead(II) chloride](lead(II)%20chloride.md)": slightly_soluble,
    "[lead(II) iodide](lead(II)%20iodide.md)": slightly_soluble,
    "[lead(II) sulfate](lead(II)%20sulfate.md)": insoluble,
    "[lithium phosphate](lithium%20phosphate.md)": slightly_soluble,
    "[mercury(I) bromide](mercury(I)%20bromide.md)": insoluble,
    "[mercury(I) chloride](mercury(I)%20chloride.md)": insoluble,
    "[mercury(I) iodide](mercury(I)%20iodide.md)": insoluble,
    "[mercury(II) bromide](mercury(II)%20bromide.md)": soluble,
    "[mercury(II) chloride](mercury(II)%20chloride.md)": soluble,
    "[mercury(II) iodide](mercury(II)%20iodide.md)": insoluble,
    "[silver bromide](silver%20bromide.md)": insoluble,
    "[silver chloride](silver%20chloride.md)": insoluble,
    "[silver ethanoate](silver%20ethanoate.md)": slightly_soluble,
    "[silver iodide](silver%20iodide.md)": insoluble,
    "[silver nitrate](silver%20nitrate.md)": soluble,
    "[silver sulfate](silver%20sulfate.md)": slightly_soluble,
    "[sodium carbonate](sodium%20carbonate.md)": soluble,
    "[sodium chloride](sodium%20chloride.md)": soluble,
    "[sodium fluoride](sodium%20fluoride.md)": soluble,
    "[sodium hydroxide](sodium%20hydroxide.md)": soluble,
    "[sodium oxide](sodium%20oxide.md)": reacts,
    "[sodium phosphate](sodium%20phosphate.md)": soluble,
    "[sodium sulfide](sodium%20sulfide.md)": reacts,
    "[sodium sulfite](sodium%20sulfite.md)": soluble,
    "[strontium hydroxide](strontium%20hydroxide.md)": slightly_soluble,
    "[strontium oxide](strontium%20oxide.md)": reacts,
    "[strontium sulfate](strontium%20sulfate.md)": slightly_soluble,
    "[thallium(I) hydroxide](thallium(I)%20hydroxide.md)": soluble,
    "[thallium(I) oxide](thallium(I)%20oxide.md)": reacts,
    "[thallium(III) oxide](thallium(III)%20oxide.md)": insoluble,
    "[uranyl carbonate](uranyl%20carbonate.md)": soluble,
  },
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="059f"--><!-- The following content is generated at 2023-10-11T09:39:11.357625+08:00. Any edits will be overridden! -->

> 1. [ammonium carbonate](ammonium%20carbonate.md): <span style="color: green;">soluble</span>
> 2. [ammonium chloride](ammonium%20chloride.md): <span style="color: green;">soluble</span>
> 3. [ammonium hydroxide](ammonia%20solution.md): <span style="color: green;">soluble</span>
> 4. [ammonium phosphate](ammonium%20phosphate.md): <span style="color: green;">soluble</span>
> 5. [ammonium sulfide](ammonium%20sulfide.md): <span style="color: violet;">reacts</span>
> 6. [ammonium sulfite](ammonium%20sulfite.md): <span style="color: green;">soluble</span>
> 7. [barium hydroxide](barium%20hydroxide.md): <span style="color: green;">soluble</span>
> 8. [barium oxide](barium%20oxide.md): <span style="color: violet;">reacts</span>
> 9. [barium sulfate](barium%20sulfate.md): <span style="color: red;">insoluble</span>
> 10. [calcium hydroxide](calcium%20hydroxide.md): <span style="color: yellow;">slightly soluble</span>
> 11. [calcium oxide](calcium%20oxide.md): <span style="color: violet;">reacts</span>
> 12. [calcium sulfate](calcium%20sulfate.md): <span style="color: yellow;">slightly soluble</span>
> 13. [calcium sulfide](calcium%20sulfide.md): <span style="color: violet;">reacts</span>
> 14. [calcium sulfite](calcium%20sulfite.md): <span style="color: red;">insoluble</span>
> 15. [copper(I) bromide](copper(I)%20bromide.md): <span style="color: red;">insoluble</span>
> 16. [copper(I) chloride](copper(I)%20chloride.md): <span style="color: red;">insoluble</span>
> 17. [copper(I) iodide](copper(I)%20iodide.md): <span style="color: red;">insoluble</span>
> 18. [copper(II) bromide](copper(II)%20bromide.md): <span style="color: green;">soluble</span>
> 19. [copper(II) carbonate](copper(II)%20carbonate.md): <span style="color: red;">insoluble</span>
> 20. [copper(II) chloride](copper(II)%20chloride.md): <span style="color: green;">soluble</span>
> 21. [copper(II) ethanoate](copper(II)%20ethanoate.md): <span style="color: green;">soluble</span>
> 22. [copper(II) hydroxide](copper(II)%20hydroxide.md): <span style="color: red;">insoluble</span>
> 23. [copper(II) iodide](copper(II)%20iodide.md): <span style="color: green;">soluble</span>
> 24. [copper(II) oxide](copper(II)%20oxide.md): <span style="color: red;">insoluble</span>
> 25. [copper(II) phosphate](copper(II)%20phosphate.md): <span style="color: red;">insoluble</span>
> 26. [copper(II) sulfate](copper(II)%20sulfate.md): <span style="color: green;">soluble</span>
> 27. [copper(II) sulfide](copper(II)%20sulfide.md): <span style="color: red;">insoluble</span>
> 28. [lead(II) bromide](lead(II)%20bromide.md): <span style="color: yellow;">slightly soluble</span>
> 29. [lead(II) chloride](lead(II)%20chloride.md): <span style="color: yellow;">slightly soluble</span>
> 30. [lead(II) iodide](lead(II)%20iodide.md): <span style="color: yellow;">slightly soluble</span>
> 31. [lead(II) sulfate](lead(II)%20sulfate.md): <span style="color: red;">insoluble</span>
> 32. [lithium phosphate](lithium%20phosphate.md): <span style="color: yellow;">slightly soluble</span>
> 33. [mercury(I) bromide](mercury(I)%20bromide.md): <span style="color: red;">insoluble</span>
> 34. [mercury(I) chloride](mercury(I)%20chloride.md): <span style="color: red;">insoluble</span>
> 35. [mercury(I) iodide](mercury(I)%20iodide.md): <span style="color: red;">insoluble</span>
> 36. [mercury(II) bromide](mercury(II)%20bromide.md): <span style="color: green;">soluble</span>
> 37. [mercury(II) chloride](mercury(II)%20chloride.md): <span style="color: green;">soluble</span>
> 38. [mercury(II) iodide](mercury(II)%20iodide.md): <span style="color: red;">insoluble</span>
> 39. [silver bromide](silver%20bromide.md): <span style="color: red;">insoluble</span>
> 40. [silver chloride](silver%20chloride.md): <span style="color: red;">insoluble</span>
> 41. [silver ethanoate](silver%20ethanoate.md): <span style="color: yellow;">slightly soluble</span>
> 42. [silver iodide](silver%20iodide.md): <span style="color: red;">insoluble</span>
> 43. [silver nitrate](silver%20nitrate.md): <span style="color: green;">soluble</span>
> 44. [silver sulfate](silver%20sulfate.md): <span style="color: yellow;">slightly soluble</span>
> 45. [sodium carbonate](sodium%20carbonate.md): <span style="color: green;">soluble</span>
> 46. [sodium chloride](sodium%20chloride.md): <span style="color: green;">soluble</span>
> 47. [sodium fluoride](sodium%20fluoride.md): <span style="color: green;">soluble</span>
> 48. [sodium hydroxide](sodium%20hydroxide.md): <span style="color: green;">soluble</span>
> 49. [sodium oxide](sodium%20oxide.md): <span style="color: violet;">reacts</span>
> 50. [sodium phosphate](sodium%20phosphate.md): <span style="color: green;">soluble</span>
> 51. [sodium sulfide](sodium%20sulfide.md): <span style="color: violet;">reacts</span>
> 52. [sodium sulfite](sodium%20sulfite.md): <span style="color: green;">soluble</span>
> 53. [strontium hydroxide](strontium%20hydroxide.md): <span style="color: yellow;">slightly soluble</span>
> 54. [strontium oxide](strontium%20oxide.md): <span style="color: violet;">reacts</span>
> 55. [strontium sulfate](strontium%20sulfate.md): <span style="color: yellow;">slightly soluble</span>
> 56. [thallium(I) hydroxide](thallium(I)%20hydroxide.md): <span style="color: green;">soluble</span>
> 57. [thallium(I) oxide](thallium(I)%20oxide.md): <span style="color: violet;">reacts</span>
> 58. [thallium(III) oxide](thallium(III)%20oxide.md): <span style="color: red;">insoluble</span>
> 59. [uranyl carbonate](uranyl%20carbonate.md): <span style="color: green;">soluble</span>

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b92d"--><!-- The following content is generated at 2023-10-11T09:39:11.311096+08:00. Any edits will be overridden! -->

1. [ammonium carbonate](ammonium%20carbonate.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-12,39,298-->
2. [ammonium chloride](ammonium%20chloride.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-18,45,298-->
3. [ammonium hydroxide](ammonia%20solution.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-21,48,298-->
4. [ammonium phosphate](ammonium%20phosphate.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-21,48,298-->
5. [ammonium sulfide](ammonium%20sulfide.md)::<span style="color: violet;">reacts</span> <!--SR:!2023-11-28,19,258-->
6. [ammonium sulfite](ammonium%20sulfite.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-22,49,298-->
7. [barium hydroxide](barium%20hydroxide.md)::<span style="color: green;">soluble</span> <!--SR:!2023-11-17,14,258-->
8. [barium oxide](barium%20oxide.md)::<span style="color: violet;">reacts</span> <!--SR:!2023-12-04,31,278-->
9. [barium sulfate](barium%20sulfate.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-12-04,31,278-->
10. [calcium hydroxide](calcium%20hydroxide.md)::<span style="color: yellow;">slightly soluble</span> <!--SR:!2023-11-24,15,278-->
11. [calcium oxide](calcium%20oxide.md)::<span style="color: violet;">reacts</span> <!--SR:!2023-11-15,12,258-->
12. [calcium sulfate](calcium%20sulfate.md)::<span style="color: yellow;">slightly soluble</span> <!--SR:!2023-11-24,12,218-->
13. [calcium sulfide](calcium%20sulfide.md)::<span style="color: violet;">reacts</span> <!--SR:!2023-11-16,13,238-->
14. [calcium sulfite](calcium%20sulfite.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-11-14,2,150-->
15. [copper(I) bromide](copper(I)%20bromide.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-11-26,17,258-->
16. [copper(I) chloride](copper(I)%20chloride.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-12-10,37,278-->
17. [copper(I) iodide](copper(I)%20iodide.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-11-17,14,258-->
18. [copper(II) bromide](copper(II)%20bromide.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-10,37,298-->
19. [copper(II) carbonate](copper(II)%20carbonate.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-12-14,41,298-->
20. [copper(II) chloride](copper(II)%20chloride.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-15,42,298-->
21. [copper(II) ethanoate](copper(II)%20ethanoate.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-21,48,298-->
22. [copper(II) hydroxide](copper(II)%20hydroxide.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-12-05,32,278-->
23. [copper(II) iodide](copper(II)%20iodide.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-11,38,298-->
24. [copper(II) oxide](copper(II)%20oxide.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-11-23,14,238-->
25. [copper(II) phosphate](copper(II)%20phosphate.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-11-19,16,258-->
26. [copper(II) sulfate](copper(II)%20sulfate.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-15,42,298-->
27. [copper(II) sulfide](copper(II)%20sulfide.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-12-05,32,278-->
28. [lead(II) bromide](lead(II)%20bromide.md)::<span style="color: yellow;">slightly soluble</span> <!--SR:!2023-11-28,25,278-->
29. [lead(II) chloride](lead(II)%20chloride.md)::<span style="color: yellow;">slightly soluble</span> <!--SR:!2023-12-07,34,278-->
30. [lead(II) iodide](lead(II)%20iodide.md)::<span style="color: yellow;">slightly soluble</span> <!--SR:!2023-11-15,4,198-->
31. [lead(II) sulfate](lead(II)%20sulfate.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-11-16,5,178-->
32. [lithium phosphate](lithium%20phosphate.md)::<span style="color: yellow;">slightly soluble</span> <!--SR:!2023-11-24,13,218-->
33. [mercury(I) bromide](mercury(I)%20bromide.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-12-27,54,298-->
34. [mercury(I) chloride](mercury(I)%20chloride.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-12-05,32,278-->
35. [mercury(I) iodide](mercury(I)%20iodide.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-12-07,34,298-->
36. [mercury(II) bromide](mercury(II)%20bromide.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-07,34,298-->
37. [mercury(II) chloride](mercury(II)%20chloride.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-22,49,298-->
38. [mercury(II) iodide](mercury(II)%20iodide.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-11-14,11,238-->
39. [silver bromide](silver%20bromide.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-12-19,46,298-->
40. [silver chloride](silver%20chloride.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-12-09,36,298-->
41. [silver ethanoate](silver%20ethanoate.md)::<span style="color: yellow;">slightly soluble</span> <!--SR:!2023-12-24,51,298-->
42. [silver iodide](silver%20iodide.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-12-19,46,298-->
43. [silver nitrate](silver%20nitrate.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-26,53,298-->
44. [silver sulfate](silver%20sulfate.md)::<span style="color: yellow;">slightly soluble</span> <!--SR:!2023-11-19,16,258-->
45. [sodium carbonate](sodium%20carbonate.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-11,38,298-->
46. [sodium chloride](sodium%20chloride.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-18,45,298-->
47. [sodium fluoride](sodium%20fluoride.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-18,45,298-->
48. [sodium hydroxide](sodium%20hydroxide.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-16,43,298-->
49. [sodium oxide](sodium%20oxide.md)::<span style="color: violet;">reacts</span> <!--SR:!2023-12-10,37,298-->
50. [sodium phosphate](sodium%20phosphate.md)::<span style="color: green;">soluble</span> <!--SR:!2023-11-14,11,258-->
51. [sodium sulfide](sodium%20sulfide.md)::<span style="color: violet;">reacts</span> <!--SR:!2023-11-13,10,258-->
52. [sodium sulfite](sodium%20sulfite.md)::<span style="color: green;">soluble</span> <!--SR:!2023-11-25,22,278-->
53. [strontium hydroxide](strontium%20hydroxide.md)::<span style="color: yellow;">slightly soluble</span> <!--SR:!2023-11-13,4,178-->
54. [strontium oxide](strontium%20oxide.md)::<span style="color: violet;">reacts</span> <!--SR:!2023-11-15,12,258-->
55. [strontium sulfate](strontium%20sulfate.md)::<span style="color: yellow;">slightly soluble</span> <!--SR:!2023-11-15,4,198-->
56. [thallium(I) hydroxide](thallium(I)%20hydroxide.md)::<span style="color: green;">soluble</span> <!--SR:!2023-12-06,33,278-->
57. [thallium(I) oxide](thallium(I)%20oxide.md)::<span style="color: violet;">reacts</span> <!--SR:!2023-11-26,16,238-->
58. [thallium(III) oxide](thallium(III)%20oxide.md)::<span style="color: red;">insoluble</span> <!--SR:!2023-12-01,20,258-->
59. [uranyl carbonate](uranyl%20carbonate.md)::<span style="color: green;">soluble</span> <!--SR:!2023-11-26,23,278-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

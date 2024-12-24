---
aliases:
  - insolubilities
  - insolubility
  - insoluble
  - solubilities
  - solubility
  - soluble
tags:
  - flashcard/active/general/solubility
  - language/in/English
---

# solubility

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

__Solubility__ is {@{the ability of a [solute](solution%20(chemistry).md) to form a [solution](solution%20(chemistry).md) with a [solvent](solvent.md)}@}.

It is measured as {@{the [concentration](concentration.md) of the solute in a saturated solution, in which no more solute can be [dissolved](solvation.md)}@}.

## solubility of ionic compounds in water

```Python
# pytextgen generate data
from pytextgen import gen, read, util
import typing
soluble = R'<span style="color\: green;">soluble</span>'
insoluble = R'<span style="color\: red;">insoluble</span>'
data: typing.Mapping[str, typing.Mapping[str, str]] = {
  'group I compounds': {
    'general solubility': soluble,
    'exception(s)': '([Li<sub>3</sub>PO<sub>4</sub>](lithium%20phosphate.md) is slightly soluble)',
  },
  'NH<sub>4</sub><sup>+</sup> compounds': {
    'general solubility': soluble,
    'exception(s)': '(none)',
  },
  'nitrates': {
    'general solubility': soluble,
    'exception(s)': '(none)',
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
    'exception(s)': 'group I and NH<sub>4</sub><sup>+</sup> compounds ([Li<sub>3</sub>PO<sub>4</sub>](lithium%20phosphate.md) is slightly soluble)',
  },
  'hydroxides': {
    'general solubility': insoluble,
    'exception(s)': 'group I, group II (except [Be(OH)<sub>2</sub>](beryllium%20hydroxide.md) and [Mg(OH)<sub>2</sub>](magnesium%20hydroxide.md)), NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds ([Ca(OH)<sub>2</sub>](calcium%20hydroxide.md) is slightly soluble)',
  },
  'oxides': {
    'general solubility': insoluble,
    'exception(s)': 'group I, group II (except [BeO](beryllium%20oxide.md)), NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds',
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
      separator="\n\n<!-- markdownlint MD028 -->\n\n",
      states=await read.read_flashcard_states(__env__.cwf_sect('901862')),
    ),
  ),
)
```

<!--pytextgen generate section="901862"--><!-- The following content is generated at 2024-02-01T20:43:13.427525+08:00. Any edits will be overridden! -->

> group I compounds
>
> - general solubility: {@{<span style="color: green;">soluble</span>}@}
> - exception(s): {@{([Li<sub>3</sub>PO<sub>4</sub>](lithium%20phosphate.md) is slightly soluble)}@}

<!-- markdownlint MD028 -->

> NH<sub>4</sub><sup>+</sup> compounds
>
> - general solubility: {@{<span style="color: green;">soluble</span>}@}
> - exception(s): {@{(none)}@}

<!-- markdownlint MD028 -->

> nitrates
>
> - general solubility: {@{<span style="color: green;">soluble</span>}@}
> - exception(s): {@{(none)}@}

<!-- markdownlint MD028 -->

> acetates (ethanoates)
>
> - general solubility: {@{<span style="color: green;">soluble</span>}@}
> - exception(s): {@{Ag<sup>+</sup> compounds}@}

<!-- markdownlint MD028 -->

> chlorides
>
> - general solubility: {@{<span style="color: green;">soluble</span>}@}
> - exception(s): {@{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds}@}

<!-- markdownlint MD028 -->

> bromides
>
> - general solubility: {@{<span style="color: green;">soluble</span>}@}
> - exception(s): {@{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, and Hg<sub>2</sub><sup>2+</sup> compounds}@}

<!-- markdownlint MD028 -->

> iodides
>
> - general solubility: {@{<span style="color: green;">soluble</span>}@}
> - exception(s): {@{Ag<sup>+</sup>, Pb<sup>2+</sup>, Cu<sup>+</sup>, Hg<sub>2</sub><sup>2+</sup>, and Hg<sup>2+</sup> compounds}@}

<!-- markdownlint MD028 -->

> sulfates
>
> - general solubility: {@{<span style="color: green;">soluble</span>}@}
> - exception(s): {@{Ag<sup>+</sup>, Pb<sup>2+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Ca<sup>2+</sup> compounds}@}

<!-- markdownlint MD028 -->

> carbonates
>
> - general solubility: {@{<span style="color: red;">insoluble</span>}@}
> - exception(s): {@{group I, NH<sub>4</sub><sup>+</sup>, and UO<sub>2</sub><sup>2+</sup> compounds}@}

<!-- markdownlint MD028 -->

> sulfites
>
> - general solubility: {@{<span style="color: red;">insoluble</span>}@}
> - exception(s): {@{group I and NH<sub>4</sub><sup>+</sup> compounds}@}

<!-- markdownlint MD028 -->

> phosphates
>
> - general solubility: {@{<span style="color: red;">insoluble</span>}@}
> - exception(s): {@{group I and NH<sub>4</sub><sup>+</sup> compounds ([Li<sub>3</sub>PO<sub>4</sub>](lithium%20phosphate.md) is slightly soluble)}@}

<!-- markdownlint MD028 -->

> hydroxides
>
> - general solubility: {@{<span style="color: red;">insoluble</span>}@}
> - exception(s): {@{group I, group II (except [Be(OH)<sub>2</sub>](beryllium%20hydroxide.md) and [Mg(OH)<sub>2</sub>](magnesium%20hydroxide.md)), NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds ([Ca(OH)<sub>2</sub>](calcium%20hydroxide.md) is slightly soluble)}@}

<!-- markdownlint MD028 -->

> oxides
>
> - general solubility: {@{<span style="color: red;">insoluble</span>}@}
> - exception(s): {@{group I, group II (except [BeO](beryllium%20oxide.md)), NH<sub>4</sub><sup>+</sup>, Ba<sup>2+</sup>, Sr<sup>2+</sup>, and Tl<sup>+</sup> compounds}@}

<!-- markdownlint MD028 -->

> sulfides
>
> - general solubility: {@{<span style="color: red;">insoluble</span>}@}
> - exception(s): {@{group I, group II, and NH<sub>4</sub><sup>+</sup> compounds}@}

<!--/pytextgen-->

### examples

```Python
# pytextgen generate data
insoluble = '<span style="color: red;">insoluble</span>'
reacts = '<span style="color: violet;">reacts</span>'
slightly_soluble = '<span style="background-color: black; color: yellow;">slightly soluble</span>'
soluble = '<span style="color: green;">soluble</span>'
return await memorize_map(
  __env__.cwf_sects("059f", "b92d", None,),
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

<!--pytextgen generate section="059f"--><!-- The following content is generated at 2023-11-04T02:46:37.245967+08:00. Any edits will be overridden! -->

> 1. [ammonium carbonate](ammonium%20carbonate.md): <span style="color: green;">soluble</span>
> 2. [ammonium chloride](ammonium%20chloride.md): <span style="color: green;">soluble</span>
> 3. [ammonium hydroxide](ammonia%20solution.md): <span style="color: green;">soluble</span>
> 4. [ammonium phosphate](ammonium%20phosphate.md): <span style="color: green;">soluble</span>
> 5. [ammonium sulfide](ammonium%20sulfide.md): <span style="color: violet;">reacts</span>
> 6. [ammonium sulfite](ammonium%20sulfite.md): <span style="color: green;">soluble</span>
> 7. [barium hydroxide](barium%20hydroxide.md): <span style="color: green;">soluble</span>
> 8. [barium oxide](barium%20oxide.md): <span style="color: violet;">reacts</span>
> 9. [barium sulfate](barium%20sulfate.md): <span style="color: red;">insoluble</span>
> 10. [calcium hydroxide](calcium%20hydroxide.md): <span style="background-color: black; color: yellow;">slightly soluble</span>
> 11. [calcium oxide](calcium%20oxide.md): <span style="color: violet;">reacts</span>
> 12. [calcium sulfate](calcium%20sulfate.md): <span style="background-color: black; color: yellow;">slightly soluble</span>
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
> 28. [lead(II) bromide](lead(II)%20bromide.md): <span style="background-color: black; color: yellow;">slightly soluble</span>
> 29. [lead(II) chloride](lead(II)%20chloride.md): <span style="background-color: black; color: yellow;">slightly soluble</span>
> 30. [lead(II) iodide](lead(II)%20iodide.md): <span style="background-color: black; color: yellow;">slightly soluble</span>
> 31. [lead(II) sulfate](lead(II)%20sulfate.md): <span style="color: red;">insoluble</span>
> 32. [lithium phosphate](lithium%20phosphate.md): <span style="background-color: black; color: yellow;">slightly soluble</span>
> 33. [mercury(I) bromide](mercury(I)%20bromide.md): <span style="color: red;">insoluble</span>
> 34. [mercury(I) chloride](mercury(I)%20chloride.md): <span style="color: red;">insoluble</span>
> 35. [mercury(I) iodide](mercury(I)%20iodide.md): <span style="color: red;">insoluble</span>
> 36. [mercury(II) bromide](mercury(II)%20bromide.md): <span style="color: green;">soluble</span>
> 37. [mercury(II) chloride](mercury(II)%20chloride.md): <span style="color: green;">soluble</span>
> 38. [mercury(II) iodide](mercury(II)%20iodide.md): <span style="color: red;">insoluble</span>
> 39. [silver bromide](silver%20bromide.md): <span style="color: red;">insoluble</span>
> 40. [silver chloride](silver%20chloride.md): <span style="color: red;">insoluble</span>
> 41. [silver ethanoate](silver%20ethanoate.md): <span style="background-color: black; color: yellow;">slightly soluble</span>
> 42. [silver iodide](silver%20iodide.md): <span style="color: red;">insoluble</span>
> 43. [silver nitrate](silver%20nitrate.md): <span style="color: green;">soluble</span>
> 44. [silver sulfate](silver%20sulfate.md): <span style="background-color: black; color: yellow;">slightly soluble</span>
> 45. [sodium carbonate](sodium%20carbonate.md): <span style="color: green;">soluble</span>
> 46. [sodium chloride](sodium%20chloride.md): <span style="color: green;">soluble</span>
> 47. [sodium fluoride](sodium%20fluoride.md): <span style="color: green;">soluble</span>
> 48. [sodium hydroxide](sodium%20hydroxide.md): <span style="color: green;">soluble</span>
> 49. [sodium oxide](sodium%20oxide.md): <span style="color: violet;">reacts</span>
> 50. [sodium phosphate](sodium%20phosphate.md): <span style="color: green;">soluble</span>
> 51. [sodium sulfide](sodium%20sulfide.md): <span style="color: violet;">reacts</span>
> 52. [sodium sulfite](sodium%20sulfite.md): <span style="color: green;">soluble</span>
> 53. [strontium hydroxide](strontium%20hydroxide.md): <span style="background-color: black; color: yellow;">slightly soluble</span>
> 54. [strontium oxide](strontium%20oxide.md): <span style="color: violet;">reacts</span>
> 55. [strontium sulfate](strontium%20sulfate.md): <span style="background-color: black; color: yellow;">slightly soluble</span>
> 56. [thallium(I) hydroxide](thallium(I)%20hydroxide.md): <span style="color: green;">soluble</span>
> 57. [thallium(I) oxide](thallium(I)%20oxide.md): <span style="color: violet;">reacts</span>
> 58. [thallium(III) oxide](thallium(III)%20oxide.md): <span style="color: red;">insoluble</span>
> 59. [uranyl carbonate](uranyl%20carbonate.md): <span style="color: green;">soluble</span>

<!--/pytextgen-->

<!--pytextgen generate section="b92d"--><!-- The following content is generated at 2024-01-04T20:17:52.642068+08:00. Any edits will be overridden! -->

- [ammonium carbonate](ammonium%20carbonate.md):@:<span style="color: green;">soluble</span>
- [ammonium chloride](ammonium%20chloride.md):@:<span style="color: green;">soluble</span>
- [ammonium hydroxide](ammonia%20solution.md):@:<span style="color: green;">soluble</span>
- [ammonium phosphate](ammonium%20phosphate.md):@:<span style="color: green;">soluble</span>
- [ammonium sulfide](ammonium%20sulfide.md):@:<span style="color: violet;">reacts</span>
- [ammonium sulfite](ammonium%20sulfite.md):@:<span style="color: green;">soluble</span>
- [barium hydroxide](barium%20hydroxide.md):@:<span style="color: green;">soluble</span>
- [barium oxide](barium%20oxide.md):@:<span style="color: violet;">reacts</span>
- [barium sulfate](barium%20sulfate.md):@:<span style="color: red;">insoluble</span>
- [calcium hydroxide](calcium%20hydroxide.md):@:<span style="background-color: black; color: yellow;">slightly soluble</span>
- [calcium oxide](calcium%20oxide.md):@:<span style="color: violet;">reacts</span>
- [calcium sulfate](calcium%20sulfate.md):@:<span style="background-color: black; color: yellow;">slightly soluble</span>
- [calcium sulfide](calcium%20sulfide.md):@:<span style="color: violet;">reacts</span>
- [calcium sulfite](calcium%20sulfite.md):@:<span style="color: red;">insoluble</span>
- [copper(I) bromide](copper(I)%20bromide.md):@:<span style="color: red;">insoluble</span>
- [copper(I) chloride](copper(I)%20chloride.md):@:<span style="color: red;">insoluble</span>
- [copper(I) iodide](copper(I)%20iodide.md):@:<span style="color: red;">insoluble</span>
- [copper(II) bromide](copper(II)%20bromide.md):@:<span style="color: green;">soluble</span>
- [copper(II) carbonate](copper(II)%20carbonate.md):@:<span style="color: red;">insoluble</span>
- [copper(II) chloride](copper(II)%20chloride.md):@:<span style="color: green;">soluble</span>
- [copper(II) ethanoate](copper(II)%20ethanoate.md):@:<span style="color: green;">soluble</span>
- [copper(II) hydroxide](copper(II)%20hydroxide.md):@:<span style="color: red;">insoluble</span>
- [copper(II) iodide](copper(II)%20iodide.md):@:<span style="color: green;">soluble</span>
- [copper(II) oxide](copper(II)%20oxide.md):@:<span style="color: red;">insoluble</span>
- [copper(II) phosphate](copper(II)%20phosphate.md):@:<span style="color: red;">insoluble</span>
- [copper(II) sulfate](copper(II)%20sulfate.md):@:<span style="color: green;">soluble</span>
- [copper(II) sulfide](copper(II)%20sulfide.md):@:<span style="color: red;">insoluble</span>
- [lead(II) bromide](lead(II)%20bromide.md):@:<span style="background-color: black; color: yellow;">slightly soluble</span>
- [lead(II) chloride](lead(II)%20chloride.md):@:<span style="background-color: black; color: yellow;">slightly soluble</span>
- [lead(II) iodide](lead(II)%20iodide.md):@:<span style="background-color: black; color: yellow;">slightly soluble</span>
- [lead(II) sulfate](lead(II)%20sulfate.md):@:<span style="color: red;">insoluble</span>
- [lithium phosphate](lithium%20phosphate.md):@:<span style="background-color: black; color: yellow;">slightly soluble</span>
- [mercury(I) bromide](mercury(I)%20bromide.md):@:<span style="color: red;">insoluble</span>
- [mercury(I) chloride](mercury(I)%20chloride.md):@:<span style="color: red;">insoluble</span>
- [mercury(I) iodide](mercury(I)%20iodide.md):@:<span style="color: red;">insoluble</span>
- [mercury(II) bromide](mercury(II)%20bromide.md):@:<span style="color: green;">soluble</span>
- [mercury(II) chloride](mercury(II)%20chloride.md):@:<span style="color: green;">soluble</span>
- [mercury(II) iodide](mercury(II)%20iodide.md):@:<span style="color: red;">insoluble</span>
- [silver bromide](silver%20bromide.md):@:<span style="color: red;">insoluble</span>
- [silver chloride](silver%20chloride.md):@:<span style="color: red;">insoluble</span>
- [silver ethanoate](silver%20ethanoate.md):@:<span style="background-color: black; color: yellow;">slightly soluble</span>
- [silver iodide](silver%20iodide.md):@:<span style="color: red;">insoluble</span>
- [silver nitrate](silver%20nitrate.md):@:<span style="color: green;">soluble</span>
- [silver sulfate](silver%20sulfate.md):@:<span style="background-color: black; color: yellow;">slightly soluble</span>
- [sodium carbonate](sodium%20carbonate.md):@:<span style="color: green;">soluble</span>
- [sodium chloride](sodium%20chloride.md):@:<span style="color: green;">soluble</span>
- [sodium fluoride](sodium%20fluoride.md):@:<span style="color: green;">soluble</span>
- [sodium hydroxide](sodium%20hydroxide.md):@:<span style="color: green;">soluble</span>
- [sodium oxide](sodium%20oxide.md):@:<span style="color: violet;">reacts</span>
- [sodium phosphate](sodium%20phosphate.md):@:<span style="color: green;">soluble</span>
- [sodium sulfide](sodium%20sulfide.md):@:<span style="color: violet;">reacts</span>
- [sodium sulfite](sodium%20sulfite.md):@:<span style="color: green;">soluble</span>
- [strontium hydroxide](strontium%20hydroxide.md):@:<span style="background-color: black; color: yellow;">slightly soluble</span>
- [strontium oxide](strontium%20oxide.md):@:<span style="color: violet;">reacts</span>
- [strontium sulfate](strontium%20sulfate.md):@:<span style="background-color: black; color: yellow;">slightly soluble</span>
- [thallium(I) hydroxide](thallium(I)%20hydroxide.md):@:<span style="color: green;">soluble</span>
- [thallium(I) oxide](thallium(I)%20oxide.md):@:<span style="color: violet;">reacts</span>
- [thallium(III) oxide](thallium(III)%20oxide.md):@:<span style="color: red;">insoluble</span>
- [uranyl carbonate](uranyl%20carbonate.md):@:<span style="color: green;">soluble</span>

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/solubility) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

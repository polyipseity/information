---
aliases:
  - Otto cycle
  - Otto cycles
  - otto cycle
  - otto cycles
tags:
  - flashcard/general/Otto_cycle
  - language/in/English
---

# Otto cycle

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

## processes

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("55aa", "f023",),
  (
    R"__[isobaric](isobaric%20process.md) expansion__: [volume](volume.md) increases from $V_0$ to $V_1$ and [work](work%20(physics).md) is done; usually ignored when analyzing the [thermodynamic cycle](thermodynamic%20cycle.md)",
    R"__[isentropic](isentropic%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_0$, [pressure](pressure.md) increases, and [work](work%20(physics).md) is received",
    R"__[isochoric](isochoric%20process.md) heating__: [pressure](pressure.md) increases",
    R"__[isentropic](isentropic%20process.md) expansion__: [volume](volume.md) increases from $V_0$ to $V_1$, [pressure](pressure.md) decreases, and [work](work%20(physics).md) is done",
    R"__[isochoric](isochoric%20process.md) cooling__: [pressure](pressure.md) decreases",
    R"__[isobaric](isobaric%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_0$ and [work](work%20(physics).md) is received; usually ignored when analyzing the [thermodynamic cycle](thermodynamic%20cycle.md)",
  ),
  pretext="starts outside the cycle in the [PV diagram](pressure–volume%20diagram.md)",
  posttext="ends outside the cycle in the [PV diagram](pressure–volume%20diagram.md)",
)
```

<!--pytextgen generate section="55aa"--><!-- The following content is generated at 2023-12-19T20:25:01.121772+08:00. Any edits will be overridden! -->

> 1. __[isobaric](isobaric%20process.md) expansion__: [volume](volume.md) increases from $V_0$ to $V_1$ and [work](work%20(physics).md) is done; usually ignored when analyzing the [thermodynamic cycle](thermodynamic%20cycle.md)
> 2. __[isentropic](isentropic%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_0$, [pressure](pressure.md) increases, and [work](work%20(physics).md) is received
> 3. __[isochoric](isochoric%20process.md) heating__: [pressure](pressure.md) increases
> 4. __[isentropic](isentropic%20process.md) expansion__: [volume](volume.md) increases from $V_0$ to $V_1$, [pressure](pressure.md) decreases, and [work](work%20(physics).md) is done
> 5. __[isochoric](isochoric%20process.md) cooling__: [pressure](pressure.md) decreases
> 6. __[isobaric](isobaric%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_0$ and [work](work%20(physics).md) is received; usually ignored when analyzing the [thermodynamic cycle](thermodynamic%20cycle.md)

<!--/pytextgen-->

<!--pytextgen generate section="f023"--><!-- The following content is generated at 2024-01-04T20:17:52.283870+08:00. Any edits will be overridden! -->

- _(starts outside the cycle in the [PV diagram](pressure–volume%20diagram.md))_→:::←__[isobaric](isobaric%20process.md) expansion__: [volume](volume.md) increases from $V_0$ to $V_1$ and [work](work%20(physics).md) is done; usually ignored when analyzing the [thermodynamic cycle](thermodynamic%20cycle.md) <!--SR:!2025-12-22,501,312!2024-09-14,198,312-->
- __[isobaric](isobaric%20process.md) expansion__: [volume](volume.md) increases from $V_0$ to $V_1$ and [work](work%20(physics).md) is done; usually ignored when analyzing the [thermodynamic cycle](thermodynamic%20cycle.md)→:::←__[isentropic](isentropic%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_0$, [pressure](pressure.md) increases, and [work](work%20(physics).md) is received <!--SR:!2024-08-25,174,312!2025-04-09,238,232-->
- __[isentropic](isentropic%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_0$, [pressure](pressure.md) increases, and [work](work%20(physics).md) is received→:::←__[isochoric](isochoric%20process.md) heating__: [pressure](pressure.md) increases <!--SR:!2025-08-06,405,292!2024-08-21,171,312-->
- __[isochoric](isochoric%20process.md) heating__: [pressure](pressure.md) increases→:::←__[isentropic](isentropic%20process.md) expansion__: [volume](volume.md) increases from $V_0$ to $V_1$, [pressure](pressure.md) decreases, and [work](work%20(physics).md) is done <!--SR:!2024-11-24,258,332!2024-09-09,183,312-->
- __[isentropic](isentropic%20process.md) expansion__: [volume](volume.md) increases from $V_0$ to $V_1$, [pressure](pressure.md) decreases, and [work](work%20(physics).md) is done→:::←__[isochoric](isochoric%20process.md) cooling__: [pressure](pressure.md) decreases <!--SR:!2024-09-30,199,312!2025-01-07,294,332-->
- __[isochoric](isochoric%20process.md) cooling__: [pressure](pressure.md) decreases→:::←__[isobaric](isobaric%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_0$ and [work](work%20(physics).md) is received; usually ignored when analyzing the [thermodynamic cycle](thermodynamic%20cycle.md) <!--SR:!2025-01-21,305,332!2025-03-16,300,292-->
- __[isobaric](isobaric%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_0$ and [work](work%20(physics).md) is received; usually ignored when analyzing the [thermodynamic cycle](thermodynamic%20cycle.md)→:::←_(ends outside the cycle in the [PV diagram](pressure–volume%20diagram.md))_ <!--SR:!2024-11-08,245,332!2024-12-10,271,332-->

<!--/pytextgen-->

## cycle analysis

> __maximum thermal efficiency of a Otto cycle__
>
> {{$$\eta_\mathrm{th} = 1 - \frac1{r^{\gamma - 1} }$$}}
>
> - where
>   - {{$\gamma$ is the [heat capacity ratio](heat%20capacity%20ratio.md) and $r = \frac{V_1}{V_2}$ is the [compression ratio](compression%20ratio.md) (i.e. the ratio of the [volume](volume.md) at its maximum over that at its minimum)}} <!--SR:!2024-12-27,237,270!2024-08-19,170,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Otto_cycle) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

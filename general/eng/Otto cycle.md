---
aliases:
  - Otto cycle
  - Otto cycles
  - otto cycle
  - otto cycles
tags:
  - flashcard/active/general/eng/Otto_cycle
  - language/in/English
---

# Otto cycle

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
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

- _(starts outside the cycle in the [PV diagram](pressure–volume%20diagram.md))_→::@::←__[isobaric](isobaric%20process.md) expansion__: [volume](volume.md) increases from $V_0$ to $V_1$ and [work](work%20(physics).md) is done; usually ignored when analyzing the [thermodynamic cycle](thermodynamic%20cycle.md) <!--SR:!2030-04-20,1567,312!2027-01-16,854,332-->
- __[isobaric](isobaric%20process.md) expansion__: [volume](volume.md) increases from $V_0$ to $V_1$ and [work](work%20(physics).md) is done; usually ignored when analyzing the [thermodynamic cycle](thermodynamic%20cycle.md)→::@::←__[isentropic](isentropic%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_0$, [pressure](pressure.md) increases, and [work](work%20(physics).md) is received <!--SR:!2030-10-09,1693,312!2026-10-13,552,232-->
- __[isentropic](isentropic%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_0$, [pressure](pressure.md) increases, and [work](work%20(physics).md) is received→::@::←__[isochoric](isochoric%20process.md) heating__: [pressure](pressure.md) increases <!--SR:!2028-11-07,1189,292!2030-08-26,1662,312-->
- __[isochoric](isochoric%20process.md) heating__: [pressure](pressure.md) increases→::@::←__[isentropic](isentropic%20process.md) expansion__: [volume](volume.md) increases from $V_0$ to $V_1$, [pressure](pressure.md) decreases, and [work](work%20(physics).md) is done <!--SR:!2027-04-01,858,332!2026-04-02,570,312-->
- __[isentropic](isentropic%20process.md) expansion__: [volume](volume.md) increases from $V_0$ to $V_1$, [pressure](pressure.md) decreases, and [work](work%20(physics).md) is done→::@::←__[isochoric](isochoric%20process.md) cooling__: [pressure](pressure.md) decreases <!--SR:!2026-06-12,620,312!2027-09-09,975,332-->
- __[isochoric](isochoric%20process.md) cooling__: [pressure](pressure.md) decreases→::@::←__[isobaric](isobaric%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_0$ and [work](work%20(physics).md) is received; usually ignored when analyzing the [thermodynamic cycle](thermodynamic%20cycle.md) <!--SR:!2026-10-15,479,312!2027-08-09,876,292-->
- __[isobaric](isobaric%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_0$ and [work](work%20(physics).md) is received; usually ignored when analyzing the [thermodynamic cycle](thermodynamic%20cycle.md)→::@::←_(ends outside the cycle in the [PV diagram](pressure–volume%20diagram.md))_ <!--SR:!2027-11-29,1116,352!2028-04-26,1233,352-->

<!--/pytextgen-->

## cycle analysis

> __maximum thermal efficiency of a Otto cycle__
>
> {@{$$\eta_\mathrm{th} = 1 - \frac1{r^{\gamma - 1} }$$}@}
>
> where
>
> - {@{$\gamma$}@} is {@{the [heat capacity ratio](heat%20capacity%20ratio.md)}@}
> - {@{$r = \frac{V_1}{V_2}$}@} is {@{the [compression ratio](compression%20ratio.md)}@} \(i.e. {@{the ratio of the [volume](volume.md) at its maximum over that at its minimum}@}\) <!--SR:!2026-09-27,639,270!2032-04-03,2256,330!2026-03-04,85,351!2026-03-03,84,351!2026-02-27,81,351!2026-02-21,76,351-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Otto_cycle) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

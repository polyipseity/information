---
aliases:
  - Diesel cycle
  - Diesel cycles
  - diesel cycle
  - diesel cycles
tags:
  - flashcard/active/general/eng/Diesel_cycle
  - language/in/English
---

# Diesel cycle

```Python
# pytextgen generate module
# import ../../../tools/utility.py.md
```

## idealized Diesel cycle

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("11aa", "33aa",),
  (
    R"__[isentropic](isentropic%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_2$, [pressure](pressure.md) increases, and [work](work%20(physics).md) is received",
    R"__[isobaric](isochoric%20process.md) expansion__: [volume](volume.md) increases from $V_2$ to $V_3$ and [work](work%20(physics).md) is done",
    R"__[isentropic](isentropic%20process.md) expansion__: [volume](volume.md) increases from $V_3$ to $V_1$, [pressure](pressure.md) decreases, and [work](work%20(physics).md) is done",
    R"__[isochoric](isochoric%20process.md) cooling__: [pressure](pressure.md) decreases",
  ),
  pretext="starts at bottom right in the [PV diagram](pressure–volume%20diagram.md)",
  posttext="ends at bottom right in the [PV diagram](pressure–volume%20diagram.md)",
)
```

<!--pytextgen generate section="11aa"--><!-- The following content is generated at 2023-12-19T20:25:01.123775+08:00. Any edits will be overridden! -->

> 1. __[isentropic](isentropic%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_2$, [pressure](pressure.md) increases, and [work](work%20(physics).md) is received
> 2. __[isobaric](isochoric%20process.md) expansion__: [volume](volume.md) increases from $V_2$ to $V_3$ and [work](work%20(physics).md) is done
> 3. __[isentropic](isentropic%20process.md) expansion__: [volume](volume.md) increases from $V_3$ to $V_1$, [pressure](pressure.md) decreases, and [work](work%20(physics).md) is done
> 4. __[isochoric](isochoric%20process.md) cooling__: [pressure](pressure.md) decreases

<!--/pytextgen-->

<!--pytextgen generate section="33aa"--><!-- The following content is generated at 2024-01-04T20:17:51.540996+08:00. Any edits will be overridden! -->

- _(starts at bottom right in the [PV diagram](pressure–volume%20diagram.md))_→::@::←__[isentropic](isentropic%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_2$, [pressure](pressure.md) increases, and [work](work%20(physics).md) is received <!--SR:!2024-12-26,255,308!2027-02-23,899,348-->
- __[isentropic](isentropic%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_2$, [pressure](pressure.md) increases, and [work](work%20(physics).md) is received→::@::←__[isobaric](isochoric%20process.md) expansion__: [volume](volume.md) increases from $V_2$ to $V_3$ and [work](work%20(physics).md) is done <!--SR:!2026-05-03,606,288!2025-04-10,319,288-->
- __[isobaric](isochoric%20process.md) expansion__: [volume](volume.md) increases from $V_2$ to $V_3$ and [work](work%20(physics).md) is done→::@::←__[isentropic](isentropic%20process.md) expansion__: [volume](volume.md) increases from $V_3$ to $V_1$, [pressure](pressure.md) decreases, and [work](work%20(physics).md) is done <!--SR:!2025-08-02,402,308!2025-10-30,484,328-->
- __[isentropic](isentropic%20process.md) expansion__: [volume](volume.md) increases from $V_3$ to $V_1$, [pressure](pressure.md) decreases, and [work](work%20(physics).md) is done→::@::←__[isochoric](isochoric%20process.md) cooling__: [pressure](pressure.md) decreases <!--SR:!2026-03-18,583,328!2026-06-03,639,328-->
- __[isochoric](isochoric%20process.md) cooling__: [pressure](pressure.md) decreases→::@::←_(ends at bottom right in the [PV diagram](pressure–volume%20diagram.md))_ <!--SR:!2025-10-07,498,328!2025-06-10,366,308-->

<!--/pytextgen-->

### maximum thermal efficiency

> __maximum thermal efficiency of a Diesel cycle__
>
> {@{$$\eta_\mathrm{th} = 1 - \frac1{r^{\gamma - 1} }\left(\frac{\alpha^\gamma - 1}{\gamma(\alpha - 1)}\right)$$}@}
>
> - where
>   - {@{$\gamma$ is the [heat capacity ratio](heat%20capacity%20ratio.md), $r = \frac{V_1}{V_2}$ is the [compression ratio](compression%20ratio.md) (i.e. the ratio of the [volume](volume.md) at its maximum over that at its minimum), and $\alpha = \frac{V_3}{V_2} = \frac{T_3}{T_1 r^{\gamma - 1} }$ is the cutoff ratio}@} <!--SR:!2025-02-16,57,150!2025-04-17,292,250-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/Diesel_cycle) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

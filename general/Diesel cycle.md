---
aliases:
  - Diesel cycle
  - Diesel cycles
  - diesel cycle
  - diesel cycles
tags:
  - flashcards/general/Diesel_cycle
  - languages/in/English
---

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../tools/utility.py.md
```
%%

# Diesel cycle

## idealized Diesel cycle

%%
```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
e = __env__
return await memorize_seq(
  e.cwf_sects("11aa", "33aa",),
  (
    R"__[isentropic](isentropic%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_2$, [pressure](pressure.md) increases, and [work](work%20(physics).md) is received",
    R"__[isobaric](isochoric%20process.md) expansion__: [volume](volume.md) increases from $V_2$ to $V_3$ and [work](work%20(physics).md) is done",
    R"__[isentropic](isentropic%20process.md) expansion__: [volume](volume.md) increases from $V_3$ to $V_1$, [pressure](pressure.md) decreases, and [work](work%20(physics).md) is done",
    R"__[isochoric](isochoric%20process.md) cooling__: [pressure](pressure.md) decreases",
  ),
)
```
%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="11aa"--><!-- The following content is generated at 2023-12-19T20:25:01.123775+08:00. Any edits will be overridden! -->

> 1. __[isentropic](isentropic%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_2$, [pressure](pressure.md) increases, and [work](work%20(physics).md) is received
> 2. __[isobaric](isochoric%20process.md) expansion__: [volume](volume.md) increases from $V_2$ to $V_3$ and [work](work%20(physics).md) is done
> 3. __[isentropic](isentropic%20process.md) expansion__: [volume](volume.md) increases from $V_3$ to $V_1$, [pressure](pressure.md) decreases, and [work](work%20(physics).md) is done
> 4. __[isochoric](isochoric%20process.md) cooling__: [pressure](pressure.md) decreases

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="33aa"--><!-- The following content is generated at 2023-12-19T20:25:01.101455+08:00. Any edits will be overridden! -->

1. _(begin)_→:::←__[isentropic](isentropic%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_2$, [pressure](pressure.md) increases, and [work](work%20(physics).md) is received <!--SR:!2023-12-30,6,268!2024-01-05,12,288-->
2. __[isentropic](isentropic%20process.md) compression__: [volume](volume.md) decreases from $V_1$ to $V_2$, [pressure](pressure.md) increases, and [work](work%20(physics).md) is received→:::←__[isobaric](isochoric%20process.md) expansion__: [volume](volume.md) increases from $V_2$ to $V_3$ and [work](work%20(physics).md) is done <!--SR:!2024-01-02,9,268!2024-01-06,9,248-->
3. __[isobaric](isochoric%20process.md) expansion__: [volume](volume.md) increases from $V_2$ to $V_3$ and [work](work%20(physics).md) is done→:::←__[isentropic](isentropic%20process.md) expansion__: [volume](volume.md) increases from $V_3$ to $V_1$, [pressure](pressure.md) decreases, and [work](work%20(physics).md) is done <!--SR:!2024-01-04,11,288!2024-01-02,9,288-->
4. __[isentropic](isentropic%20process.md) expansion__: [volume](volume.md) increases from $V_3$ to $V_1$, [pressure](pressure.md) decreases, and [work](work%20(physics).md) is done→:::←__[isochoric](isochoric%20process.md) cooling__: [pressure](pressure.md) decreases <!--SR:!2024-01-04,11,288!2024-01-05,12,288-->
5. __[isochoric](isochoric%20process.md) cooling__: [pressure](pressure.md) decreases→:::←_(end)_ <!--SR:!2024-01-01,8,268!2024-01-03,10,288-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### maximum thermal efficiency

> __maximum thermal efficiency of a Diesel cycle__
>
> {{$$\eta_\mathrm{th} = 1 - \frac1{r^{\gamma - 1} }\left(\frac{\alpha^\gamma - 1}{\gamma(\alpha - 1)}\right)$$}}
>
> - where
>     - {{$\gamma$ is the [heat capacity ratio](heat%20capacity%20ratio.md), $r = \frac{V_1}{V_2}$ is the [compression ratio](compression%20ratio.md) (i.e. the ratio of the [volume](volume.md) at its maximum over that at its minimum), and $\alpha = \frac{V_3}{V_2} = \frac{T_3}{T_1 r^{\gamma - 1} }$ is the cutoff ratio}} <!--SR:!2023-12-29,5,230!2023-12-29,8,250-->

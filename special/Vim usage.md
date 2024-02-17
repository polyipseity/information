---
aliases:
  - Vim help
  - Vim usage
tags:
  - flashcard/special/Vim_usage
  - language/in/English
---

# Vim usage

See also [Vim help files](https://vimhelp.org/).

- help with \[subject\]:::<ul><li>:h[elp] [subject]</li><li>&lt;F1&gt;</li><li>&lt;Help&gt;</li></ul> <!--SR:!2026-01-04,738,313!2024-04-23,349,333-->

## autocomplete

- cycle forward:::\<Tab\> <!--SR:!2026-06-18,886,348!2025-12-30,788,328-->
- cycle backward:::\<Ctrl\>+p <!--SR:!2026-01-16,805,328!2024-05-07,317,288-->
- show possibilities:::\<Ctrl\>+d <!--SR:!2024-04-21,170,173!2024-05-05,178,248-->

## pattern

- repeat (N=1) times:::(N) <a id="^repeatN"></a>^repeatN <!--SR:!2024-08-30,402,313!2024-06-03,385,348-->

## motion

- left:::\[[repeat N](#^repeatN)\]h <!--SR:!2024-06-10,392,348!2025-04-06,588,308-->
- down:::\[[repeat N](#^repeatN)\]j <!--SR:!2024-05-09,361,333!2025-12-17,775,328-->
- up:::\[[repeat N](#^repeatN)\]k <!--SR:!2024-09-14,423,290!2024-09-07,440,307-->
- right:::\[[repeat N](#^repeatN)\]l <!--SR:!2027-07-12,1243,348!2026-08-08,904,328-->
- before next word:::\[[repeat N](#^repeatN)\]w <!--SR:!2024-04-24,115,253!2024-07-12,353,288-->
- end of current word:::\[[repeat N](#^repeatN)\]e <!--SR:!2024-05-20,125,293!2024-04-25,350,333-->
- beginning of line:::0 <!--SR:!2024-04-03,330,330!2024-04-24,349,333-->
- end of line:::$ <!--SR:!2024-04-01,329,333!2024-04-22,348,333-->
- line \[N=(last)\]:::\[N\]G <!--SR:!2024-08-29,386,290!2026-04-17,810,313-->
- line \[N=1\]:::\[N\]gg <!--SR:!2024-03-20,319,333!2024-05-15,124,293-->
- matching character:::% <!--SR:!2024-10-24,457,293!2025-06-07,631,313-->

## write and quit

- quit current buffer::::q\[uit\]\<Enter\> <!--SR:!2024-03-06,306,333!2025-07-20,625,313-->
- quit current buffer, discard changes::::q\[uit\]!\<Enter\> <!--SR:!2024-03-21,320,333!2025-09-14,709,313-->
- write \[range=%\] to \[file=(current)\]::::\[range\]w\[rite\]\[!\] \[file\]\<Enter\> <!--SR:!2024-12-06,454,293!2024-05-27,379,348-->
- write to \[file=(current)\] and quit::::wq[!] \[file\]\<Enter\> <!--SR:!2024-03-27,325,333!2024-06-11,393,348-->

## insert

- quit insert mode:::\<Esc\> <!--SR:!2024-04-20,347,333!2024-03-31,328,333-->
- insert before cursor:::\[[repeat N](#^repeatN)\]i <!--SR:!2025-10-10,727,313!2024-02-20,279,328-->
- insert after cursor:::\[[repeat N](#^repeatN)\]a <!--SR:!2026-12-19,1073,333!2026-01-03,792,328-->
- insert after end of line:::\[[repeat N](#^repeatN)\]A <!--SR:!2025-10-05,640,273!2024-04-21,348,333-->
- change text from cursor to ([motion](#motion)):::c([motion](#motion)) <!--SR:!2025-07-20,680,313!2025-07-01,648,313-->
- insert lines below cursor:::\[[repeat N](#^repeatN)\]o <!--SR:!2024-03-27,281,273!2024-04-20,300,293-->
- insert lines above cursor:::\[[repeat N](#^repeatN)\]O <!--SR:!2025-10-09,727,313!2025-08-22,692,313-->

## replace

- exit replace mode:::([replace](#replace))\<Esc\> <!--SR:!2024-03-22,321,333!2024-06-24,404,348-->
- replace with (char):::\[[repeat N](#^repeatN)\]r(char) <!--SR:!2024-06-09,326,273!2026-05-03,822,313-->
- enter replace mode:::\[[repeat N](#^repeatN)\]R <!--SR:!2025-08-26,696,313!2025-12-16,741,313-->

## visual

- exit visual mode:::([visual](#visual))\<Esc\> <!--SR:!2024-06-05,385,348!2024-06-15,396,348-->
- highlight characters:::v <!--SR:!2026-07-03,967,348!2026-01-12,801,328-->
- highlight lines:::V <!--SR:!2024-04-16,296,273!2025-10-01,654,288-->
- highlight block:::\<Ctrl\>+v <!--SR:!2024-02-24,270,273!2024-05-24,375,348-->
- copy highlight into \["register=(latest)\]:::([visual](#visual))\["register\]y <!--SR:!2024-09-13,422,293!2024-08-09,368,288-->

## edit

- delete under cursor:::<ul><li>\[[repeat N](#^repeatN)\]x</li><li>\[[repeat N](#^repeatN)\]Delete</li></ul> <!--SR:!2024-05-28,380,347!2025-11-13,762,328-->
- delete from cursor to ([motion](#motion)):::d([motion](#motion)) <!--SR:!2024-05-11,363,330!2024-05-10,362,333-->
- delete lines:::\[[repeat N](#^repeatN)\]dd <!--SR:!2024-04-26,351,333!2026-01-07,796,328-->
- undo:::\[[repeat N](#^repeatN)\]u <!--SR:!2024-06-30,376,313!2024-05-24,126,293-->
- restore last changed line:::U <!--SR:!2026-05-07,825,313!2026-02-28,848,328-->
- copy from cursor to (motion) into \["register=(latest)\]:::\["register\]y(motion) <!--SR:!2024-04-14,287,273!2024-02-21,281,328-->
- paste \["register=(latest)\] after cursor:::\[[repeat N](#^repeatN)\]\["register\]p <!--SR:!2025-12-24,782,327!2024-05-29,381,348-->
- paste \["register=(latest)\] before cursor:::\[[repeat N](#^repeatN)\]\["register\]P <!--SR:!2026-12-25,1077,333!2025-12-19,777,327-->

## search and substitute

- search forward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]/(pattern)\[/\]\[offset\]\<Enter\> <!--SR:!2025-06-24,647,313!2024-03-24,279,273-->
- search backward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]?(pattern)\[?\]\[offset\]\<Enter\> <!--SR:!2024-06-01,304,250!2025-12-25,783,328-->
- repeat last search:::n <!--SR:!2027-02-27,1125,333!2025-11-18,767,328-->
- repeat last search reversed:::N <!--SR:!2025-06-01,631,313!2024-07-14,378,288-->
- repeat last search forward:::/\<Enter\> <!--SR:!2024-07-10,369,293!2024-07-25,396,293-->
- repeat last search backward:::?\<Enter\> <!--SR:!2024-10-12,449,293!2025-09-11,602,268-->
- substitute (pattern) with (string) in \[range=.\] with \[flags\]::::\[range\]s\[ubstitute\]/(pattern)/(string)/\[flags\]\<Enter\> <!--SR:!2025-04-21,556,273!2024-03-07,307,333-->

## command

- show filepath and cursor position:::\<Ctrl\>+g <!--SR:!2024-02-21,182,268!2024-03-15,51,148-->
- execute (command) in shell::::!(command)\<Enter\> <!--SR:!2025-02-05,460,273!2026-01-09,741,313-->

## options

- show ([option](#list%20of%20options)) value::::se\[t\] ([option](#list%20of%20options))?\<Enter\> <!--SR:!2024-08-16,366,293!2024-02-19,278,327-->
- set boolean but show non-boolean ([option](#list%20of%20options))::::se\[t\] ([option](#list%20of%20options))\<Enter\> <!--SR:!2026-11-05,1038,333!2025-05-10,497,268-->
- unset boolean ([option](#list%20of%20options))::::se\[t\] no([option](#list%20of%20options))\<Enter\> <!--SR:!2024-04-02,237,273!2024-05-12,364,333-->
- invert boolean ([option](#list%20of%20options))::::se\[t\] inv([option](#list%20of%20options))\<Enter\> <!--SR:!2024-03-04,304,333!2025-08-25,695,313-->

### list of options

- ignorecase, ic:::ignore case in search <!--SR:!2025-11-09,758,328!2026-01-11,800,328-->
- incsearch, is:::highlight while typing search <!--SR:!2025-06-23,647,313!2024-03-06,166,253-->
- hlsearch, hls:::highlight last search matches <!--SR:!2025-07-17,677,310!2025-12-26,784,328-->

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

- help with \[subject\]:::<ul><li>:h[elp] [subject]</li><li>&lt;F1&gt;</li><li>&lt;Help&gt;</li></ul> <!--SR:!2026-01-04,738,313!2028-09-10,1601,353-->

## autocomplete

- cycle forward:::\<Tab\> <!--SR:!2026-06-18,886,348!2025-12-30,788,328-->
- cycle backward:::\<Ctrl\>+p <!--SR:!2026-01-16,805,328!2026-11-07,912,288-->
- show possibilities:::\<Ctrl\>+d <!--SR:!2025-06-22,426,193!2024-08-04,90,228-->

## pattern

- repeat (N=1) times:::(N) <a id="^repeatN"></a>^repeatN <!--SR:!2024-08-30,402,313!2029-06-18,1841,368-->

## motion

- left:::\[[repeat N](#^repeatN)\]h <!--SR:!2029-07-28,1874,368!2025-04-06,588,308-->
- down:::\[[repeat N](#^repeatN)\]j <!--SR:!2028-11-22,1658,353!2025-12-17,775,328-->
- up:::\[[repeat N](#^repeatN)\]k <!--SR:!2024-09-14,423,290!2024-09-07,440,307-->
- right:::\[[repeat N](#^repeatN)\]l <!--SR:!2027-07-12,1243,348!2026-08-08,904,328-->
- before next word:::\[[repeat N](#^repeatN)\]w <!--SR:!2025-02-08,290,253!2027-04-26,1016,288-->
- end of current word:::\[[repeat N](#^repeatN)\]e <!--SR:!2025-10-12,508,313!2028-09-16,1605,353-->
- beginning of line:::0 <!--SR:!2028-05-15,1501,350!2028-09-11,1601,353-->
- end of line:::$ <!--SR:!2028-05-19,1509,353!2028-09-06,1598,353-->
- line \[N=(last)\]:::\[N\]G <!--SR:!2024-08-29,386,290!2026-04-17,810,313-->
- line \[N=1\]:::\[N\]gg <!--SR:!2027-02-14,1061,333!2025-10-01,504,313-->
- matching character:::% <!--SR:!2024-10-24,457,293!2025-06-07,631,313-->

## write and quit

- quit current buffer::::q\[uit\]\<Enter\> <!--SR:!2026-12-19,1018,333!2025-07-20,625,313-->
- quit current buffer, discard changes::::q\[uit\]!\<Enter\> <!--SR:!2028-03-29,1469,353!2025-09-14,709,313-->
- write \[range=%\] to \[file=(current)\]::::\[range\]w\[rite\]\[!\] \[file\]\<Enter\> <!--SR:!2024-12-06,454,293!2029-05-13,1812,368-->
- write to \[file=(current)\] and quit::::wq[!] \[file\]\<Enter\> <!--SR:!2027-03-14,1081,333!2028-03-09,1367,348-->

## insert

- quit insert mode:::\<Esc\> <!--SR:!2028-08-28,1591,353!2028-05-13,1504,353-->
- insert before cursor:::\[[repeat N](#^repeatN)\]i <!--SR:!2025-10-10,727,313!2026-08-22,914,328-->
- insert after cursor:::\[[repeat N](#^repeatN)\]a <!--SR:!2026-12-19,1073,333!2026-01-03,792,328-->
- insert after end of line:::\[[repeat N](#^repeatN)\]A <!--SR:!2025-10-05,640,273!2027-06-24,1158,333-->
- change text from cursor to ([motion](#motion)):::c([motion](#motion)) <!--SR:!2025-07-20,680,313!2025-07-01,648,313-->
- insert lines below cursor:::\[[repeat N](#^repeatN)\]o <!--SR:!2026-05-03,766,273!2027-08-23,1220,313-->
- insert lines above cursor:::\[[repeat N](#^repeatN)\]O <!--SR:!2025-10-09,727,313!2025-08-22,692,313-->

## replace

- exit replace mode:::([replace](#replace))\<Esc\> <!--SR:!2028-04-02,1472,353!2029-10-09,1932,368-->
- replace with (char):::\[[repeat N](#^repeatN)\]r(char) <!--SR:!2027-11-02,1241,293!2026-05-03,822,313-->
- enter replace mode:::\[[repeat N](#^repeatN)\]R <!--SR:!2025-08-26,696,313!2025-12-16,741,313-->

## visual

- exit visual mode:::([visual](#visual))\<Esc\> <!--SR:!2028-02-04,1339,348!2029-08-21,1893,368-->
- highlight characters:::v <!--SR:!2026-07-03,967,348!2026-01-12,801,328-->
- highlight lines:::V <!--SR:!2027-05-17,1126,293!2025-10-01,654,288-->
- highlight block:::\<Ctrl\>+v <!--SR:!2025-06-19,343,253!2027-12-19,1304,348-->
- copy highlight into \["register=(latest)\]:::([visual](#visual))\["register\]y <!--SR:!2024-09-13,422,293!2024-08-09,368,288-->

## edit

- delete under cursor:::<ul><li>\[[repeat N](#^repeatN)\]x</li><li>\[[repeat N](#^repeatN)\]Delete</li></ul> <!--SR:!2029-05-14,1812,367!2025-11-13,762,328-->
- delete from cursor to ([motion](#motion)):::d([motion](#motion)) <!--SR:!2027-08-21,1197,330!2027-08-28,1204,333-->
- delete lines:::\[[repeat N](#^repeatN)\]dd <!--SR:!2028-09-23,1610,353!2026-01-07,796,328-->
- undo:::\[[repeat N](#^repeatN)\]u <!--SR:!2028-12-13,1627,333!2025-10-18,512,313-->
- restore last changed line:::U <!--SR:!2026-05-07,825,313!2026-02-28,848,328-->
- copy from cursor to (motion) into \["register=(latest)\]:::\["register\]y(motion) <!--SR:!2026-06-07,783,273!2026-08-30,921,328-->
- paste \["register=(latest)\] after cursor:::\[[repeat N](#^repeatN)\]\["register\]p <!--SR:!2025-12-24,782,327!2029-05-25,1822,368-->
- paste \["register=(latest)\] before cursor:::\[[repeat N](#^repeatN)\]\["register\]P <!--SR:!2026-12-25,1077,333!2025-12-19,777,327-->

## search and substitute

- search forward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]/(pattern)\[/\]\[offset\]\<Enter\> <!--SR:!2025-06-24,647,313!2026-04-26,761,273-->
- search backward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]?(pattern)\[?\]\[offset\]\<Enter\> <!--SR:!2027-05-03,1066,270!2025-12-25,783,328-->
- repeat last search:::n <!--SR:!2027-02-27,1125,333!2025-11-18,767,328-->
- repeat last search reversed:::N <!--SR:!2025-06-01,631,313!2027-07-07,1088,288-->
- repeat last search forward:::/\<Enter\> <!--SR:!2027-06-26,1080,293!2027-09-29,1159,293-->
- repeat last search backward:::?\<Enter\> <!--SR:!2024-10-12,449,293!2025-09-11,602,268-->
- substitute (pattern) with (string) in \[range=.\] with \[flags\]::::\[range\]s\[ubstitute\]/(pattern)/(string)/\[flags\]\<Enter\> <!--SR:!2025-04-21,556,273!2026-12-23,1021,333-->

## command

- show filepath and cursor position:::\<Ctrl\>+g <!--SR:!2026-01-01,680,288!2024-09-10,106,148-->
- execute (command) in shell::::!(command)\<Enter\> <!--SR:!2025-02-05,460,273!2026-01-09,741,313-->

## options

- show ([option](#list%20of%20options)) value::::se\[t\] ([option](#list%20of%20options))?\<Enter\> <!--SR:!2024-08-16,366,293!2026-08-15,908,327-->
- set boolean but show non-boolean ([option](#list%20of%20options))::::se\[t\] ([option](#list%20of%20options))\<Enter\> <!--SR:!2026-11-05,1038,333!2025-05-10,497,268-->
- unset boolean ([option](#list%20of%20options))::::se\[t\] no([option](#list%20of%20options))\<Enter\> <!--SR:!2026-01-11,646,273!2028-12-07,1669,353-->
- invert boolean ([option](#list%20of%20options))::::se\[t\] inv([option](#list%20of%20options))\<Enter\> <!--SR:!2024-08-02,151,313!2025-08-25,695,313-->

### list of options

- ignorecase, ic:::ignore case in search <!--SR:!2025-11-09,758,328!2026-01-11,800,328-->
- incsearch, is:::highlight while typing search <!--SR:!2025-06-23,647,313!2025-04-29,419,253-->
- hlsearch, hls:::highlight last search matches <!--SR:!2025-07-17,677,310!2025-12-26,784,328-->

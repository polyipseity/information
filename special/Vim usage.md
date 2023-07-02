---
tags:
  - flashcards/special/Vim_usage
---

# Vim usage

See also [Vim help files](https://vimhelp.org/).

- help with \[subject\]:::<ul><li>:h[elp] [subject]</li><li>&lt;F1&gt;</li><li>&lt;Help&gt;</li></ul> <!--SR:!2023-12-28,236,313!2024-04-23,349,333-->

## autocomplete
- cycle forward:::\<Tab\> <!--SR:!2024-01-14,196,328!2023-10-19,185,308-->
- cycle backward:::\<Ctrl\>+p <!--SR:!2023-10-22,189,308!2024-05-07,317,288-->
- show possibilities:::\<Ctrl\>+d <!--SR:!2023-07-08,32,153!2023-08-03,37,248-->

## pattern
- repeat (N=1) times:::(N) ^repeatN <!--SR:!2023-07-22,128,313!2024-06-03,385,348-->

## motion
- left:::\[[repeat N](#^repeatN)\]h <!--SR:!2024-06-10,392,348!2023-08-26,143,288-->
- down:::\[[repeat N](#^repeatN)\]j <!--SR:!2024-05-09,361,333!2023-10-15,182,308-->
- up:::\[[repeat N](#^repeatN)\]k <!--SR:!2023-07-16,111,270!2024-09-07,440,307-->
- right:::\[[repeat N](#^repeatN)\]l <!--SR:!2024-02-15,275,328!2024-02-16,276,328-->
- before next word:::\[[repeat N](#^repeatN)\]w <!--SR:!2023-12-31,231,273!2023-07-25,117,288-->
- end of current word:::\[[repeat N](#^repeatN)\]e <!--SR:!2024-01-16,251,313!2024-04-25,350,333-->
- beginning of line:::0 <!--SR:!2024-04-03,330,330!2024-04-24,349,333-->
- end of line:::$ <!--SR:!2024-04-01,329,333!2024-04-22,348,333-->
- line \[N=(last)\]:::\[N\]G <!--SR:!2023-08-09,133,290!2024-01-28,259,313-->
- line \[N=1\]:::\[N\]gg <!--SR:!2024-03-20,319,333!2024-01-12,249,313-->
- matching character:::% <!--SR:!2023-07-23,118,273!2023-09-13,154,293-->

## write and quit
- quit current buffer::::q\[uit\]\<Enter\> <!--SR:!2024-03-06,306,333!2023-10-23,200,313-->
- quit current buffer, discard changes::::q\[uit\]!\<Enter\> <!--SR:!2024-03-21,320,333!2023-10-03,172,293-->
- write \[range=%\] to \[file=(current)\]::::\[range\]w\[rite\]\[!\] \[file\]\<Enter\> <!--SR:!2023-09-09,154,293!2024-05-27,379,348-->
- write to \[file=(current)\] and quit::::wq[!] \[file\]\<Enter\> <!--SR:!2024-03-27,325,333!2024-06-11,393,348-->

## insert
- quit insert mode:::\<Esc\> <!--SR:!2024-04-20,347,333!2024-03-31,328,333-->
- insert before cursor:::\[[repeat N](#^repeatN)\]i <!--SR:!2023-10-14,179,293!2024-02-20,279,328-->
- insert after cursor:::\[[repeat N](#^repeatN)\]a <!--SR:!2024-01-11,248,313!2023-10-20,186,308-->
- insert after end of line:::\[[repeat N](#^repeatN)\]A <!--SR:!2024-01-04,234,273!2024-04-21,348,333-->
- change text from cursor to ([motion](#motion)):::c([motion](#motion)) <!--SR:!2023-09-07,165,293!2023-09-19,162,293-->
- insert lines below cursor:::\[[repeat N](#^repeatN)\]o <!--SR:!2024-03-27,281,273!2024-04-20,300,293-->
- insert lines above cursor:::\[[repeat N](#^repeatN)\]O <!--SR:!2023-10-12,179,293!2023-09-27,167,293-->

## replace
- exit replace mode:::([replace](#replace))\<Esc\> <!--SR:!2024-03-22,321,333!2024-06-24,404,348-->
- replace with (char):::\[[repeat N](#^repeatN)\]r(char) <!--SR:!2023-07-17,113,273!2024-02-01,263,313-->
- enter replace mode:::\[[repeat N](#^repeatN)\]R <!--SR:!2023-09-26,167,293!2023-12-06,237,313-->

## visual
- exit visual mode:::([visual](#visual))\<Esc\> <!--SR:!2024-06-05,385,348!2024-06-15,396,348-->
- highlight characters:::v <!--SR:!2023-11-07,214,328!2023-10-23,188,308-->
- highlight lines:::V <!--SR:!2024-04-16,296,273!2023-12-17,175,268-->
- highlight block:::\<Ctrl\>+v <!--SR:!2024-02-24,270,273!2024-05-24,375,348-->
- copy highlight into \["register=(latest)\]:::([visual](#visual))\["register\]y <!--SR:!2023-07-14,107,273!2023-08-06,127,288-->

## edit
- delete under cursor:::<ul><li>\[[repeat N](#^repeatN)\]x</li><li>\[[repeat N](#^repeatN)\]Delete</li></ul> <!--SR:!2024-05-28,380,347!2023-10-10,179,308-->
- delete from cursor to ([motion](#motion)):::d([motion](#motion)) <!--SR:!2024-05-11,363,330!2024-05-10,362,333-->
- delete lines:::\[[repeat N](#^repeatN)\]dd <!--SR:!2024-04-26,351,333!2023-10-19,187,308-->
- undo:::\[[repeat N](#^repeatN)\]u <!--SR:!2024-06-30,376,313!2024-01-19,254,313-->
- restore last changed line:::U <!--SR:!2024-02-02,264,313!2023-10-22,199,308-->
- copy from cursor to (motion) into \["register=(latest)\]:::\["register\]y(motion) <!--SR:!2024-04-14,287,273!2024-02-21,281,328-->
- paste \["register=(latest)\] after cursor:::\[[repeat N](#^repeatN)\]\["register\]p <!--SR:!2023-10-17,185,307!2024-05-29,381,348-->
- paste \["register=(latest)\] before cursor:::\[[repeat N](#^repeatN)\]\["register\]P <!--SR:!2024-01-13,249,313!2023-10-17,183,307-->

## search and substitute
- search forward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]/(pattern)\[/\]\[offset\]\<Enter\> <!--SR:!2023-09-16,159,293!2024-03-24,279,273-->
- search backward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]?(pattern)\[?\]\[offset\]\<Enter\> <!--SR:!2023-08-02,90,230!2023-10-18,184,308-->
- repeat last search:::n <!--SR:!2024-01-29,260,313!2023-10-11,180,308-->
- repeat last search reversed:::N <!--SR:!2023-09-08,154,293!2024-07-14,378,288-->
- repeat last search forward:::/\<Enter\> <!--SR:!2023-07-04,94,273!2024-07-25,396,293-->
- repeat last search backward:::?\<Enter\> <!--SR:!2023-07-21,116,273!2024-01-18,225,268-->
- substitute (pattern) with (string) in \[range=.\] with \[flags\]::::\[range\]s\[ubstitute\]/(pattern)/(string)/\[flags\]\<Enter\> <!--SR:!2023-10-12,157,253!2024-03-07,307,333-->

## command
- show filepath and cursor position:::\<Ctrl\>+g <!--SR:!2023-08-23,52,248!2023-08-08,49,188-->
- execute (command) in shell::::!(command)\<Enter\> <!--SR:!2023-10-19,130,253!2023-12-30,237,313-->

## options
- show ([option](#list%20of%20options)) value::::se\[t\] ([option](#list%20of%20options))?\<Enter\> <!--SR:!2023-08-16,125,293!2024-02-19,278,327-->
- set boolean but show non-boolean ([option](#list%20of%20options))::::se\[t\] ([option](#list%20of%20options))\<Enter\> <!--SR:!2024-01-02,240,313!2023-12-30,186,268-->
- unset boolean ([option](#list%20of%20options))::::se\[t\] no([option](#list%20of%20options))\<Enter\> <!--SR:!2023-08-09,87,273!2024-05-12,364,333-->
- invert boolean ([option](#list%20of%20options))::::se\[t\] inv([option](#list%20of%20options))\<Enter\> <!--SR:!2024-03-04,304,333!2023-09-25,166,293-->

### list of options
- ignorecase, ic:::ignore case in search <!--SR:!2023-10-08,178,308!2023-10-21,188,308-->
- incsearch, is:::highlight while typing search <!--SR:!2023-09-15,159,293!2023-07-17,113,273-->
- hlsearch, hls:::highlight last search matches <!--SR:!2023-09-03,162,290!2023-10-16,184,308-->

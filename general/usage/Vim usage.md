#general/usage #flashcards/general/usage/Vim_usage

# Vim usage

See also [Vim help files](https://vimhelp.org/).

- help with \[subject\]:::<ul><li>:h[elp] [subject]</li><li>&lt;F1&gt;</li><li>&lt;Help&gt;</li></ul> <!--SR:!2023-05-06,74,313!2023-05-10,78,313-->

## autocomplete
- cycle forward:::\<Tab\> <!--SR:!2023-05-17,85,328!2023-04-17,60,308-->
- cycle backward:::\<Ctrl\>+p <!--SR:!2023-10-22,189,308!2023-06-25,105,288-->
- show possibilities:::\<Ctrl\>+d <!--SR:!2023-04-25,15,173!2023-04-23,23,268-->

## pattern
- repeat (N=1) times:::(N) ^repeatN <!--SR:!2023-07-22,128,313!2023-05-15,83,328-->

## motion
- left:::\[[repeat N](#^repeatN)\]h <!--SR:!2023-05-15,83,328!2023-08-26,143,288-->
- down:::\[[repeat N](#^repeatN)\]j <!--SR:!2023-05-12,80,313!2023-10-15,182,308-->
- up:::\[[repeat N](#^repeatN)\]k <!--SR:!2023-07-16,111,270!2023-06-24,105,287-->
- right:::\[[repeat N](#^repeatN)\]l <!--SR:!2023-05-16,84,328!2023-05-16,84,328-->
- before next word:::\[[repeat N](#^repeatN)\]w <!--SR:!2023-05-14,65,253!2023-07-25,117,288-->
- end of current word:::\[[repeat N](#^repeatN)\]e <!--SR:!2023-05-10,78,313!2023-05-11,79,313-->
- beginning of line:::0 <!--SR:!2023-05-09,77,310!2023-05-11,79,313-->
- end of line:::$ <!--SR:!2023-05-08,76,313!2023-05-10,78,313-->
- line \[N=(last)\]:::\[N\]G <!--SR:!2023-08-09,133,290!2023-05-12,80,313-->
- line \[N=1\]:::\[N\]gg <!--SR:!2023-05-06,74,313!2023-05-08,76,313-->
- matching character:::% <!--SR:!2023-07-23,118,273!2023-09-13,154,293-->

## write and quit
- quit current buffer::::q\[uit\]\<Enter\> <!--SR:!2023-05-05,73,313!2023-10-23,200,313-->
- quit current buffer, discard changes::::q\[uit\]!\<Enter\> <!--SR:!2023-05-06,74,313!2023-10-03,172,293-->
- write \[range=%\] to \[file=(current)\]::::\[range\]w\[rite\]\[!\] \[file\]\<Enter\> <!--SR:!2023-09-09,154,293!2023-05-14,82,328-->
- write to \[file=(current)\] and quit::::wq[!] \[file\]\<Enter\> <!--SR:!2023-05-07,75,313!2023-05-15,83,328-->

## insert
- quit insert mode:::\<Esc\> <!--SR:!2023-05-09,77,313!2023-05-08,76,313-->
- insert before cursor:::\[[repeat N](#^repeatN)\]i <!--SR:!2023-04-18,61,293!2023-05-17,85,328-->
- insert after cursor:::\[[repeat N](#^repeatN)\]a <!--SR:!2023-05-08,76,313!2023-04-17,60,308-->
- insert after end of line:::\[[repeat N](#^repeatN)\]A <!--SR:!2023-05-15,66,253!2023-05-09,77,313-->
- change text from cursor to ([motion](#motion)):::c([motion](#motion)) <!--SR:!2023-09-07,165,293!2023-09-19,162,293-->
- insert lines below cursor:::\[[repeat N](#^repeatN)\]o <!--SR:!2023-06-20,100,273!2023-06-25,99,293-->
- insert lines above cursor:::\[[repeat N](#^repeatN)\]O <!--SR:!2023-10-12,179,293!2023-09-27,167,293-->

## replace
- exit replace mode:::([replace](#replace))\<Esc\> <!--SR:!2023-05-06,74,313!2023-05-17,85,328-->
- replace with (char):::\[[repeat N](#^repeatN)\]r(char) <!--SR:!2023-07-17,113,273!2023-05-13,81,313-->
- enter replace mode:::\[[repeat N](#^repeatN)\]R <!--SR:!2023-09-26,167,293!2023-12-06,237,313-->

## visual
- exit visual mode:::([visual](#visual))\<Esc\> <!--SR:!2023-05-17,85,328!2023-05-16,84,328-->
- highlight characters:::v <!--SR:!2023-11-07,214,328!2023-04-18,61,308-->
- highlight lines:::V <!--SR:!2023-06-24,103,273!2023-04-22,22,268-->
- highlight block:::\<Ctrl\>+v <!--SR:!2023-05-30,76,253!2023-05-15,83,328-->
- copy highlight into \["register=(latest)\]:::([visual](#visual))\["register\]y <!--SR:!2023-07-14,107,273!2023-08-06,127,288-->

## edit
- delete under cursor:::<ul><li>\[[repeat N](#^repeatN)\]x</li><li>\[[repeat N](#^repeatN)\]Delete</li></ul> <!--SR:!2023-05-14,82,327!2023-10-10,179,308-->
- delete from cursor to ([motion](#motion)):::d([motion](#motion)) <!--SR:!2023-05-13,81,310!2023-05-13,81,313-->
- delete lines:::\[[repeat N](#^repeatN)\]dd <!--SR:!2023-05-11,79,313!2023-10-19,187,308-->
- undo:::\[[repeat N](#^repeatN)\]u <!--SR:!2023-06-20,95,293!2023-05-10,78,313-->
- restore last changed line:::U <!--SR:!2023-05-12,80,313!2023-10-22,199,308-->
- copy from cursor to (motion) into \["register=(latest)\]:::\["register\]y(motion) <!--SR:!2023-06-28,106,273!2023-05-16,84,328-->
- paste \["register=(latest)\] after cursor:::\[[repeat N](#^repeatN)\]\["register\]p <!--SR:!2023-10-17,185,307!2023-05-14,82,328-->
- paste \["register=(latest)\] before cursor:::\[[repeat N](#^repeatN)\]\["register\]P <!--SR:!2023-05-09,77,313!2023-04-17,60,307-->

## search and substitute
- search forward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]/(pattern)\[/\]\[offset\]\<Enter\> <!--SR:!2023-09-16,159,293!2023-06-18,98,273-->
- search backward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]?(pattern)\[?\]\[offset\]\<Enter\> <!--SR:!2023-05-04,39,230!2023-04-17,60,308-->
- repeat last search:::n <!--SR:!2023-05-13,81,313!2023-10-11,180,308-->
- repeat last search reversed:::N <!--SR:!2023-09-08,154,293!2023-06-29,98,268-->
- repeat last search forward:::/\<Enter\> <!--SR:!2023-07-04,94,273!2023-06-22,101,273-->
- repeat last search backward:::?\<Enter\> <!--SR:!2023-07-21,116,273!2023-06-07,84,268-->
- substitute (pattern) with (string) in \[range=.\] with \[flags\]::::\[range\]s\[ubstitute\]/(pattern)/(string)/\[flags\]\<Enter\> <!--SR:!2023-05-08,60,253!2023-05-05,73,313-->

## command
- show filepath and cursor position:::\<Ctrl\>+g <!--SR:!2023-07-02,95,268!2023-05-25,48,208-->
- execute (command) in shell::::!(command)\<Enter\> <!--SR:!2023-04-21,18,253!2023-05-07,75,313-->

## options
- show ([option](#list%20of%20options)) value::::se\[t\] ([option](#list%20of%20options))?\<Enter\> <!--SR:!2023-08-16,125,293!2023-05-17,85,327-->
- set boolean but show non-boolean ([option](#list%20of%20options))::::se\[t\] ([option](#list%20of%20options))\<Enter\> <!--SR:!2023-05-07,75,313!2023-04-21,23,268-->
- unset boolean ([option](#list%20of%20options))::::se\[t\] no([option](#list%20of%20options))\<Enter\> <!--SR:!2023-05-12,31,273!2023-05-12,80,313-->
- invert boolean ([option](#list%20of%20options))::::se\[t\] inv([option](#list%20of%20options))\<Enter\> <!--SR:!2023-05-05,73,313!2023-09-25,166,293-->

### list of options
- ignorecase, ic:::ignore case in search <!--SR:!2023-10-08,178,308!2023-10-21,188,308-->
- incsearch, is:::highlight while typing search <!--SR:!2023-09-15,159,293!2023-07-17,113,273-->
- hlsearch, hls:::highlight last search matches <!--SR:!2023-09-03,162,290!2023-10-16,184,308-->

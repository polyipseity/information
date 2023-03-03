#flashcards/general/usage/Vim_usage #general/usage

# Vim usage

See also [Vim help files](https://vimhelp.org/).

- help with \[subject\]:::<ul><li>:h[elp] [subject]</li><li>&lt;F1&gt;</li><li>&lt;Help&gt;</li></ul> <!--SR:!2023-05-06,74,313!2023-05-10,78,313-->

## autocomplete
- cycle forward:::\<Tab\> <!--SR:!2023-05-17,85,328!2023-04-17,60,308-->
- cycle backward:::\<Ctrl\>+p <!--SR:!2023-04-16,59,308!2023-03-12,28,268-->
- show possibilities:::\<Ctrl\>+d <!--SR:!2023-03-15,12,193!2023-03-31,43,288-->

## pattern
- repeat (N=1) times:::(N) ^repeatN <!--SR:!2023-03-16,32,293!2023-05-15,83,328-->

## motion
- left:::\[[repeat N](#^repeatN)\]h <!--SR:!2023-05-15,83,328!2023-04-05,48,288-->
- down:::\[[repeat N](#^repeatN)\]j <!--SR:!2023-05-12,80,313!2023-04-16,59,308-->
- up:::\[[repeat N](#^repeatN)\]k <!--SR:!2023-03-27,43,270!2023-03-11,27,267-->
- right:::\[[repeat N](#^repeatN)\]l <!--SR:!2023-05-16,84,328!2023-05-16,84,328-->
- before next word:::\[[repeat N](#^repeatN)\]w <!--SR:!2023-03-10,26,253!2023-03-30,42,288-->
- end of current word:::\[[repeat N](#^repeatN)\]e <!--SR:!2023-05-10,78,313!2023-05-11,79,313-->
- beginning of line:::0 <!--SR:!2023-05-09,77,310!2023-05-11,79,313-->
- end of line:::$ <!--SR:!2023-05-08,76,313!2023-05-10,78,313-->
- line \[N=(last)\]:::\[N\]G <!--SR:!2023-03-28,44,290!2023-05-12,80,313-->
- line \[N=1\]:::\[N\]gg <!--SR:!2023-05-06,74,313!2023-05-08,76,313-->
- matching character:::% <!--SR:!2023-03-27,43,273!2023-04-12,50,293-->

## write and quit
- quit current buffer::::q\[uit\]\<Enter\> <!--SR:!2023-05-05,73,313!2023-04-06,49,293-->
- quit current buffer, discard changes::::q\[uit\]!\<Enter\> <!--SR:!2023-05-06,74,313!2023-04-14,57,293-->
- write \[range=%\] to \[file=(current)\]::::\[range\]w\[rite\]\[!\] \[file\]\<Enter\> <!--SR:!2023-04-08,51,293!2023-05-14,82,328-->
- write to \[file=(current)\] and quit::::wq[!] \[file\]\<Enter\> <!--SR:!2023-05-07,75,313!2023-05-15,83,328-->

## insert
- quit insert mode:::\<Esc\> <!--SR:!2023-05-09,77,313!2023-05-08,76,313-->
- insert before cursor:::\[[repeat N](#^repeatN)\]i <!--SR:!2023-04-18,61,293!2023-05-17,85,328-->
- insert after cursor:::\[[repeat N](#^repeatN)\]a <!--SR:!2023-05-08,76,313!2023-04-17,60,308-->
- insert after end of line:::\[[repeat N](#^repeatN)\]A <!--SR:!2023-03-10,26,253!2023-05-09,77,313-->
- change text from cursor to ([motion](#motion)):::c([motion](#motion)) <!--SR:!2023-03-26,42,273!2023-04-10,53,293-->
- insert lines below cursor:::\[[repeat N](#^repeatN)\]o <!--SR:!2023-03-12,28,253!2023-03-18,34,293-->
- insert lines above cursor:::\[[repeat N](#^repeatN)\]O <!--SR:!2023-04-16,59,293!2023-04-13,56,293-->

## replace
- exit replace mode:::([replace](#replace))\<Esc\> <!--SR:!2023-05-06,74,313!2023-05-17,85,328-->
- replace with (char):::\[[repeat N](#^repeatN)\]r(char) <!--SR:!2023-03-26,42,273!2023-05-13,81,313-->
- enter replace mode:::\[[repeat N](#^repeatN)\]R <!--SR:!2023-04-12,55,293!2023-04-13,56,293-->

## visual
- exit visual mode:::([visual](#visual))\<Esc\> <!--SR:!2023-05-17,85,328!2023-05-16,84,328-->
- highlight characters:::v <!--SR:!2023-04-07,50,308!2023-04-18,61,308-->
- highlight lines:::V <!--SR:!2023-03-13,29,253!2023-03-31,43,288-->
- highlight block:::\<Ctrl\>+v <!--SR:!2023-03-15,31,253!2023-05-15,83,328-->
- copy highlight into \["register=(latest)\]:::([visual](#visual))\["register\]y <!--SR:!2023-03-29,41,273!2023-04-01,44,288-->

## edit
- delete under cursor:::<ul><li>\[[repeat N](#^repeatN)\]x</li><li>\[[repeat N](#^repeatN)\]Delete</li></ul> <!--SR:!2023-05-14,82,327!2023-04-14,57,308-->
- delete from cursor to ([motion](#motion)):::d([motion](#motion)) <!--SR:!2023-05-13,81,310!2023-05-13,81,313-->
- delete lines:::\[[repeat N](#^repeatN)\]dd <!--SR:!2023-05-11,79,313!2023-04-15,58,308-->
- undo:::\[[repeat N](#^repeatN)\]u <!--SR:!2023-03-17,33,293!2023-05-10,78,313-->
- restore last changed line:::U <!--SR:!2023-05-12,80,313!2023-04-06,49,288-->
- copy from cursor to (motion) into \["register=(latest)\]:::\["register\]y(motion) <!--SR:!2023-03-14,30,253!2023-05-16,84,328-->
- paste \["register=(latest)\] after cursor:::\[[repeat N](#^repeatN)\]\["register\]p <!--SR:!2023-04-15,58,307!2023-05-14,82,328-->
- paste \["register=(latest)\] before cursor:::\[[repeat N](#^repeatN)\]\["register\]P <!--SR:!2023-05-09,77,313!2023-04-17,60,307-->

## search and substitute
- search forward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]/(pattern)\[/\]\[offset\]\<Enter\> <!--SR:!2023-04-10,53,293!2023-03-12,28,253-->
- search backward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]?(pattern)\[?\]\[offset\]\<Enter\> <!--SR:!2023-03-11,27,250!2023-04-17,60,308-->
- repeat last search:::n <!--SR:!2023-05-13,81,313!2023-04-14,57,308-->
- repeat last search reversed:::N <!--SR:!2023-04-07,50,293!2023-03-23,35,268-->
- repeat last search forward:::/\<Enter\> <!--SR:!2023-04-01,35,273!2023-03-13,29,253-->
- repeat last search backward:::?\<Enter\> <!--SR:!2023-03-27,43,273!2023-03-15,31,268-->
- substitute (pattern) with (string) in \[range=.\] with \[flags\]::::\[range\]s\[ubstitute\]/(pattern)/(string)/\[flags\]\<Enter\> <!--SR:!2023-03-09,25,253!2023-05-05,73,313-->

## command
- show filepath and cursor position:::\<Ctrl\>+g <!--SR:!2023-03-28,35,268!2023-03-06,18,228-->
- execute (command) in shell::::!(command)\<Enter\> <!--SR:!2023-04-03,31,273!2023-05-07,75,313-->

## options
- show ([option](#list%20of%20options)) value::::se\[t\] ([option](#list%20of%20options))?\<Enter\> <!--SR:!2023-04-13,41,293!2023-05-17,85,327-->
- set boolean but show non-boolean ([option](#list%20of%20options))::::se\[t\] ([option](#list%20of%20options))\<Enter\> <!--SR:!2023-05-07,75,313!2023-03-29,45,288-->
- unset boolean ([option](#list%20of%20options))::::se\[t\] no([option](#list%20of%20options))\<Enter\> <!--SR:!2023-04-11,54,293!2023-05-12,80,313-->
- invert boolean ([option](#list%20of%20options))::::se\[t\] inv([option](#list%20of%20options))\<Enter\> <!--SR:!2023-05-05,73,313!2023-04-12,55,293-->

### list of options
- ignorecase, ic:::ignore case in search <!--SR:!2023-04-13,56,308!2023-04-16,59,308-->
- incsearch, is:::highlight while typing search <!--SR:!2023-04-09,52,293!2023-03-26,42,273-->
- hlsearch, hls:::highlight last search matches <!--SR:!2023-03-25,41,270!2023-04-15,58,308-->

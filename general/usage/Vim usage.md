#flashcards/general/usage/Vim_usage #general/usage

# Vim usage

See also [Vim help files](https://vimhelp.org/).

- help with \[subject\]:::<ul><li>:h[elp] [subject]</li><li>&lt;F1&gt;</li><li>&lt;Help&gt;</li></ul> <!--SR:!2023-02-17,15,293!2023-02-19,17,293-->

## autocomplete
- cycle forward:::\<Tab\> <!--SR:!2023-02-20,18,308!2023-02-15,13,288-->
- cycle backward:::\<Ctrl\>+p <!--SR:!2023-02-16,14,288!2023-02-09,8,268-->
- show possibilities:::\<Ctrl\>+d <!--SR:!2023-02-03,2,233!2023-02-16,14,288-->

## pattern
- repeat (N=1) times:::(N) ^repeatN <!--SR:!2023-02-04,2,253!2023-02-20,18,308-->

## motion
- left:::\[[repeat N](#^repeatN)\]h <!--SR:!2023-02-20,18,308!2023-02-03,2,248-->
- down:::\[[repeat N](#^repeatN)\]j <!--SR:!2023-02-19,17,293!2023-02-16,14,288-->
- up:::\[[repeat N](#^repeatN)\]k <!--SR:!2023-02-11,10,250!2023-02-09,8,267-->
- right:::\[[repeat N](#^repeatN)\]l <!--SR:!2023-02-20,18,308!2023-02-20,18,308-->
- before next word:::\[[repeat N](#^repeatN)\]w <!--SR:!2023-02-08,7,253!2023-02-15,13,288-->
- end of current word:::\[[repeat N](#^repeatN)\]e <!--SR:!2023-02-19,17,293!2023-02-18,16,293-->
- beginning of line:::0 <!--SR:!2023-02-19,17,290!2023-02-19,17,293-->
- end of line:::$ <!--SR:!2023-02-19,17,293!2023-02-18,16,293-->
- line \[N=(last)\]:::\[N\]G <!--SR:!2023-02-12,11,270!2023-02-18,16,293-->
- line \[N=1\]:::\[N\]gg <!--SR:!2023-02-17,15,293!2023-02-18,16,293-->
- matching character:::% <!--SR:!2023-02-09,8,253!2023-02-17,15,293-->

## write and quit
- quit current buffer::::q\[uit\]\<Enter\> <!--SR:!2023-02-17,15,293!2023-02-04,2,253-->
- quit current buffer, discard changes::::q\[uit\]!\<Enter\> <!--SR:!2023-02-17,15,293!2023-02-15,13,273-->
- delete under cursor:::<ul><li>x</li><li>Delete</li></ul> <!--SR:!2023-02-18,16,307!2023-02-16,14,288-->
- write \[range=%\] to \[file=(current)\]::::\[range\]w\[rite\]\[!\] \[file\]\<Enter\> <!--SR:!2023-02-15,13,273!2023-02-20,18,308-->
- write to \[file=(current)\] and quit::::wq[!] \[file\]\<Enter\> <!--SR:!2023-02-19,17,293!2023-02-20,18,308-->

## insert
- quit insert mode:::\<Esc\> <!--SR:!2023-02-18,16,293!2023-02-19,17,293-->
- insert before cursor:::\[[repeat N](#^repeatN)\]i <!--SR:!2023-02-14,13,273!2023-02-17,15,308-->
- insert after cursor:::\[[repeat N](#^repeatN)\]a <!--SR:!2023-02-18,16,293!2023-02-16,14,288-->
- insert after end of line:::\[[repeat N](#^repeatN)\]A <!--SR:!2023-02-08,7,253!2023-02-19,17,293-->
- change text from cursor to ([motion](#motion)):::c([motion](#motion)) <!--SR:!2023-02-11,10,253!2023-02-15,13,273-->
- insert lines below cursor:::\[[repeat N](#^repeatN)\]o <!--SR:!2023-02-10,9,253!2023-02-04,2,253-->
- insert lines above cursor:::\[[repeat N](#^repeatN)\]O <!--SR:!2023-02-14,13,273!2023-02-15,13,273-->

## replace
- exit replace mode:::([replace](#replace))\<Esc\> <!--SR:!2023-02-19,17,293!2023-02-20,18,308-->
- replace with (char):::\[[repeat N](#^repeatN)\]r(char) <!--SR:!2023-02-11,10,253!2023-02-18,16,293-->
- enter replace mode:::\[[repeat N](#^repeatN)\]R <!--SR:!2023-02-15,13,273!2023-02-15,13,273-->

## visual
- exit visual mode:::([visual](#visual))\<Esc\> <!--SR:!2023-02-20,18,308!2023-02-20,18,308-->
- highlight characters:::v <!--SR:!2023-02-04,2,268!2023-02-13,12,288-->
- highlight lines:::V <!--SR:!2023-02-11,10,253!2023-02-16,14,288-->
- highlight block:::\<Ctrl\>+v <!--SR:!2023-02-11,10,253!2023-02-20,18,308-->
- copy highlight into \["register=(latest)\]:::([visual](#visual))\["register\]y <!--SR:!2023-02-15,13,273!2023-02-16,14,288-->

## edit
- delete from cursor to ([motion](#motion)):::d([motion](#motion)) <!--SR:!2023-02-18,16,290!2023-02-19,17,293-->
- delete lines:::\[[repeat N](#^repeatN)\]dd <!--SR:!2023-02-18,16,293!2023-02-16,14,288-->
- undo:::\[[repeat N](#^repeatN)\]u <!--SR:!2023-02-04,2,253!2023-02-18,16,293-->
- restore last changed line:::U <!--SR:!2023-02-17,15,293!2023-02-03,2,248-->
- copy from cursor to (motion) into \["register=(latest)\]:::\["register\]y(motion) <!--SR:!2023-02-11,10,253!2023-02-20,18,308-->
- paste \["register=(latest)\] after cursor:::\[[repeat N](#^repeatN)\]\["register\]p <!--SR:!2023-02-15,13,287!2023-02-20,18,308-->
- paste \["register=(latest)\] before cursor:::\[[repeat N](#^repeatN)\]\["register\]P <!--SR:!2023-02-19,17,293!2023-02-15,13,287-->

## search and substitute
- search forward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]/(pattern)\[/\]\[offset\]\<Enter\> <!--SR:!2023-02-15,13,273!2023-02-03,2,233-->
- search backward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]?(pattern)\[?\]\[offset\]\<Enter\> <!--SR:!2023-02-09,8,250!2023-02-16,14,288-->
- repeat last search:::n <!--SR:!2023-02-19,17,293!2023-02-16,14,288-->
- repeat last search reversed:::N <!--SR:!2023-02-04,2,253!2023-02-03,2,248-->
- repeat last search forward:::/\<Enter\> <!--SR:!2023-02-15,13,273!2023-02-11,10,253-->
- repeat last search backward:::?\<Enter\> <!--SR:!2023-02-10,9,253!2023-02-10,9,268-->
- substitute (pattern) with (string) in \[range=.\] with \[flags\]::::\[range\]s\[ubstitute\]/(pattern)/(string)/\[flags\]\<Enter\> <!--SR:!2023-02-09,8,253!2023-02-19,17,293-->

## command
- show path and cursor position:::\<Ctrl\>+g <!--SR:!2023-02-10,9,268!2023-02-03,2,248-->
- execute (command) in shell::::!(command)\<Enter\> <!--SR:!2023-02-18,16,293!2023-02-17,15,293-->

## options
- show ([option](#list%20of%20options)) value::::se\[t\] ([option](#list%20of%20options))?\<Enter\> <!--SR:!2023-02-18,16,293!2023-02-20,18,307-->
- set boolean but show non-boolean ([option](#list%20of%20options))::::se\[t\] ([option](#list%20of%20options))\<Enter\> <!--SR:!2023-02-17,15,293!2023-02-08,7,268-->
- unset boolean ([option](#list%20of%20options))::::se\[t\] no([option](#list%20of%20options))\<Enter\> <!--SR:!2023-02-15,13,273!2023-02-18,16,293-->
- invert boolean ([option](#list%20of%20options))::::se\[t\] inv([option](#list%20of%20options))\<Enter\> <!--SR:!2023-02-18,16,293!2023-02-15,13,273-->

### list of options
- ignorecase, ic:::ignore case in search <!--SR:!2023-02-16,14,288!2023-02-16,14,288-->
- incsearch, is:::highlight while typing search <!--SR:!2023-02-15,13,273!2023-02-10,9,253-->
- hlsearch, hls:::highlight last search matches <!--SR:!2023-02-10,9,250!2023-02-15,13,288-->

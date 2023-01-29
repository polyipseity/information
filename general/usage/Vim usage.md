#flashcards/general/usage/Vim_usage #general/usage

# Vim usage

See also [Vim help files](https://vimhelp.org/).

- help with \[subject\]::::h\[elp\] \[subject\], \<F1\>, \<Help\> <!--SR:!2023-02-02,4,273!2023-02-02,4,273-->

## autocomplete
- next autocomplete:::\<Tab\> <!--SR:!2023-02-02,4,288!2023-02-02,4,288-->
- previous autocomplete:::\<Ctrl\>+P <!--SR:!2023-02-02,4,288!2023-02-01,3,268-->
- list possibilities:::\<Ctrl\>+D <!--SR:!2023-02-01,3,253!2023-02-02,4,288-->

## pattern
- repeat (N=1) times:::(N) ^repeatN <!--SR:!2023-02-02,4,273!2023-02-02,4,288-->

## motion
- left:::\[[repeat N](#^repeatN)\]h <!--SR:!2023-02-02,4,288!2023-02-01,3,268-->
- down:::\[[repeat N](#^repeatN)\]j <!--SR:!2023-02-02,4,273!2023-02-02,4,288-->
- up:::\[[repeat N](#^repeatN)\]k <!--SR:!2023-02-01,3,250!2023-02-01,3,267-->
- right:::\[[repeat N](#^repeatN)\]l <!--SR:!2023-02-02,4,288!2023-02-02,4,288-->
- before next word:::\[[repeat N](#^repeatN)\]w <!--SR:!2023-02-01,3,253!2023-02-02,4,288-->
- end of current word:::\[[repeat N](#^repeatN)\]e <!--SR:!2023-02-02,4,273!2023-02-02,4,273-->
- beginning of line:::0 <!--SR:!2023-02-02,4,270!2023-02-02,4,273-->
- end of line:::$ <!--SR:!2023-02-02,4,273!2023-02-02,4,273-->
- line \[N=(last)\]:::\[N\]G <!--SR:!2023-02-01,3,250!2023-02-02,4,273-->
- line \[N=1\]:::\[N\]gg <!--SR:!2023-02-02,4,273!2023-02-02,4,273-->
- matching character:::% <!--SR:!2023-02-01,3,253!2023-02-02,4,273-->

## write and quit
- quit current buffer::::q\[uit\]\<Enter\> <!--SR:!2023-02-02,4,273!2023-02-02,4,273-->
- quit current bufferdiscard changes::::q\[uit\]!\<Enter\> <!--SR:!2023-02-02,4,273!2023-02-02,4,273-->
- delete under cursor:::x/Delete <!--SR:!2023-02-02,4,287!2023-02-02,4,288-->
- write \[range=%\] to \[file=(current)\]::::\[range\]w\[rite\]\[!\] \[file\]\<Enter\> <!--SR:!2023-02-02,4,273!2023-02-02,4,288-->
- write to \[file=(current)\] and quit::::wq[!] \[file\]\<Enter\> <!--SR:!2023-02-02,4,273!2023-02-02,4,288-->

## insert
- leave insert mode:::\<Esc\> <!--SR:!2023-02-02,4,273!2023-02-02,4,273-->
- insert before cursor:::\[[repeat N](#^repeatN)\]i <!--SR:!2023-02-01,3,253!2023-02-02,4,288-->
- insert after cursor:::\[[repeat N](#^repeatN)\]a <!--SR:!2023-02-02,4,273!2023-02-02,4,288-->
- insert after end of line:::\[[repeat N](#^repeatN)\]A <!--SR:!2023-02-01,3,253!2023-02-02,4,273-->
- change text from cursor to ([motion](#motion)):::c([motion](#motion)) <!--SR:!2023-02-01,3,253!2023-02-02,4,273-->
- insert lines below cursor:::\[[repeat N](#^repeatN)\]o <!--SR:!2023-02-01,3,253!2023-02-02,4,273-->
- insert lines above cursor:::\[[repeat N](#^repeatN)\]O <!--SR:!2023-02-01,3,253!2023-02-02,4,273-->

## replace
- exit replace mode:::([replace](#replace))\<Esc\> <!--SR:!2023-02-02,4,273!2023-02-02,4,288-->
- replace with (char):::\[[repeat N](#^repeatN)\]r(char) <!--SR:!2023-02-01,3,253!2023-02-02,4,273-->
- enter replace mode:::\[[repeat N](#^repeatN)\]R <!--SR:!2023-02-02,4,273!2023-02-02,4,273-->

## visual
- exit visual mode:::([visual](#visual))\<Esc\> <!--SR:!2023-02-02,4,288!2023-02-02,4,288-->
- highlight characters:::v <!--SR:!2023-02-02,4,288!2023-02-01,3,268-->
- highlight lines:::V <!--SR:!2023-02-01,3,253!2023-02-02,4,288-->
- highlight block:::\<Ctrl\>+v <!--SR:!2023-02-01,3,253!2023-02-02,4,288-->
- copy highlight into \["register=(latest)\]:::([visual](#visual))\["register\]y <!--SR:!2023-02-02,4,273!2023-02-02,4,288-->

## edit
- delete from cursor to ([motion](#motion)):::d([motion](#motion)) <!--SR:!2023-02-02,4,270!2023-02-02,4,273-->
- delete lines:::\[[repeat N](#^repeatN)\]dd <!--SR:!2023-02-02,4,273!2023-02-02,4,288-->
- undo:::\[[repeat N](#^repeatN)\]u <!--SR:!2023-02-02,4,273!2023-02-02,4,273-->
- restore last changed line:::U <!--SR:!2023-02-02,4,273!2023-02-01,3,268-->
- copy from cursor to (motion) into \["register=(latest)\]:::\["register\]y(motion) <!--SR:!2023-02-01,3,253!2023-02-02,4,288-->
- paste \["register=(latest)\] after cursor:::\[[repeat N](#^repeatN)\]\["register\]p <!--SR:!2023-02-02,4,287!2023-02-02,4,288-->
- paste \["register=(latest)\] before cursor:::\[[repeat N](#^repeatN)\]\["register\]P <!--SR:!2023-02-02,4,273!2023-02-02,4,287-->

## search and substitute
- search forward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]/(pattern)\[/\]\[offset\]\<Enter\> <!--SR:!2023-02-02,4,273!2023-02-01,3,253-->
- search backward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]?(pattern)\[?\]\[offset\]\<Enter\> <!--SR:!2023-02-01,3,250!2023-02-02,4,288-->
- repeat last search:::n <!--SR:!2023-02-02,4,273!2023-02-02,4,288-->
- repeat last search reversed:::N <!--SR:!2023-02-02,4,273!2023-02-01,3,268-->
- repeat last search forward:::/\<Enter\> <!--SR:!2023-02-02,4,273!2023-02-01,3,253-->
- repeat last search backward:::?\<Enter\> <!--SR:!2023-02-01,3,253!2023-02-01,3,268-->
- substitute in (pattern) with (string) in \[range=.\] with \[flags\]::::\[range\]s\[ubstitute\]/(pattern)/(string)/\[flags\]\<Enter\> <!--SR:!2023-02-01,3,253!2023-02-02,4,273-->

## command
- show path and cursor position:::\<Ctrl\>+g <!--SR:!2023-02-01,3,268!2023-02-01,3,268-->
- execute (command)::::!(command)\<Enter\> <!--SR:!2023-02-02,4,273!2023-02-02,4,273-->

## options
- show ([option](#list%20of%20options)) value::::se\[t\] ([option](#list%20of%20options))?\<Enter\> <!--SR:!2023-02-02,4,273!2023-02-02,4,287-->
- set boolean but show non-boolean ([option](#list%20of%20options))::::se\[t\] ([option](#list%20of%20options))\<Enter\> <!--SR:!2023-02-02,4,273!2023-02-01,3,268-->
- unset boolean ([option](#list%20of%20options))::::se\[t\] no([option](#list%20of%20options))\<Enter\> <!--SR:!2023-02-02,4,273!2023-02-02,4,273-->
- invert boolean ([option](#list%20of%20options))::::se\[t\] inv([option](#list%20of%20options))\<Enter\> <!--SR:!2023-02-02,4,273!2023-02-02,4,273-->

### list of options
- ignorecase, ic:::ignore case in search <!--SR:!2023-02-02,4,288!2023-02-02,4,288-->
- incsearch, is:::highlight while typing search <!--SR:!2023-02-02,4,273!2023-02-01,3,253-->
- hlsearch, hls:::highlight last search matches <!--SR:!2023-02-01,3,250!2023-02-02,4,288-->

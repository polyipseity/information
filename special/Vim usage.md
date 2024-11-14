---
aliases:
  - Vim help
  - Vim usage
tags:
  - flashcard/active/special/Vim_usage
  - language/in/English
---

# Vim usage

See also [Vim help files](https://vimhelp.org/).

- help with \[subject\] ::@:: <ul><li>:h[elp] [subject]</li><li>&lt;F1&gt;</li><li>&lt;Help&gt;</li></ul>

## autocomplete

- cycle forward ::@:: \<Tab\>
- cycle backward ::@:: \<Ctrl\>+p
- show possibilities ::@:: \<Ctrl\>+d

## pattern

- repeat (N=1) times ::@:: (N) <a id="^repeatN"></a>^repeatN

## motion

- left ::@:: \[[repeat N](#^repeatN)\]h
- down ::@:: \[[repeat N](#^repeatN)\]j
- up ::@:: \[[repeat N](#^repeatN)\]k
- right ::@:: \[[repeat N](#^repeatN)\]l
- before next word ::@:: \[[repeat N](#^repeatN)\]w
- end of current word ::@:: \[[repeat N](#^repeatN)\]e
- beginning of line ::@:: 0
- end of line ::@:: $
- line \[N=(last)\] ::@:: \[N\]G
- line \[N=1\] ::@:: \[N\]gg
- matching character ::@:: %

## write and quit

- quit current buffer ::@:: :q\[uit\]\<Enter\>
- quit current buffer, discard changes ::@:: :q\[uit\]!\<Enter\>
- write \[range=%\] to \[file=(current)\] ::@:: :\[range\]w\[rite\]\[!\] \[file\]\<Enter\>
- write to \[file=(current)\] and quit ::@:: :wq[!] \[file\]\<Enter\>

## insert

- quit insert mode ::@:: \<Esc\>
- insert before cursor ::@:: \[[repeat N](#^repeatN)\]i
- insert after cursor ::@:: \[[repeat N](#^repeatN)\]a
- insert after end of line ::@:: \[[repeat N](#^repeatN)\]A
- change text from cursor to ([motion](#motion)) ::@:: c([motion](#motion))
- insert lines below cursor ::@:: \[[repeat N](#^repeatN)\]o
- insert lines above cursor ::@:: \[[repeat N](#^repeatN)\]O

## replace

- exit replace mode ::@:: ([replace](#replace))\<Esc\>
- replace with (char) ::@:: \[[repeat N](#^repeatN)\]r(char)
- enter replace mode ::@:: \[[repeat N](#^repeatN)\]R

## visual

- exit visual mode ::@:: ([visual](#visual))\<Esc\>
- highlight characters ::@:: v
- highlight lines ::@:: V
- highlight block ::@:: \<Ctrl\>+v
- copy highlight into \["register=(latest)\] ::@:: ([visual](#visual))\["register\]y

## edit

- delete under cursor ::@:: <ul><li>\[[repeat N](#^repeatN)\]x</li><li>\[[repeat N](#^repeatN)\]Delete</li></ul>
- delete from cursor to ([motion](#motion)) ::@:: d([motion](#motion))
- delete lines ::@:: \[[repeat N](#^repeatN)\]dd
- undo ::@:: \[[repeat N](#^repeatN)\]u
- restore last changed line ::@:: U
- copy from cursor to (motion) into \["register=(latest)\] ::@:: \["register\]y(motion)
- paste \["register=(latest)\] after cursor ::@:: \[[repeat N](#^repeatN)\]\["register\]p
- paste \["register=(latest)\] before cursor ::@:: \[[repeat N](#^repeatN)\]\["register\]P

## search and substitute

- search forward for \[N=1\]th occurence of (pattern) with \[offset\] ::@:: \[N\]/(pattern)\[/\]\[offset\]\<Enter\>
- search backward for \[N=1\]th occurence of (pattern) with \[offset\] ::@:: \[N\]?(pattern)\[?\]\[offset\]\<Enter\>
- repeat last search ::@:: n
- repeat last search reversed ::@:: N
- repeat last search forward ::@:: /\<Enter\>
- repeat last search backward ::@:: ?\<Enter\>
- substitute (pattern) with (string) in \[range=.\] with \[flags\] ::@:: :\[range\]s\[ubstitute\]/(pattern)/(string)/\[flags\]\<Enter\>

## command

- show filepath and cursor position ::@:: \<Ctrl\>+g
- execute (command) in shell ::@:: :!(command)\<Enter\>

## options

- show ([option](#list%20of%20options)) value ::@:: :se\[t\] ([option](#list%20of%20options))?\<Enter\>
- set boolean but show non-boolean ([option](#list%20of%20options)) ::@:: :se\[t\] ([option](#list%20of%20options))\<Enter\>
- unset boolean ([option](#list%20of%20options)) ::@:: :se\[t\] no([option](#list%20of%20options))\<Enter\>
- invert boolean ([option](#list%20of%20options)) ::@:: :se\[t\] inv([option](#list%20of%20options))\<Enter\>

### list of options

- ignorecase, ic ::@:: ignore case in search
- incsearch, is ::@:: highlight while typing search
- hlsearch, hls ::@:: highlight last search matches

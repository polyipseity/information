#flashcards/general/usage/Vim_usage #general/usage

# Vim usage

See also [Vim help files](https://vimhelp.org/).

## normal mode

### motion
- left:::\[[repeat N](#^repeatN)\]h
- down:::\[[repeat N](#^repeatN)\]j
- up:::\[[repeat N](#^repeatN)\]k
- right:::\[[repeat N](#^repeatN)\]l
- before next word:::\[[repeat N](#^repeatN)\]w
- end of current word:::\[[repeat N](#^repeatN)\]e
- beginning of line:::0
- end of line:::$
- line \[N=(last)\]:::\[N\]G
- line \[N=1\]:::\[N\]gg
- matching character:::%

### writing and quiting
- quit current buffer::::q\[uit\]&lt;Enter&gt;
- quit current bufferdiscard changes::::q\[uit\]!&lt;Enter&gt;
- delete under cursor:::x/Delete
- [insert](#insert%20mode) before cursor:::i
- [insert](#insert%20mode) after cursor:::a
- write and quit::::wq[!]&lt;Enter&gt;

### editing
- delete from cursor to ([motion](#motion)):::d([motion](#motion))
- delete line(s):::\[[repeat N](#^repeatN)\]dd
- undo:::\[[repeat N](#^repeatN)\]u
- restore last changed line:::U
- paste after cursor:::\[[repeat N](#^repeatN)\]p
- paste before cursor:::\[[repeat N](#^repeatN)\]P
- replace with (char):::\[[repeat N](#^repeatN)\]r(char)
- change text from cursor to ([motion](#motion)):::c([motion](#motion))

### searching and substitution
- search forward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]/(pattern)\[/\]\[offset\]&lt;Enter&gt;
- search backward for \[N=1\]th occurence of (pattern) with \[offset\]:::\[N\]?(pattern)\[?\]\[offset\]&lt;Enter&gt;
- repeat last search:::n
- repeat last search reversed:::N
- repeat last search forward:::/&lt;Enter&gt;
- repeat last search backward:::?&lt;Enter&gt;
- substitute in (pattern) with (string) in \[range=.\] with \[flags\	]::::\[range\]s\[ubstitute\]/(pattern)/(string)/\[flags\]&lt;Enter&gt;

### pattern
- repeat (N=1) time(s):::(N) ^repeatN

### commands


## insert mode
- leave [insert mode](#insert%20mode):::Esc

---
aliases:
  - Python dictionaries
  - Python dictionary
tags:
  - flashcard/active/special/academia/HKUST/BIEN_3300/Python/dictionary
  - language/in/English
---

# Python dictionary

A Python dictionary works like a dictionary. In the latter, you lookup a word to get its definition. In the former, you {@{lookup a key to get the value}@}. <!--SR:!fsrs,2029-07-25T00:00:00.000Z,1072,1072.36160804,1,2,9,0,0,2026-08-18T00:00:00.000Z-->

## creation

To create a dictionary, use {@{curly brackets `{}`}@}. To add keys and values, {@{separate each key-value pair with a comma `,` and separate the key and the value with a colon `:`}@}: <!--SR:!2026-10-28,291,330!fsrs,2029-09-19T00:00:00.000Z,1115,1114.75652523,1,2,9,0,0,2026-08-31T00:00:00.000Z-->

```Python
empty_dict = {}
nonempty_dict = {"key": "value", "key2": 123, 123: "value3", 96: 42}
```

The values can be {@{anything}@} while the keys can be {@{almost anything, as there are some restrictions on the type of keys}@}. It is {@{not mentioned}@} here. <!--SR:!fsrs,2029-06-30T00:00:00.000Z,1053,1053.01305103,1,2,9,0,0,2026-08-12T00:00:00.000Z!2026-10-22,285,330!2026-12-03,327,342-->

## lookup

To lookup the value for a key, simply write {@{`dictionary[key]`}@}. To check whether a key is in a dictionary, use {@{the `in` operator: `key in dictionary`}@}. <!--SR:!fsrs,2029-12-01T00:00:00.000Z,1157,1156.92457827,1,2,9,0,0,2026-10-01T00:00:00.000Z!2026-10-09,272,330-->

## modification

To add a value for a key not yet in the dictionary or update the value for a key already in the dictionary, simply write {@{`dictionary[key] = value`}@}. <!--SR:!fsrs,2029-05-26T00:00:00.000Z,1026,1025.83973773,1,2,9,0,0,2026-08-04T00:00:00.000Z-->

## iteration

You can iterate through the keys of a dictionary by {@{`for key in dictionary:` or `for key in dictionary.keys():`}@}. For values, do {@{`for value in dictionary.values():`}@}. For both, do {@{`for key, value in dictionary.items():`}@}. <!--SR:!2026-10-12,275,330!2026-10-11,274,330!fsrs,2030-01-07T00:00:00.000Z,1187,1187.45608877,1,2,9,0,0,2026-10-08T00:00:00.000Z-->

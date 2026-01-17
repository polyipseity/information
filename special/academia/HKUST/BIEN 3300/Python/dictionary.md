---
aliases:
  - Python dictionaries
  - Python dictionary
tags:
  - flashcard/active/special/academia/HKUST/BIEN_3300/Python/dictionary
  - language/in/English
---

# Python dictionary

A Python dictionary works like a dictionary. In the latter, you lookup a word to get its definition. In the former, you {@{lookup a key to get the value}@}. <!--SR:!2026-08-17,241,330-->

## creation

To create a dictionary, use {@{curly brackets `{}`}@}. To add keys and values, {@{separate each key-value pair with a comma `,` and separate the key and the value with a colon `:`}@}: <!--SR:!2026-10-28,291,330!2026-08-30,252,330-->

```Python
empty_dict = {}
nonempty_dict = {"key": "value", "key2": 123, 123: "value3", 96: 42}
```

The values can be {@{anything}@} while the keys can be {@{almost anything, as there are some restrictions on the type of keys}@}. It is {@{not mentioned}@} here. <!--SR:!2026-08-11,236,330!2026-10-22,285,330!2026-12-03,327,342-->

## lookup

To lookup the value for a key, simply write {@{`dictionary[key]`}@}. To check whether a key is in a dictionary, use {@{the `in` operator: `key in dictionary`}@}. <!--SR:!2026-09-30,263,330!2026-10-09,272,330-->

## modification

To add a value for a key not yet in the dictionary or update the value for a key already in the dictionary, simply write {@{`dictionary[key] = value`}@}. <!--SR:!2026-08-03,229,330-->

## iteration

You can iterate through the keys of a dictionary by {@{`for key in dictionary:` or `for key in dictionary.keys():`}@}. For values, do {@{`for value in dictionary.values():`}@}. For both, do {@{`for key, value in dictionary.items():`}@}. <!--SR:!2026-10-12,275,330!2026-10-11,274,330!2026-10-08,271,330-->

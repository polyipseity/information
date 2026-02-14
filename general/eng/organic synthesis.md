---
aliases:
  - organic synthesis
tags:
  - flashcard/active/general/eng/organic_synthesis
  - language/in/English
---

# organic synthesis

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

## considerations

```Python
# pytextgen generate data
return await memorize_table(
  __env__.cwf_sects('d912', '2939'),
  ('name', 'description',),
  (
    ('availability', '[Reagents](reagent.md) should be readily available and cheap.',),
    ('formation of [by-products](by-product.md)', 'Avoid forming [by-products](by-product.md), especially harmful ones.',),
    ('number of steps', 'Less steps mean less loss.',),
    ('[reaction rate](reaction%20rate.md)', '[Catalysts](catalysis.md) and high [temperature](temperature.md) can hasten slow organic reactions at the expense of higher production cost.',),
    ('[yield](yield%20(chemistry).md)', 'Organic reactions seldom give 100% [yield](yield%20(chemistry).md).',),
  ),
  lambda datum: map(cloze, datum),
)
```

<!--pytextgen generate section="d912"--><!-- The following content is generated at 2026-01-25T23:32:18.976268+08:00. Any edits will be overridden! -->

> | name                                            | description                                                                                                                                        |
> | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
> | {@{availability}@}                              | {@{[Reagents](reagent.md) should be readily available and cheap.}@}                                                                                |
> | {@{formation of [by-products](by-product.md)}@} | {@{Avoid forming [by-products](by-product.md), especially harmful ones.}@}                                                                         |
> | {@{number of steps}@}                           | {@{Less steps mean less loss.}@}                                                                                                                   |
> | {@{[reaction rate](reaction%20rate.md)}@}       | {@{[Catalysts](catalysis.md) and high [temperature](temperature.md) can hasten slow organic reactions at the expense of higher production cost.}@} |
> | {@{[yield](yield%20(chemistry).md)}@}           | {@{Organic reactions seldom give 100% [yield](yield%20(chemistry).md).}@}                                                                          |

<!--/pytextgen-->

<!--pytextgen generate section="2939"--><!-- The following content is generated at 2024-01-04T20:17:52.393394+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←availability
- availability→::@::←formation of [by-products](by-product.md)
- formation of [by-products](by-product.md)→::@::←number of steps
- number of steps→::@::←[reaction rate](reaction%20rate.md)
- [reaction rate](reaction%20rate.md)→::@::←[yield](yield%20(chemistry).md)
- [yield](yield%20(chemistry).md)→::@::←_(end)_

<!--/pytextgen-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/organic_synthesis) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

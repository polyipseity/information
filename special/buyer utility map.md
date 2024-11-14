---
aliases:
  - Buyer Utility Map
  - buyer utility map
tags:
  - flashcard/active/special/buyer_utility_map
  - language/in/English
---

# buyer utility map

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

It is similar to a {@{[customer journey map](customer%20journey%20map.md)}@}.

## 6 stages of buyer experience cycle

The {@{6 stages of buyer experience}@} cycle are the {@{map column headers}@}.

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("29ba", "93ab"),
  """
purchase
delivery
use
supplements
maintenance
disposal
""".strip().splitlines(),
)
```

<!--pytextgen generate section="29ba"--><!-- The following content is generated at 2024-04-22T01:24:34.755556+08:00. Any edits will be overridden! -->

> 1. purchase
> 2. delivery
> 3. use
> 4. supplements
> 5. maintenance
> 6. disposal

<!--/pytextgen-->

<!--pytextgen generate section="93ab"--><!-- The following content is generated at 2024-04-22T01:24:34.779674+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←purchase
- purchase→::@::←delivery
- delivery→::@::←use
- use→::@::←supplements
- supplements→::@::←maintenance
- maintenance→::@::←disposal
- disposal→::@::←_(end)_

<!--/pytextgen-->

## 6 utility levers

The {@{6 utility levers}@} are the {@{map row headers}@}.

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("9571", "aa92"),
  """
convenience: ease of spatial and temporal accessibility
environmental friendliness
fun and image: conveyed feel, look, or attitude
productivity: less effort, time, or money
risk reduction: financial, physical, reputational
simplicity: remove complexity or hassle
""".strip().splitlines(),
)
```

<!--pytextgen generate section="9571"--><!-- The following content is generated at 2024-04-22T01:24:34.815211+08:00. Any edits will be overridden! -->

> 1. convenience: ease of spatial and temporal accessibility
> 2. environmental friendliness
> 3. fun and image: conveyed feel, look, or attitude
> 4. productivity: less effort, time, or money
> 5. risk reduction: financial, physical, reputational
> 6. simplicity: remove complexity or hassle

<!--/pytextgen-->

<!--pytextgen generate section="aa92"--><!-- The following content is generated at 2024-04-22T01:24:34.799107+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←convenience: ease of spatial and temporal accessibility
- convenience: ease of spatial and temporal accessibility→::@::←environmental friendliness
- environmental friendliness→::@::←fun and image: conveyed feel, look, or attitude
- fun and image: conveyed feel, look, or attitude→::@::←productivity: less effort, time, or money
- productivity: less effort, time, or money→::@::←risk reduction: financial, physical, reputational
- risk reduction: financial, physical, reputational→::@::←simplicity: remove complexity or hassle
- simplicity: remove complexity or hassle→::@::←_(end)_

<!--/pytextgen-->

## usage

Mark down {@{customer pains with crosses}@} on the map. Optionally, mark down {@{current industry focuses with red points}@}. Then, identify {@{new unaddressed customer pains}@}.

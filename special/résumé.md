---
aliases:
  - resume
  - résumé
tags:
  - flashcard/active/special/résumé
  - language/in/English
---

# résumé

```Python
# pytextgen generate module
# import ../../tools/utility.py.md
```

The format outlined below is {@{only recommended and does not need to be followed strictly}@}.

## format

To optimize the résumé for successful application and {@{[applicant tracking system](applicant%20tracking%20system.md)}@}:

- content ::@:: include: email address, keywords, LinkedIn link, phone number; exclude: date of birth, gender, home address
- fonts ::@:: 1 font style only; name: 14; contact: 8; body: 11 or 12; header: 11 or 12, bold
- formatting ::@:: consistent, minimal
- length ::@:: 1 single-sided page
- line spacing ::@:: single
- order ::@:: reverse chronological

## content

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects('50ff', '20fa'),
  (
    '[profile summary](#profile%20summary)',
    '[education](#education)',
    '[experience](#experience)',
    '[achievements](#achievements)',
    '[skills](#skills)',
    '[others](#others)',
  ),
)
```

<!--pytextgen generate section="50ff"--><!-- The following content is generated at 2024-01-26T12:42:06.721939+08:00. Any edits will be overridden! -->

> 1. [profile summary](#profile%20summary)
> 2. [education](#education)
> 3. [experience](#experience)
> 4. [achievements](#achievements)
> 5. [skills](#skills)
> 6. [others](#others)

<!--/pytextgen-->

<!--pytextgen generate section="20fa"--><!-- The following content is generated at 2024-01-26T12:42:06.646432+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[profile summary](#profile%20summary)
- [profile summary](#profile%20summary)→::@::←[education](#education)
- [education](#education)→::@::←[experience](#experience)
- [experience](#experience)→::@::←[achievements](#achievements)
- [achievements](#achievements)→::@::←[skills](#skills)
- [skills](#skills)→::@::←[others](#others)
- [others](#others)→::@::←_(end)_

<!--/pytextgen-->

### profile summary

Two recommended formats:

1. I–you ::@:: what I want from you; what I can do for you; requirements, if any
2. A.S.K. ::@:: attitude; skills; knowledge; requirements, if any

### experience

- industry experience ::@:: if no salary
- work experience ::@:: all, 0 to 3 sub-points according to importance
  - work experience sub-points ::@:: statistics (numbers); IROAR: impact, results, outcomes, achievements, responsibilities

### skills

The most important skills in general are {@{adaptivity, fast learning, and resilience}@}.

## referees

Ensure you {@{have contact information of at least 3 referees}@}. A good example would be {@{a professor, a previous supervisor, and a project lead of your volunteer team}@}. {@{No need to}@} put them on the résumé.

---
aliases:
  - ESST occupational health index
  - HKUST ESST occupational health index
tags:
  - flashcard/archive/special/academia/HKUST/ESST/occupational_health/index
  - function/index
  - language/in/English
---

# index

- HKUST ESST occupational health

```Python
# pytextgen generate module
# import ../../../../../../tools/utility.py.md
```

The content is in teaching order.

- [occupational health areas](#occupational%20health%20areas)
- occupational health services in [Hong Kong](../../../../../general/Hong%20Kong.md) ::@:: Under Labour Department, there is an occupational hygiene section and an occupational medicine section.
  - occupational hygiene section ::@:: industrial hygienists anticipate, recognize, evaluate, and control workplace hazards
  - [occupational medicine section](#occupational%20medicine%20section)
- [occupational hazard types](#occupational%20hazard%20types)
- [occupational hazard factors](#occupational%20hazard%20factors)
- chemical hazards ::@:: dusts or particulates, gases or vapors
  - gases or vapors hazards ::@:: benzene; epoxy; hydrogen sulfide, a common sewer gas; polyurethane
  - dusts or particulates hazards ::@:: asbestos, mesothelioma; cement, cement contact dermatitis; silica, silicosis
- [physical hazards](#physical%20hazards)
  - ultraviolet radiation ::@:: in decreasing wavelength (and hence increasing energy): UV-A: 400~315 nm, UV-B: 315~280 nm, UV-C: 280~100 nm
    - ultraviolet radiation sources ::@:: fluorescent tubes, sun, ultraviolet lamps, welding arcs
    - UV-A and UV-B health effects ::@:: skin: aging, cancer, erythema, photosensitization
    - UV-C health effects ::@:: eyes: conjunctivitis, photokeratitis due to welder's flash
    - ultraviolet radiation effect on airborne chemicals ::@:: chlorinated hydrocarbons to phosgene, oxygen to ozone
  - noise ::@:: unwanted sound
    - human audible frequency range ::@:: 20~20000 Hz
    - noise health effects ::@:: communication interference, noise induced hearing loss, psychological effects
    - noise health effect factors ::@:: employment length, exposure time, frequency distribution, level
    - noise types ::@:: continuous, impact, intermittent
  - temperature hazards ::@:: Too hot or too cold. Usually too hot for most industries.
    - [workplaces with temperature hazards](#workplaces%20with%20temperature%20hazards)
    - heat disorders ::@:: heat cramps, heat exhaustion, heat rash, heat stroke
      - heat rash ::@:: red spots on skin
      - heat exhaustion ::@:: fainting, headache, nausea, tiredness due to water loss
      - heat cramps ::@:: muscle cramps, often painful, due to core temperature increase and electrolyte loss
      - heat stroke ::@:: most serious, can be fatal
        - [heat stroke syndromes](#heat%20stroke%20syndromes)
- biological hazards ::@:: animal handlers/food processors, _Streptococcus suis_ infection; healthcare/lab, tuberculosis; ventilation maintenance, [Legionnaires' Disease](../../../../../general/Legionnaires'%20Disease.md)
  - [Legionnaires' Disease](../../../../../general/Legionnaires'%20Disease.md) ::@:: Usually caused by _Legionella pneumophila_. Transmitted by inhalation of aerosols. Related occupations include maintenance of systems using water. A notifiable occupational disease under the Employees' Compensation Ordinance (Cap. 282).
    - [Legionnaires' Disease syndromes](#Legionnaires'%20Disease%20syndromes)
- ergonomics ::@:: maximize comfort zone, minimize injurious forces
  - ergonomic injuries ::@:: mechanical stresses or stretches, occupational cumulative trauma disorders
    - occupational cumulative trauma disorders ::@:: carpal tunnel syndrome, tendinitis, tenosynovitis
- socio-psychological hazards ::@:: occupational stress, workplace violence
- particulate sizes ::@:: according to the [American Conference of Governmental Industrial Hygienists](../../../../../general/American%20Conference%20of%20Governmental%20Industrial%20Hygienists.md), inhalable dusts: ≤ 100 µm, thoraic dusts: ≤ 10 µm, respirable dusts: ≤ 4 µm
- toxicity equation ::@:: toxicity × quantity × time
- occupational exposure limits ::@:: ceiling (C), short term exposure limit (STEL), time weighted average (TWA)
  - ceiling (C) ::@:: at any time
  - short term exposure limit (STEL) ::@:: 15-minute average, 60-minute exposure 4 times daily
  - time weighted average (TWA) ::@:: 8-hour average, repeated daily exposure
- exposure measurement methods ::@:: air or surface sampling and laboratory analysis, direct reading
  - direct reading ::@:: colorimetry like color detection tubes, electronic instruments
  - air or surface and laboratory analysis ::@:: active sampling and passive sampling like badges
- [hazard control hierarchy](#hazard%20control%20hierarchy)
  - personal protective equipment
    - personal protective equipment disadvantages ::@:: administrative burden, expensive, physiological burden
      - eye and face protection ::@:: face shields, safety glasses, safety goggles
        - safety goggle characteristics ::@:: chemical splash proof, direct vent, impact resistant, indirect vent
      - breathing protection ::@:: air-purifying respirators
        - air-purifying respirator characteristics ::@:: full-face, half-face, negative pressure
        - respirator fit tests ::@:: qualitative fit test and quantitative fit test
      - skin protection against corrosives and solvents ::@:: chemical gloves, can be made from butyl, latex, nitrile, polyvinyl chloride, etc.
        - chemical gloves precaution ::@:: test for leaks or pinholes, use the correct type for different chemicals
- occupational health goals ::@:: protect the environment, general community, and workers' health

## oversized data

### Legionnaires' Disease syndromes

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("29ba", "857e",),
  """
breathlessness
cough
fever
headache
malaise
muscle ache
pneumonia
""".strip().splitlines(),
)
```

<!--pytextgen generate section="29ba"--><!-- The following content is generated at 2024-02-09T10:20:46.039466+08:00. Any edits will be overridden! -->

> 1. breathlessness
> 2. cough
> 3. fever
> 4. headache
> 5. malaise
> 6. muscle ache
> 7. pneumonia

<!--/pytextgen-->

<!--pytextgen generate section="857e"--><!-- The following content is generated at 2024-02-09T10:20:46.005949+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←breathlessness
- breathlessness→::@::←cough
- cough→::@::←fever
- fever→::@::←headache
- headache→::@::←malaise
- malaise→::@::←muscle ache
- muscle ache→::@::←pneumonia
- pneumonia→::@::←_(end)_

<!--/pytextgen-->

### hazard control hierarchy

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("93ab", "ee35",),
  """
hazard reduction or elimination
engineering
administration
personal protective equipment
""".strip().splitlines(),
  pretext="most preferable", posttext="least preferable",
)
```

<!--pytextgen generate section="93ab"--><!-- The following content is generated at 2024-02-12T16:43:42.695370+08:00. Any edits will be overridden! -->

> 1. hazard reduction or elimination
> 2. engineering
> 3. administration
> 4. personal protective equipment

<!--/pytextgen-->

<!--pytextgen generate section="ee35"--><!-- The following content is generated at 2024-02-18T15:35:10.884856+08:00. Any edits will be overridden! -->

- _(most preferable)_→::@::←hazard reduction or elimination
- hazard reduction or elimination→::@::←engineering
- engineering→::@::←administration
- administration→::@::←personal protective equipment
- personal protective equipment→::@::←_(least preferable)_

<!--/pytextgen-->

### heat stroke syndromes

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("b12d", "7832",),
  """
convulsions
dry hot skin
elevated core temperature
high temperature
mental confusion
reduced sweating
""".strip().splitlines(),
)
```

<!--pytextgen generate section="b12d"--><!-- The following content is generated at 2024-02-09T10:20:45.970034+08:00. Any edits will be overridden! -->

> 1. convulsions
> 2. dry hot skin
> 3. elevated core temperature
> 4. high temperature
> 5. mental confusion
> 6. reduced sweating

<!--/pytextgen-->

<!--pytextgen generate section="7832"--><!-- The following content is generated at 2024-02-09T10:20:45.926284+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←convulsions
- convulsions→::@::←dry hot skin
- dry hot skin→::@::←elevated core temperature
- elevated core temperature→::@::←high temperature
- high temperature→::@::←mental confusion
- mental confusion→::@::←reduced sweating
- reduced sweating→::@::←_(end)_

<!--/pytextgen-->

### occupational hazard factors

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("1a67", "058b",),
  """
control
environment
equipment
material
process
user
""".strip().splitlines(),
)
```

<!--pytextgen generate section="1a67"--><!-- The following content is generated at 2024-02-09T10:20:45.730827+08:00. Any edits will be overridden! -->

> 1. control
> 2. environment
> 3. equipment
> 4. material
> 5. process
> 6. user

<!--/pytextgen-->

<!--pytextgen generate section="058b"--><!-- The following content is generated at 2024-02-09T10:20:45.701708+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←control
- control→::@::←environment
- environment→::@::←equipment
- equipment→::@::←material
- material→::@::←process
- process→::@::←user
- user→::@::←_(end)_

<!--/pytextgen-->

### occupational hazard types

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("f9a2", "b123",),
  """
biological
chemical
ergonomic
occupation-specific
physical
socio-psychological
""".strip().splitlines(),
)
```

<!--pytextgen generate section="f9a2"--><!-- The following content is generated at 2024-03-07T00:02:22.082267+08:00. Any edits will be overridden! -->

> 1. biological
> 2. chemical
> 3. ergonomic
> 4. occupation-specific
> 5. physical
> 6. socio-psychological

<!--/pytextgen-->

<!--pytextgen generate section="b123"--><!-- The following content is generated at 2024-03-07T00:02:22.051287+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←biological
- biological→::@::←chemical
- chemical→::@::←ergonomic
- ergonomic→::@::←occupation-specific
- occupation-specific→::@::←physical
- physical→::@::←socio-psychological
- socio-psychological→::@::←_(end)_

<!--/pytextgen-->

### occupational health areas

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("d929", "afb9",),
  """
general community environment
occupational hygiene
occupational medicine
occupational rehabilitation
workers
workplace
""".strip().splitlines(),
)
```

<!--pytextgen generate section="d929"--><!-- The following content is generated at 2024-02-09T10:20:45.574880+08:00. Any edits will be overridden! -->

> 1. general community environment
> 2. occupational hygiene
> 3. occupational medicine
> 4. occupational rehabilitation
> 5. workers
> 6. workplace

<!--/pytextgen-->

<!--pytextgen generate section="afb9"--><!-- The following content is generated at 2024-02-09T10:20:45.549913+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←general community environment
- general community environment→::@::←occupational hygiene
- occupational hygiene→::@::←occupational medicine
- occupational medicine→::@::←occupational rehabilitation
- occupational rehabilitation→::@::←workers
- workers→::@::←workplace
- workplace→::@::←_(end)_

<!--/pytextgen-->

### occupational medicine section

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("b36a", "207b",),
  """
conduct medical clearance
diagnosis
education
promotion
treatment
""".strip().splitlines(),
)
```

<!--pytextgen generate section="b36a"--><!-- The following content is generated at 2024-02-09T10:20:45.620870+08:00. Any edits will be overridden! -->

> 1. conduct medical clearance
> 2. diagnosis
> 3. education
> 4. promotion
> 5. treatment

<!--/pytextgen-->

<!--pytextgen generate section="207b"--><!-- The following content is generated at 2024-02-09T10:20:45.596886+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←conduct medical clearance
- conduct medical clearance→::@::←diagnosis
- diagnosis→::@::←education
- education→::@::←promotion
- promotion→::@::←treatment
- treatment→::@::←_(end)_

<!--/pytextgen-->

### physical hazards

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("e372", "81ab",),
  """
ionizing radiation
noise
nonionizing radiation
pressure
temperature
vibration
""".strip().splitlines(),
)
```

<!--pytextgen generate section="e372"--><!-- The following content is generated at 2024-02-09T10:20:45.768548+08:00. Any edits will be overridden! -->

> 1. ionizing radiation
> 2. noise
> 3. nonionizing radiation
> 4. pressure
> 5. temperature
> 6. vibration

<!--/pytextgen-->

<!--pytextgen generate section="81ab"--><!-- The following content is generated at 2024-02-09T10:20:45.804458+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←ionizing radiation
- ionizing radiation→::@::←noise
- noise→::@::←nonionizing radiation
- nonionizing radiation→::@::←pressure
- pressure→::@::←temperature
- temperature→::@::←vibration
- vibration→::@::←_(end)_

<!--/pytextgen-->

### workplaces with temperature hazards

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("f272", "41ab",),
  """
cold storages
glassworks
kitchens
laundries
steelworks
""".strip().splitlines(),
)
```

<!--pytextgen generate section="f272"--><!-- The following content is generated at 2024-02-09T10:20:45.886183+08:00. Any edits will be overridden! -->

> 1. cold storages
> 2. glassworks
> 3. kitchens
> 4. laundries
> 5. steelworks

<!--/pytextgen-->

<!--pytextgen generate section="41ab"--><!-- The following content is generated at 2024-02-09T10:20:45.843746+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←cold storages
- cold storages→::@::←glassworks
- glassworks→::@::←kitchens
- kitchens→::@::←laundries
- laundries→::@::←steelworks
- steelworks→::@::←_(end)_

<!--/pytextgen-->

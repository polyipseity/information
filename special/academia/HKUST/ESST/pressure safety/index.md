---
aliases:
  - ESST pressure safety index
  - HKUST ESST pressure safety index
tags:
  - flashcard/archive/special/academia/HKUST/ESST/pressure_safety
  - function/index
  - language/in/English
---

# index

- HKUST ESST pressure safety

```Python
# pytextgen generate module
# import ../../../../../../tools/utility.py.md
```

The content is in teaching order.

- [pressure](../../../../../general/pressure.md) _P_ ::@:: [force](../../../../../general/force.md) applied perpendicular to a surface per unit area
  - [pressure](../../../../../general/pressure.md) [units of measurement](../../../../../general/unit%20of%20measurement.md) ::@:: [SI unit](../../../../../general/International%20System%20of%20Units.md): [pascal](../../../../../general/pascal%20(unit).md) (Pa), Pa = N/m<sup>2</sup>, 1 bar = 100000 Pa, 1 atm = 101325 Pa
- pressured system ::@:: One or more [pressure vessels](../../../../../general/pressure%20vessel.md), pipework, and associated protective devices.
  - pressured system classification in [Hong Kong](../../../../../general/Hong%20Kong.md) ::@:: [boiler](../../../../../general/boiler.md) and [pressure vessel](../../../../../general/pressure%20vessel.md)
    - [boiler examples](#boiler%20examples)
    - [pressure vessel examples](#pressure%20vessel%20examples)
  - an example of a pressured system ::@:: Several boilers are connected to an air receiver. Each boiler has a control for controlling the flow to the air receiver. The air receiver can be used for many applications.
- hazards
  - [hazard causes](#hazard%20causes)
  - [hazard types](#hazard%20types)
  - [hazard factors](#hazard%20factors)
- [design safety](#design%20safety)
- technical requirements ::@:: Boilers and Pressure Vessels Regulations 2002 (Cap. 56A)
  - [boiler requirements](#boiler%20requirements)
  - [air or steam receiver requirements](#air%20or%20steam%20receiver%20requirements)
  - [pressurized fuel container requirements](#pressurized%20fuel%20container%20requirements)
  - [auxiliary equipments](#auxiliary%20equipments)
- [safety measures](#safety%20measures)
  - spring-loaded safety valve ::@:: Ensures the pressure is below the maximum permissible working pressure. Positioned downstream. Away from inlets to avoid disturbances.
  - calibrated pressure gauge ::@:: Has red marking indicating the maximum permissible working pressure. Allows a test device to be fitted.
  - thermal protection ::@:: Shutdown requires action to be taken first to avoid overheating. Install fusible pressure release plug.
  - coolant protection ::@:: Shuts down compressors when the water temperature exceeds maximum.
  - lubricant protection ::@:: Shuts down compressors when the lubricant pressure drops below minimum.
  - air inlet and outlet monitoring ::@:: A water manometer or pressure-indicating device for each compressor air inlet.
- hydraulic system
  - hydraulic system hazards ::@:: burns, flailing or ruptured fittings or hoses, pinhole leak injury
  - [hydraulic system safety measures](#hydraulic%20system%20safety%20measures)
  - [combined gas law](../../../../../general/ideal%20gas%20law.md#combined%20gas%20law) ::@:: _PV_/_T_ = _k_: When volume decreases or temperature increases, pressure increases.
- compressed gas cylinder
  - compressed gas cylinder hazards ::@:: Pressure can reach over 100 bars. Leaking gas produce a force 20 to 50 times the cylinder weight, which is about 100 kg, similar to a rocket or guided missile. Over-pressurized vessel fail at a weak point if it exists. If that point is very weak, the vessel can fail at or below normal operating pressure.
  - [compressed gas cylinder safety measures](#compressed%20gas%20cylinder%20safety%20measures)
- [relevant legislation in Hong Kong](#relevant%20legislation%20in%20Hong%20Kong)
  - Boilers and Pressure Vessels Ordinance (Cap. 56) ::@:: Provision of control and operation of boilers and pressure vessels. Ensures standards. Defines _appointed examiners_ and _competent person_. Requires certificate of examination and certificate of fitness.
  - certificate of fitness ::@:: Required for auxiliary equipment, boiler pressure vessel, and steam container, but NOT pressurized fuel container, to be used. Valid for 26 months. Must renew after hired, prohibition order, repair, or sold. The examination process is outlined under hydraulic test.
  - hydraulic test
    - hydraulic test for seamless steel air receivers ::@:: $\text{test pressure} = \begin{cases} \mathrm{MPWP} + 1.4 \times 10^7 \mathrm{\ Pa} & \text{ if } 1.4 \times 10^7 \mathrm{\ Pa} < \mathrm{MPWP} \le 2.8 \times 10^7 \mathrm{\ Pa} \\ 1.5 \,\mathrm{MPWP} & \text{ if } \mathrm{MPWP} > 2.8 \times 10^7 \mathrm{\ Pa} \end{cases}$.
    - hydraulic test for other air receivers ::@:: $\text{test pressure} = \begin{cases} 2 \,\mathrm{MPWP} & \text{ if } \mathrm{MPWP} \le 7 \times 10^5 \mathrm{\ Pa} \\ 1.5 \,\mathrm{MPWP} + 3.5 \times 10^5 \mathrm{\ Pa} & \text{ if } \mathrm{MPWP} > 7 \times 10^5 \mathrm{\ Pa} \end{cases}$.
  - Dangerous Goods (General) Regulations (Repealed) (Cap. 295B) ::@:: Governs pressurized cylinders.
  - pressurized cylinder ::@:: Governed by Dangerous Goods (General) Regulations (Repealed) (Cap. 295B) instead. Requires hydraulic stretch test and hydraulic pressure test. Valid for 5 years.
  - hydraulic stretch test and hydraulic pressure test ::@:: For permanent gas, the pressure for hydraulic stretch test is not less than 21 MPa and for hydraulic pressure test is not less than 20 MPa. For liquefied gas, the pressure is not less than 4/3 of the working pressure for both tests. The cylinder shall be destroyed if it shows a permanent volumetric expansion of more than 10%, leakage, or deformation under the tests.

## oversized data

### air or steam receiver requirements

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("29a2", "3842",),
  """
control: spring-loaded safety valve for controlling the working pressure
identity: mark each receiver with a distinguishing number
indication: pressure gauge with red marking showing the maximum permissible working pressure
safety: automatic mechanism like reducing valve to prevent over-pressurizing
safety: withstand the maximum permissible working pressure
""".strip().splitlines(),
)
```

<!--pytextgen generate section="29a2"--><!-- The following content is generated at 2024-02-20T14:07:01.573880+08:00. Any edits will be overridden! -->

> 1. control: spring-loaded safety valve for controlling the working pressure
> 2. identity: mark each receiver with a distinguishing number
> 3. indication: pressure gauge with red marking showing the maximum permissible working pressure
> 4. safety: automatic mechanism like reducing valve to prevent over-pressurizing
> 5. safety: withstand the maximum permissible working pressure

<!--/pytextgen-->

<!--pytextgen generate section="3842"--><!-- The following content is generated at 2024-02-20T14:07:01.560765+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←control: spring-loaded safety valve for controlling the working pressure
- control: spring-loaded safety valve for controlling the working pressure→::@::←identity: mark each receiver with a distinguishing number
- identity: mark each receiver with a distinguishing number→::@::←indication: pressure gauge with red marking showing the maximum permissible working pressure
- indication: pressure gauge with red marking showing the maximum permissible working pressure→::@::←safety: automatic mechanism like reducing valve to prevent over-pressurizing
- safety: automatic mechanism like reducing valve to prevent over-pressurizing→::@::←safety: withstand the maximum permissible working pressure
- safety: withstand the maximum permissible working pressure→::@::←_(end)_

<!--/pytextgen-->

### auxiliary equipments

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("5920", "9281",),
  """
flue damper
fuel pump
heater
multiple burner
pipe
""".strip().splitlines(),
)
```

<!--pytextgen generate section="5920"--><!-- The following content is generated at 2024-02-09T19:56:53.046293+08:00. Any edits will be overridden! -->

> 1. flue damper
> 2. fuel pump
> 3. heater
> 4. multiple burner
> 5. pipe

<!--/pytextgen-->

<!--pytextgen generate section="9281"--><!-- The following content is generated at 2024-02-09T19:56:53.031289+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←flue damper
- flue damper→::@::←fuel pump
- fuel pump→::@::←heater
- heater→::@::←multiple burner
- multiple burner→::@::←pipe
- pipe→::@::←_(end)_

<!--/pytextgen-->

### boiler examples

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("d929", "afb9",),
  """
electric heated boiler
electric steam boiler
fire-tube boiler
fossil fuel boiler
thermal oil heater
""".strip().splitlines(),
)
```

<!--pytextgen generate section="d929"--><!-- The following content is generated at 2024-02-09T19:56:52.638827+08:00. Any edits will be overridden! -->

> 1. electric heated boiler
> 2. electric steam boiler
> 3. fire-tube boiler
> 4. fossil fuel boiler
> 5. thermal oil heater

<!--/pytextgen-->

<!--pytextgen generate section="afb9"--><!-- The following content is generated at 2024-02-09T19:56:52.621799+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←electric heated boiler
- electric heated boiler→::@::←electric steam boiler
- electric steam boiler→::@::←fire-tube boiler
- fire-tube boiler→::@::←fossil fuel boiler
- fossil fuel boiler→::@::←thermal oil heater
- thermal oil heater→::@::←_(end)_

<!--/pytextgen-->

### boiler requirements

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("96ff", "3e9a",),
  """
control: spring-loaded safety valve and separate stop-valve for controlling the working pressure
identity: mark each boiler with a distinguishing number
indication: pressure gauge with red marking showing the maximum permissible working pressure
indication: transparent water level gauge
safety: fusible pressure release plug or efficient low-water alarm
""".strip().splitlines(),
)
```

<!--pytextgen generate section="96ff"--><!-- The following content is generated at 2024-02-20T14:07:01.649622+08:00. Any edits will be overridden! -->

> 1. control: spring-loaded safety valve and separate stop-valve for controlling the working pressure
> 2. identity: mark each boiler with a distinguishing number
> 3. indication: pressure gauge with red marking showing the maximum permissible working pressure
> 4. indication: transparent water level gauge
> 5. safety: fusible pressure release plug or efficient low-water alarm

<!--/pytextgen-->

<!--pytextgen generate section="3e9a"--><!-- The following content is generated at 2024-02-20T14:07:01.672633+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←control: spring-loaded safety valve and separate stop-valve for controlling the working pressure
- control: spring-loaded safety valve and separate stop-valve for controlling the working pressure→::@::←identity: mark each boiler with a distinguishing number
- identity: mark each boiler with a distinguishing number→::@::←indication: pressure gauge with red marking showing the maximum permissible working pressure
- indication: pressure gauge with red marking showing the maximum permissible working pressure→::@::←indication: transparent water level gauge
- indication: transparent water level gauge→::@::←safety: fusible pressure release plug or efficient low-water alarm
- safety: fusible pressure release plug or efficient low-water alarm→::@::←_(end)_

<!--/pytextgen-->

### compressed gas cylinder safety measures

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("9012", "33bb",),
  """
design: correct fittings and regulators
design: flashback arrestor for flammable or oxidizing gas is used to prevent ignition
operator: close inactive valves
operator: frequent examination for damages
operator: keep upright
operator: mark empty cylinders
operator: no electric arcs, greases, heat sources, or oils nearby to prevent explosion
""".strip().splitlines(),
)
```

<!--pytextgen generate section="9012"--><!-- The following content is generated at 2024-02-20T13:14:06.434725+08:00. Any edits will be overridden! -->

> 1. design: correct fittings and regulators
> 2. design: flashback arrestor for flammable or oxidizing gas is used to prevent ignition
> 3. operator: close inactive valves
> 4. operator: frequent examination for damages
> 5. operator: keep upright
> 6. operator: mark empty cylinders
> 7. operator: no electric arcs, greases, heat sources, or oils nearby to prevent explosion

<!--/pytextgen-->

<!--pytextgen generate section="33bb"--><!-- The following content is generated at 2024-02-20T13:14:06.445729+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←design: correct fittings and regulators
- design: correct fittings and regulators→::@::←design: flashback arrestor for flammable or oxidizing gas is used to prevent ignition
- design: flashback arrestor for flammable or oxidizing gas is used to prevent ignition→::@::←operator: close inactive valves
- operator: close inactive valves→::@::←operator: frequent examination for damages
- operator: frequent examination for damages→::@::←operator: keep upright
- operator: keep upright→::@::←operator: mark empty cylinders
- operator: mark empty cylinders→::@::←operator: no electric arcs, greases, heat sources, or oils nearby to prevent explosion
- operator: no electric arcs, greases, heat sources, or oils nearby to prevent explosion→::@::←_(end)_

<!--/pytextgen-->

### design safety

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("038b", "857e",),
  """
examinable with safely accessible interior
expected working life
fluid properties
operating limits, like valve operating conditions
proper materials
protective devices that release contents do so safely
""".strip().splitlines(),
)
```

<!--pytextgen generate section="038b"--><!-- The following content is generated at 2024-02-19T20:56:23.901793+08:00. Any edits will be overridden! -->

> 1. examinable with safely accessible interior
> 2. expected working life
> 3. fluid properties
> 4. operating limits, like valve operating conditions
> 5. proper materials
> 6. protective devices that release contents do so safely

<!--/pytextgen-->

<!--pytextgen generate section="857e"--><!-- The following content is generated at 2024-02-19T20:56:23.890793+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←examinable with safely accessible interior
- examinable with safely accessible interior→::@::←expected working life
- expected working life→::@::←fluid properties
- fluid properties→::@::←operating limits, like valve operating conditions
- operating limits, like valve operating conditions→::@::←proper materials
- proper materials→::@::←protective devices that release contents do so safely
- protective devices that release contents do so safely→::@::←_(end)_

<!--/pytextgen-->

### hazard causes

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("98ba", "2984",),
  """
blocked or restricted flow
compressor malfunction
external fire
failure of automatic controls
formation and ignition or detonation of carbonaceous deposits
ignition or detonation of oil or oil vapor
overheating
""".strip().splitlines(),
)
```

<!--pytextgen generate section="98ba"--><!-- The following content is generated at 2024-02-09T19:56:52.734301+08:00. Any edits will be overridden! -->

> 1. blocked or restricted flow
> 2. compressor malfunction
> 3. external fire
> 4. failure of automatic controls
> 5. formation and ignition or detonation of carbonaceous deposits
> 6. ignition or detonation of oil or oil vapor
> 7. overheating

<!--/pytextgen-->

<!--pytextgen generate section="2984"--><!-- The following content is generated at 2024-02-09T19:56:52.708301+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←blocked or restricted flow
- blocked or restricted flow→::@::←compressor malfunction
- compressor malfunction→::@::←external fire
- external fire→::@::←failure of automatic controls
- failure of automatic controls→::@::←formation and ignition or detonation of carbonaceous deposits
- formation and ignition or detonation of carbonaceous deposits→::@::←ignition or detonation of oil or oil vapor
- ignition or detonation of oil or oil vapor→::@::←overheating
- overheating→::@::←_(end)_

<!--/pytextgen-->

### hazard factors

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("aa98", "1192",),
  """
control complexity
equipment age, condition, and suitability
fluid properties
pressure
prevailing conditions
worker knowledge and skills
""".strip().splitlines(),
)
```

<!--pytextgen generate section="aa98"--><!-- The following content is generated at 2024-02-19T20:13:03.105296+08:00. Any edits will be overridden! -->

> 1. control complexity
> 2. equipment age, condition, and suitability
> 3. fluid properties
> 4. pressure
> 5. prevailing conditions
> 6. worker knowledge and skills

<!--/pytextgen-->

<!--pytextgen generate section="1192"--><!-- The following content is generated at 2024-02-19T20:13:03.087677+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←control complexity
- control complexity→::@::←equipment age, condition, and suitability
- equipment age, condition, and suitability→::@::←fluid properties
- fluid properties→::@::←pressure
- pressure→::@::←prevailing conditions
- prevailing conditions→::@::←worker knowledge and skills
- worker knowledge and skills→::@::←_(end)_

<!--/pytextgen-->

### hazard types

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("837b", "937a",),
  """
blast, explosion, flying debris, and shockwave
chemical burn
fire and thermal burn
poisoning
suffocation
""".strip().splitlines(),
)
```

<!--pytextgen generate section="837b"--><!-- The following content is generated at 2024-02-19T20:13:03.130902+08:00. Any edits will be overridden! -->

> 1. blast, explosion, flying debris, and shockwave
> 2. chemical burn
> 3. fire and thermal burn
> 4. poisoning
> 5. suffocation

<!--/pytextgen-->

<!--pytextgen generate section="937a"--><!-- The following content is generated at 2024-02-19T20:13:03.118404+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←blast, explosion, flying debris, and shockwave
- blast, explosion, flying debris, and shockwave→::@::←chemical burn
- chemical burn→::@::←fire and thermal burn
- fire and thermal burn→::@::←poisoning
- poisoning→::@::←suffocation
- suffocation→::@::←_(end)_

<!--/pytextgen-->

### hydraulic system safety measures

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("cd12", "93fa",),
  """
design: fix hose strap to restrain the failing motion of dislocated flexible hoses
design: high flashpoint hydraulic oil
design: proper construction, design, and materials
operator: frequent examination for damages
operator: pressurize in stages
operator: segregate and indicate work area
""".strip().splitlines(),
)
```

<!--pytextgen generate section="cd12"--><!-- The following content is generated at 2024-02-20T13:55:14.042175+08:00. Any edits will be overridden! -->

> 1. design: fix hose strap to restrain the failing motion of dislocated flexible hoses
> 2. design: high flashpoint hydraulic oil
> 3. design: proper construction, design, and materials
> 4. operator: frequent examination for damages
> 5. operator: pressurize in stages
> 6. operator: segregate and indicate work area

<!--/pytextgen-->

<!--pytextgen generate section="93fa"--><!-- The following content is generated at 2024-02-20T13:55:14.024176+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←design: fix hose strap to restrain the failing motion of dislocated flexible hoses
- design: fix hose strap to restrain the failing motion of dislocated flexible hoses→::@::←design: high flashpoint hydraulic oil
- design: high flashpoint hydraulic oil→::@::←design: proper construction, design, and materials
- design: proper construction, design, and materials→::@::←operator: frequent examination for damages
- operator: frequent examination for damages→::@::←operator: pressurize in stages
- operator: pressurize in stages→::@::←operator: segregate and indicate work area
- operator: segregate and indicate work area→::@::←_(end)_

<!--/pytextgen-->

### pressure vessel examples

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("948b", "152a",),
  """
air receiver
fixed vessel for starting internal combustion engine
pressured fuel container
spraying paint container
""".strip().splitlines(),
)
```

<!--pytextgen generate section="948b"--><!-- The following content is generated at 2024-02-09T19:56:52.672841+08:00. Any edits will be overridden! -->

> 1. air receiver
> 2. fixed vessel for starting internal combustion engine
> 3. pressured fuel container
> 4. spraying paint container

<!--/pytextgen-->

<!--pytextgen generate section="152a"--><!-- The following content is generated at 2024-02-09T19:56:52.689301+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←air receiver
- air receiver→::@::←fixed vessel for starting internal combustion engine
- fixed vessel for starting internal combustion engine→::@::←pressured fuel container
- pressured fuel container→::@::←spraying paint container
- spraying paint container→::@::←_(end)_

<!--/pytextgen-->

### pressurized fuel container requirements

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("10ab", "23fb",),
  """
control: accessible valves and safety devices
control: remote control valve as close to burner as possible
safety: all piping properly secured save for 0.6 m immediately before the burner
safety: maximum permissible working pressure not more than 500 kPa
safety: pressure release valve
""".strip().splitlines(),
)
```

<!--pytextgen generate section="10ab"--><!-- The following content is generated at 2024-02-19T20:13:03.173682+08:00. Any edits will be overridden! -->

> 1. control: accessible valves and safety devices
> 2. control: remote control valve as close to burner as possible
> 3. safety: all piping properly secured save for 0.6 m immediately before the burner
> 4. safety: maximum permissible working pressure not more than 500 kPa
> 5. safety: pressure release valve

<!--/pytextgen-->

<!--pytextgen generate section="23fb"--><!-- The following content is generated at 2024-02-19T20:13:03.186373+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←control: accessible valves and safety devices
- control: accessible valves and safety devices→::@::←control: remote control valve as close to burner as possible
- control: remote control valve as close to burner as possible→::@::←safety: all piping properly secured save for 0.6 m immediately before the burner
- safety: all piping properly secured save for 0.6 m immediately before the burner→::@::←safety: maximum permissible working pressure not more than 500 kPa
- safety: maximum permissible working pressure not more than 500 kPa→::@::←safety: pressure release valve
- safety: pressure release valve→::@::←_(end)_

<!--/pytextgen-->

### relevant legislation in Hong Kong

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("78bb", "2876",),
  """
Boilers and Pressure Vessels Ordinance (Cap. 56)
Boilers and Pressure Vessels Regulations (Cap. 56A)
Boilers and Pressure Vessels (Forms) Order (Cap. 56B)
Dangerous Goods (General) Regulations (Repealed) (Cap. 295B)
""".strip().splitlines(),
)
```

<!--pytextgen generate section="78bb"--><!-- The following content is generated at 2024-02-09T19:56:53.153815+08:00. Any edits will be overridden! -->

> 1. Boilers and Pressure Vessels Ordinance (Cap. 56)
> 2. Boilers and Pressure Vessels Regulations (Cap. 56A)
> 3. Boilers and Pressure Vessels (Forms) Order (Cap. 56B)
> 4. Dangerous Goods (General) Regulations (Repealed) (Cap. 295B)

<!--/pytextgen-->

<!--pytextgen generate section="2876"--><!-- The following content is generated at 2024-02-09T19:56:53.136813+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←Boilers and Pressure Vessels Ordinance (Cap. 56)
- Boilers and Pressure Vessels Ordinance (Cap. 56)→::@::←Boilers and Pressure Vessels Regulations (Cap. 56A)
- Boilers and Pressure Vessels Regulations (Cap. 56A)→::@::←Boilers and Pressure Vessels (Forms) Order (Cap. 56B)
- Boilers and Pressure Vessels (Forms) Order (Cap. 56B)→::@::←Dangerous Goods (General) Regulations (Repealed) (Cap. 295B)
- Dangerous Goods (General) Regulations (Repealed) (Cap. 295B)→::@::←_(end)_

<!--/pytextgen-->

### safety measures

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("eeef", "184a",),
  """
air inlet and outlet monitoring
calibrated pressure gauge
coolant protection
explosion protection
lubricant protection
safety valve
thermal protection
""".strip().splitlines(),
)
```

<!--pytextgen generate section="eeef"--><!-- The following content is generated at 2024-02-09T19:56:53.064301+08:00. Any edits will be overridden! -->

> 1. air inlet and outlet monitoring
> 2. calibrated pressure gauge
> 3. coolant protection
> 4. explosion protection
> 5. lubricant protection
> 6. safety valve
> 7. thermal protection

<!--/pytextgen-->

<!--pytextgen generate section="184a"--><!-- The following content is generated at 2024-02-09T19:56:53.080815+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←air inlet and outlet monitoring
- air inlet and outlet monitoring→::@::←calibrated pressure gauge
- calibrated pressure gauge→::@::←coolant protection
- coolant protection→::@::←explosion protection
- explosion protection→::@::←lubricant protection
- lubricant protection→::@::←safety valve
- safety valve→::@::←thermal protection
- thermal protection→::@::←_(end)_

<!--/pytextgen-->

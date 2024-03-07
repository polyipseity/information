---
aliases:
  - ESST pressure safety outline
  - HKUST ESST pressure safety outline
tags:
  - flashcard/special/academia/HKUST/ESST/pressure_safety/outline
  - language/in/English
---

# HKUST ESST pressure safety outline

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../../../../../tools/utility.py.md
```

%%

The content is in teaching order.

- [pressure](../../../../../general/pressure.md) _P_ ::: [force](../../../../../general/force.md) applied perpendicular to a surface per unit area <!--SR:!2024-03-10,16,302!2024-03-08,14,297-->
  - [pressure](../../../../../general/pressure.md) [units of measurement](../../../../../general/unit%20of%20measurement.md) ::: [SI unit](../../../../../general/International%20System%20of%20Units.md): [pascal](../../../../../general/pascal%20(unit).md) (Pa), Pa = N/m<sup>2</sup>, 1 bar = 100000 Pa, 1 atm = 101325 Pa <!--SR:!2024-03-10,16,297!2024-03-11,17,306-->
- pressured system ::: One or more [pressure vessels](../../../../../general/pressure%20vessel.md), pipework, and associated protective devices. <!--SR:!2024-04-07,35,306!2024-03-10,16,297-->
  - pressured system classification in [Hong Kong](../../../../../general/Hong%20Kong.md) ::: [boiler](../../../../../general/boiler.md) and [pressure vessel](../../../../../general/pressure%20vessel.md) <!--SR:!2024-03-11,17,303!2024-03-12,18,306-->
    - [boiler examples](#boiler%20examples)
    - [pressure vessel examples](#pressure%20vessel%20examples)
  - an example of a pressured system ::: Several boilers are connected to an air receiver. Each boiler has a control for controlling the flow to the air receiver. The air receiver can be used for many applications. <!--SR:!2024-04-14,40,306!2024-03-11,17,306-->
- hazards
  - [hazard causes](#hazard%20causes)
  - [hazard types](#hazard%20types)
  - [hazard factors](#hazard%20factors)
- [design safety](#design%20safety)
- technical requirements ::: Boilers and Pressure Vessels Regulations 2002 (Cap. 56A) <!--SR:!2024-03-09,5,266!2024-04-10,38,303-->
  - [boiler requirements](#boiler%20requirements)
  - [air or steam receiver requirements](#air%20or%20steam%20receiver%20requirements)
  - [pressurized fuel container requirements](#pressurized%20fuel%20container%20requirements)
  - [auxiliary equipments](#auxiliary%20equipments)
- [safety measures](#safety%20measures)
  - spring-loaded safety valve ::: Ensures the pressure is below the maximum permissible working pressure. Positioned downstream. Away from inlets to avoid disturbances. <!--SR:!2024-03-25,24,266!2024-04-24,49,303-->
  - calibrated pressure gauge ::: Has red marking indicating the maximum permissible working pressure. Allows a test device to be fitted. <!--SR:!2024-03-09,15,297!2024-03-10,16,306-->
  - thermal protection ::: Shutdown requires action to be taken first to avoid overheating. Install fusible pressure release plug. <!--SR:!2024-04-21,46,306!2024-03-08,14,306-->
  - coolant protection ::: Shuts down compressors when the water temperature exceeds maximum. <!--SR:!2024-04-27,52,306!2024-04-09,36,306-->
  - lubricant protection ::: Shuts down compressors when the lubricant pressure drops below minimum. <!--SR:!2024-03-10,16,306!2024-04-20,45,297-->
  - air inlet and outlet monitoring ::: A water manometer or pressure-indicating device for each compressor air inlet. <!--SR:!2024-03-22,21,263!2024-04-16,43,303-->
- hydraulic system
  - hydraulic system hazards ::: burns, flailing or ruptured fittings or hoses, pinhole leak injury <!--SR:!2024-03-12,7,263!2024-03-08,14,303-->
  - [hydraulic system safety measures](#hydraulic%20system%20safety%20measures)
  - [combined gas law](../../../../../general/ideal%20gas%20law.md#combined%20gas%20law) ::: _PV_/_T_ = _k_: When volume decreases or temperature increases, pressure increases. <!--SR:!2024-03-12,18,303!2024-03-10,16,303-->
- compressed gas cylinder
  - compressed gas cylinder hazards ::: Pressure can reach over 100 bars. Leaking gas produce a force 20 to 50 times the cylinder weight, which is about 100 kg, similar to a rocket or guided missile. Over-pressurized vessel fail at a weak point if it exists. If that point is very weak, the vessel can fail at or below normal operating pressure. <!--SR:!2024-03-27,24,286!2024-04-04,32,303-->
  - [compressed gas cylinder safety measures](#compressed%20gas%20cylinder%20safety%20measures)
- [relevant legislation in Hong Kong](#relevant%20legislation%20in%20Hong%20Kong)
  - Boilers and Pressure Vessels Ordinance (Cap. 56) ::: Provision of control and operation of boilers and pressure vessels. Ensures standards. Defines _appointed examiners_ and _competent person_. Requires certificate of examination and certificate of fitness. <!--SR:!2024-04-10,34,286!2024-03-23,22,266-->
  - certificate of fitness ::: Required for auxiliary equipment, boiler pressure vessel, and steam container, but NOT pressurized fuel container, to be used. Valid for 26 months. Must renew after hired, prohibition order, repair, or sold. The examination process is outlined under hydraulic test. <!--SR:!2024-03-19,13,226!2024-03-22,19,263-->
  - hydraulic test
    - hydraulic test for seamless steel air receivers ::: $\text{test pressure} = \begin{cases} \mathrm{MPWP} + 1.4 \times 10^7 \mathrm{\ Pa} & \text{ if } 1.4 \times 10^7 \mathrm{\ Pa} < \mathrm{MPWP} \le 2.8 \times 10^7 \mathrm{\ Pa} \\ 1.5 \,\mathrm{MPWP} & \text{ if } \mathrm{MPWP} > 2.8 \times 10^7 \mathrm{\ Pa} \end{cases}$. <!--SR:!2024-03-16,11,226!2024-03-25,25,286-->
    - hydraulic test for other air receivers ::: $\text{test pressure} = \begin{cases} 2 \,\mathrm{MPWP} & \text{ if } \mathrm{MPWP} \le 7 \times 10^5 \mathrm{\ Pa} \\ 1.5 \,\mathrm{MPWP} + 3.5 \times 10^5 \mathrm{\ Pa} & \text{ if } \mathrm{MPWP} > 7 \times 10^5 \mathrm{\ Pa} \end{cases}$. <!--SR:!2024-03-23,17,223!2024-04-08,35,283-->
  - Dangerous Goods (General) Regulations (Repealed) (Cap. 295B) ::: Governs pressurized cylinders. <!--SR:!2024-04-11,36,283!2024-03-30,27,263-->
- pressurized cylinder ::: Governed by Dangerous Goods (General) Regulations (Repealed) (Cap. 295B) instead. Requires hydraulic stretch test and hydraulic pressure test. Valid for 5 years. <!--SR:!2024-04-12,38,283!2024-04-02,32,270-->
  - hydraulic stretch test and hydraulic pressure test ::: For permanent gas, the pressure for hydraulic stretch test is not less than 21 MPa and for hydraulic pressure test is not less than 20 MPa. For liquefied gas, the pressure is not less than 4/3 of the working pressure. The cylinder shall be destroyed if it shows a permanent volumetric expansion of more than 10%, leakage, or deformation under the tests. <!--SR:!2024-03-08,10,246!2024-03-27,24,277-->

## oversized data

### air or steam receiver requirements

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="29a2"--><!-- The following content is generated at 2024-02-20T14:07:01.573880+08:00. Any edits will be overridden! -->

> 1. control: spring-loaded safety valve for controlling the working pressure
> 2. identity: mark each receiver with a distinguishing number
> 3. indication: pressure gauge with red marking showing the maximum permissible working pressure
> 4. safety: automatic mechanism like reducing valve to prevent over-pressurizing
> 5. safety: withstand the maximum permissible working pressure

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3842"--><!-- The following content is generated at 2024-02-20T14:07:01.560765+08:00. Any edits will be overridden! -->

- _(begin)_→:::←control: spring-loaded safety valve for controlling the working pressure <!--SR:!2024-03-13,15,266!2024-04-23,48,306-->
- control: spring-loaded safety valve for controlling the working pressure→:::←identity: mark each receiver with a distinguishing number <!--SR:!2024-03-24,21,286!2024-04-08,36,306-->
- identity: mark each receiver with a distinguishing number→:::←indication: pressure gauge with red marking showing the maximum permissible working pressure <!--SR:!2024-03-10,13,284!2024-03-14,17,304-->
- indication: pressure gauge with red marking showing the maximum permissible working pressure→:::←safety: automatic mechanism like reducing valve to prevent over-pressurizing <!--SR:!2024-03-09,5,166!2024-03-15,16,266-->
- safety: automatic mechanism like reducing valve to prevent over-pressurizing→:::←safety: withstand the maximum permissible working pressure <!--SR:!2024-03-17,14,226!2024-03-10,9,243-->
- safety: withstand the maximum permissible working pressure→:::←_(end)_ <!--SR:!2024-04-10,38,303!2024-04-01,27,286-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### auxiliary equipments

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5920"--><!-- The following content is generated at 2024-02-09T19:56:53.046293+08:00. Any edits will be overridden! -->

> 1. flue damper
> 2. fuel pump
> 3. heater
> 4. multiple burner
> 5. pipe

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9281"--><!-- The following content is generated at 2024-02-09T19:56:53.031289+08:00. Any edits will be overridden! -->

- _(begin)_→:::←flue damper <!--SR:!2024-03-20,21,286!2024-03-08,14,306-->
- flue damper→:::←fuel pump <!--SR:!2024-04-08,36,303!2024-03-13,12,266-->
- fuel pump→:::←heater <!--SR:!2024-04-05,32,286!2024-03-31,28,286-->
- heater→:::←multiple burner <!--SR:!2024-03-13,14,266!2024-03-22,21,266-->
- multiple burner→:::←pipe <!--SR:!2024-03-09,6,266!2024-04-07,32,286-->
- pipe→:::←_(end)_ <!--SR:!2024-04-15,43,303!2024-03-14,8,266-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### boiler examples

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d929"--><!-- The following content is generated at 2024-02-09T19:56:52.638827+08:00. Any edits will be overridden! -->

> 1. electric heated boiler
> 2. electric steam boiler
> 3. fire-tube boiler
> 4. fossil fuel boiler
> 5. thermal oil heater

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="afb9"--><!-- The following content is generated at 2024-02-09T19:56:52.621799+08:00. Any edits will be overridden! -->

- _(begin)_→:::←electric heated boiler <!--SR:!2024-04-09,34,283!2024-04-28,53,306-->
- electric heated boiler→:::←electric steam boiler <!--SR:!2024-04-28,53,306!2024-04-01,28,286-->
- electric steam boiler→:::←fire-tube boiler <!--SR:!2024-03-27,24,263!2024-03-09,6,246-->
- fire-tube boiler→:::←fossil fuel boiler <!--SR:!2024-03-09,11,243!2024-03-13,9,246-->
- fossil fuel boiler→:::←thermal oil heater <!--SR:!2024-03-10,7,246!2024-03-08,2,166-->
- thermal oil heater→:::←_(end)_ <!--SR:!2024-04-18,45,306!2024-04-03,31,286-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### boiler requirements

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="96ff"--><!-- The following content is generated at 2024-02-20T14:07:01.649622+08:00. Any edits will be overridden! -->

> 1. control: spring-loaded safety valve and separate stop-valve for controlling the working pressure
> 2. identity: mark each boiler with a distinguishing number
> 3. indication: pressure gauge with red marking showing the maximum permissible working pressure
> 4. indication: transparent water level gauge
> 5. safety: fusible pressure release plug or efficient low-water alarm

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3e9a"--><!-- The following content is generated at 2024-02-20T14:07:01.672633+08:00. Any edits will be overridden! -->

- _(begin)_→:::←control: spring-loaded safety valve and separate stop-valve for controlling the working pressure <!--SR:!2024-03-14,7,203!2024-04-21,48,306-->
- control: spring-loaded safety valve and separate stop-valve for controlling the working pressure→:::←identity: mark each boiler with a distinguishing number <!--SR:!2024-03-08,11,266!2024-03-17,17,266-->
- identity: mark each boiler with a distinguishing number→:::←indication: pressure gauge with red marking showing the maximum permissible working pressure <!--SR:!2024-03-13,16,304!2024-03-14,17,304-->
- indication: pressure gauge with red marking showing the maximum permissible working pressure→:::←indication: transparent water level gauge <!--SR:!2024-03-21,18,263!2024-04-24,49,306-->
- indication: transparent water level gauge→:::←safety: fusible pressure release plug or efficient low-water alarm <!--SR:!2024-03-08,2,150!2024-03-28,25,286-->
- safety: fusible pressure release plug or efficient low-water alarm→:::←_(end)_ <!--SR:!2024-03-09,15,306!2024-03-12,6,226-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### compressed gas cylinder safety measures

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9012"--><!-- The following content is generated at 2024-02-20T13:14:06.434725+08:00. Any edits will be overridden! -->

> 1. design: correct fittings and regulators
> 2. design: flashback arrestor for flammable or oxidizing gas is used to prevent ignition
> 3. operator: close inactive valves
> 4. operator: frequent examination for damages
> 5. operator: keep upright
> 6. operator: mark empty cylinders
> 7. operator: no electric arcs, greases, heat sources, or oils nearby to prevent explosion

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="33bb"--><!-- The following content is generated at 2024-02-20T13:14:06.445729+08:00. Any edits will be overridden! -->

- _(begin)_→:::←design: correct fittings and regulators <!--SR:!2024-03-09,12,246!2024-04-14,40,306-->
- design: correct fittings and regulators→:::←design: flashback arrestor for flammable or oxidizing gas is used to prevent ignition <!--SR:!2024-03-18,15,246!2024-03-17,14,246-->
- design: flashback arrestor for flammable or oxidizing gas is used to prevent ignition→:::←operator: close inactive valves <!--SR:!2024-03-11,8,206!2024-04-04,30,283-->
- operator: close inactive valves→:::←operator: frequent examination for damages <!--SR:!2024-04-03,31,286!2024-03-08,11,246-->
- operator: frequent examination for damages→:::←operator: keep upright <!--SR:!2024-04-09,37,306!2024-03-08,14,303-->
- operator: keep upright→:::←operator: mark empty cylinders <!--SR:!2024-03-20,21,286!2024-03-23,20,266-->
- operator: mark empty cylinders→:::←operator: no electric arcs, greases, heat sources, or oils nearby to prevent explosion <!--SR:!2024-04-18,43,303!2024-03-28,28,286-->
- operator: no electric arcs, greases, heat sources, or oils nearby to prevent explosion→:::←_(end)_ <!--SR:!2024-03-09,15,306!2024-03-08,10,246-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### design safety

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="038b"--><!-- The following content is generated at 2024-02-19T20:56:23.901793+08:00. Any edits will be overridden! -->

> 1. examinable with safely accessible interior
> 2. expected working life
> 3. fluid properties
> 4. operating limits, like valve operating conditions
> 5. proper materials
> 6. protective devices that release contents do so safely

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="857e"--><!-- The following content is generated at 2024-02-19T20:56:23.890793+08:00. Any edits will be overridden! -->

- _(begin)_→:::←examinable with safely accessible interior <!--SR:!2024-03-09,6,246!2024-04-22,47,303-->
- examinable with safely accessible interior→:::←expected working life <!--SR:!2024-03-19,19,266!2024-03-29,22,263-->
- expected working life→:::←fluid properties <!--SR:!2024-04-07,35,306!2024-03-16,13,246-->
- fluid properties→:::←operating limits, like valve operating conditions <!--SR:!2024-03-12,5,186!2024-03-14,11,266-->
- operating limits, like valve operating conditions→:::←proper materials <!--SR:!2024-03-08,2,166!2024-03-08,11,246-->
- proper materials→:::←protective devices that release contents do so safely <!--SR:!2024-03-11,17,306!2024-04-28,52,303-->
- protective devices that release contents do so safely→:::←_(end)_ <!--SR:!2024-04-19,45,303!2024-03-11,8,206-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### hazard causes

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="98ba"--><!-- The following content is generated at 2024-02-09T19:56:52.734301+08:00. Any edits will be overridden! -->

> 1. blocked or restricted flow
> 2. compressor malfunction
> 3. external fire
> 4. failure of automatic controls
> 5. formation and ignition or detonation of carbonaceous deposits
> 6. ignition or detonation of oil or oil vapor
> 7. overheating

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2984"--><!-- The following content is generated at 2024-02-09T19:56:52.708301+08:00. Any edits will be overridden! -->

- _(begin)_→:::←blocked or restricted flow <!--SR:!2024-04-08,34,286!2024-03-11,17,303-->
- blocked or restricted flow→:::←compressor malfunction <!--SR:!2024-03-16,13,246!2024-04-20,47,306-->
- compressor malfunction→:::←external fire <!--SR:!2024-03-12,9,246!2024-03-15,12,246-->
- external fire→:::←failure of automatic controls <!--SR:!2024-03-10,5,266!2024-04-12,40,306-->
- failure of automatic controls→:::←formation and ignition or detonation of carbonaceous deposits <!--SR:!2024-03-27,26,266!2024-03-15,16,263-->
- formation and ignition or detonation of carbonaceous deposits→:::←ignition or detonation of oil or oil vapor <!--SR:!2024-04-15,42,303!2024-04-20,45,303-->
- ignition or detonation of oil or oil vapor→:::←overheating <!--SR:!2024-04-12,40,306!2024-04-02,30,286-->
- overheating→:::←_(end)_ <!--SR:!2024-03-10,16,306!2024-03-28,22,266-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### hazard factors

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="aa98"--><!-- The following content is generated at 2024-02-19T20:13:03.105296+08:00. Any edits will be overridden! -->

> 1. control complexity
> 2. equipment age, condition, and suitability
> 3. fluid properties
> 4. pressure
> 5. prevailing conditions
> 6. worker knowledge and skills

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1192"--><!-- The following content is generated at 2024-02-19T20:13:03.087677+08:00. Any edits will be overridden! -->

- _(begin)_→:::←control complexity <!--SR:!2024-03-26,20,266!2024-05-11,66,310-->
- control complexity→:::←equipment age, condition, and suitability <!--SR:!2024-04-14,39,286!2024-03-25,25,286-->
- equipment age, condition, and suitability→:::←fluid properties <!--SR:!2024-03-26,23,286!2024-03-24,19,226-->
- fluid properties→:::←pressure <!--SR:!2024-03-19,18,266!2024-03-21,21,266-->
- pressure→:::←prevailing conditions <!--SR:!2024-03-29,25,286!2024-04-04,32,306-->
- prevailing conditions→:::←worker knowledge and skills <!--SR:!2024-03-09,3,226!2024-03-12,13,246-->
- worker knowledge and skills→:::←_(end)_ <!--SR:!2024-03-10,16,303!2024-04-10,36,283-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### hazard types

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="837b"--><!-- The following content is generated at 2024-02-19T20:13:03.130902+08:00. Any edits will be overridden! -->

> 1. blast, explosion, flying debris, and shockwave
> 2. chemical burn
> 3. fire and thermal burn
> 4. poisoning
> 5. suffocation

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="937a"--><!-- The following content is generated at 2024-02-19T20:13:03.118404+08:00. Any edits will be overridden! -->

- _(begin)_→:::←blast, explosion, flying debris, and shockwave <!--SR:!2024-03-09,8,243!2024-04-18,44,303-->
- blast, explosion, flying debris, and shockwave→:::←chemical burn <!--SR:!2024-04-06,34,286!2024-04-06,34,306-->
- chemical burn→:::←fire and thermal burn <!--SR:!2024-03-17,12,246!2024-03-26,23,263-->
- fire and thermal burn→:::←poisoning <!--SR:!2024-03-11,7,266!2024-03-16,12,246-->
- poisoning→:::←suffocation <!--SR:!2024-03-11,17,306!2024-03-31,27,286-->
- suffocation→:::←_(end)_ <!--SR:!2024-04-05,30,283!2024-04-19,45,303-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### hydraulic system safety measures

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="cd12"--><!-- The following content is generated at 2024-02-20T13:55:14.042175+08:00. Any edits will be overridden! -->

> 1. design: fix hose strap to restrain the failing motion of dislocated flexible hoses
> 2. design: high flashpoint hydraulic oil
> 3. design: proper construction, design, and materials
> 4. operator: frequent examination for damages
> 5. operator: pressurize in stages
> 6. operator: segregate and indicate work area

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="93fa"--><!-- The following content is generated at 2024-02-20T13:55:14.024176+08:00. Any edits will be overridden! -->

- _(begin)_→:::←design: fix hose strap to restrain the failing motion of dislocated flexible hoses <!--SR:!2024-03-09,12,246!2024-04-19,45,303-->
- design: fix hose strap to restrain the failing motion of dislocated flexible hoses→:::←design: high flashpoint hydraulic oil <!--SR:!2024-03-11,12,226!2024-03-08,11,246-->
- design: high flashpoint hydraulic oil→:::←design: proper construction, design, and materials <!--SR:!2024-03-20,19,266!2024-04-04,32,286-->
- design: proper construction, design, and materials→:::←operator: frequent examination for damages <!--SR:!2024-03-24,21,246!2024-03-13,10,206-->
- operator: frequent examination for damages→:::←operator: pressurize in stages <!--SR:!2024-03-11,10,206!2024-03-12,14,246-->
- operator: pressurize in stages→:::←operator: segregate and indicate work area <!--SR:!2024-03-16,15,226!2024-03-20,20,266-->
- operator: segregate and indicate work area→:::←_(end)_ <!--SR:!2024-03-10,16,306!2024-03-10,9,186-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### pressure vessel examples

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="948b"--><!-- The following content is generated at 2024-02-09T19:56:52.672841+08:00. Any edits will be overridden! -->

> 1. air receiver
> 2. fixed vessel for starting internal combustion engine
> 3. pressured fuel container
> 4. spraying paint container

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="152a"--><!-- The following content is generated at 2024-02-09T19:56:52.689301+08:00. Any edits will be overridden! -->

- _(begin)_→:::←air receiver <!--SR:!2024-03-12,18,306!2024-03-11,17,306-->
- air receiver→:::←fixed vessel for starting internal combustion engine <!--SR:!2024-04-13,38,286!2024-03-13,6,243-->
- fixed vessel for starting internal combustion engine→:::←pressured fuel container <!--SR:!2024-03-11,6,263!2024-04-05,32,286-->
- pressured fuel container→:::←spraying paint container <!--SR:!2024-03-09,15,306!2024-03-23,16,286-->
- spraying paint container→:::←_(end)_ <!--SR:!2024-03-12,18,306!2024-03-29,23,263-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### pressurized fuel container requirements

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="10ab"--><!-- The following content is generated at 2024-02-19T20:13:03.173682+08:00. Any edits will be overridden! -->

> 1. control: accessible valves and safety devices
> 2. control: remote control valve as close to burner as possible
> 3. safety: all piping properly secured save for 0.6 m immediately before the burner
> 4. safety: maximum permissible working pressure not more than 500 kPa
> 5. safety: pressure release valve

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="23fb"--><!-- The following content is generated at 2024-02-19T20:13:03.186373+08:00. Any edits will be overridden! -->

- _(begin)_→:::←control: accessible valves and safety devices <!--SR:!2024-03-23,20,266!2024-03-08,14,303-->
- control: accessible valves and safety devices→:::←control: remote control valve as close to burner as possible <!--SR:!2024-04-15,40,286!2024-04-11,37,286-->
- control: remote control valve as close to burner as possible→:::←safety: all piping properly secured save for 0.6 m immediately before the burner <!--SR:!2024-03-24,23,266!2024-03-16,12,243-->
- safety: all piping properly secured save for 0.6 m immediately before the burner→:::←safety: maximum permissible working pressure not more than 500 kPa <!--SR:!2024-03-08,2,186!2024-03-08,3,206-->
- safety: maximum permissible working pressure not more than 500 kPa→:::←safety: pressure release valve <!--SR:!2024-03-13,15,266!2024-04-08,36,306-->
- safety: pressure release valve→:::←_(end)_ <!--SR:!2024-04-17,43,306!2024-03-16,9,186-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### relevant legislation in Hong Kong

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="78bb"--><!-- The following content is generated at 2024-02-09T19:56:53.153815+08:00. Any edits will be overridden! -->

> 1. Boilers and Pressure Vessels Ordinance (Cap. 56)
> 2. Boilers and Pressure Vessels Regulations (Cap. 56A)
> 3. Boilers and Pressure Vessels (Forms) Order (Cap. 56B)
> 4. Dangerous Goods (General) Regulations (Repealed) (Cap. 295B)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2876"--><!-- The following content is generated at 2024-02-09T19:56:53.136813+08:00. Any edits will be overridden! -->

- _(begin)_→:::←Boilers and Pressure Vessels Ordinance (Cap. 56) <!--SR:!2024-03-28,24,266!2024-03-12,18,303-->
- Boilers and Pressure Vessels Ordinance (Cap. 56)→:::←Boilers and Pressure Vessels Regulations (Cap. 56A) <!--SR:!2024-03-09,15,306!2024-03-09,15,303-->
- Boilers and Pressure Vessels Regulations (Cap. 56A)→:::←Boilers and Pressure Vessels (Forms) Order (Cap. 56B) <!--SR:!2024-03-09,15,303!2024-03-08,14,303-->
- Boilers and Pressure Vessels (Forms) Order (Cap. 56B)→:::←Dangerous Goods (General) Regulations (Repealed) (Cap. 295B) <!--SR:!2024-03-13,8,206!2024-03-28,25,263-->
- Dangerous Goods (General) Regulations (Repealed) (Cap. 295B)→:::←_(end)_ <!--SR:!2024-03-11,17,306!2024-03-21,18,266-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### safety measures

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="eeef"--><!-- The following content is generated at 2024-02-09T19:56:53.064301+08:00. Any edits will be overridden! -->

> 1. air inlet and outlet monitoring
> 2. calibrated pressure gauge
> 3. coolant protection
> 4. explosion protection
> 5. lubricant protection
> 6. safety valve
> 7. thermal protection

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="184a"--><!-- The following content is generated at 2024-02-09T19:56:53.080815+08:00. Any edits will be overridden! -->

- _(begin)_→:::←air inlet and outlet monitoring <!--SR:!2024-03-10,12,266!2024-04-14,42,303-->
- air inlet and outlet monitoring→:::←calibrated pressure gauge <!--SR:!2024-03-17,14,246!2024-03-27,22,266-->
- calibrated pressure gauge→:::←coolant protection <!--SR:!2024-03-09,3,166!2024-03-13,14,266-->
- coolant protection→:::←explosion protection <!--SR:!2024-03-12,6,203!2024-04-15,42,306-->
- explosion protection→:::←lubricant protection <!--SR:!2024-04-16,43,306!2024-04-22,48,306-->
- lubricant protection→:::←safety valve <!--SR:!2024-03-30,24,266!2024-04-16,42,306-->
- safety valve→:::←thermal protection <!--SR:!2024-04-14,41,306!2024-04-13,41,303-->
- thermal protection→:::←_(end)_ <!--SR:!2024-03-11,17,303!2024-03-18,11,226-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

---
aliases:
  - ESST pressure safety outline
  - HKUST ESST pressure safety outline
tags:
  - flashcards/special/academia/HKUST/ESST/pressure_safety/outline
  - languages/in/English
---

# HKUST ESST pressure safety outline

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../../../../../tools/utility.py.md
```

%%

The content is in teaching order.

- [pressure](../../../../../general/pressure.md) _P_ ::: [force](../../../../../general/force.md) applied perpendicular to a surface per unit area
  - [pressure](../../../../../general/pressure.md) [units of measurement](../../../../../general/unit%20of%20measurement.md) ::: [SI unit](../../../../../general/International%20System%20of%20Units.md): [pascal](../../../../../general/pascal%20(unit).md) (Pa), Pa = N/m<sup>2</sup>, 1 bar = 100000 Pa, 1 atm = 101325 Pa
- pressured system ::: One or more [pressure vessels](../../../../../general/pressure%20vessel.md), pipework, and associated protective devices.
  - pressured system classification in [Hong Kong](../../../../../general/Hong%20Kong.md) ::: [boiler](../../../../../general/boiler.md) and [pressure vessel](../../../../../general/pressure%20vessel.md)
    - [boiler examples](#boiler%20examples)
    - [pressure vessel examples](#pressure%20vessel%20examples)
  - an example of a pressured system ::: Several boilers are connected to an air receiver. Each boiler has a control for controlling the flow to the air receiver. The air receiver can be used for many applications.
- hazards
  - [hazard causes](#hazard%20causes)
  - [hazard types](#hazard%20types)
  - [hazard control factors](#hazard%20control%20factors)
- design safety
  - [design safety goals](#design%20safety%20goals)
  - [design safety considerations](#design%20safety%20considerations)
- technical requirements ::: Boilers and Pressure Vessels Regulations 2002 (Cap. 56A)
  - [boiler requirements](#boiler%20requirements)
  - [air or steam receiver requirements](#air%20or%20steam%20receiver%20requirements)
  - [pressurized fuel container requirements](#pressurized%20fuel%20container%20requirements)
  - [auxiliary equipments](#auxiliary%20equipments)
- [safety control measures](#safety%20control%20measures)
  - spring-loaded safety valve ::: Ensures the pressure is below the maximum permissible working pressure. Positioned downstream. Away from inlets to avoid disturbances.
  - calibrated pressure gauge ::: Has red marking indicating the the maximum permissible working pressure. Allows a test device to be fitted.
  - thermal protection ::: Shutdown requires action to be taken first to avoid overheating. Install fusible pressure release plug.
  - coolant protection ::: Shuts down compressors when the water temperature exceeds maximum.
  - lubricant protection ::: Shuts down compressors when the lubricant pressure drops below minimum.
  - air inlet and outlet monitoring ::: A water manometer or pressure-indicating device for each compressor air inlet.
- hydraulic system
  - hydraulic system hazards ::: burns, flailing or ruptured fittings or hoses, pinhole leak injury
  - [hydraulic system safety measures](#hydraulic%20system%20safety%20measures)
  - [combined gas law](../../../../../general/ideal%20gas%20law.md#combined%20gas%20law) ::: _PV_/_T_ = _k_: When volume decreases or temperature increases, pressure increases.
- compressed gas cylinder
  - compressed gas cylinder hazards ::: Pressure can reach over 100 bars. Leaking gas produce a force 20 to 50 times the cylinder weight, which is about 100 kg, similar to a rocket or guided missile. Over-pressurized vessel fail at a weak point if it exists. If that point is very weak, the vessel can fail at or below normal operating pressure.
  - [compressed gas cylinder safety measures](#compressed%20gas%20cylinder%20safety%20measures)
- [relevant legislation in Hong Kong](#relevant%20legislation%20in%20Hong%20Kong)
  - Boilers and Pressure Vessels Ordinance (Cap. 56) ::: Provision of control and operation of boilers and pressure vessels. Ensure standards. Define "appointed examiners" and "competent person". Require Certificate of Fitness and Certificate of Examination.
  - Certificate of Fitness ::: Required for boiler pressure vessel, steam container, and auxiliary equipment, but NOT pressurized fuel container, to be used. Valid for 26 months. Must renew after repair, prohibition order, hired, or sold. The examination process is outlined under hydraulic test.
  - hydraulic test
    - hydraulic test for seamless steel air receivers ::: $\text{test pressure} = \begin{cases} \mathrm{MPWP} + 1.4 \times 10^7 \mathrm{\ Pa} & \text{ if } 1.4 \times 10^7 \mathrm{\ Pa} < \mathrm{MPWP} \le 2.8 \times 10^7 \mathrm{\ Pa} \\ 1.5 \,\mathrm{MPWP} & \text{ if } \mathrm{MPWP} > 2.8 \times 10^7 \mathrm{\ Pa} \end{cases}$.
    - hydraulic test for other air receivers ::: $\text{test pressure} = \begin{cases} 2 \,\mathrm{MPWP} & \text{ if } \mathrm{MPWP} \le 7 \times 10^5 \mathrm{\ Pa} \\ 1.5 \,\mathrm{MPWP} + 3.5 \times 10^5 \mathrm{\ Pa} & \text{ if } \mathrm{MPWP} > 7 \times 10^5 \mathrm{\ Pa} \end{cases}$.
  - Dangerous Goods (General) Regulations (Repealed) (Cap. 295B) ::: Governs pressurized cylinders.
  - pressurized cylinder ::: Governed by Dangerous Goods (General) Regulations (Repealed) (Cap. 295B) instead. Requires hydraulic stretch test and hydraulic pressure test. Valid for 5 years.
  - hydraulic stretch test and hydraulic pressure test ::: For permanent gas, the pressure for hydraulic stretch test is not less than 21 MPa and for hydraulic pressure test is not less than 20 MPa. For liquefied gas, the pressure is not less than 4/3 of the working pressure. The cylinder shall be destroyed if it shows a permanent volumetric expansion of more than 10%, leakage, or deformation under the tests.

## oversized data

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

- _(begin)_→:::←electric heated boiler
- electric heated boiler→:::←electric steam boiler
- electric steam boiler→:::←fire-tube boiler
- fire-tube boiler→:::←fossil fuel boiler
- fossil fuel boiler→:::←thermal oil heater
- thermal oil heater→:::←_(end)_

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

- _(begin)_→:::←air receiver
- air receiver→:::←fixed vessel for starting internal combustion engine
- fixed vessel for starting internal combustion engine→:::←pressured fuel container
- pressured fuel container→:::←spraying paint container
- spraying paint container→:::←_(end)_

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

- _(begin)_→:::←blocked or restricted flow
- blocked or restricted flow→:::←compressor malfunction
- compressor malfunction→:::←external fire
- external fire→:::←failure of automatic controls
- failure of automatic controls→:::←formation and ignition or detonation of carbonaceous deposits
- formation and ignition or detonation of carbonaceous deposits→:::←ignition or detonation of oil or oil vapor
- ignition or detonation of oil or oil vapor→:::←overheating
- overheating→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### hazard types

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
return await memorize_seq(
  __env__.cwf_sects("837b", "937a",),
  """
blast
chemical burn
explosion
fire
flying debris
poisoning
shockwave
suffocation
thermal burn
""".strip().splitlines(),
)
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="837b"--><!-- The following content is generated at 2024-02-09T19:56:52.769306+08:00. Any edits will be overridden! -->

> 1. blast
> 2. chemical burn
> 3. explosion
> 4. fire
> 5. flying debris
> 6. poisoning
> 7. shockwave
> 8. suffocation
> 9. thermal burn

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="937a"--><!-- The following content is generated at 2024-02-09T19:56:52.792818+08:00. Any edits will be overridden! -->

- _(begin)_→:::←blast
- blast→:::←chemical burn
- chemical burn→:::←explosion
- explosion→:::←fire
- fire→:::←flying debris
- flying debris→:::←poisoning
- poisoning→:::←shockwave
- shockwave→:::←suffocation
- suffocation→:::←thermal burn
- thermal burn→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### hazard control factors

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
return await memorize_seq(
  __env__.cwf_sects("aa98", "1192",),
  """
control complexity
equipment age
equipment condition
equipment suitability
fluid type and properties
pressure
prevailing conditions
worker knowledge
worker skills
""".strip().splitlines(),
)
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="aa98"--><!-- The following content is generated at 2024-02-09T19:56:52.829846+08:00. Any edits will be overridden! -->

> 1. control complexity
> 2. equipment age
> 3. equipment condition
> 4. equipment suitability
> 5. fluid type and properties
> 6. pressure
> 7. prevailing conditions
> 8. worker knowledge
> 9. worker skills

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="1192"--><!-- The following content is generated at 2024-02-09T19:56:52.813819+08:00. Any edits will be overridden! -->

- _(begin)_→:::←control complexity
- control complexity→:::←equipment age
- equipment age→:::←equipment condition
- equipment condition→:::←equipment suitability
- equipment suitability→:::←fluid type and properties
- fluid type and properties→:::←pressure
- pressure→:::←prevailing conditions
- prevailing conditions→:::←worker knowledge
- worker knowledge→:::←worker skills
- worker skills→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### design safety goals

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
return await memorize_seq(
  __env__.cwf_sects("038b", "857e",),
  """
examinable
has protective devices
protective devices that release contents do so safely
safely accessible interior
suitable material
""".strip().splitlines(),
)
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="038b"--><!-- The following content is generated at 2024-02-09T19:56:52.853822+08:00. Any edits will be overridden! -->

> 1. examinable
> 2. has protective devices
> 3. protective devices that release contents do so safely
> 4. safely accessible interior
> 5. suitable material

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="857e"--><!-- The following content is generated at 2024-02-09T19:56:52.874126+08:00. Any edits will be overridden! -->

- _(begin)_→:::←examinable
- examinable→:::←has protective devices
- has protective devices→:::←protective devices that release contents do so safely
- protective devices that release contents do so safely→:::←safely accessible interior
- safely accessible interior→:::←suitable material
- suitable material→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### design safety considerations

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
return await memorize_seq(
  __env__.cwf_sects("2929", "dd81",),
  """
expected working life
fluid type and properties
operating limits
valve operating conditions
""".strip().splitlines(),
)
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2929"--><!-- The following content is generated at 2024-02-09T19:56:52.911757+08:00. Any edits will be overridden! -->

> 1. expected working life
> 2. fluid type and properties
> 3. operating limits
> 4. valve operating conditions

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="dd81"--><!-- The following content is generated at 2024-02-09T19:56:52.892630+08:00. Any edits will be overridden! -->

- _(begin)_→:::←expected working life
- expected working life→:::←fluid type and properties
- fluid type and properties→:::←operating limits
- operating limits→:::←valve operating conditions
- valve operating conditions→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### boiler requirements

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
return await memorize_seq(
  __env__.cwf_sects("96ff", "3e9a",),
  """
fusible pressure release plug or efficient low-water alarm
marked with a distinguishing number
pressure gauge with red marking showing the maximum permissible working pressure
spring-loaded safety valve and a separate stop-valve for controlling the maximum permissible working pressure
transparent water level gauge
""".strip().splitlines(),
)
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="96ff"--><!-- The following content is generated at 2024-02-09T19:56:52.929757+08:00. Any edits will be overridden! -->

> 1. fusible pressure release plug or efficient low-water alarm
> 2. marked with a distinguishing number
> 3. pressure gauge with red marking showing the maximum permissible working pressure
> 4. spring-loaded safety valve and a separate stop-valve for controlling the maximum permissible working pressure
> 5. transparent water level gauge

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3e9a"--><!-- The following content is generated at 2024-02-09T19:56:52.944756+08:00. Any edits will be overridden! -->

- _(begin)_→:::←fusible pressure release plug or efficient low-water alarm
- fusible pressure release plug or efficient low-water alarm→:::←marked with a distinguishing number
- marked with a distinguishing number→:::←pressure gauge with red marking showing the maximum permissible working pressure
- pressure gauge with red marking showing the maximum permissible working pressure→:::←spring-loaded safety valve and a separate stop-valve for controlling the maximum permissible working pressure
- spring-loaded safety valve and a separate stop-valve for controlling the maximum permissible working pressure→:::←transparent water level gauge
- transparent water level gauge→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### air or steam receiver requirements

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
return await memorize_seq(
  __env__.cwf_sects("29a2", "3842",),
  """
automatic mechanism like reducing valve to prevent over-pressurizing
marked with a distinguishing number
pressure gauge with red marking showing the maximum permissible working pressure
spring-loaded safety valve for controlling the maximum permissible working pressure
withstand the maximum permissible working pressure
""".strip().splitlines(),
)
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="29a2"--><!-- The following content is generated at 2024-02-09T19:56:52.979288+08:00. Any edits will be overridden! -->

> 1. automatic mechanism like reducing valve to prevent over-pressurizing
> 2. marked with a distinguishing number
> 3. pressure gauge with red marking showing the maximum permissible working pressure
> 4. spring-loaded safety valve for controlling the maximum permissible working pressure
> 5. withstand the maximum permissible working pressure

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3842"--><!-- The following content is generated at 2024-02-09T19:56:52.962765+08:00. Any edits will be overridden! -->

- _(begin)_→:::←automatic mechanism like reducing valve to prevent over-pressurizing
- automatic mechanism like reducing valve to prevent over-pressurizing→:::←marked with a distinguishing number
- marked with a distinguishing number→:::←pressure gauge with red marking showing the maximum permissible working pressure
- pressure gauge with red marking showing the maximum permissible working pressure→:::←spring-loaded safety valve for controlling the maximum permissible working pressure
- spring-loaded safety valve for controlling the maximum permissible working pressure→:::←withstand the maximum permissible working pressure
- withstand the maximum permissible working pressure→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### pressurized fuel container requirements

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
return await memorize_seq(
  __env__.cwf_sects("10ab", "23fb",),
  """
accessible valves and safety devices
all piping properly secured save for 0.6 m immediately before the burner
maximum permissible working pressure not more than 500 kPa
pressure release valve
remote control valve as close to burner as possible
""".strip().splitlines(),
)
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="10ab"--><!-- The following content is generated at 2024-02-09T19:56:53.014286+08:00. Any edits will be overridden! -->

> 1. accessible valves and safety devices
> 2. all piping properly secured save for 0.6 m immediately before the burner
> 3. maximum permissible working pressure not more than 500 kPa
> 4. pressure release valve
> 5. remote control valve as close to burner as possible

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="23fb"--><!-- The following content is generated at 2024-02-09T19:56:52.996287+08:00. Any edits will be overridden! -->

- _(begin)_→:::←accessible valves and safety devices
- accessible valves and safety devices→:::←all piping properly secured save for 0.6 m immediately before the burner
- all piping properly secured save for 0.6 m immediately before the burner→:::←maximum permissible working pressure not more than 500 kPa
- maximum permissible working pressure not more than 500 kPa→:::←pressure release valve
- pressure release valve→:::←remote control valve as close to burner as possible
- remote control valve as close to burner as possible→:::←_(end)_

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

- _(begin)_→:::←flue damper
- flue damper→:::←fuel pump
- fuel pump→:::←heater
- heater→:::←multiple burner
- multiple burner→:::←pipe
- pipe→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### safety control measures

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

- _(begin)_→:::←air inlet and outlet monitoring
- air inlet and outlet monitoring→:::←calibrated pressure gauge
- calibrated pressure gauge→:::←coolant protection
- coolant protection→:::←explosion protection
- explosion protection→:::←lubricant protection
- lubricant protection→:::←safety valve
- safety valve→:::←thermal protection
- thermal protection→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### hydraulic system safety measures

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
return await memorize_seq(
  __env__.cwf_sects("cd12", "93fa",),
  """
fix hose strap to restrain the failing motion of flexible hoses when dislocated
frequent examination for damages
high flashpoint hydraulic oil
pressurize in stages
proper construction
proper design
proper material
segregate and indicate work area
""".strip().splitlines(),
)
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="cd12"--><!-- The following content is generated at 2024-02-09T19:56:53.096835+08:00. Any edits will be overridden! -->

> 1. fix hose strap to restrain the failing motion of flexible hoses when dislocated
> 2. frequent examination for damages
> 3. high flashpoint hydraulic oil
> 4. pressurize in stages
> 5. proper construction
> 6. proper design
> 7. proper material
> 8. segregate and indicate work area

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="93fa"--><!-- The following content is generated at 2024-02-09T19:56:53.106816+08:00. Any edits will be overridden! -->

- _(begin)_→:::←fix hose strap to restrain the failing motion of flexible hoses when dislocated
- fix hose strap to restrain the failing motion of flexible hoses when dislocated→:::←frequent examination for damages
- frequent examination for damages→:::←high flashpoint hydraulic oil
- high flashpoint hydraulic oil→:::←pressurize in stages
- pressurize in stages→:::←proper construction
- proper construction→:::←proper design
- proper design→:::←proper material
- proper material→:::←segregate and indicate work area
- segregate and indicate work area→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### compressed gas cylinder safety measures

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
return await memorize_seq(
  __env__.cwf_sects("9012", "33bb",),
  """
close inactive valves
correct fittings and regulators
empty cylinders are marked empty
flashback arrestor when a flammable or oxidizing gas is used or otherwise the cylinder gas ignites
frequent inspection, keep upright
no electric arcs or heat sources nearby
no oily or greasy substances or otherwise explosion
""".strip().splitlines(),
)
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="9012"--><!-- The following content is generated at 2024-02-09T19:56:53.126839+08:00. Any edits will be overridden! -->

> 1. close inactive valves
> 2. correct fittings and regulators
> 3. empty cylinders are marked empty
> 4. flashback arrestor when a flammable or oxidizing gas is used or otherwise the cylinder gas ignites
> 5. frequent inspection, keep upright
> 6. no electric arcs or heat sources nearby
> 7. no oily or greasy substances or otherwise explosion

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="33bb"--><!-- The following content is generated at 2024-02-09T19:56:53.116815+08:00. Any edits will be overridden! -->

- _(begin)_→:::←close inactive valves
- close inactive valves→:::←correct fittings and regulators
- correct fittings and regulators→:::←empty cylinders are marked empty
- empty cylinders are marked empty→:::←flashback arrestor when a flammable or oxidizing gas is used or otherwise the cylinder gas ignites
- flashback arrestor when a flammable or oxidizing gas is used or otherwise the cylinder gas ignites→:::←frequent inspection, keep upright
- frequent inspection, keep upright→:::←no electric arcs or heat sources nearby
- no electric arcs or heat sources nearby→:::←no oily or greasy substances or otherwise explosion
- no oily or greasy substances or otherwise explosion→:::←_(end)_

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

- _(begin)_→:::←Boilers and Pressure Vessels Ordinance (Cap. 56)
- Boilers and Pressure Vessels Ordinance (Cap. 56)→:::←Boilers and Pressure Vessels Regulations (Cap. 56A)
- Boilers and Pressure Vessels Regulations (Cap. 56A)→:::←Boilers and Pressure Vessels (Forms) Order (Cap. 56B)
- Boilers and Pressure Vessels (Forms) Order (Cap. 56B)→:::←Dangerous Goods (General) Regulations (Repealed) (Cap. 295B)
- Dangerous Goods (General) Regulations (Repealed) (Cap. 295B)→:::←_(end)_

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

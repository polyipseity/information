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

- [pressure](../../../../../general/pressure.md) _P_ ::: [force](../../../../../general/force.md) applied perpendicular to a surface per unit area <!--SR:!2024-02-23,4,282!2024-02-23,4,277-->
  - [pressure](../../../../../general/pressure.md) [units of measurement](../../../../../general/unit%20of%20measurement.md) ::: [SI unit](../../../../../general/International%20System%20of%20Units.md): [pascal](../../../../../general/pascal%20(unit).md) (Pa), Pa = N/m<sup>2</sup>, 1 bar = 100000 Pa, 1 atm = 101325 Pa <!--SR:!2024-02-23,4,277!2024-02-23,4,286-->
- pressured system ::: One or more [pressure vessels](../../../../../general/pressure%20vessel.md), pipework, and associated protective devices. <!--SR:!2024-02-22,3,266!2024-02-23,4,277-->
  - pressured system classification in [Hong Kong](../../../../../general/Hong%20Kong.md) ::: [boiler](../../../../../general/boiler.md) and [pressure vessel](../../../../../general/pressure%20vessel.md) <!--SR:!2024-02-23,4,283!2024-02-23,4,286-->
    - [boiler examples](#boiler%20examples)
    - [pressure vessel examples](#pressure%20vessel%20examples)
  - an example of a pressured system ::: Several boilers are connected to an air receiver. Each boiler has a control for controlling the flow to the air receiver. The air receiver can be used for many applications. <!--SR:!2024-02-23,4,286!2024-02-23,4,286-->
- hazards
  - [hazard causes](#hazard%20causes)
  - [hazard types](#hazard%20types)
  - [hazard control factors](#hazard%20control%20factors)
- design safety
  - [design safety goals](#design%20safety%20goals)
  - [design safety considerations](#design%20safety%20considerations)
- technical requirements ::: Boilers and Pressure Vessels Regulations 2002 (Cap. 56A) <!--SR:!2024-02-22,3,266!2024-02-22,3,263-->
  - [boiler requirements](#boiler%20requirements)
  - [air or steam receiver requirements](#air%20or%20steam%20receiver%20requirements)
  - [pressurized fuel container requirements](#pressurized%20fuel%20container%20requirements)
  - [auxiliary equipments](#auxiliary%20equipments)
- [safety control measures](#safety%20control%20measures)
  - spring-loaded safety valve ::: Ensures the pressure is below the maximum permissible working pressure. Positioned downstream. Away from inlets to avoid disturbances. <!--SR:!2024-02-22,3,266!2024-02-22,3,263-->
  - calibrated pressure gauge ::: Has red marking indicating the the maximum permissible working pressure. Allows a test device to be fitted. <!--SR:!2024-02-23,4,277!2024-02-23,4,286-->
  - thermal protection ::: Shutdown requires action to be taken first to avoid overheating. Install fusible pressure release plug. <!--SR:!2024-02-20,1,246!2024-02-23,4,286-->
  - coolant protection ::: Shuts down compressors when the water temperature exceeds maximum. <!--SR:!2024-02-22,3,266!2024-02-20,1,246-->
  - lubricant protection ::: Shuts down compressors when the lubricant pressure drops below minimum. <!--SR:!2024-02-23,4,286!2024-02-23,4,277-->
  - air inlet and outlet monitoring ::: A water manometer or pressure-indicating device for each compressor air inlet. <!--SR:!2024-02-22,3,263!2024-02-22,3,263-->
- hydraulic system
  - hydraulic system hazards ::: burns, flailing or ruptured fittings or hoses, pinhole leak injury <!--SR:!2024-02-22,3,263!2024-02-23,4,283-->
  - [hydraulic system safety measures](#hydraulic%20system%20safety%20measures)
  - [combined gas law](../../../../../general/ideal%20gas%20law.md#combined%20gas%20law) ::: _PV_/_T_ = _k_: When volume decreases or temperature increases, pressure increases. <!--SR:!2024-02-23,4,283!2024-02-23,4,283-->
- compressed gas cylinder
  - compressed gas cylinder hazards ::: Pressure can reach over 100 bars. Leaking gas produce a force 20 to 50 times the cylinder weight, which is about 100 kg, similar to a rocket or guided missile. Over-pressurized vessel fail at a weak point if it exists. If that point is very weak, the vessel can fail at or below normal operating pressure. <!--SR:!2024-02-20,1,246!2024-02-22,3,263-->
  - [compressed gas cylinder safety measures](#compressed%20gas%20cylinder%20safety%20measures)
- [relevant legislation in Hong Kong](#relevant%20legislation%20in%20Hong%20Kong)
  - Boilers and Pressure Vessels Ordinance (Cap. 56) ::: Provision of control and operation of boilers and pressure vessels. Ensures standards. Defines _appointed examiners_ and _competent person_. Requires certificate of fitness and certificate of examination. <!--SR:!2024-02-20,1,246!2024-02-22,3,266-->
  - certificate of fitness ::: Required for boiler pressure vessel, steam container, and auxiliary equipment, but NOT pressurized fuel container, to be used. Valid for 26 months. Must renew after repair, prohibition order, hired, or sold. The examination process is outlined under hydraulic test. <!--SR:!2024-02-22,3,266!2024-02-20,1,243-->
  - hydraulic test
    - hydraulic test for seamless steel air receivers ::: $\text{test pressure} = \begin{cases} \mathrm{MPWP} + 1.4 \times 10^7 \mathrm{\ Pa} & \text{ if } 1.4 \times 10^7 \mathrm{\ Pa} < \mathrm{MPWP} \le 2.8 \times 10^7 \mathrm{\ Pa} \\ 1.5 \,\mathrm{MPWP} & \text{ if } \mathrm{MPWP} > 2.8 \times 10^7 \mathrm{\ Pa} \end{cases}$. <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
    - hydraulic test for other air receivers ::: $\text{test pressure} = \begin{cases} 2 \,\mathrm{MPWP} & \text{ if } \mathrm{MPWP} \le 7 \times 10^5 \mathrm{\ Pa} \\ 1.5 \,\mathrm{MPWP} + 3.5 \times 10^5 \mathrm{\ Pa} & \text{ if } \mathrm{MPWP} > 7 \times 10^5 \mathrm{\ Pa} \end{cases}$. <!--SR:!2024-02-20,1,243!2024-02-22,3,263-->
  - Dangerous Goods (General) Regulations (Repealed) (Cap. 295B) ::: Governs pressurized cylinders. <!--SR:!2024-02-22,3,263!2024-02-22,3,263-->
- pressurized cylinder ::: Governed by Dangerous Goods (General) Regulations (Repealed) (Cap. 295B) instead. Requires hydraulic stretch test and hydraulic pressure test. Valid for 5 years. <!--SR:!2024-02-22,3,263!2024-03-01,12,270-->
  - hydraulic stretch test and hydraulic pressure test ::: For permanent gas, the pressure for hydraulic stretch test is not less than 21 MPa and for hydraulic pressure test is not less than 20 MPa. For liquefied gas, the pressure is not less than 4/3 of the working pressure. The cylinder shall be destroyed if it shows a permanent volumetric expansion of more than 10%, leakage, or deformation under the tests. <!--SR:!2024-02-20,1,246!2024-02-22,3,257-->

## oversized data

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

- _(begin)_→:::←automatic mechanism like reducing valve to prevent over-pressurizing <!--SR:!2024-02-20,1,246!2024-02-22,3,266-->
- automatic mechanism like reducing valve to prevent over-pressurizing→:::←marked with a distinguishing number <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- marked with a distinguishing number→:::←pressure gauge with red marking showing the maximum permissible working pressure <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- pressure gauge with red marking showing the maximum permissible working pressure→:::←spring-loaded safety valve for controlling the maximum permissible working pressure <!--SR:!2024-02-20,1,246!2024-02-22,3,266-->
- spring-loaded safety valve for controlling the maximum permissible working pressure→:::←withstand the maximum permissible working pressure <!--SR:!2024-02-20,1,246!2024-02-20,1,243-->
- withstand the maximum permissible working pressure→:::←_(end)_ <!--SR:!2024-02-22,3,263!2024-02-22,3,266-->

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

- _(begin)_→:::←flue damper <!--SR:!2024-02-22,3,266!2024-02-23,4,286-->
- flue damper→:::←fuel pump <!--SR:!2024-02-22,3,263!2024-02-22,3,266-->
- fuel pump→:::←heater <!--SR:!2024-02-22,3,266!2024-02-20,1,246-->
- heater→:::←multiple burner <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- multiple burner→:::←pipe <!--SR:!2024-02-22,3,266!2024-02-20,1,246-->
- pipe→:::←_(end)_ <!--SR:!2024-02-22,3,263!2024-02-22,3,266-->

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

- _(begin)_→:::←electric heated boiler <!--SR:!2024-02-22,3,263!2024-02-22,3,266-->
- electric heated boiler→:::←electric steam boiler <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- electric steam boiler→:::←fire-tube boiler <!--SR:!2024-02-22,3,263!2024-02-22,3,266-->
- fire-tube boiler→:::←fossil fuel boiler <!--SR:!2024-02-20,1,243!2024-02-22,3,266-->
- fossil fuel boiler→:::←thermal oil heater <!--SR:!2024-02-22,3,266!2024-02-20,1,246-->
- thermal oil heater→:::←_(end)_ <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->

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

- _(begin)_→:::←fusible pressure release plug or efficient low-water alarm <!--SR:!2024-02-20,1,246!2024-02-23,4,286-->
- fusible pressure release plug or efficient low-water alarm→:::←marked with a distinguishing number <!--SR:!2024-02-20,1,246!2024-02-22,3,266-->
- marked with a distinguishing number→:::←pressure gauge with red marking showing the maximum permissible working pressure
- pressure gauge with red marking showing the maximum permissible working pressure→:::←spring-loaded safety valve and a separate stop-valve for controlling the maximum permissible working pressure <!--SR:!2024-02-20,1,243!2024-02-22,3,266-->
- spring-loaded safety valve and a separate stop-valve for controlling the maximum permissible working pressure→:::←transparent water level gauge <!--SR:!2024-02-20,1,243!2024-02-22,3,266-->
- transparent water level gauge→:::←_(end)_ <!--SR:!2024-02-23,4,286!2024-02-22,3,266-->

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

- _(begin)_→:::←close inactive valves <!--SR:!2024-02-20,1,246!2024-02-23,4,283-->
- close inactive valves→:::←correct fittings and regulators <!--SR:!2024-02-20,1,246!2024-02-20,1,246-->
- correct fittings and regulators→:::←empty cylinders are marked empty <!--SR:!2024-02-20,1,246!2024-02-22,3,266-->
- empty cylinders are marked empty→:::←flashback arrestor when a flammable or oxidizing gas is used or otherwise the cylinder gas ignites <!--SR:!2024-02-20,1,246!2024-02-22,3,266-->
- flashback arrestor when a flammable or oxidizing gas is used or otherwise the cylinder gas ignites→:::←frequent inspection, keep upright <!--SR:!2024-02-22,3,266!2024-02-20,1,246-->
- frequent inspection, keep upright→:::←no electric arcs or heat sources nearby <!--SR:!2024-02-20,1,243!2024-02-20,1,246-->
- no electric arcs or heat sources nearby→:::←no oily or greasy substances or otherwise explosion <!--SR:!2024-02-23,4,286!2024-02-23,4,283-->
- no oily or greasy substances or otherwise explosion→:::←_(end)_ <!--SR:!2024-02-23,4,286!2024-02-20,1,246-->

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

- _(begin)_→:::←expected working life <!--SR:!2024-02-22,3,266!2024-02-23,4,283-->
- expected working life→:::←fluid type and properties <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- fluid type and properties→:::←operating limits <!--SR:!2024-02-20,1,246!2024-02-22,3,266-->
- operating limits→:::←valve operating conditions <!--SR:!2024-02-22,3,266!2024-02-22,3,263-->
- valve operating conditions→:::←_(end)_ <!--SR:!2024-02-22,3,263!2024-02-20,1,246-->

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

- _(begin)_→:::←examinable <!--SR:!2024-02-22,3,266!2024-02-22,3,263-->
- examinable→:::←has protective devices <!--SR:!2024-02-20,1,246!2024-02-23,4,286-->
- has protective devices→:::←protective devices that release contents do so safely <!--SR:!2024-02-23,4,286!2024-02-23,4,283-->
- protective devices that release contents do so safely→:::←safely accessible interior <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- safely accessible interior→:::←suitable material <!--SR:!2024-02-22,3,266!2024-02-20,1,246-->
- suitable material→:::←_(end)_ <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->

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

- _(begin)_→:::←blocked or restricted flow <!--SR:!2024-02-22,3,266!2024-02-23,4,283-->
- blocked or restricted flow→:::←compressor malfunction <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- compressor malfunction→:::←external fire <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- external fire→:::←failure of automatic controls <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- failure of automatic controls→:::←formation and ignition or detonation of carbonaceous deposits <!--SR:!2024-02-20,1,246!2024-02-22,3,263-->
- formation and ignition or detonation of carbonaceous deposits→:::←ignition or detonation of oil or oil vapor <!--SR:!2024-02-22,3,263!2024-02-20,1,243-->
- ignition or detonation of oil or oil vapor→:::←overheating <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- overheating→:::←_(end)_ <!--SR:!2024-02-23,4,286!2024-02-22,3,266-->

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

- _(begin)_→:::←control complexity <!--SR:!2024-02-22,3,266!2024-03-06,16,290-->
- control complexity→:::←equipment age <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- equipment age→:::←equipment condition <!--SR:!2024-02-22,3,266!2024-02-23,4,286-->
- equipment condition→:::←equipment suitability <!--SR:!2024-02-22,3,263!2024-02-22,3,266-->
- equipment suitability→:::←fluid type and properties <!--SR:!2024-02-20,1,246!2024-02-20,1,246-->
- fluid type and properties→:::←pressure <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- pressure→:::←prevailing conditions <!--SR:!2024-02-20,1,246!2024-02-22,3,266-->
- prevailing conditions→:::←worker knowledge <!--SR:!2024-02-20,1,246!2024-02-20,1,246-->
- worker knowledge→:::←worker skills <!--SR:!2024-02-23,4,286!2024-02-22,3,266-->
- worker skills→:::←_(end)_ <!--SR:!2024-02-23,4,283!2024-02-22,3,263-->

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

- _(begin)_→:::←blast <!--SR:!2024-02-20,1,243!2024-02-22,3,263-->
- blast→:::←chemical burn <!--SR:!2024-02-22,3,266!2024-02-23,4,286-->
- chemical burn→:::←explosion <!--SR:!2024-02-23,4,283!2024-02-22,3,266-->
- explosion→:::←fire <!--SR:!2024-02-22,3,266!2024-02-22,3,263-->
- fire→:::←flying debris <!--SR:!2024-02-22,3,263!2024-02-22,3,266-->
- flying debris→:::←poisoning <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- poisoning→:::←shockwave <!--SR:!2024-02-22,3,266!2024-02-20,1,246-->
- shockwave→:::←suffocation <!--SR:!2024-02-23,4,286!2024-02-20,1,246-->
- suffocation→:::←thermal burn <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- thermal burn→:::←_(end)_ <!--SR:!2024-02-22,3,263!2024-02-22,3,263-->

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

- _(begin)_→:::←fix hose strap to restrain the failing motion of flexible hoses when dislocated <!--SR:!2024-02-20,1,246!2024-02-22,3,263-->
- fix hose strap to restrain the failing motion of flexible hoses when dislocated→:::←frequent examination for damages <!--SR:!2024-02-20,1,246!2024-02-20,1,246-->
- frequent examination for damages→:::←high flashpoint hydraulic oil <!--SR:!2024-02-20,1,246!2024-02-20,1,246-->
- high flashpoint hydraulic oil→:::←pressurize in stages <!--SR:!2024-02-20,1,246!2024-02-20,1,246-->
- pressurize in stages→:::←proper construction <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- proper construction→:::←proper design <!--SR:!2024-02-22,3,263!2024-02-22,3,263-->
- proper design→:::←proper material <!--SR:!2024-02-23,4,286!2024-02-22,3,266-->
- proper material→:::←segregate and indicate work area <!--SR:!2024-02-20,1,246!2024-02-22,3,266-->
- segregate and indicate work area→:::←_(end)_ <!--SR:!2024-02-23,4,286!2024-02-20,1,246-->

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

- _(begin)_→:::←air receiver <!--SR:!2024-02-23,4,286!2024-02-23,4,286-->
- air receiver→:::←fixed vessel for starting internal combustion engine <!--SR:!2024-02-22,3,266!2024-02-22,3,263-->
- fixed vessel for starting internal combustion engine→:::←pressured fuel container <!--SR:!2024-02-22,3,263!2024-02-22,3,266-->
- pressured fuel container→:::←spraying paint container <!--SR:!2024-02-23,4,286!2024-02-22,3,266-->
- spraying paint container→:::←_(end)_ <!--SR:!2024-02-23,4,286!2024-02-22,3,263-->

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

- _(begin)_→:::←accessible valves and safety devices <!--SR:!2024-02-20,1,246!2024-02-23,4,283-->
- accessible valves and safety devices→:::←all piping properly secured save for 0.6 m immediately before the burner <!--SR:!2024-02-22,3,266!2024-02-22,3,263-->
- all piping properly secured save for 0.6 m immediately before the burner→:::←maximum permissible working pressure not more than 500 kPa <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- maximum permissible working pressure not more than 500 kPa→:::←pressure release valve <!--SR:!2024-02-20,1,246!2024-02-22,3,266-->
- pressure release valve→:::←remote control valve as close to burner as possible <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- remote control valve as close to burner as possible→:::←_(end)_ <!--SR:!2024-02-23,4,286!2024-02-20,1,246-->

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

- _(begin)_→:::←Boilers and Pressure Vessels Ordinance (Cap. 56) <!--SR:!2024-02-20,1,246!2024-02-23,4,283-->
- Boilers and Pressure Vessels Ordinance (Cap. 56)→:::←Boilers and Pressure Vessels Regulations (Cap. 56A) <!--SR:!2024-02-23,4,286!2024-02-23,4,283-->
- Boilers and Pressure Vessels Regulations (Cap. 56A)→:::←Boilers and Pressure Vessels (Forms) Order (Cap. 56B) <!--SR:!2024-02-23,4,283!2024-02-23,4,283-->
- Boilers and Pressure Vessels (Forms) Order (Cap. 56B)→:::←Dangerous Goods (General) Regulations (Repealed) (Cap. 295B) <!--SR:!2024-02-22,3,266!2024-02-22,3,263-->
- Dangerous Goods (General) Regulations (Repealed) (Cap. 295B)→:::←_(end)_ <!--SR:!2024-02-23,4,286!2024-02-22,3,266-->

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

- _(begin)_→:::←air inlet and outlet monitoring <!--SR:!2024-02-20,1,246!2024-02-22,3,263-->
- air inlet and outlet monitoring→:::←calibrated pressure gauge <!--SR:!2024-02-20,1,246!2024-02-20,1,246-->
- calibrated pressure gauge→:::←coolant protection <!--SR:!2024-02-20,1,246!2024-02-20,1,246-->
- coolant protection→:::←explosion protection <!--SR:!2024-02-20,1,243!2024-02-22,3,266-->
- explosion protection→:::←lubricant protection <!--SR:!2024-02-22,3,266!2024-02-22,3,266-->
- lubricant protection→:::←safety valve <!--SR:!2024-02-20,1,246!2024-02-20,1,246-->
- safety valve→:::←thermal protection <!--SR:!2024-02-22,3,266!2024-02-22,3,263-->
- thermal protection→:::←_(end)_ <!--SR:!2024-02-23,4,283!2024-02-20,1,246-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

---
aliases:
  - ESST electrical safety index
  - HKUST ESST electrical safety index
tags:
  - flashcard/archive/special/academia/HKUST/ESST/electrical_safety
  - function/index
  - language/in/English
---

# index

- HKUST ESST electrical safety

```Python
# pytextgen generate module
# import ../../../../../../tools/utility.py.md
```

The content is in teaching order.

- [Ohm's law](../../../../../general/Ohm's%20law.md) ::@:: _V_ = _IR_
- [electric current](../../../../../general/electric%20current.md) types ::@:: [alternating current](../../../../../general/alternating%20current.md) (AC), [direct current](../../../../../general/direct%20current.md) (DC)
  - [alternating current](../../../../../general/alternating%20current.md) (AC) ::@:: [electric current](../../../../../general/electric%20current.md) that periodically reverses direction and varies its magnitude continuously
  - [direct current](../../../../../general/direct%20current.md) (DC) ::@:: [electric current](../../../../../general/electric%20current.md) that flows in one direction only
- [units of measurement](../../../../../general/unit%20of%20measurement.md)
  - [current](../../../../../general/electric%20current.md) _I_ ::@:: [ampere](../../../../../general/ampere.md) A
  - [resistance](../../../../../general/electrical%20resistance%20and%20conductance.md) _R_ (DC) or [impedance](../../../../../general/electrical%20impedance.md) _Z_ (AC) ::@:: [ohm](../../../../../general/ohm.md) Ω
  - [voltage](../../../../../general/voltage.md) _V_ ::@:: [volt](../../../../../general/volt.md) V
- [voltage](../../../../../general/voltage.md) classification ::@:: [extra-low voltage](../../../../../general/extra-low%20voltage.md), [low voltage](../../../../../general/low%20voltage.md), [high voltage](../../../../../general/high%20voltage.md)
  - [extra-low voltage](../../../../../general/extra-low%20voltage.md) ::@:: defining risk: low; [BS 7671](../../../../../general/BS%207671.md): AC [RMS](../../../../../general/root%20mean%20square.md): <= 50 V, DC: <= 120 V ignoring [ripple](ripple%20(electrical).md)
  - [low voltage](../../../../../general/low%20voltage.md) ::@:: defining risk: [electrical shock](../../../../../general/electrical%20injury.md); [BS 7671](../../../../../general/BS%207671.md): AC [RMS](../../../../../general/root%20mean%20square.md): > 50 V, <= 1000 V, <= 600 V between conductors and earth, DC: > 120 V ignoring [ripple](ripple%20(electrical).md), <= 1500 V, <= 900 V between conductors and earth
  - [high voltage](../../../../../general/high%20voltage.md) ::@:: defining risk: [electrical arcing](../../../../../general/electric%20arc.md); [BS 7671](../../../../../general/BS%207671.md): AC [RMS](../../../../../general/root%20mean%20square.md): > 1000 V, > 600 V between conductors and earth, DC: > 1500 V, > 900 V between conductors and earth
- examples of effects of [current](../../../../../general/electric%20current.md)
  - 1 mA :@: barely perceptible
  - 16 mA :@: let go threshold, i.e. maximum current a person can still control the muscle to stop touching the electricity source
  - 20 mA :@: respiratory paralysis
  - 100 mA :@: [ventricular fibrillation](../../../../../general/ventricular%20fibrillation.md)
  - 2 A :@: [cardiac arrest](../../../../../general/cardiac%20arrest.md) and internal [organ](../../../../../general/organ%20(biology).md) damage
  - 15 A, 20 A :@: common [fuse](fuse%20(electrical).md) or [circuit breaker](../../../../../general/circuit%20breaker.md) triggers
- electrical hazards ::@:: [electric arc](../../../../../general/electric%20arc.md), [electrical injury](../../../../../general/electrical%20injury.md), [explosion](../../../../../general/explosion.md), [fire](../../../../../general/fire.md)
  - [electric arc](../../../../../general/electric%20arc.md) ::@:: Electric arcs can go through air to a person. They can also vaporize materials and produce extremely loud noises. These can cause non-contact burns. Emitted [infrared](../../../../../general/infrared.md) and [ultraviolet](../../../../../general/ultraviolete.md) radiation can cause eye damage.
  - [electrical injury](../../../../../general/electrical%20injury.md) ::@:: Electricity can interfere with normal electrical signals in the body. Involuntary muscle contraction can cause falls. Electricity can also cause contact burns, damaging internal organs.
  - [explosion](../../../../../general/explosion.md) ::@:: Electricity can detonate.
  - [fire](../../../../../general/fire.md) ::@:: Electricity can ignite.
- [hazardous scenarios](#hazardous%20scenarios)
- [hazard causes](#hazard%20causes)
- [hazard control](#hazard%20control)
  - [grounding](../../../../../general/ground%20(electricity).md) ::@:: Connect dead parts to the earth so that said dead part has zero potential during a fault. [EMSD](../../../../../general/Electrical%20and%20Mechanical%20Services%20Department.md): Z<sub>2</sub> <= 50 Z<sub>S</sub>/U<sub>O</sub> Ω, where Z<sub>S</sub> is the sum of live wire [impedance](../../../../../general/electrical%20impedance.md) Z<sub>1</sub>, ground wire [impedance](../../../../../general/electrical%20impedance.md) Z<sub>2</sub>, and ground [impedance](../../../../../general/electrical%20impedance.md) Z<sub>e</sub>, and U<sub>O</sub> is the source [voltage](../../../../../general/voltage.md), [diameter](../../../../../general/diameter.md) >= 12.5 mm
  - protective bonding ::@:: Connect several conductive parts to ensure the parts have the same potential so that they do not conduct current during a fault. May be used with [grounding](../../../../../general/ground%20(electrical).md).
  - [circuit breaker](../../../../../general/circult%20breaker.md) ::@:: [miniature circuit breaker](../../../../../general/circuit%20breaker.md) (MCB), [residual-current circuit breaker with over-current protection/ground-fault circuit interrupter](../../../../../general/residual-current%20device.md) (RCBO/GFCI), [residual-current device](../../../../../general/residual-current%20device.md) (RCD)
    - [residual-current device](../../../../../general/residual-current%20device.md) (RCD) ::@:: Breaks a circuit when it detects leakage current to [ground](../../../../../general/ground%20(electricity).md).
    - [miniature circuit breaker](../../../../../general/circuit%20breaker.md) (MCB) ::@:: A resettable [fuse](../../../../../general/fuse%20(electrical).md). Breaks a circuit when it detects overload.
    - [residual-current circuit breaker with over-current protection/ground-fault circuit interrupter](../../../../../general/residual-current%20device.md) (RCBO/GFCI) ::@:: A combination of RCD and MCB.
  - [center tap](../../../../../general/center%20tap.md) ::@:: Used if one wants to provide two separate secondary voltage sources half of the original voltage. Make a contact halfway along a winding of a [transformer](../../../../../general/transformer.md) and ground it. Then the voltage of both wires in contact with the end of the winding is only half the potential difference of the entire winding. The voltages in the two wires are 180 degree out-of-phase of each other (or negative voltage in one of the wire). This can be used to provide extra-low voltage by reducing voltage from 220 V to 110 V, and then use a center tap to split it to two 55 V sources.
  - [double insulation](../../../../../general/appliance%20classes.md#Class%20II) ::@:: Indicated by the double insulation symbol: ⧈ (a square inside another square). No single failure can cause dangerous voltage to be exposed as to cause [electric shock](../../../../../general/electrical%20injury.md), all without the use of an earthed metal casing. Usually this is done by adding supplementary insulation on top of the basic insulation. Earthing is unnecessary in this case as any fault causes a fault current too low to trigger a [fuse](../../../../../general/fuse%20(electrical).md), because of the high-[impedance](../../../../../general/electrical%20impedance.md) casing.
  - compliance with cable standards ::@:: [BS 1363](../../../../../general/BS%201363.md): Live (L) wire is brown, has a [fuse](../../../../../general/fuse%20(electrical).md), and on the right side of the plug when viewed from the plug cover. Neutral (N) wire is blue, and on the left side of the plug when viewed from the plug cover. Earth wire is green and yellow, and on the top side of the plug.
  - [intrinsic safety](../../../../../general/intrinsic%20safety.md) ::@:: Applicable for devices operating on low [current](../../../../../general/electric%20current.md) and low [voltage](../../../../../general/voltage.md). Especially useful for operation in hazardous environment, like sewages, coal mines, and chemical storage. Such a device cannot produce enough heat or spark to cause ignition, even if the device has deteriorated or is damaged. See [IEC](../../../../../general/International%20Electrotechnical%20Commission.md) 60079-11.
  - [personal protective equipment](../../../../../general/personal%20protective%20equipment.md) (PPE) ::@:: Last resort. Electrical protective equipment includes arc-rating clothing, insulating gloves, etc.
- [lockout–tagout](../../../../../general/lockout–tagout.md) ::@:: Safety procedure to follow to ensure that dangerous equipment is shut off and cannot start before completing maintenance or repair. Especially important when more than one person are working on the same system.
- [relevant legislation in Hong Kong](#relevant%20legislation%20in%20Hong%20Kong)
  - Electricity Ordinance (Cap. 406) ::@:: Governs the generation, transmission, distribution, and utilization of electricity. Important sub-chapters include Electricity (Registration) Regulations (Cap. 406D), Electricity (Wiring) Regulations (Cap. 406E), and Electrical Products (Safety) Regulation (Cap. 406G).
    - Electricity (Wiring) Regulations (Cap. 406E) ::@:: Stipulates safety requirements of the design, installation, testing, and certification of fixed electrical installations. To ensure the quality and workmanship of the installations. A practical guideline is provided by [EMSD](../../../../../general/Electrical%20and%20Mechanical%20Services%20Department.md) as the _Code of Practice for the Electricity (Wiring) Regulations_.
    - Electricity (Registration) Regulations (Cap. 406D) ::@:: Stipulates the experience and qualifications of registered electrical contractors and workers. To ensure the quality and workmanship of electrical work. A grading system with A, B, C, H, and R is established to match workers and the type of work.
    - Electrical Products (Safety) Regulation (Cap. 406G) ::@:: Stipulates the safety of all household electrical products supplied in [Hong Kong](../../../../../general/Hong%20Kong.md). Requires suppliers to ensure a certificate of safety compliance has been issued. Enforced by the [Customs and Excise Department](../../../../../general/Customs%20and%20Excise%20Department%20(Hong%20Kong).md). Classifies 6 kinds of prescribed products that shall comply with the essential and specific safety requirements.
      - [6 kinds of prescribed products](#6%20kinds%20of%20prescribed%20products)
      - [substandard plugs](#substandard%20plugs)
  - _Code of Practice for the Electricity (Wiring) Regulations_ ::@:: By [EMSD](../../../../../general/Electrical%20and%20Mechanical%20Services%20Department.md). Has many examples of regulated standards to ensure compliance with Electricity (Wiring) Regulations (Cap. 406E).
  - Consumer Goods Safety Ordinance (Cap. 456) ::@:: In addition to Electrical Products (Safety) Regulation (Cap. 406G), all consumer goods in Hong Kong also need to comply with the general safety requirement.
    - [general safety requirement stipulations](#general%20safety%20requirement%20stipulations)
  - Factories and Industrial Undertakings (Electricity) Regulations (Cap. 59W) ::@:: Under the Factories and Industrial Undertakings Ordinance (Cap. 59). To protect workers from electrical hazards. Applicable to all industrial activities in which electricity is generated, transmitted, distributed, or used, but NOT applicable to supplying electricity in accordance with the Electricity Ordinance (Cap. 406).

## oversized data

### 6 kinds of prescribed products

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("5671", "2bc7",),
  """
adaptors
extension units
flexible cords
lamp holders
plugs
unventilated thermal storage type electric water heaters
""".strip().splitlines(),
)
```

<!--pytextgen generate section="5671"--><!-- The following content is generated at 2024-02-09T09:19:32.611770+08:00. Any edits will be overridden! -->

> 1. adaptors
> 2. extension units
> 3. flexible cords
> 4. lamp holders
> 5. plugs
> 6. unventilated thermal storage type electric water heaters

<!--/pytextgen-->

<!--pytextgen generate section="2bc7"--><!-- The following content is generated at 2024-02-09T09:19:32.596318+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←adaptors
- adaptors→::@::←extension units
- extension units→::@::←flexible cords
- flexible cords→::@::←lamp holders
- lamp holders→::@::←plugs
- plugs→::@::←unventilated thermal storage type electric water heaters
- unventilated thermal storage type electric water heaters→::@::←_(end)_

<!--/pytextgen-->

### general safety requirement stipulations

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("ee23", "292d",),
  """
instructions
manner of presentation
safety
standards
use of marks
warnings
""".strip().splitlines(),
)
```

<!--pytextgen generate section="ee23"--><!-- The following content is generated at 2024-02-14T17:52:38.899168+08:00. Any edits will be overridden! -->

> 1. instructions
> 2. manner of presentation
> 3. safety
> 4. standards
> 5. use of marks
> 6. warnings

<!--/pytextgen-->

<!--pytextgen generate section="292d"--><!-- The following content is generated at 2024-02-14T17:52:38.914301+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←instructions
- instructions→::@::←manner of presentation
- manner of presentation→::@::←safety
- safety→::@::←standards
- standards→::@::←use of marks
- use of marks→::@::←warnings
- warnings→::@::←_(end)_

<!--/pytextgen-->

### hazard causes

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("3219", "5bab",),
  """
improper contact
lack of maintenance
overloading
short circuiting
using substandard electrical appliances
wet condition
""".strip().splitlines(),
)
```

<!--pytextgen generate section="3219"--><!-- The following content is generated at 2024-02-09T00:05:47.436681+08:00. Any edits will be overridden! -->

> 1. improper contact
> 2. lack of maintenance
> 3. overloading
> 4. short circuiting
> 5. using substandard electrical appliances
> 6. wet condition

<!--/pytextgen-->

<!--pytextgen generate section="5bab"--><!-- The following content is generated at 2024-02-09T00:05:47.457257+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←improper contact
- improper contact→::@::←lack of maintenance
- lack of maintenance→::@::←overloading
- overloading→::@::←short circuiting
- short circuiting→::@::←using substandard electrical appliances
- using substandard electrical appliances→::@::←wet condition
- wet condition→::@::←_(end)_

<!--/pytextgen-->

### hazard control

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("a257", "f234",),
  """
[center tap](../../../../../general/center%20tap.md)
[circuit breaker](../../../../../general/circult%20breaker.md)
compliance with cable standards
[double insulation](../../../../../general/appliance%20classes.md#Class%20II)
grounding
[intrinsic safety](../../../../../general/intrinsic%20safety.md)
live parts are either insulated or unreachable
[personal protective equipment](../../../../../general/personal%20protective%20equipment.md) (PPE)
protective bonding
""".strip().splitlines(),
)
```

<!--pytextgen generate section="a257"--><!-- The following content is generated at 2024-02-09T00:10:28.980504+08:00. Any edits will be overridden! -->

> 1. [center tap](../../../../../general/center%20tap.md)
> 2. [circuit breaker](../../../../../general/circult%20breaker.md)
> 3. compliance with cable standards
> 4. [double insulation](../../../../../general/appliance%20classes.md#Class%20II)
> 5. grounding
> 6. [intrinsic safety](../../../../../general/intrinsic%20safety.md)
> 7. live parts are either insulated or unreachable
> 8. [personal protective equipment](../../../../../general/personal%20protective%20equipment.md) (PPE)
> 9. protective bonding

<!--/pytextgen-->

<!--pytextgen generate section="f234"--><!-- The following content is generated at 2024-02-09T00:10:28.927666+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←[center tap](../../../../../general/center%20tap.md)
- [center tap](../../../../../general/center%20tap.md)→::@::←[circuit breaker](../../../../../general/circult%20breaker.md)
- [circuit breaker](../../../../../general/circult%20breaker.md)→::@::←compliance with cable standards
- compliance with cable standards→::@::←[double insulation](../../../../../general/appliance%20classes.md#Class%20II)
- [double insulation](../../../../../general/appliance%20classes.md#Class%20II)→::@::←grounding
- grounding→::@::←[intrinsic safety](../../../../../general/intrinsic%20safety.md)
- [intrinsic safety](../../../../../general/intrinsic%20safety.md)→::@::←live parts are either insulated or unreachable
- live parts are either insulated or unreachable→::@::←[personal protective equipment](../../../../../general/personal%20protective%20equipment.md) (PPE)
- [personal protective equipment](../../../../../general/personal%20protective%20equipment.md) (PPE)→::@::←protective bonding
- protective bonding→::@::←_(end)_

<!--/pytextgen-->

### hazardous scenarios

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("d929", "afb9",),
  """
contact with overhead power lines
damaged cover
use of inappropriate measurement tools
""".strip().splitlines(),
)
```

<!--pytextgen generate section="d929"--><!-- The following content is generated at 2024-02-09T00:10:06.190900+08:00. Any edits will be overridden! -->

> 1. contact with overhead power lines
> 2. damaged cover
> 3. use of inappropriate measurement tools

<!--/pytextgen-->

<!--pytextgen generate section="afb9"--><!-- The following content is generated at 2024-02-09T00:01:47.212615+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←contact with overhead power lines
- contact with overhead power lines→::@::←damaged cover
- damaged cover→::@::←use of inappropriate measurement tools
- use of inappropriate measurement tools→::@::←_(end)_

<!--/pytextgen-->

### relevant legislation in Hong Kong

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("b234", "46f1",),
  """
Factories and Industrial Undertakings (Electricity) Regulations (Cap. 59W)
Electricity Ordinance (Cap. 406)
_Code of Practice for the Electricity (Wiring) Regulations_
Consumer Goods Safety Ordinance (Cap. 456)
""".strip().splitlines(),
)
```

<!--pytextgen generate section="b234"--><!-- The following content is generated at 2024-02-12T16:43:42.627779+08:00. Any edits will be overridden! -->

> 1. Factories and Industrial Undertakings (Electricity) Regulations (Cap. 59W)
> 2. Electricity Ordinance (Cap. 406)
> 3. _Code of Practice for the Electricity (Wiring) Regulations_
> 4. Consumer Goods Safety Ordinance (Cap. 456)

<!--/pytextgen-->

<!--pytextgen generate section="46f1"--><!-- The following content is generated at 2024-02-12T16:43:42.666363+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←Factories and Industrial Undertakings (Electricity) Regulations (Cap. 59W)
- Factories and Industrial Undertakings (Electricity) Regulations (Cap. 59W)→::@::←Electricity Ordinance (Cap. 406)
- Electricity Ordinance (Cap. 406)→::@::←_Code of Practice for the Electricity (Wiring) Regulations_
- _Code of Practice for the Electricity (Wiring) Regulations_→::@::←Consumer Goods Safety Ordinance (Cap. 456)
- Consumer Goods Safety Ordinance (Cap. 456)→::@::←_(end)_

<!--/pytextgen-->

### substandard plugs

```Python
# pytextgen generate data
return await memorize_seq(
  __env__.cwf_sects("662a", "3905",),
  """
cannot withstand high [temperature](../../../../../general/temperature.md)
loose electric plug
no [fuse](../../../../../general/fuse%20(electrical).md)
no insulating sleeves
no safety shutter
""".strip().splitlines(),
)
```

<!--pytextgen generate section="662a"--><!-- The following content is generated at 2024-02-09T09:14:53.814167+08:00. Any edits will be overridden! -->

> 1. cannot withstand high [temperature](../../../../../general/temperature.md)
> 2. loose electric plug
> 3. no [fuse](../../../../../general/fuse%20(electrical).md)
> 4. no insulating sleeves
> 5. no safety shutter

<!--/pytextgen-->

<!--pytextgen generate section="3905"--><!-- The following content is generated at 2024-02-09T09:14:53.797631+08:00. Any edits will be overridden! -->

- _(begin)_→::@::←cannot withstand high [temperature](../../../../../general/temperature.md)
- cannot withstand high [temperature](../../../../../general/temperature.md)→::@::←loose electric plug
- loose electric plug→::@::←no [fuse](../../../../../general/fuse%20(electrical).md)
- no [fuse](../../../../../general/fuse%20(electrical).md)→::@::←no insulating sleeves
- no insulating sleeves→::@::←no safety shutter
- no safety shutter→::@::←_(end)_

<!--/pytextgen-->

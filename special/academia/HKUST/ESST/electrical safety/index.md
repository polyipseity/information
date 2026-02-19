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
# import ../../../../../tools/utility.py.md
```

The content is in teaching order.

- [Ohm's law](../../../../../general/Ohm's%20law.md) ::@:: _V_ = _IR_ <!--SR:!2024-04-30,64,310!2024-05-01,64,310-->
- [electric current](../../../../../general/electric%20current.md) types ::@:: [alternating current](../../../../../general/alternating%20current.md) (AC), [direct current](../../../../../general/direct%20current.md) (DC) <!--SR:!2024-04-17,51,310!2024-05-16,77,324-->
  - [alternating current](../../../../../general/alternating%20current.md) (AC) ::@:: [electric current](../../../../../general/electric%20current.md) that periodically reverses direction and varies its magnitude continuously <!--SR:!2024-05-02,65,310!2024-04-21,55,310-->
  - [direct current](../../../../../general/direct%20current.md) (DC) ::@:: [electric current](../../../../../general/electric%20current.md) that flows in one direction only <!--SR:!2024-05-19,80,329!2024-05-06,69,329-->
- [units of measurement](../../../../../general/unit%20of%20measurement.md)
  - [current](../../../../../general/electric%20current.md) _I_ ::@:: [ampere](../../../../../general/ampere.md) A <!--SR:!2024-05-10,72,324!2024-05-08,71,324-->
  - [resistance](../../../../../general/electrical%20resistance%20and%20conductance.md) _R_ (DC) or [impedance](../../../../../general/electrical%20impedance.md) _Z_ (AC) ::@:: [ohm](../../../../../general/ohm.md) Ω <!--SR:!2024-05-05,68,329!2024-05-05,68,329-->
  - [voltage](../../../../../general/voltage.md) _V_ ::@:: [volt](../../../../../general/volt.md) V <!--SR:!2024-05-08,71,324!2024-05-20,81,329-->
- [voltage](../../../../../general/voltage.md) classification ::@:: [extra-low voltage](../../../../../general/extra-low%20voltage.md), [low voltage](../../../../../general/low%20voltage.md), [high voltage](../../../../../general/high%20voltage.md) <!--SR:!2024-05-01,65,324!2024-05-11,73,324-->
  - [extra-low voltage](../../../../../general/extra-low%20voltage.md) ::@:: defining risk: low; [BS 7671](../../../../../general/BS%207671.md): AC [RMS](../../../../../general/root%20mean%20square.md): <= 50 V, DC: <= 120 V ignoring [ripple](ripple%20(electrical).md) <!--SR:!2024-03-26,33,289!2024-05-12,74,329-->
  - [low voltage](../../../../../general/low%20voltage.md) ::@:: defining risk: [electrical shock](../../../../../general/electrical%20injury.md); [BS 7671](../../../../../general/BS%207671.md): AC [RMS](../../../../../general/root%20mean%20square.md): > 50 V, <= 1000 V, <= 600 V between conductors and earth, DC: > 120 V ignoring [ripple](ripple%20(electrical).md), <= 1500 V, <= 900 V between conductors and earth <!--SR:!2024-05-05,55,269!2024-05-03,67,324-->
  - [high voltage](../../../../../general/high%20voltage.md) ::@:: defining risk: [electrical arcing](../../../../../general/electric%20arc.md); [BS 7671](../../../../../general/BS%207671.md): AC [RMS](../../../../../general/root%20mean%20square.md): > 1000 V, > 600 V between conductors and earth, DC: > 1500 V, > 900 V between conductors and earth <!--SR:!2024-03-24,31,284!2024-05-18,79,329-->
- examples of effects of [current](../../../../../general/electric%20current.md)
  - 1 mA :@: barely perceptible <!--SR:!2024-04-07,44,290-->
  - 16 mA :@: let go threshold, i.e. maximum current a person can still control the muscle to stop touching the electricity source <!--SR:!2024-04-26,46,289-->
  - 20 mA :@: respiratory paralysis <!--SR:!2024-04-13,41,269-->
  - 100 mA :@: [ventricular fibrillation](../../../../../general/ventricular%20fibrillation.md) <!--SR:!2024-04-10,21,244-->
  - 2 A :@: [cardiac arrest](../../../../../general/cardiac%20arrest.md) and internal [organ](../../../../../general/organ%20(biology).md) damage <!--SR:!2024-05-09,57,289-->
  - 15 A, 20 A :@: common [fuse](fuse%20(electrical).md) or [circuit breaker](../../../../../general/circuit%20breaker.md) triggers <!--SR:!2024-05-15,76,324-->
- electrical hazards ::@:: [electric arc](../../../../../general/electric%20arc.md), [electrical injury](../../../../../general/electrical%20injury.md), [explosion](../../../../../general/explosion.md), [fire](../../../../../general/fire.md) <!--SR:!2024-04-23,34,249!2024-05-15,76,329-->
  - [electric arc](../../../../../general/electric%20arc.md) ::@:: Electric arcs can go through air to a person. They can also vaporize materials and produce extremely loud noises. These can cause non-contact burns. Emitted [infrared](../../../../../general/infrared.md) and [ultraviolet](../../../../../general/ultraviolete.md) radiation can cause eye damage. <!--SR:!2024-05-02,52,269!2024-05-04,68,329-->
  - [electrical injury](../../../../../general/electrical%20injury.md) ::@:: Electricity can interfere with normal electrical signals in the body. Involuntary muscle contraction can cause falls. Electricity can also cause contact burns, damaging internal organs. <!--SR:!2024-05-04,54,269!2024-05-12,74,329-->
  - [explosion](../../../../../general/explosion.md) ::@:: Electricity can detonate. <!--SR:!2024-04-16,50,310!2024-05-03,66,324-->
  - [fire](../../../../../general/fire.md) ::@:: Electricity can ignite. <!--SR:!2024-04-30,64,310!2024-05-05,67,310-->
- [hazardous scenarios](#hazardous%20scenarios)
- [hazard causes](#hazard%20causes)
- [hazard control](#hazard%20control)
  - [grounding](../../../../../general/ground%20(electricity).md) ::@:: Connect dead parts to the earth so that said dead part has zero potential during a fault. [EMSD](../../../../../general/Electrical%20and%20Mechanical%20Services%20Department.md): Z<sub>2</sub> <= 50 Z<sub>S</sub>/U<sub>O</sub> Ω, where Z<sub>S</sub> is the sum of live wire [impedance](../../../../../general/electrical%20impedance.md) Z<sub>1</sub>, ground wire [impedance](../../../../../general/electrical%20impedance.md) Z<sub>2</sub>, and ground [impedance](../../../../../general/electrical%20impedance.md) Z<sub>e</sub>, and U<sub>O</sub> is the source [voltage](../../../../../general/voltage.md), [diameter](../../../../../general/diameter.md) >= 12.5 mm <!--SR:!2024-04-23,47,264!2024-03-24,33,290-->
  - protective bonding ::@:: Connect several conductive parts to ensure the parts have the same potential so that they do not conduct current during a fault. May be used with [grounding](../../../../../general/ground%20(electrical).md). <!--SR:!2024-07-10,96,284!2024-04-21,52,309-->
  - [circuit breaker](../../../../../general/circult%20breaker.md) ::@:: [miniature circuit breaker](../../../../../general/circuit%20breaker.md) (MCB), [residual-current circuit breaker with over-current protection/ground-fault circuit interrupter](../../../../../general/residual-current%20device.md) (RCBO/GFCI), [residual-current device](../../../../../general/residual-current%20device.md) (RCD) <!--SR:!2024-03-25,28,287!2024-05-28,84,347-->
    - [residual-current device](../../../../../general/residual-current%20device.md) (RCD) ::@:: Breaks a circuit when it detects leakage current to [ground](../../../../../general/ground%20(electricity).md). <!--SR:!2024-04-29,62,310!2024-04-28,61,310-->
    - [miniature circuit breaker](../../../../../general/circuit%20breaker.md) (MCB) ::@:: A resettable [fuse](../../../../../general/fuse%20(electrical).md). Breaks a circuit when it detects overload. <!--SR:!2024-05-12,73,324!2024-04-25,59,310-->
    - [residual-current circuit breaker with over-current protection/ground-fault circuit interrupter](../../../../../general/residual-current%20device.md) (RCBO/GFCI) ::@:: A combination of RCD and MCB. <!--SR:!2024-04-19,53,310!2024-04-27,58,309-->
  - [center tap](../../../../../general/center%20tap.md) ::@:: Used if one wants to provide two separate secondary voltage sources half of the original voltage. Make a contact halfway along a winding of a [transformer](../../../../../general/transformer.md) and ground it. Then the voltage of both wires in contact with the end of the winding is only half the potential difference of the entire winding. The voltages in the two wires are 180 degree out-of-phase of each other (or negative voltage in one of the wire). This can be used to provide extra-low voltage by reducing voltage from 220 V to 110 V, and then use a center tap to split it to two 55 V sources. <!--SR:!2024-04-16,44,264!2024-04-23,57,310-->
  - [double insulation](../../../../../general/appliance%20classes.md#Class%20II) ::@:: Indicated by the double insulation symbol: ⧈ (a square inside another square). No single failure can cause dangerous voltage to be exposed as to cause [electric shock](../../../../../general/electrical%20injury.md), all without the use of an earthed metal casing. Usually this is done by adding supplementary insulation on top of the basic insulation. Earthing is unnecessary in this case as any fault causes a fault current too low to trigger a [fuse](../../../../../general/fuse%20(electrical).md), because of the high-[impedance](../../../../../general/electrical%20impedance.md) casing. <!--SR:!2024-04-15,42,269!2024-04-10,47,309-->
  - compliance with cable standards ::@:: [BS 1363](../../../../../general/BS%201363.md): Live (L) wire is brown, has a [fuse](../../../../../general/fuse%20(electrical).md), and on the right side of the plug when viewed from the plug cover. Neutral (N) wire is blue, and on the left side of the plug when viewed from the plug cover. Earth wire is green and yellow, and on the top side of the plug. <!--SR:!2024-05-24,67,270!2024-05-06,68,310-->
  - [intrinsic safety](../../../../../general/intrinsic%20safety.md) ::@:: Applicable for devices operating on low [current](../../../../../general/electric%20current.md) and low [voltage](../../../../../general/voltage.md). Especially useful for operation in hazardous environment, like sewages, coal mines, and chemical storage. Such a device cannot produce enough heat or spark to cause ignition, even if the device has deteriorated or is damaged. See [IEC](../../../../../general/International%20Electrotechnical%20Commission.md) 60079-11. <!--SR:!2024-04-13,39,249!2024-05-02,66,329-->
  - [personal protective equipment](../../../../../general/personal%20protective%20equipment.md) (PPE) ::@:: Last resort. Electrical protective equipment includes arc-rating clothing, insulating gloves, etc. <!--SR:!2024-04-20,38,269!2024-05-13,75,329-->
- [lockout–tagout](../../../../../general/lockout–tagout.md) ::@:: Safety procedure to follow to ensure that dangerous equipment is shut off and cannot start before completing maintenance or repair. Especially important when more than one person are working on the same system. <!--SR:!2024-04-17,50,304!2024-05-15,76,324-->
- [relevant legislation in Hong Kong](#relevant%20legislation%20in%20Hong%20Kong)
  - Electricity Ordinance (Cap. 406) ::@:: Governs the generation, transmission, distribution, and utilization of electricity. Important sub-chapters include Electricity (Registration) Regulations (Cap. 406D), Electricity (Wiring) Regulations (Cap. 406E), and Electrical Products (Safety) Regulation (Cap. 406G). <!--SR:!2024-03-26,29,244!2024-05-18,79,329-->
    - Electricity (Wiring) Regulations (Cap. 406E) ::@:: Stipulates safety requirements of the design, installation, testing, and certification of fixed electrical installations. To ensure the quality and workmanship of the installations. A practical guideline is provided by [EMSD](../../../../../general/Electrical%20and%20Mechanical%20Services%20Department.md) as the _Code of Practice for the Electricity (Wiring) Regulations_. <!--SR:!2024-04-19,44,249!2024-03-29,22,284-->
    - Electricity (Registration) Regulations (Cap. 406D) ::@:: Stipulates the experience and qualifications of registered electrical contractors and workers. To ensure the quality and workmanship of electrical work. A grading system with A, B, C, H, and R is established to match workers and the type of work. <!--SR:!2024-03-28,34,270!2024-04-29,21,270-->
    - Electrical Products (Safety) Regulation (Cap. 406G) ::@:: Stipulates the safety of all household electrical products supplied in [Hong Kong](../../../../../general/Hong%20Kong.md). Requires suppliers to ensure a certificate of safety compliance has been issued. Enforced by the [Customs and Excise Department](../../../../../general/Customs%20and%20Excise%20Department%20(Hong%20Kong).md). Classifies 6 kinds of prescribed products that shall comply with the essential and specific safety requirements. <!--SR:!2024-03-24,18,204!2024-04-24,47,264-->
      - [6 kinds of prescribed products](#6%20kinds%20of%20prescribed%20products)
      - [substandard plugs](#substandard%20plugs)
  - _Code of Practice for the Electricity (Wiring) Regulations_ ::@:: By [EMSD](../../../../../general/Electrical%20and%20Mechanical%20Services%20Department.md). Has many examples of regulated standards to ensure compliance with Electricity (Wiring) Regulations (Cap. 406E). <!--SR:!2024-04-03,37,289!2024-04-24,58,310-->
  - Consumer Goods Safety Ordinance (Cap. 456) ::@:: In addition to Electrical Products (Safety) Regulation (Cap. 406G), all consumer goods in Hong Kong also need to comply with the general safety requirement. <!--SR:!2024-05-01,40,274!2024-04-17,42,314-->
    - [general safety requirement stipulations](#general%20safety%20requirement%20stipulations) <!--SR:!2024-02-19,2,190!2024-02-19,6,249-->
  - Factories and Industrial Undertakings (Electricity) Regulations (Cap. 59W) ::@:: Under the Factories and Industrial Undertakings Ordinance (Cap. 59). To protect workers from electrical hazards. Applicable to all industrial activities in which electricity is generated, transmitted, distributed, or used, but NOT applicable to supplying electricity in accordance with the Electricity Ordinance (Cap. 406). <!--SR:!2024-03-27,29,249!2024-06-01,54,244-->

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

- _(begin)_→::@::←adaptors <!--SR:!2024-05-07,61,327!2024-05-25,81,347-->
- adaptors→::@::←extension units <!--SR:!2024-04-20,48,327!2024-04-15,46,307-->
- extension units→::@::←flexible cords <!--SR:!2024-04-18,31,307!2024-06-02,87,347-->
- flexible cords→::@::←lamp holders <!--SR:!2024-04-11,37,267!2024-03-31,33,307-->
- lamp holders→::@::←plugs <!--SR:!2024-03-30,36,307!2024-04-05,39,307-->
- plugs→::@::←unventilated thermal storage type electric water heaters <!--SR:!2024-05-26,69,287!2024-04-12,22,287-->
- unventilated thermal storage type electric water heaters→::@::←_(end)_ <!--SR:!2024-05-30,85,347!2024-04-13,47,327-->

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

- _(begin)_→::@::←instructions <!--SR:!2024-03-28,17,254!2024-06-03,82,354-->
- instructions→::@::←manner of presentation <!--SR:!2024-03-25,7,254!2024-04-07,34,294-->
- manner of presentation→::@::←safety <!--SR:!2024-04-06,16,234!2024-03-27,26,294-->
- safety→::@::←standards <!--SR:!2024-05-17,58,294!2024-04-01,28,274-->
- standards→::@::←use of marks <!--SR:!2024-04-16,32,274!2024-04-02,22,294-->
- use of marks→::@::←warnings <!--SR:!2024-04-04,31,294!2024-03-25,24,294-->
- warnings→::@::←_(end)_ <!--SR:!2024-06-06,85,354!2024-03-25,14,294-->

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

- _(begin)_→::@::←improper contact <!--SR:!2024-03-26,6,227!2024-05-30,85,347-->
- improper contact→::@::←lack of maintenance <!--SR:!2024-04-08,41,327!2024-03-25,28,287-->
- lack of maintenance→::@::←overloading <!--SR:!2024-03-31,11,287!2024-04-05,25,207-->
- overloading→::@::←short circuiting <!--SR:!2024-05-07,62,327!2024-05-21,77,347-->
- short circuiting→::@::←using substandard electrical appliances <!--SR:!2024-04-02,29,247!2024-05-02,55,287-->
- using substandard electrical appliances→::@::←wet condition <!--SR:!2024-05-21,64,287!2024-03-25,7,247-->
- wet condition→::@::←_(end)_ <!--SR:!2024-06-01,87,347!2024-04-05,18,267-->

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

- _(begin)_→::@::←[center tap](../../../../../general/center%20tap.md) <!--SR:!2024-05-08,66,327!2024-05-24,80,347-->
- [center tap](../../../../../general/center%20tap.md)→::@::←[circuit breaker](../../../../../general/circult%20breaker.md) <!--SR:!2024-04-23,48,267!2024-04-08,39,307-->
- [circuit breaker](../../../../../general/circult%20breaker.md)→::@::←compliance with cable standards <!--SR:!2024-05-16,58,267!2024-04-05,39,307-->
- compliance with cable standards→::@::←[double insulation](../../../../../general/appliance%20classes.md#Class%20II) <!--SR:!2024-03-23,12,247!2024-04-13,44,307-->
- [double insulation](../../../../../general/appliance%20classes.md#Class%20II)→::@::←grounding <!--SR:!2024-04-12,43,307!2024-04-14,23,267-->
- grounding→::@::←[intrinsic safety](../../../../../general/intrinsic%20safety.md) <!--SR:!2024-04-11,20,227!2024-03-29,32,307-->
- [intrinsic safety](../../../../../general/intrinsic%20safety.md)→::@::←live parts are either insulated or unreachable <!--SR:!2024-03-24,13,227!2024-03-27,30,287-->
- live parts are either insulated or unreachable→::@::←[personal protective equipment](../../../../../general/personal%20protective%20equipment.md) (PPE) <!--SR:!2024-04-16,29,227!2024-03-28,31,287-->
- [personal protective equipment](../../../../../general/personal%20protective%20equipment.md) (PPE)→::@::←protective bonding <!--SR:!2024-05-29,84,347!2024-05-31,79,307-->
- protective bonding→::@::←_(end)_ <!--SR:!2024-05-22,78,347!2024-03-29,11,267-->

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

- _(begin)_→::@::←contact with overhead power lines <!--SR:!2024-04-26,58,327!2024-05-15,73,347-->
- contact with overhead power lines→::@::←damaged cover <!--SR:!2024-04-29,60,327!2024-04-24,56,327-->
- damaged cover→::@::←use of inappropriate measurement tools <!--SR:!2024-04-12,32,287!2024-05-26,82,347-->
- use of inappropriate measurement tools→::@::←_(end)_ <!--SR:!2024-05-23,79,347!2024-05-03,45,287-->

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

- _(begin)_→::@::←Factories and Industrial Undertakings (Electricity) Regulations (Cap. 59W) <!--SR:!2024-03-27,33,307!2024-05-23,79,347-->
- Factories and Industrial Undertakings (Electricity) Regulations (Cap. 59W)→::@::←Electricity Ordinance (Cap. 406) <!--SR:!2024-03-23,3,267!2024-03-25,31,307-->
- Electricity Ordinance (Cap. 406)→::@::←_Code of Practice for the Electricity (Wiring) Regulations_ <!--SR:!2024-05-21,78,347!2024-04-09,40,307-->
- _Code of Practice for the Electricity (Wiring) Regulations_→::@::←Consumer Goods Safety Ordinance (Cap. 456) <!--SR:!2024-03-30,12,267!2024-03-30,32,307-->
- Consumer Goods Safety Ordinance (Cap. 456)→::@::←_(end)_ <!--SR:!2024-05-14,71,347!2024-06-01,71,287-->

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

- _(begin)_→::@::←cannot withstand high [temperature](../../../../../general/temperature.md) <!--SR:!2024-03-30,33,307!2024-05-26,82,347-->
- cannot withstand high [temperature](../../../../../general/temperature.md)→::@::←loose electric plug <!--SR:!2024-04-14,48,327!2024-04-22,55,327-->
- loose electric plug→::@::←no [fuse](../../../../../general/fuse%20(electrical).md) <!--SR:!2024-05-10,64,327!2024-04-01,35,307-->
- no [fuse](../../../../../general/fuse%20(electrical).md)→::@::←no insulating sleeves <!--SR:!2024-04-16,49,327!2024-03-23,9,267-->
- no insulating sleeves→::@::←no safety shutter <!--SR:!2024-05-26,81,347!2024-04-01,35,307-->
- no safety shutter→::@::←_(end)_ <!--SR:!2024-04-27,59,327!2024-05-02,44,287-->

<!--/pytextgen-->

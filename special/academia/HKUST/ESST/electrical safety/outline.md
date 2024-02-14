---
aliases:
  - ESST electrical safety outline
  - HKUST ESST electrical safety outline
tags:
  - flashcards/special/academia/HKUST/ESST/electrical_safety/outline
  - languages/in/English
---

# HKUST ESST electrical safety outline

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate module
# import ../../../../../../tools/utility.py.md
```

%%

The content below is in teaching order.

- [Ohm's law](../../../../../general/Ohm's%20law.md) ::: _V_ = _IR_ <!--SR:!2024-02-26,15,290!2024-02-27,16,290-->
- [electric current](../../../../../general/electric%20current.md) types ::: [alternating current](../../../../../general/alternating%20current.md) (AC), [direct current](../../../../../general/direct%20current.md) (DC) <!--SR:!2024-02-24,13,290!2024-02-29,18,304-->
- [alternating current](../../../../../general/alternating%20current.md) (AC) ::: [electric current](../../../../../general/electric%20current.md) that periodically reverses direction and varies its magnitude continuously <!--SR:!2024-02-27,16,290!2024-02-25,14,290-->
- [direct current](../../../../../general/direct%20current.md) (DC) ::: [electric current](../../../../../general/electric%20current.md) that flows in one direction only <!--SR:!2024-02-29,18,309!2024-02-27,16,309-->
- [units of measurement](../../../../../general/unit%20of%20measurement.md)
- [current](../../../../../general/electric%20current.md) _I_ ::: [ampere](../../../../../general/ampere.md) A <!--SR:!2024-02-28,17,304!2024-02-27,16,304-->
- [resistance](../../../../../general/electrical%20resistance%20and%20conductance.md) _R_ (DC) or [impedance](../../../../../general/electrical%20impedance.md) _Z_ (AC) ::: [ohm](../../../../../general/ohm.md) Ω <!--SR:!2024-02-27,16,309!2024-02-27,16,309-->
- [voltage](../../../../../general/voltage.md) _V_ ::: [volt](../../../../../general/volt.md) V <!--SR:!2024-02-27,16,304!2024-02-29,18,309-->
- [voltage](../../../../../general/voltage.md) classification ::: [extra-low voltage](../../../../../general/extra-low%20voltage.md), [low voltage](../../../../../general/low%20voltage.md), [high voltage](../../../../../general/high%20voltage.md) <!--SR:!2024-02-26,15,304!2024-02-28,17,304-->
- [extra-low voltage](../../../../../general/extra-low%20voltage.md) ::: defining risk: low; [BS 7671](../../../../../general/BS%207671.md): AC [RMS](../../../../../general/root%20mean%20square.md): <= 50 V, DC: <= 120 V ignoring [ripple](ripple%20(electrical).md) <!--SR:!2024-02-22,11,289!2024-02-28,17,309-->
- [low voltage](../../../../../general/low%20voltage.md) ::: defining risk: [electrical shock](../../../../../general/electrical%20injury.md); [BS 7671](../../../../../general/BS%207671.md): AC [RMS](../../../../../general/root%20mean%20square.md): > 50 V, <= 1000 V, <= 600 V between conductors and earth, DC: > 120 V ignoring [ripple](ripple%20(electrical).md), <= 1500 V, <= 900 V between conductors and earth <!--SR:!2024-02-19,8,269!2024-02-26,15,304-->
- [high voltage](../../../../../general/high%20voltage.md) ::: defining risk: [electrical arcing](../../../../../general/electric%20arc.md); [BS 7671](../../../../../general/BS%207671.md): AC [RMS](../../../../../general/root%20mean%20square.md): > 1000 V, > 600 V between conductors and earth, DC: > 1500 V, > 900 V between conductors and earth <!--SR:!2024-02-22,11,284!2024-02-29,18,309-->
- examples of effects of [current](../../../../../general/electric%20current.md)
  - 1 mA :: barely perceptible <!--SR:!2024-02-23,12,270-->
  - 16 mA :: let go threshold, i.e. maximum current a person can still control the muscle to stop touching the electricity source <!--SR:!2024-02-22,11,289-->
  - 20 mA :: respiratory paralysis <!--SR:!2024-02-17,6,269-->
- 100 mA :: [ventricular fibrillation](../../../../../general/ventricular%20fibrillation.md) <!--SR:!2024-02-19,6,244-->
  - 2 A :: [cardiac arrest](../../../../../general/cardiac%20arrest.md) and internal [organ](../../../../../general/organ%20(biology).md) damage <!--SR:!2024-02-22,11,289-->
  - 15 A, 20 A :: common [fuse](fuse%20(electrical).md) or [circuit breaker](../../../../../general/circuit%20breaker.md) triggers <!--SR:!2024-02-29,18,304-->
- electrical hazards ::: [electric arc](../../../../../general/electric%20arc.md), [electrical injury](../../../../../general/electrical%20injury.md), [explosion](../../../../../general/explosion.md), [fire](../../../../../general/fire.md) <!--SR:!2024-02-21,10,289!2024-02-29,18,309-->
  - [electric arc](../../../../../general/electric%20arc.md) ::: Electric arcs can go through air to a person. They can also vaporize materials and produce extremely loud noises. These can cause non-contact burns. Emitted [infrared](../../../../../general/infrared.md) and [ultraviolet](../../../../../general/ultraviolete.md) radiation can cause eye damage. <!--SR:!2024-02-18,7,269!2024-02-26,15,309-->
  - [electrical injury](../../../../../general/electrical%20injury.md) ::: Electricity can interfere with normal electrical signals in the body. Involuntary muscle contraction can cause falls. Electricity can also cause contact burns, damaging internal organs. <!--SR:!2024-02-18,7,269!2024-02-28,17,309-->
  - [explosion](../../../../../general/explosion.md) ::: Electricity can detonate. <!--SR:!2024-02-24,13,290!2024-02-27,16,304-->
  - [fire](../../../../../general/fire.md) ::: Electricity can ignite. <!--SR:!2024-02-26,15,290!2024-02-28,17,290-->
- [hazardous scenarios](#hazardous%20scenarios)
- [hazard causes](#hazard%20causes)
- [hazard control](#hazard%20control)
  - [grounding](../../../../../general/ground%20(electricity).md) ::: Connect dead parts to the earth so that said dead part has zero potential during a fault. [EMSD](../../../../../general/Electrical%20and%20Mechanical%20Services%20Department.md): Z<sub>2</sub> <= 50 Z<sub>S</sub>/U<sub>O</sub> Ω, where Z<sub>S</sub> is the sum of live wire [impedance](../../../../../general/electrical%20impedance.md) Z<sub>1</sub>, ground wire [impedance](../../../../../general/electrical%20impedance.md) Z<sub>2</sub>, and ground [impedance](../../../../../general/electrical%20impedance.md) Z<sub>e</sub>, and U<sub>O</sub> is the source [voltage](../../../../../general/voltage.md), [diameter](../../../../../general/diameter.md) >= 12.5 mm <!--SR:!2024-02-18,7,264!2024-02-20,9,270-->
  - protective bonding ::: Connect several conductive parts to ensure the parts have the same potential so that they do not conduct current during a fault. May be used with [grounding](../../../../../general/ground%20(electrical).md). <!--SR:!2024-02-23,12,284!2024-02-29,18,309-->
- [circuit breaker](../../../../../general/circult%20breaker.md) ::: [miniature circuit breaker](../../../../../general/circuit%20breaker.md) (MCB), [residual-current circuit breaker with over-current protection/ground-fault circuit interrupter](../../../../../general/residual-current%20device.md) (RCBO/GFCI), [residual-current device](../../../../../general/residual-current%20device.md) (RCD) <!--SR:!2024-02-15,3,287!2024-02-16,4,307-->
    - [residual-current device](../../../../../general/residual-current%20device.md) (RCD) ::: Breaks a circuit when it detects leakage current to [ground](../../../../../general/ground%20(electricity).md). <!--SR:!2024-02-27,16,290!2024-02-27,16,290-->
    - [miniature circuit breaker](../../../../../general/circuit%20breaker.md) (MCB) ::: A resettable [fuse](../../../../../general/fuse%20(electrical).md). Breaks a circuit when it detects overload. <!--SR:!2024-02-29,18,304!2024-02-26,15,290-->
    - [residual-current circuit breaker with over-current protection/ground-fault circuit interrupter](../../../../../general/residual-current%20device.md) (RCBO/GFCI) ::: A combination of RCD and MCB. <!--SR:!2024-02-25,14,290!2024-02-29,18,309-->
  - [center tap](../../../../../general/center%20tap.md) ::: Used if one wants to provide two separate secondary voltage sources half of the original voltage. Make a contact halfway along a winding of a [transformer](../../../../../general/transformer.md) and ground it. Then the voltage of both wires in contact with the end of the winding is only half the potential difference of the entire winding. The voltages in the two wires are 180 degree out-of-phase of each other (or negative voltage in one of the wire). This can be used to provide extra-low voltage by reducing voltage from 220 V to 110 V, and then use a center tap to split it to two 55 V sources. <!--SR:!2024-02-17,6,264!2024-02-26,15,290-->
  - [double insulation](../../../../../general/appliance%20classes.md#Class%20II) ::: Indicated by the double insulation symbol: ⧈ (a square inside another square). No single failure can cause dangerous voltage to be exposed as to cause [electric shock](../../../../../general/electrical%20injury.md), all without the use of an earthed metal casing. Usually this is done by adding supplementary insulation on top of the basic insulation. Earthing is unnecessary in this case as any fault causes a fault current too low to trigger a [fuse](../../../../../general/fuse%20(electrical).md), because of the high-[impedance](../../../../../general/electrical%20impedance.md) casing. <!--SR:!2024-02-17,6,269!2024-02-23,12,289-->
  - compliance with cable standards ::: [BS 1363](../../../../../general/BS%201363.md): Live (L) wire is brown, has a [fuse](../../../../../general/fuse%20(electrical).md), and on the right side of the plug when viewed from the plug cover. Neutral (N) wire is blue, and on the left side of the plug when viewed from the plug cover. Earth wire is green and yellow, and on the top side of the plug. <!--SR:!2024-02-20,9,270!2024-02-28,17,290-->
- [intrinsic safety](../../../../../general/intrinsic%20safety.md) ::: Applicable for devices operating on low [current](../../../../../general/electric%20current.md) and low [voltage](../../../../../general/voltage.md). Especially useful for operation in hazardous environment, like sewages, coal mines, and chemical storage. Such a device cannot produce enough heat or spark to cause ignition, even if the device has deteriorated or is damaged. See [IEC](../../../../../general/International%20Electrotechnical%20Commission.md) 60079-11. <!--SR:!2024-02-19,6,249!2024-02-26,15,309-->
  - [personal protective equipment](../../../../../general/personal%20protective%20equipment.md) (PPE) ::: Last resort. Electrical protective equipment includes arc-rating clothing, insulating gloves, etc. <!--SR:!2024-02-22,11,289!2024-02-28,17,309-->
- [lockout–tagout](../../../../../general/lockout–tagout.md) ::: Safety procedure to follow to ensure that dangerous equipment is shut off and cannot start before completing maintenance or repair. Especially important when more than one person are working on the same system. <!--SR:!2024-02-27,16,304!2024-02-29,18,304-->
- [relevant legislation in Hong Kong](#relevant%20legislation%20in%20Hong%20Kong)
- Electricity Ordinance (Cap. 406) ::: Governs the generation, transmission, distribution, and utilization of electricity. Important sub-chapters include Electricity (Registration) Regulations (Cap. 406D), Electricity (Wiring) Regulations (Cap. 406E), and Electrical Products (Safety) Regulation (Cap. 406G). <!--SR:!2024-02-25,11,244!2024-02-29,18,309-->
- Electricity (Wiring) Regulations (Cap. 406E) ::: Stipulates safety requirements of the design, installation, testing, and certification of fixed electrical installations. To ensure the quality and workmanship of the installations. A practical guideline is provided by [EMSD](../../../../../general/Electrical%20and%20Mechanical%20Services%20Department.md) as the _Code of Practice for the Electricity (Wiring) Regulations_. <!--SR:!2024-02-19,6,249!2024-02-28,17,304-->
    - Electricity (Registration) Regulations (Cap. 406D) ::: Stipulates the experience and qualifications of registered electrical contractors and workers. To ensure the quality and workmanship of electrical work. A grading system with A, B, C, H, and R is established to match workers and the type of work. <!--SR:!2024-02-23,12,270!2024-02-26,15,290-->
    - Electrical Products (Safety) Regulation (Cap. 406G) ::: Stipulates the safety of all household electrical products supplied in [Hong Kong](../../../../../general/Hong%20Kong.md). Requires suppliers to ensure a "certificate of safety compliance" has been issued. Enforced by the [Customs and Excise Department](../../../../../general/Customs%20and%20Excise%20Department%20(Hong%20Kong).md). Classifies six kinds of prescribed products that shall comply with the Essential and Specific Safety Requirements. <!--SR:!2024-02-15,4,244!2024-02-19,8,264-->
      - [six kinds of prescribed products](#six%20kinds%20of%20prescribed%20products)
      - [substandard plugs](#substandard%20plugs)
  - _Code of Practice for the Electricity (Wiring) Regulations_ ::: By [EMSD](../../../../../general/Electrical%20and%20Mechanical%20Services%20Department.md). Has many examples of regulated standards to ensure compliance with Electricity (Wiring) Regulations (Cap. 406E). <!--SR:!2024-02-24,13,289!2024-02-26,15,290-->
- Consumer Goods Safety Ordinance (Cap. 456) ::: In addition to Electrical Products (Safety) Regulation (Cap. 406G), all consumer goods in Hong Kong also need to comply with the General Safety Requirement, stipulating instructions, manner of presentation, safety, standards, use of marks, and warnings. <!--SR:!2024-02-16,2,210!2024-02-19,6,249-->
  - Factories and Industrial Undertakings (Electricity) Regulations (Cap. 59W) ::: Under the Factories and Industrial Undertakings Ordinance (Cap. 59). To protect workers from electrical hazards. Applicable to all industrial activities in which electricity is generated, transmitted, distributed, or used, but NOT applicable to supplying electricity in accordance with the Electricity Ordinance (Cap. 406). <!--SR:!2024-02-15,4,249!2024-02-17,6,264-->

## data

### hazardous scenarios

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
return await memorize_seq(
  __env__.cwf_sects("d929", "afb9",),
  """
contact with overhead power lines
damaged cover
use of inappropriate measurement tools
""".strip().splitlines(),
)
```

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="d929"--><!-- The following content is generated at 2024-02-09T00:10:06.190900+08:00. Any edits will be overridden! -->

> 1. contact with overhead power lines
> 2. damaged cover
> 3. use of inappropriate measurement tools

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="afb9"--><!-- The following content is generated at 2024-02-09T00:01:47.212615+08:00. Any edits will be overridden! -->

- _(begin)_→:::←contact with overhead power lines <!--SR:!2024-02-15,3,287!2024-02-16,4,307-->
- contact with overhead power lines→:::←damaged cover <!--SR:!2024-02-15,3,287!2024-02-15,3,287-->
- damaged cover→:::←use of inappropriate measurement tools <!--SR:!2024-02-16,4,307!2024-02-16,4,307-->
- use of inappropriate measurement tools→:::←_(end)_ <!--SR:!2024-02-16,4,307!2024-02-16,4,307-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### hazard causes

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3219"--><!-- The following content is generated at 2024-02-09T00:05:47.436681+08:00. Any edits will be overridden! -->

> 1. improper contact
> 2. lack of maintenance
> 3. overloading
> 4. short circuiting
> 5. using substandard electrical appliances
> 6. wet condition

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5bab"--><!-- The following content is generated at 2024-02-09T00:05:47.457257+08:00. Any edits will be overridden! -->

- _(begin)_→:::←improper contact <!--SR:!2024-02-15,3,287!2024-02-16,4,307-->
- improper contact→:::←lack of maintenance <!--SR:!2024-02-16,4,307!2024-02-15,3,287-->
- lack of maintenance→:::←overloading <!--SR:!2024-02-16,4,307!2024-02-16,2,247-->
- overloading→:::←short circuiting <!--SR:!2024-02-16,4,307!2024-02-16,4,307-->
- short circuiting→:::←using substandard electrical appliances <!--SR:!2024-02-16,2,247!2024-02-15,3,287-->
- using substandard electrical appliances→:::←wet condition <!--SR:!2024-02-15,3,287!2024-02-15,3,287-->
- wet condition→:::←_(end)_ <!--SR:!2024-02-16,4,307!2024-02-16,4,307-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### hazard control

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="a257"--><!-- The following content is generated at 2024-02-09T00:10:28.980504+08:00. Any edits will be overridden! -->

> 1. [center tap](../../../../../general/center%20tap.md)
> 2. [circuit breaker](../../../../../general/circult%20breaker.md)
> 3. compliance with cable standards
> 4. [double insulation](../../../../../general/appliance%20classes.md#Class%20II)
> 5. grounding
> 6. [intrinsic safety](../../../../../general/intrinsic%20safety.md)
> 7. live parts are either insulated or unreachable
> 8. [personal protective equipment](../../../../../general/personal%20protective%20equipment.md) (PPE)
> 9. protective bonding

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="f234"--><!-- The following content is generated at 2024-02-09T00:10:28.927666+08:00. Any edits will be overridden! -->

- _(begin)_→:::←[center tap](../../../../../general/center%20tap.md) <!--SR:!2024-02-17,4,287!2024-02-16,4,307-->
- [center tap](../../../../../general/center%20tap.md)→:::←[circuit breaker](../../../../../general/circult%20breaker.md) <!--SR:!2024-02-16,2,247!2024-02-15,3,287-->
- [circuit breaker](../../../../../general/circult%20breaker.md)→:::←compliance with cable standards <!--SR:!2024-02-16,3,267!2024-02-15,3,287-->
- compliance with cable standards→:::←[double insulation](../../../../../general/appliance%20classes.md#Class%20II) <!--SR:!2024-02-15,3,287!2024-02-15,3,287-->
- [double insulation](../../../../../general/appliance%20classes.md#Class%20II)→:::←grounding <!--SR:!2024-02-15,3,287!2024-02-15,3,287-->
- grounding→:::←[intrinsic safety](../../../../../general/intrinsic%20safety.md) <!--SR:!2024-02-16,3,267!2024-02-15,3,287-->
- [intrinsic safety](../../../../../general/intrinsic%20safety.md)→:::←live parts are either insulated or unreachable <!--SR:!2024-02-16,3,267!2024-02-16,3,267-->
- live parts are either insulated or unreachable→:::←[personal protective equipment](../../../../../general/personal%20protective%20equipment.md) (PPE) <!--SR:!2024-02-15,3,287!2024-02-15,3,287-->
- [personal protective equipment](../../../../../general/personal%20protective%20equipment.md) (PPE)→:::←protective bonding <!--SR:!2024-02-16,4,307!2024-02-15,3,287-->
- protective bonding→:::←_(end)_ <!--SR:!2024-02-16,4,307!2024-02-15,3,287-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### relevant legislation in Hong Kong

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="b234"--><!-- The following content is generated at 2024-02-12T16:43:42.627779+08:00. Any edits will be overridden! -->

> 1. Factories and Industrial Undertakings (Electricity) Regulations (Cap. 59W)
> 2. Electricity Ordinance (Cap. 406)
> 3. _Code of Practice for the Electricity (Wiring) Regulations_
> 4. Consumer Goods Safety Ordinance (Cap. 456)

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="46f1"--><!-- The following content is generated at 2024-02-12T16:43:42.666363+08:00. Any edits will be overridden! -->

- _(begin)_→:::←Factories and Industrial Undertakings (Electricity) Regulations (Cap. 59W) <!--SR:!2024-02-15,3,287!2024-02-16,4,307-->
- Factories and Industrial Undertakings (Electricity) Regulations (Cap. 59W)→:::←Electricity Ordinance (Cap. 406) <!--SR:!2024-02-16,4,307!2024-02-15,3,287-->
- Electricity Ordinance (Cap. 406)→:::←_Code of Practice for the Electricity (Wiring) Regulations_ <!--SR:!2024-02-16,4,307!2024-02-15,3,287-->
- _Code of Practice for the Electricity (Wiring) Regulations_→:::←Consumer Goods Safety Ordinance (Cap. 456) <!--SR:!2024-02-15,3,287!2024-02-16,4,307-->
- Consumer Goods Safety Ordinance (Cap. 456)→:::←_(end)_ <!--SR:!2024-02-16,4,307!2024-02-15,3,287-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### six kinds of prescribed products

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="5671"--><!-- The following content is generated at 2024-02-09T09:19:32.611770+08:00. Any edits will be overridden! -->

> 1. adaptors
> 2. extension units
> 3. flexible cords
> 4. lamp holders
> 5. plugs
> 6. unventilated thermal storage type electric water heaters

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="2bc7"--><!-- The following content is generated at 2024-02-09T09:19:32.596318+08:00. Any edits will be overridden! -->

- _(begin)_→:::←adaptors <!--SR:!2024-02-16,4,307!2024-02-16,4,307-->
- adaptors→:::←extension units <!--SR:!2024-02-16,4,307!2024-02-15,3,287-->
- extension units→:::←flexible cords <!--SR:!2024-02-16,4,307!2024-02-16,4,307-->
- flexible cords→:::←lamp holders <!--SR:!2024-02-15,3,287!2024-02-16,4,307-->
- lamp holders→:::←plugs <!--SR:!2024-02-15,3,287!2024-02-15,3,287-->
- plugs→:::←unventilated thermal storage type electric water heaters <!--SR:!2024-02-15,3,287!2024-02-16,4,307-->
- unventilated thermal storage type electric water heaters→:::←_(end)_ <!--SR:!2024-02-16,4,307!2024-02-15,3,287-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

### substandard plugs

%%

```Python
# 08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate data
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

%%

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="662a"--><!-- The following content is generated at 2024-02-09T09:14:53.814167+08:00. Any edits will be overridden! -->

> 1. cannot withstand high [temperature](../../../../../general/temperature.md)
> 2. loose electric plug
> 3. no [fuse](../../../../../general/fuse%20(electrical).md)
> 4. no insulating sleeves
> 5. no safety shutter

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

<!--08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e generate section="3905"--><!-- The following content is generated at 2024-02-09T09:14:53.797631+08:00. Any edits will be overridden! -->

- _(begin)_→:::←cannot withstand high [temperature](../../../../../general/temperature.md) <!--SR:!2024-02-15,3,287!2024-02-16,4,307-->
- cannot withstand high [temperature](../../../../../general/temperature.md)→:::←loose electric plug <!--SR:!2024-02-15,3,287!2024-02-15,3,287-->
- loose electric plug→:::←no [fuse](../../../../../general/fuse%20(electrical).md) <!--SR:!2024-02-16,4,307!2024-02-16,3,267-->
- no [fuse](../../../../../general/fuse%20(electrical).md)→:::←no insulating sleeves <!--SR:!2024-02-16,4,307!2024-02-15,3,287-->
- no insulating sleeves→:::←no safety shutter <!--SR:!2024-02-16,4,307!2024-02-15,3,287-->
- no safety shutter→:::←_(end)_ <!--SR:!2024-02-15,3,287!2024-02-15,3,287-->

<!--/08e5b0a3-f78a-46af-bf50-eb9b12f7fa1e-->

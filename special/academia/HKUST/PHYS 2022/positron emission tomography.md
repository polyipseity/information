---
aliases:
  - PET
  - PET scan
  - positron emission tomography
  - positron emission tomography scan
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/positron_emission_tomography
  - language/in/English
---

# positron emission tomography

_Positron emission tomography_ images where a [positron](positron.md) was made inside a living body, without surgery. A radioactive tracer carries that positron to the tissue of interest. Every [annihilation](annihilation.md) of the positron with a neighbouring electron fires two gamma ray photons of $511\ \text{keV}$ in exactly opposite directions. The machine never sees the positron or the tracer, only photon pairs, and each pair tells it where the tracer went.

An X-ray records tissue density. A PET scan records the chemistry of the tissue that took up the tracer, giving an image of metabolism rather than anatomy. A region that takes up a lot of tracer shows up brightly. What the brightness means depends on which tracer was used.

---

Flashcards for this section are as follows:

- overview: what the technique images, and from what signal ::@:: The places where the tracer's positrons annihilate, which are the places the tracer reached; each annihilation there fires a pair of gamma ray photons in opposite directions.
- what the machine never sees ::@:: The positron and the tracer; it sees only the pairs of gamma ray photons that the annihilations produce.
- what the image records against what an X-ray records ::@:: This records the chemistry and the metabolism of the tissue that took up the tracer, where an X-ray records density.
- what the brightness of a spot in the image depends on ::@:: The tracer that was used.
- whether the scan needs surgery ::@:: No; the positron is made inside the body by an injected tracer.

## the tracer chain

1. The positron-emitting isotope is attached to a radioactive tracer in a synthesis lab.
2. The tracer is injected into the patient's body immediately after synthesis.
3. The tracer attaches to specific organs inside the body.
4. The isotope emits positrons.
5. Each positron annihilates with a neighbouring electron, producing two gamma ray photons travelling in opposite directions.
6. Both photons are detected on opposite sides of the detector, and the signal goes to a computer that forms the image.

Steps 1 to 3 deliver the tracer. Step 1 keeps two jobs apart: the isotope supplies the signal, the molecule picks the tissue. Step 2 is a matter of timing: short half-lives mean the tracer loses activity between the bench and the patient. Step 3 gives the image its meaning. A tracer that failed to bind would give a bright image of wherever the isotope happened to end up, which is nowhere in particular.

Steps 4 to 6 do the detection, following the annihilation described in [annihilation](annihilation.md). Step 6 is the only step that produces data rather than physics: it turns a shower of unrelated events into a position.

---

Flashcards for this section are as follows:

- overview: the six steps of the chain in one line ::@:: Attach a positron-emitting isotope to a tracer in a synthesis lab, inject the tracer, let it bind its target organ, let the isotope emit positrons, let each positron annihilate with a neighbouring electron into two opposed gamma photons, and detect both photons in coincidence to form the image.
- step 1, attaching the positron-emitting isotope to a tracer: where it happens ::@:: In a synthesis lab, where the isotope is attached to a radioactive tracer molecule.
- step 2, the injection: when it happens ::@:: Immediately after synthesis, so that the short half-life of the isotope is not spent outside the patient.
- step 3, once the tracer is inside: what it does ::@:: It attaches to specific organs, which is what decides where the image is bright.
- step 4, once the tracer has bound: what the isotope does ::@:: It emits positrons.
- step 5: what happens to each of those positrons ::@:: It annihilates with a neighbouring electron, producing a pair of gamma ray photons travelling in opposite directions.
- step 6: what the detector does with the pair, and what the computer does with the signal ::@:: The two photons are detected on opposite sides of the detector, and the signal is sent to a computer that forms the image.
- steps 1 to 3 against steps 4 to 6: what each half is for ::@:: The first half delivers and targets the tracer, and the second half detects the photons the isotope produces.
- why the isotope and the tracer are two separate parts of the molecule ::@:: The isotope supplies the signal and the tracer decides where that signal comes from.
- why step 3 is the step that gives the image its meaning ::@:: A tracer that failed to bind would make the image bright wherever the isotope happened to end up, which is nowhere in particular.
- step 6 in one phrase: what it adds that the other five steps do not ::@:: It is the only step that produces data rather than physics, turning a shower of unrelated events into a position.

## what each tracer targets

Each tracer binds to one thing. That molecule is what makes the image specific. F-18 and Ga-68 are isotopes, named by element symbol and mass number. FDG, DOTA, and PSMA are the molecules those isotopes are attached to. Both isotopes are positron emitters with short half-lives. Each molecule was chosen for its chemistry rather than for its radioactivity.

| tracer | isotope | what it attaches to |
| --- | --- | --- |
| FDG | F-18, fluorine-18 | altered glucose metabolism: cancers, infections, inflammation |
| DOTA | Ga-68, gallium-68 | neuroendocrine tumours |
| PSMA | F-18, fluorine-18 | the prostate-specific membrane of prostate cancer |

FDG does not bind to cancer. It is a glucose analogue, and any tissue metabolising glucose faster than its neighbours takes it up: a tumour, an infection, or an area of inflammation. The scan locates a metabolic change. It does not say whether the change is malignant, since a hot spot on an FDG scan is a statement about activity, not a diagnosis. The other two tracers are narrower, each reaching one specific target rather than a metabolic change.

---

Flashcards for this section are as follows:

- what makes an image specific: the molecule or the isotope ::@:: The molecule, since each tracer binds to one target and the molecule was chosen for its chemistry rather than for its radioactivity.
- FDG: what it attaches to, and the three kinds of tissue that follow from that ::@:: Altered glucose metabolism, which covers cancers, infections, and areas of inflammation.
- DOTA: what it attaches to ::@:: Neuroendocrine tumours.
- PSMA: what it attaches to ::@:: The prostate-specific membrane of prostate cancer.
- what the element symbol and the number in a name like F-18 or Ga-68 give you ::@:: The element and its mass number; FDG, DOTA, and PSMA are the molecules the isotopes are attached to.
- what kind of isotopes F-18 and Ga-68 are, and what decided the molecule each one carries ::@:: Both are positron emitters with short half-lives, and each molecule was chosen for its chemistry rather than for its radioactivity.
- what kind of molecule FDG is, and why that decides what it binds ::@:: A glucose analogue, so it is taken up wherever glucose is being metabolised rather than by cancer specifically.
- a counterexample: a bright spot on an FDG scan ::@:: A statement about metabolic activity rather than a diagnosis on its own, since inflammation and infection take up the tracer too.
- how DOTA and PSMA compare in reach with FDG ::@:: They are narrower: DOTA reaches neuroendocrine tumours, and PSMA reaches a membrane found on prostate cancer cells.

## why the geometry makes the image possible

The detector surrounds the patient with a ring. A real event fires one photon into one side of the ring and the other into the opposite side. The two leave back to back, so the two detector hits and the annihilation point lie on one straight line. The line is the data. The machine collects many of them, each from a different annihilation, and intersects them to recover a position. A single pair would give a line and nothing more. A single photon gives no line at all, so the two have to be counted together.

A coincidence requirement keeps those lines clean. The detector registers an event only when both photons of a pair arrive within a short window of each other. A random pair of unrelated photons is very unlikely to land inside that window. Each accepted line is then very likely a real annihilation, so the machine can still reconstruct from the few events it keeps. The fixed $511\ \text{keV}$ does the same job in the energy channel: the energy window admits the pair and excludes scattered photons that lost energy on the way in.

---

Flashcards for this section are as follows:

- overview: what one detected pair gives, and what many of them give ::@:: One pair gives a line of known direction through the annihilation point and nothing more; many such lines intersected together give a position.
- the coincidence requirement, stated as a rule ::@:: An event is registered only when both photons of a pair arrive within a short window of each other.
- the coincidence requirement's effect on the data ::@:: Most unrelated photon pairs fail it, so the lines that survive are almost all real annihilations and the machine can reconstruct from few accepted lines.
- the fixed $511\ \text{keV}$ and what the detector does with it ::@:: The detector accepts that energy and discards photons that have scattered and lost energy on the way in.
- a counterexample: detecting one photon at a time instead ::@:: It would localise nothing, since a single photon gives no line through the event at all.

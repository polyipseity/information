---
aliases:
  - kinetic theory
  - kinetic theory of gases
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/kinetic_theory_of_gases
  - language/in/English
---

# kinetic theory of gases

The _kinetic theory of gases_ models a gas as a large number of molecules in constant random motion, each small compared with the distances between them. Their collisions with one another and with the walls of the container explain the macroscopic properties of the gas, and the same model accounts for its heat capacity through the number of degrees of freedom its molecules have.

---

Flashcards for this section are as follows:

- overview: the model and what it explains ::@:: A gas is many molecules in constant random motion, and their collisions explain the macroscopic properties of pressure, volume, and temperature.
- overview: what the number of degrees of freedom determines ::@:: The heat capacity of the gas.

## ideal gas law

The experimental work of Robert Boyle (1627–1691), Jacques Charles (1746–1823), and Joseph Louis Gay-Lussac (1778–1850) culminates in the ideal gas equation for $N$ molecules of a "simple" gas, $PV = Nk_BT = nN_Ak_BT = nRT$. Here $k_B = 1.38 \times 10^{-23}\ \text{J/K}$ is the Boltzmann constant, $N_A = 6.02 \times 10^{23}\ \text{mol}^{-1}$ is Avogadro's number, $n$ is the amount of gas in moles, and $R = 8.31\ \text{J mol}^{-1}\text{K}^{-1}$ is the ideal gas constant.

---

Flashcards for this section are as follows:

- the ideal gas equation in terms of the number of molecules $N$ and the Boltzmann constant $k_B$ ::@:: $PV = Nk_BT$.
- the ideal gas equation in terms of the amount $n$ and the ideal gas constant $R$ ::@:: $PV = nRT$, reached through $N = nN_A$.
- the value of the Boltzmann constant $k_B$ ::@:: $1.38 \times 10^{-23}\ \text{J/K}$.
- the value of Avogadro's number $N_A$ ::@:: $6.02 \times 10^{23}\ \text{mol}^{-1}$.
- the value of the ideal gas constant $R$ ::@:: $8.31\ \text{J mol}^{-1}\text{K}^{-1}$.
- the people whose work the ideal gas equation culminates: the three named ::@:: Robert Boyle, Jacques Charles, and Joseph Louis Gay-Lussac.

## equipartition of energy

The average molecular kinetic energy of the gas is proportional to the absolute temperature, and the internal energy $U$ is proportional to that average. Writing the average as $\bar K$, the internal energy is $U = N\bar K = nN_A\bar K$. The internal energy is distributed equally among the $f$ degrees of freedom of the system, which gives $\bar K = \frac{f}{2}k_BT$ and $U = \frac{f}{2}nRT$.

---

Flashcards for this section are as follows:

- the average molecular kinetic energy and the absolute temperature: how the two are related ::@:: The average molecular kinetic energy is proportional to the absolute temperature.
- the internal energy $U$ in terms of the average molecular kinetic energy $\bar K$ and the number of molecules $N$ ::@:: $U = N\bar K = nN_A\bar K$.
- equipartition: the average kinetic energy per molecule in terms of $f$, $k_B$, and $T$ ::@:: $\bar K = \frac{f}{2}k_BT$; the internal energy is distributed equally among the $f$ degrees of freedom.
- equipartition: the internal energy $U$ in terms of $f$, $n$, $R$, and $T$ ::@:: $U = \frac{f}{2}nRT$.

## molar heat capacity

The heat capacity of a body is $C = Q/\Delta T = \Delta U/\Delta T$, and its molar heat capacity at constant volume is $C_V = C/n$. A gas held at constant volume does no work, so the heat added equals the change in internal energy, $Q = \Delta U$. Combining this with the equipartition result gives $C_V = \frac{dU}{n\,dT} = \frac{fR}{2}$, so measuring $C_V$ is a way to measure $f$. At constant pressure the heat capacity is larger by one gas constant, $C_p = C_V + R$.

---

Flashcards for this section are as follows:

- heat capacity $C$ in terms of the heat $Q$ and the temperature change $\Delta T$ ::@:: $C = Q/\Delta T = \Delta U/\Delta T$.
- the molar heat capacity at constant volume $C_V$ in terms of $C$ and the amount $n$ ::@:: $C_V = C/n$.
- the molar heat capacity at constant volume $C_V$ in terms of $f$ and the gas constant $R$ ::@:: $C_V = \frac{dU}{n\,dT} = \frac{fR}{2}$.
- how the number of degrees of freedom $f$ is measured ::@:: From the measured molar heat capacity, through $C_V = \frac{fR}{2}$.
- the relation between $C_p$ and $C_V$ with the gas constant $R$ ::@:: $C_p = C_V + R$.

### gases

Real gases at ordinary temperatures are close to the classical value of $C_V$ when their molecules are simple. Helium and argon, both monatomic, sit near $f = 3$; nitrogen and oxygen, both diatomic, near $f = 5$; and the polyatomic gases measure above the classical $f = 6$.

| gas | molecules | $f$ (classical) | $C_V$ in $\text{J mol}^{-1}\text{K}^{-1}$ |
| --- | --- | --- | --- |
| helium | monatomic | 3 | 12.5 |
| argon | monatomic | 3 | 12.6 |
| nitrogen | diatomic | 5 | 20.7 |
| oxygen | diatomic | 5 | 20.8 |
| ammonia | polyatomic | 6 | 29.1 |
| carbon dioxide | polyatomic | 6 | 29.7 |

---

Flashcards for this section are as follows:

- helium and argon: the $f$ they correspond to and their measured $C_V$ ::@:: $f = 3$, the monatomic value, with $C_V = 12.5$ for helium and $12.6$ for argon.
- nitrogen and oxygen: the $f$ they correspond to and their measured $C_V$ ::@:: $f = 5$, the diatomic value, with $C_V = 20.7$ for nitrogen and $20.8$ for oxygen.
- the polyatomic gases of the table: their classical $f$ and their measured $C_V$ ::@:: $f = 6$, with $C_V = 29.1$ for ammonia and $29.7\ \text{J mol}^{-1}\text{K}^{-1}$ for carbon dioxide.

### large molecules

A large molecule has far more degrees of freedom than a small one, and its molar heat capacity scales with them. An alpha helix of a protein has a molar heat capacity of about $800\ \text{cal mol}^{-1}\text{K}^{-1}$, which is $400R$ and corresponds to $f = 400$. The protein chymotrypsinogen is larger still: about $9000\ \text{cal mol}^{-1}\text{K}^{-1}$, or $4500R$, giving $f = 4500$.

---

Flashcards for this section are as follows:

- the alpha helix: its molar heat capacity in $\text{cal mol}^{-1}\text{K}^{-1}$ and in $R$, and the $f$ it gives ::@:: About $800\ \text{cal mol}^{-1}\text{K}^{-1} = 400R$, giving $f = 400$.
- chymotrypsinogen: its molar heat capacity in $\text{cal mol}^{-1}\text{K}^{-1}$ and in $R$, and the $f$ it gives ::@:: About $9000\ \text{cal mol}^{-1}\text{K}^{-1} = 4500R$, giving $f = 4500$.

## limits of the classical model

The classical result $C_V = \frac{fR}{2}$ holds at every temperature, but measurement does not. Each degree of freedom contributes its share of $\frac{R}{2}$ only above the temperature at which it is excited, and classical physics gives no reason for that temperature.

---

Flashcards for this section are as follows:

- the classical prediction for $C_V$ against temperature, and what measurement shows instead ::@:: The classical $C_V = \frac{fR}{2}$ is constant in temperature, while measurement shows it rising in steps as further degrees of freedom become active.

### the constant-volume plateaus

Plotted against temperature, the ratio $c_V/R$ sits at a plateau of $3/2$ while only the three translational degrees of freedom are active, rises to $5/2$ once rotation becomes active, and reaches $7/2$ once vibration does.

---

Flashcards for this section are as follows:

- the three plateaus of $c_V/R$ as the temperature rises, and what is active at each ::@:: $3/2$ with only translation active, $5/2$ once rotation is active, and $7/2$ once vibration is active.

### the constant-pressure levels

The same failure shows in the constant-pressure heat capacity, $C_p = C_V + R$, measured in $\text{kJ kmol}^{-1}\text{K}^{-1}$ over the range from $300\ \text{K}$ to about $3500\ \text{K}$. The noble gases argon, helium, neon, krypton, xenon, and radon hold a flat line at the level of $f = 3$ across the whole range, while air climbs towards $f = 5$, hydrogen towards $f = 6$, and carbon dioxide towards $f = 13$, the last still rising at $3000\ \text{K}$. Water vapour and oxygen rise between them.

---

Flashcards for this section are as follows:

- at constant pressure, the level of $f$ each of the named gases approaches over $300\ \text{K}$ to $3500\ \text{K}$ ::@:: $f = 3$ for argon, helium, neon, krypton, xenon, and radon; $f = 5$ for air; $f = 6$ for hydrogen; and $f = 13$ for carbon dioxide.

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

The theory rests on several assumptions: gas molecules are point masses with negligible volume compared to the container; they undergo perfectly elastic collisions with each other and with the walls (no net kinetic energy is lost); there are no intermolecular attractive or repulsive forces except during brief collisions. The average kinetic energy of the molecules is directly proportional to the absolute temperature of the gas.

---

Flashcards for this section are as follows:

- overview: the model and what it explains ::@:: A gas is many molecules in constant random motion, and their collisions explain the macroscopic properties of pressure, volume, and temperature. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- overview: what the number of degrees of freedom determines ::@:: The heat capacity of the gas. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the kinetic theory assumptions: the four key ones ::@:: Molecules are point masses with negligible volume; collisions are perfectly elastic; there are no intermolecular forces except during collisions; and average kinetic energy is proportional to absolute temperature. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

## ideal gas law

The experimental work of Robert Boyle (1627–1691), Jacques Charles (1746–1823), and Joseph Louis Gay-Lussac (1778–1850) culminates in the ideal gas equation for $N$ molecules of a "simple" gas, $PV = Nk_BT = nN_Ak_BT = nRT$. Here $k_B = 1.38 \times 10^{-23}\ \text{J/K}$ is the Boltzmann constant, $N_A = 6.022 \times 10^{23}\ \text{mol}^{-1}$ is Avogadro's number, $n$ is the amount of gas in moles, and $R = 8.31\ \text{J mol}^{-1}\text{K}^{-1}$ is the ideal gas constant.

Molecular collisions with the walls make the pressure. Take a wall of area $A$ perpendicular to the $x$ axis. Pressure is the momentum delivered to the wall per unit area per unit time, $P = \frac{1}{A}\frac{dp}{dt}$. Split the molecules by their velocity component $v_x$. In equilibrium the distribution is symmetric, so half of them head toward the wall. Those with $v_x$ in $[v_x, v_x + dv_x]$ hit it within time $dt$ only if they sit in the slab of thickness $v_x\,dt$ in front of it. That slab holds $\tfrac{1}{2} n f(v_x)\,dv_x \cdot A \cdot v_x\,dt$ such molecules, with $n = N/V$ the number density and $f(v_x)$ the normalised distribution of the component, $\int f(v_x)\,dv_x = 1$. For any function $g$ of $v_x$, write $\langle g \rangle = \int g(v_x) f(v_x)\,dv_x$ over the full distribution. Each collision reverses $v_x$ and delivers $\Delta p = 2mv_x$, so the momentum the wall gains within time $dt$ is $$dp = \int 2mv_x \cdot \tfrac{1}{2} n f(v_x) v_x A\,dt\,dv_x = nmA\langle v_x^2\rangle\,dt.$$ Dividing by $A\,dt$ gives $P = nm\langle v_x^2\rangle$.

Equipartition asserts that each quadratic degree of freedom carries $\tfrac{1}{2}k_BT$ in equilibrium, so $\tfrac{1}{2}m\langle v_x^2\rangle = \tfrac{1}{2}k_BT$ and $\langle v_x^2\rangle = k_BT/m$. The gas is isotropic, so $\langle v^2\rangle = 3\langle v_x^2\rangle$ and $$\langle v^2\rangle = \frac{3k_BT}{m}, \qquad P = \frac{N}{V}k_BT,$$ which rearranges to $PV = Nk_BT$.

Four named gas laws are special cases of this equation, each holding one variable constant. Boyle's law states $P_1V_1 = P_2V_2$ at constant $T$ and $n$: decreasing the volume increases the wall collision frequency, and so the pressure. Charles's law states $V_1/T_1 = V_2/T_2$ at constant $P$ and $n$: heating the gas increases the average molecular speed, and the container must expand to keep the pressure constant. Gay-Lussac's law states $P_1/T_1 = P_2/T_2$ at constant $V$ and $n$: heating increases molecular speed and so the force of wall collisions, raising the pressure. Avogadro's law states $V_1/n_1 = V_2/n_2$ at constant $P$ and $T$: adding more molecules requires the container to expand to keep the pressure constant.

---

Flashcards for this section are as follows:

- the ideal gas equation in terms of the number of molecules $N$ and the Boltzmann constant $k_B$ ::@:: $PV = Nk_BT$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the ideal gas equation in terms of the amount $n$ and the ideal gas constant $R$ ::@:: $PV = nRT$, reached through $N = nN_A$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the value of the Boltzmann constant $k_B$ ::@:: $1.38 \times 10^{-23}\ \text{J/K}$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the value of Avogadro's number $N_A$ ::@:: $6.022 \times 10^{23}\ \text{mol}^{-1}$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the value of the ideal gas constant $R$ ::@:: $8.31\ \text{J mol}^{-1}\text{K}^{-1}$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the people whose work the ideal gas equation culminates: the three named ::@:: Robert Boyle, Jacques Charles, and Joseph Louis Gay-Lussac. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- Boyle's law: the relationship when $T$ and $n$ are constant ::@:: $P_1V_1 = P_2V_2$: decreasing volume increases pressure. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- Charles's law: the relationship when $P$ and $n$ are constant ::@:: $V_1/T_1 = V_2/T_2$: heating increases volume. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- Gay-Lussac's law: the relationship when $V$ and $n$ are constant ::@:: $P_1/T_1 = P_2/T_2$: heating increases pressure. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- Avogadro's law: the relationship when $P$ and $T$ are constant ::@:: $V_1/n_1 = V_2/n_2$: adding molecules increases volume. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the kinetic-theory definition of the pressure $P$ on a wall of area $A$ ::@:: $P = \frac{1}{A}\frac{dp}{dt}$, the momentum delivered to the wall per unit area per unit time. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- with each collision reversing $v_x$ and delivering $\Delta p = 2mv_x$: the momentum the wall gains within time $dt$, and the pressure it gives ::@:: $dp = \int 2mv_x \cdot \tfrac{1}{2} n f(v_x) v_x A\,dt\,dv_x = nmA\langle v_x^2\rangle\,dt$, so dividing by $A\,dt$ gives $P = nm\langle v_x^2\rangle$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the pressure $P = \frac{1}{A}\frac{dp}{dt}$ on a wall of area $A$: how the molecules that hit it within time $dt$ are counted ::@:: Molecules with velocity component in $[v_x, v_x + dv_x]$ toward the wall hit only if they sit within thickness $v_x\,dt$ of it, so the count is $\tfrac{1}{2} n f(v_x)\,dv_x \cdot A \cdot v_x\,dt$, half the molecules heading toward the wall by symmetry. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- equipartition applied to one translational degree of freedom: what it gives for $\langle v_x^2\rangle$ ::@:: $\tfrac{1}{2}m\langle v_x^2\rangle = \tfrac{1}{2}k_BT$, so $\langle v_x^2\rangle = k_BT/m$, each quadratic degree of freedom carrying $\tfrac{1}{2}k_BT$ in equilibrium. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the isotropy of an equilibrium gas: what it gives for the mean square speed $\langle v^2\rangle$ ::@:: $\langle v^2\rangle = 3\langle v_x^2\rangle$, so $\langle v^2\rangle = 3k_BT/m$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- substituting $\langle v_x^2\rangle = k_BT/m$ into $P = nm\langle v_x^2\rangle$: the ideal gas law it yields ::@:: $P = \frac{N}{V}k_BT$, which rearranges to $PV = Nk_BT$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## equipartition of energy

The average molecular kinetic energy of the gas is proportional to the absolute temperature, and the internal energy $U$ is proportional to that average. Writing the average as $\bar K$, the internal energy is $U = N\bar K = nN_A\bar K$. The internal energy is distributed equally among the $f$ degrees of freedom of the system, which gives $\bar K = \frac{f}{2}k_BT$ and $U = \frac{f}{2}nRT$.

---

Flashcards for this section are as follows:

- the average molecular kinetic energy and the absolute temperature: how the two are related ::@:: The average molecular kinetic energy is proportional to the absolute temperature. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the internal energy $U$ in terms of the average molecular kinetic energy $\bar K$ and the number of molecules $N$ ::@:: $U = N\bar K = nN_A\bar K$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- equipartition: the average kinetic energy per molecule in terms of $f$, $k_B$, and $T$ ::@:: $\bar K = \frac{f}{2}k_BT$; the internal energy is distributed equally among the $f$ degrees of freedom. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- equipartition: the internal energy $U$ in terms of $f$, $n$, $R$, and $T$ ::@:: $U = \frac{f}{2}nRT$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

## molar heat capacity

The heat capacity of a body is $C = Q/\Delta T = \Delta U/\Delta T$, and its molar heat capacity at constant volume is $C_V = C/n$. A gas held at constant volume does no work, so the heat added equals the change in internal energy, $Q = \Delta U$. Combining this with the equipartition result gives $C_V = \frac{dU}{n\,dT} = \frac{fR}{2}$, so measuring $C_V$ is a way to measure $f$. At constant pressure the heat capacity is larger by one gas constant, $C_p = C_V + R$.

---

Flashcards for this section are as follows:

- heat capacity $C$ in terms of the heat $Q$ and the temperature change $\Delta T$ ::@:: $C = Q/\Delta T = \Delta U/\Delta T$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the molar heat capacity at constant volume $C_V$ in terms of $C$ and the amount $n$ ::@:: $C_V = C/n$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the molar heat capacity at constant volume $C_V$ in terms of $f$ and the gas constant $R$ ::@:: $C_V = \frac{dU}{n\,dT} = \frac{fR}{2}$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- how the number of degrees of freedom $f$ is measured ::@:: From the measured molar heat capacity, through $C_V = \frac{fR}{2}$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the relation between $C_p$ and $C_V$ with the gas constant $R$ ::@:: $C_p = C_V + R$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

### gases

Real gases at ordinary temperatures are close to the classical value of $C_V$ when their molecules are simple. The polyatomic gases measure above that classical value, which for them is $f = 6$.

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

- helium and argon: the $f$ they correspond to and their measured $C_V$ ::@:: $f = 3$, the monatomic value, with $C_V = 12.5$ for helium and $12.6$ for argon. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- nitrogen and oxygen: the $f$ they correspond to and their measured $C_V$ ::@:: $f = 5$, the diatomic value, with $C_V = 20.7$ for nitrogen and $20.8$ for oxygen. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the polyatomic gases of the table: their classical $f$ and their measured $C_V$ ::@:: $f = 6$, with $C_V = 29.1$ for ammonia and $29.7\ \text{J mol}^{-1}\text{K}^{-1}$ for carbon dioxide. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

### large molecules

A large molecule has far more degrees of freedom than a small one, and its molar heat capacity scales with them. An alpha helix of a protein has a molar heat capacity of about $800\ \text{cal mol}^{-1}\text{K}^{-1}$, which is $400R$, so $f = 800$. The protein chymotrypsinogen is larger still: about $9000\ \text{cal mol}^{-1}\text{K}^{-1}$, or $4500R$, giving $f = 9000$.

---

Flashcards for this section are as follows:

- the alpha helix: its molar heat capacity in $\text{cal mol}^{-1}\text{K}^{-1}$ and in $R$, and the $f$ it gives ::@:: About $800\ \text{cal mol}^{-1}\text{K}^{-1} = 400R$, giving $f = 800$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- chymotrypsinogen: its molar heat capacity in $\text{cal mol}^{-1}\text{K}^{-1}$ and in $R$, and the $f$ it gives ::@:: About $9000\ \text{cal mol}^{-1}\text{K}^{-1} = 4500R$, giving $f = 9000$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

## limits of the classical model

The classical result $C_V = \frac{fR}{2}$ holds at every temperature, but measurement does not. Each degree of freedom contributes its share of $\frac{R}{2}$ only above the temperature at which it is excited, and classical physics gives no reason for that temperature.

---

Flashcards for this section are as follows:

- the classical prediction for $C_V$ against temperature, and what measurement shows instead ::@:: The classical $C_V = \frac{fR}{2}$ is constant in temperature, while measurement shows it rising in steps as further degrees of freedom become active. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

### constant-volume plateaus

Plotted against temperature, the ratio $c_V/R$ sits at a plateau of $3/2$ while only the three translational degrees of freedom are active, rises to $5/2$ once rotation becomes active, and reaches $7/2$ once vibration does.

---

Flashcards for this section are as follows:

- the three plateaus of $c_V/R$ as the temperature rises, and what is active at each ::@:: $3/2$ with only translation active, $5/2$ once rotation is active, and $7/2$ once vibration is active. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

### constant-pressure levels

The same failure shows in the constant-pressure heat capacity, $C_p = C_V + R$, measured in $\text{kJ kmol}^{-1}\text{K}^{-1}$ over the range from $300\ \text{K}$ to about $3500\ \text{K}$. The noble gases argon, helium, neon, krypton, xenon, and radon hold a flat line at the level of $f = 3$ across the whole range, while air climbs towards $f = 5$, hydrogen towards $f = 6$, and carbon dioxide towards $f = 13$, the last still rising at $3000\ \text{K}$. Water vapour and oxygen rise between them.

---

Flashcards for this section are as follows:

- at constant pressure, the level of $f$ each of the named gases approaches over $300\ \text{K}$ to $3500\ \text{K}$ ::@:: $f = 3$ for argon, helium, neon, krypton, xenon, and radon; $f = 5$ for air; $f = 6$ for hydrogen; and $f = 13$ for carbon dioxide. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

<!-- check: ignore-next-line[header_style]: proper noun -->
## Maxwell–Boltzmann distribution

Maxwell derived the distribution of molecular speeds in the 1850s, and Boltzmann made the calculation more rigorous by 1895, so the result is called the Maxwell–Boltzmann distribution. For $N$ molecules of mass $m$ at temperature $T$, the number of molecules with speeds near $v$ follows $$f(v) = 4\pi N\left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2 e^{-mv^2/(2k_B T)},$$ where $k_B$ is the Boltzmann constant. The peak of the curve sits at the most probable speed for that temperature. Nitrogen at $300$, $1000$, and $4000\ \text{K}$ shows what raising the temperature does: the peak moves to higher speed while the curve spreads and flattens. Measurement was not precise enough in 1895 to check the shape, and experiment confirmed it in 1921.

The whole derivation sits on the density of the velocity triple $(v_x, v_y, v_z)$, and the Boltzmann factor separates as $e^{-m(v_x^2+v_y^2+v_z^2)/(2k_BT)}$. Normalising this over all velocities gives $$p(v_x, v_y, v_z) = \left(\frac{m}{2\pi k_BT}\right)^{3/2} e^{-m(v_x^2+v_y^2+v_z^2)/(2k_BT)},$$ the product of three identical one-dimensional normal densities, one per component. This object is the multivariate normal distribution, here in three dimensions, with zero mean and covariance matrix $(k_BT/m) I$, the number $k_BT/m$ times the identity matrix. The same covariance in every direction makes the density spherically symmetric, so it depends on the velocity only through $v^2 = v_x^2+v_y^2+v_z^2$, and each component is an independent normal random variable with mean $0$ and variance $k_BT/m$.

The speed distribution is the radial part of that multivariate normal. In spherical coordinates a shell of radius $v$ and thickness $dv$ has volume $4\pi v^2\,dv$, so its share of the probability is $4\pi v^2 p(v_x,v_y,v_z)\,dv$, the density evaluated at $v^2 = v_x^2+v_y^2+v_z^2$. Multiplying by the $N$ molecules gives $$f(v) = 4\pi N\left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2 e^{-mv^2/(2k_B T)},$$ the $f(v)$ of the first paragraph, and the factor $v^2$ comes from the geometry of the shell rather than from the Gaussian itself. Equivalently, the distribution of $v/\sqrt{k_BT/m}$ is the chi distribution with three degrees of freedom, the magnitude $\sqrt{z_1^2+z_2^2+z_3^2}$ of three independent standard normal variables $z_1$, $z_2$, $z_3$. Unlike the symmetric multivariate normal behind it, the speed distribution lives only on $v\geq0$ and is right-skewed, which shows in the order of its three characteristic speeds: the most probable $v_p = \sqrt{2k_BT/m}$, the mean $\bar v = \sqrt{8k_BT/(\pi m)}$, and the root-mean-square $v_{rms} = \sqrt{3k_BT/m}$.

The aggregate level turns normal for a different reason: a quantity that adds very many independent molecular contributions approaches a normal distribution by the central limit theorem.

---

Flashcards for this section are as follows:

- the Maxwell–Boltzmann distribution $f(v)$ for $N$ molecules of mass $m$ at temperature $T$, with $k_B$ the Boltzmann constant ::@:: $f(v) = 4\pi N\left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2 e^{-mv^2/(2k_B T)}$, the number of molecules with speeds near $v$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what the peak of the Maxwell–Boltzmann speed distribution of a gas gives ::@:: The most probable speed of a molecule at that temperature. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what raising the temperature $T$ does to the Maxwell–Boltzmann speed distribution of nitrogen ::@:: The peak moves to higher speed and the curve spreads and flattens, as the $300$, $1000$, and $4000\ \text{K}$ curves show. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what distribution the density $p(v_x, v_y, v_z)$ of the velocity triple of an equilibrium gas is ::@:: a multivariate normal distribution, the product of three identical one-dimensional normal densities, one per component. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the mean and covariance matrix of the multivariate normal followed by the molecular velocities of a gas at temperature $T$ ::@:: mean zero and covariance matrix $(k_BT/m) I$, the number $k_BT/m$ times the identity matrix, so the density is spherically symmetric. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why the speed distribution $f(v)$ carries the factor $v^2$ ::@:: the shell geometry: in spherical coordinates the shell at radius $v$ has volume $4\pi v^2\,dv$, so it collects $4\pi v^2 p(v_x,v_y,v_z)$ of the multivariate normal. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what distribution $v/\sqrt{k_BT/m}$ has, in terms of independent standard normal variables $z_1$, $z_2$, $z_3$ ::@:: the chi distribution with three degrees of freedom, the distribution of $\sqrt{z_1^2+z_2^2+z_3^2}$, scaled by $\sqrt{k_BT/m}$ to give $v$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- how the Maxwell–Boltzmann speed distribution $f(v)$ differs in shape from the multivariate normal it derives from ::@:: it lives only on $v\geq 0$, rises from zero and tails off asymmetrically, where the multivariate normal is symmetric about its zero mean. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the order of the most probable, mean, and root-mean-square speeds $v_p$, $\bar v$, and $v_{rms}$ of a Maxwell–Boltzmann gas at temperature $T$ ::@:: $v_p = \sqrt{2k_BT/m} < \bar v = \sqrt{8k_BT/(\pi m)} < v_{rms} = \sqrt{3k_BT/m}$, the order a right-skewed distribution produces. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- which theorem makes an aggregate gas property that sums very many independent molecular contributions take a normal distribution ::@:: the central limit theorem. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## effusion and diffusion

Effusion is the escape of gas molecules through a tiny hole into a vacuum, and diffusion is the intermixing of different gases driven by concentration gradients. Graham's law of effusion states that the rate of effusion of a gas is inversely proportional to the square root of its molar mass: $\text{Rate}_1/\text{Rate}_2 = \sqrt{m_2/m_1}$. At the same temperature, lighter molecules have a higher root-mean-square speed, $v_{\text{rms}} = \sqrt{3k_BT/m}$, so they effuse and diffuse faster. Hydrogen, the lightest gas, effuses roughly four times faster than oxygen.

---

Flashcards for this section are as follows:

- effusion: what it is ::@:: The escape of gas molecules through a tiny hole into a vacuum. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- diffusion: what it is ::@:: The intermixing of different gases driven by concentration gradients. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- Graham's law: the relationship between effusion rate and molar mass ::@:: $\text{Rate}_1/\text{Rate}_2 = \sqrt{m_2/m_1}$: the rate is inversely proportional to the square root of the molar mass. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- root-mean-square speed: its formula ::@:: $v_{\text{rms}} = \sqrt{3k_BT/m}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

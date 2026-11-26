---
aliases:
  - RL
  - reinforcement learning
tags:
  - flashcard/active/special/academia/HKUST/SOSC_1960/reinforcement_learning
  - language/in/English
---

# reinforcement learning

Reinforcement learning is learning from the consequences of an action rather than from a labelled example. An agent acts, receives a reward, and changes how it chooses next time. The reward is the only feedback it gets.

---

Flashcards for this section are as follows:

- what reinforcement learning learns from ::@:: The consequences of an action.
- what an agent changes once a reward arrives ::@:: How it chooses next time.
- what feedback an agent learning by reinforcement gets ::@:: A reward, and no labelled answer for each input.
- what the abbreviation RL stands for in machine learning ::@:: Reinforcement learning.

## from conditioning

Psychology had long modelled animal learning with simple update rules, the Rescorla and Wagner model of 1972 among them. Those models describe [classical conditioning](classical%20conditioning.md) and [operant conditioning](operant%20conditioning.md). They inspired some of the earliest reinforcement-learning algorithms, including the 1981 algorithm of Richard Sutton and Andrew Barto, which came out of classical conditioning. The borrowing ran from psychology into computing.

---

Flashcards for this section are as follows:

- the kind of rule psychology's models of animal learning use ::@:: Simple update rules.
- the named animal-learning model built from a simple update rule ::@:: The Rescorla and Wagner model of 1972.
- what animal-learning models with simple update rules inspired ::@:: Some of the earliest reinforcement-learning algorithms.
- what Richard Sutton and Andrew Barto's 1981 algorithm came out of ::@:: Models of classical conditioning.
- the direction the ideas were borrowed between psychology and computing ::@:: From psychology into computing.

## learning algorithms

### reward prediction error

An agent learns from the gap between the reward it expected and the reward it got. The gap is the reward prediction error, central to reinforcement-learning (RL) algorithms (Sutton & Barto, 1998). In the late 1990s that error matched the firing of dopamine neurons in learning experiments (Schultz et al., 1997). A machine-learning term named a signal the brain carries.

---

Flashcards for this section are as follows:

- what a reinforcement-learning agent learns from ::@:: The gap between the reward it expected and the reward it got.
- the name for the gap between the reward an agent expects and the reward it receives ::@:: The reward prediction error.
- what the reward prediction error is central to ::@:: Reinforcement-learning (RL) algorithms (Sutton & Barto, 1998).
- what the reward prediction error matched in the late 1990s ::@:: The firing of dopamine neurons in learning experiments (Schultz et al., 1997).
- what a machine-learning term turned out to name ::@:: A signal the brain carries.

### deep reinforcement learning

Deep reinforcement learning pairs deep networks with reinforcement-learning algorithms. A network mastered Go, long thought far harder than chess for a machine (Silver et al., 2016). Another reached human-level play in Atari games from pixel-level data (Mnih et al., 2015). Later algorithms learned many games and environments with little or no human intervention (Silver et al., 2018).

---

Flashcards for this section are as follows:

- what deep reinforcement learning adds to reinforcement-learning algorithms ::@:: Deep networks.
- what pairing deep networks with reinforcement-learning algorithms produced ::@:: The game-playing results.
- the board game a deep network mastered, long thought far harder than chess for a machine ::@:: Go (Silver et al., 2016).
- the input a suite of Atari games was learned from ::@:: Pixel-level data (Mnih et al., 2015).
- the level of play a deep network reached in a suite of Atari games ::@:: Human level.
- what later deep reinforcement-learning algorithms managed with little or no human intervention ::@:: Learning many games and environments (Silver et al., 2018).

## references

- Mnih, V., Kavukcuoglu, K., Silver, D., et al. (2015). [Human-level control through deep reinforcement learning](https://doi.org/10.1038/nature14236). _Nature_, _518_(7540), 529-533.
    - Source of the Atari result.
- O'Toole, A. J., & Ludvig, E. A. (2026). [The use of AI in psychology: A historical perspective](https://doi.org/10.1111/bjop.70061). _British Journal of Psychology_, _117_(2).
    - Source of the material on animal-learning models and the earliest reinforcement-learning algorithms, the reward prediction error, and deep reinforcement learning.
    - Open access under a Creative Commons license; the publisher footer does not name the variant.
- Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian conditioning: Variations in the effectiveness of reinforcement and nonreinforcement. In A. H. Black & W. F. Prokasy (Eds.), _Classical conditioning II: Current research and theory_ (pp. 64-99). Appleton-Century-Crofts.
    - The model of 1972 named in the text.
- Schultz, W., Dayan, P., & Montague, P. R. (1997). [A neural substrate of prediction and reward](https://doi.org/10.1126/science.275.5306.1593). _Science_, _275_(5306), 1593-1599.
    - Source of the dopamine neuron result.
- Silver, D., Huang, A., Maddison, C. J., et al. (2016). [Mastering the game of Go with deep neural networks and tree search](https://doi.org/10.1038/nature16961). _Nature_, _529_(7587), 484-489.
    - Source of the Go result.
- Silver, D., Hubert, T., Schrittwieser, J., et al. (2018). [A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play](https://doi.org/10.1126/science.aar6404). _Science_, _362_(6419), 1140-1144.
    - Source of the later algorithms that learned several games.
- Sutton, R. S., & Barto, A. G. (1981). [Toward a modern theory of adaptive networks: Expectation and prediction](https://doi.org/10.1037/0033-295X.88.2.135). _Psychological Review_, _88_(2), 135-170.
    - Source of the 1981 algorithm and its origin in classical conditioning.
- Sutton, R. S., & Barto, A. G. (1998). _Reinforcement learning: An introduction_. MIT Press.
    - The text the reward prediction error is credited to.
- \[missing\].
    - Source of the claim that models of animal learning inspired the earliest reinforcement-learning algorithms.

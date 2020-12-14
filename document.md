# Fabric: Transfer API

This may be revised if there are problems with the API while implementing it.

## Goals
- To facilitate the transfer of transferable between participants.
### Non-goals
- To impose constraints on the logic of transfers.
- To impose constraints on how participants store and represent their states.


## Definitions
- **Transfer**
  the relocation of an arbitrary amount of transferable between multiple participants
- **Transferable**
  a instance of an arbitrary type with arbitrary data that can be transferred
- **Participant**
  an arbitrary entity that can be involved in transfers
- **Controller**
  an arbitrary entity which executes the logic of transfers
### Rationale
An API should only constrain things that are part of its goal.
Anything out of scope of the goal should not be constrained.

This ensures that independent systems can work together well without giving special treatments to other systems.
Implementations can have a greater freedom when implementing the API.
Maintability is high as there are less constraints, which could be violated through reasons such as the complex interactions between different systems, made by the API.

To achieve this, only essential things are specified.
- **Transfer** is a part of the goal of this API and thus defined.
- **Transferable** represents the information being transferred in transfers.
- **Participant** represents the starting point(s) and ending point(s) of transfers.
- **Controller** represents the consumer of this API.


## Design
The API is designed with the following rules in mind:
- Clear separation of concerns. Each interface should only handle one concern.  This allows selective implementation of capabilities.
- Expose as much information as the consumer actually needed. This reduces the implementation burden and avoids accidental violation of constraints due to the consumer.
- The API should be abstract.  The API is unlikely to be able to accomdate everything - there are almost always special cases that does not work well with the API.  However, this does not mean we should try to accomdate as much as we can.  Abstraction can help with this by remove unneeded dependencies on any particular one or one set of implementation, but instead only rely on the necessary aspects of implementations.  There may still be special cases and unremovable-but-unnecessary dependencies, but with some careful designing, most or even all of them can be avoided.
- The API should be generalized.  The zero-one-infinity rule can explain this.  Applied to this API, it means this API should not exist, should be extremely specialized for one and only one thing, or should be generalized for infinitely many cases (in the architectural aspect, we still need to respect constraints imposed by other aspects).  The fist case is...  inappropriate for obvious reasons.  Indeed, there may indeed be cases where all three of these does not make sense, such as booleans, but considering that transfer can be applied to a lot of things, the last case makes the most sense for this API.
- Low allocation.  As the API is likely to be called frequently within a Minecraft tick, small allocations in the API may contrib significantly to the allocation pressure.  However, that does not mean allocation needs to be avoided completely as Java is designed to handle a large range of allocation pressure.
- Performant.  As the API is likely to be called frequently within a Minecraft tick, there should be as little overhead when using the API.  Performance penalties that comes from the implementation should not be attributed to the API, though the API should be designed in such a way that it is easy to implement the API performantly.
- Immutable objects are preferred.  Immutability ensures correctness.  They also play well in multithreaded enviroments (just in case this API becomes multithreadable :p).  As for allocation, profiling is needed.  The source of allocation of immutable objects comes from immutable objects is manipulation of state, while that of mutable objects comes from making defensive copies.  For generational garbage collectors, immutable objects are easier to collect than mutable objects as generational garbage collectors assume that most references are young objects pointing to young or old objects instead of old objects pointing to young objects.  Mutable objects can violate that due to the setter where it is possible to make a young object be referenced by the old mutable object.  This is not possible with immutable objects.

Note that we do not need to follow all the rules strictly - there may be conflicts among them.
In that case, a compromise is needed.
However, a best effort should be made to avoid conflicts and follow the rules strictly.

To respect the separation of concerns, each section should only describe one interface.
Apart from that, accessibility rules will be designated below:

|entity             |accessible entities in the API                    |
|-------------------|--------------------------------------------------|
|API                |transferable, participant                         |
|transferable       |(none)                                            |
|participant        |transferable                                      |
|controller         |API, transferable, participant                    |

This means that the entity in the left column should only access entities in the right column.

Note that API and controller will not have an interface.
This is because the API is for describing the collection of interfaces,
while the controller is just an alias for the consumer of the API of which the API should not care.

### Transferable
A transferable have the following properties:
- type
- data

They are used together to determine whether multiple transferable are compatabile.
It should be immutable.

#### Data-only
A transferable could be designed to have only one property, which is data.
However, in Minecraft, there are registeries that are pretty much fixed.
Apart from that, the API is much more likely to handle transferabale with no special data attached to it.
This and the limited amount of types can be used to cache transferable to reduce memory allocation pressure.  Immutability is required to support this.
The type property is used for such purposes.
#### Amount property
Amount is not included in transferable as it is an extrinsic property.
Think of one item of type A and many items of type A.
The properties of the one item and each item from the stash of item in isolation should be the same.
Apart from that, this would break the type property optimization.
#### Conversion functions
Conversion functions could be added to the transferable, but that is of no concern to the API itself.
However, this may be of concern to the implementors of participants.  Actually implementing is needed to figure out whether it is suitable for the API.


### Participant
A participant have the following functions:
- (TODO: Simulation, transaction, mix of both, or other exotic methods?)
#### Merging insert and extract
Insert and extract could be merged together into one function that allows for negative amount.
However, this does not really offer much benefits.
The disadvantage is that people may get confused over what negative values mean.
#### Check transfer function
Check transfer functions allow for transfers that do not change the state of the participants.
##### Need for checking
If only transfers that changes the state is allowed,
if a less than desireable transfer happen such as not fulfilling the full amount,
the only way to rollback is to call the opposite transfer method.
However, this may not always be possible.

Check transfer functions allow for the execution of the transfer be dependent on the predicted execution of the transfer.
##### Check and transfer relationship
In order to make the check transfer function useful, some constraints are required.
Given the same state and the same input, the transfer function and the check transfer function should return the same result.
This is to establish a relationship between checking and execution.


## Implementation
(TODO: this will be about implementation, such as whether the amount should be a fraction, ect.)


## Conjectures
These, while seems to make sense, needs statistics to be proven.
- It is much more likely that a constructed transferable does not have data rather than having data in all conditions.

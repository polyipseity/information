# Fabric: Transfer & View API

This may be revised if there are problems with the API while implementing it.

## Goals
- To facilitate the transfer of content between participants.
- To provide an unified way to access view content.
- To provide an unified way to manipuate view content.
### Non-goals
- To impose constraints on the logic of transfers.
- To impose constraints on how participants store and represent their states.
- To impose constraints on allowed content of views.


## Definitions
- **Content**
  a instance of an arbitrary type with arbitrary data that can be transferred or stored
- **Transfer**
  the relocation of an arbitrary amount of content between multiple participants
- **Participant**
  an arbitrary entity that can be involved in transfers
- **Controller**
  an arbitrary entity which executes the logic of transfers
- **View**
  an arbitrary entity that contains content

### Rationale
An API should only constrain things that are part of its goal.
Anything out of scope of the goal should not be constrained.

This ensures that independent systems can work together well without giving special treatments to other systems.
Implementations can have a greater freedom when implementing the API.
Maintability is high as there are less constraints, which could be violated through reasons such as the complex interactions between different systems, made by the API.

To achieve this, only essential things are specified.
- **Content** represents the information being transferred in transfers and things stored in views.
- **Transfer** is a part of the goal of this API and thus defined.
- **Participant** represents the starting point(s) and ending point(s) of transfers.
- **View** represents the storage of content.
- **Controller** represents the consumer of this API.


## Design
The API is designed with the following rules in mind:
- Clear separation of concerns.<br>
  Each interface should only handle one concern.  This allows selective implementation of capabilities.<br>
  For this reason, the transfer API and the view API are separate interfaces.

- Expose as much information as the consumer actually needed.<br>
  This reduces the implementation burden and avoids accidental violation of constraints due to the consumer.

- The API should be abstract.<br>
  The API is unlikely to be able to accomdate everything - there are almost always special cases that does not work well with the API.<br>
  However, this does not mean we should try to accomdate as much as we can.<br>
  Abstraction can help with this by remove unneeded dependencies on any particular one or one set of implementation, but instead only rely on the necessary aspects of implementations.<br>
  There may still be special cases and unremovable-but-unnecessary dependencies, but with some careful designing, most or even all of them can be avoided.

- The API should be generalized.<br>
  The zero-one-infinity rule can explain this.<br>
  Applied to this API, it means this API should not exist, should be extremely specialized for one and only one thing, or should be generalized for infinitely many cases (in the architectural aspect, we still need to respect constraints imposed by other aspects).<br>
  The fist case is...  inappropriate for obvious reasons.<br>
  Indeed, there may indeed be cases where all three of these does not make sense, such as booleans, but considering that transfer can be applied to a lot of things, the last case makes the most sense for this API.

- Low allocation.<br>
  As the API is likely to be called frequently within a Minecraft tick, small allocations in the API may contrib significantly to the allocation pressure.<br>
  However, that does not mean allocation needs to be avoided completely as Java is designed to handle a large range of allocation pressure.  This includes high allocation pressure that Minecraft is already applying.

- Performant.<br>
  As the API is likely to be called frequently within a Minecraft tick, there should be as little overhead when using the API.<br>
  Performance penalties that comes from the implementation should not be attributed to the API, though the API should be designed in such a way that it is easy to implement the API performantly.

- Immutable objects are preferred.<br>
  Immutability ensures correctness.  They also play well in multithreaded enviroments (just in case this API becomes multithreadable :p).<br>
  As for allocation, profiling is needed.  The source of allocation of immutable objects comes from immutable objects is manipulation of state, while that of mutable objects comes from making defensive copies.<br>
  For generational garbage collectors, immutable objects are easier to collect than mutable objects as generational garbage collectors assume that most references are young objects pointing to young or old objects instead of old objects pointing to young objects.  Mutable objects can violate that due to the setter where it is possible to make a young object be referenced by the old mutable object.  This is not possible with immutable objects.

- Consistency.<br>
  The layout of the API should be structually equal for each cases that the API handles.

Note that we do not need to follow all the rules strictly - there may be conflicts among them.
In that case, a compromise is needed.
However, a best effort should be made to avoid conflicts and follow the rules strictly.

To respect the separation of concerns, each section should only describe one interface.
Apart from that, accessibility rules will be designated below:

|entity             |accessible entities in the API                    |
|-------------------|--------------------------------------------------|
|API                |content, participant, view                        |
|content            |(none)                                            |
|participant        |content                                           |
|view               |content                                           |
|controller         |API, content, participant, view                   |

This means that the entity in the left column should only access entities in the right column.

Note that API and controller will not have an interface.
This is because the API is for describing the collection of interfaces,
while the controller is just an alias for the consumer of the API of which the API should not care.

### Content
A content have the following properties:
- type, instance of category
- data, arbitrary
- category, class

They are used together to determine whether multiple content are compatabile.
Category is used to allow participants to quickly filter the type accepted.
It should be immutable.

#### Data-only
A content could be designed to have only one property, which is data.

However, in Minecraft, there are registeries that are pretty much fixed.
Apart from that, the API is much more likely to handle transferabale with no special data attached to it.
This and the limited amount of types can be used to cache content to reduce memory allocation pressure.  Immutability is required to support this.

The type property is used for such purposes.
#### Amount property
Amount is not included in content as it is an extrinsic property.
Think of one item of type A and many items of type A.
The properties of the one item and each item from the stash of item in isolation should be the same.
Apart from that, this would break the type property optimization.
#### Conversion functions
Conversion functions could be added to the content, but that is of no concern to the API itself.
However, this may be of concern to the implementors of participants.  Actually implementing is needed to figure out whether it is suitable for the API.
#### Category
Implementations usually only handles a subset of types.
This is true because content can contain anything, even things unexpected.
Usually the types are instances of the same class.
Category is used to provide the class of the type.


### Participant
A participant have the following functions:
- insert with context, type, and amount
- extract with context, type, and amount
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
Given the same state and the same input, the same output should be returned in all cases.
This is to establish a relationship between checking and execution.
##### Informal analysis
Given that the API should handle transfers only, there are only 2 things matter to the API:
- transfer: depends on state, changes state
- check: depends on state, keeps state

We can treat transfer as some sort of a barrier, i.e. once a transfer has occured, all previous checks are invalidated.
This is due to the state changing, which invalidates all previous results of checks which depends on the previous state.
This will be important in later sections.
##### Multiple actions
To reduce allocation, all functions in participants will not accept multiple actions.
However, this poses a question.

Some controllers may want to treat multiple actions as one atomic operation.
This, however, will not work with check and transfer.

This is due to the fact that transfer only accepts one action at a time, yet it invalidates all the previous checks.
A new check could be made, but the operation will no longer be atomic, i.e., cannot always rollback.

Checking multiple actions without changing the state is impossible here, yet we still need to somehow be able to rollback.
Since we know nothing about participants, participants will have to provide their own rollback code.

However, since multiple actions are controlled by the controller, the rollback code cannot be executed by the participants itself.  The controller will need to execute the code.

Also, rollback code between multiple actions may involve multiple participants, so the rollback code should be stored in the controller instead.

To sum it up, we need a mechanism for participants to pass their rollback code to the controller.  A context object is purposed to be used for such purposes.  The functions will be passed the context object, which allows the participants to manipulate the context object in ways allowed by the context object.
#### Context
A context holds the context in which the transfer is executed in.

It is originally designed to store rollbacks.
Later, it is generalized into something that determines how the transfer should be run.

The current design is that the context controls the mode of the transfer which is determined by the controller.
To support any participant state manipulation action, two `Runnable`s are accepted, one is for the action and another one is for the rollback action.
A context may do anything with the provided two actions.


## Compatibility
### Vanilla
Vanilla transfers and views are simple, so it should be trivial to adapt them to the API.

The vanilla implementation is slightly inefficient, so adapters could optimize the implementations of the API for vanilla things.

### Existing similar APIs
The API should be compatible with most similar existing APIs reasonably well
due to the low amount of constraints imposed by the API.
Adapters should be made in order to achieve this.


## Implementation

### Provider API
The Provier API is recently introduced to Fabric.
It allows consumers of the API to lookup an API object for an object.
This can be used to provider transfer and view capability to the object.

However, it is limited to blocks and items only, though custom lookups can be made.
#### `ItemApiLookup` replacement
The default `ItemApiLookup` provided by the provider API accepts `ItemStack` as its keys.
However, the intention of `ItemApiLookup` seems to be about providing capability to an `Item` instead of an `ItemStack` as hinted by its name.
Moreover, this is inconsistent with `BlockApiLookup`, where a `Block` is accepted instead.

To improve consistency, a custom `ItemApiLookup` is provided which accepts `ItemConvertible` instead of `ItemStack` as its key.
#### `XXXLookupContext`
The provider API allows us to pass a context object to the API provider.

In order to ensure easy transition consumers of the API for future changes, such as the addition of new data in context,
a `XXXLookupContext` is created for each `XXXApiLookup`.
Any addition or deletion of fields can be buffered against by keeping the old factory method for the context.  The old factory method can be marked as deprecated if needed.

Whereas if the context object does not exist, addition of new fields requires breaking changes.
For example, `BlockLookupContext` only has the `direction` property now, which means it could be replaced with `Direction` directly.  However if at a later date, a new field is desired, the context will not be `Direction` anymore, forcing the consumers of the API to update in order to work.

### Built-in implementations
#### `Context`
For now, the API comes with 3 implementations:
- `SimulationContext`<br>
  It discards both the action and the rollback action.  Nothing occurs, can be used as a check for a single action.
  Ignores `#close`.
- `ExecutionContext`<br>
  Executes the action, discards the rollback action.  This can be used to execute a single action.
  Ignores `#close`.
- `TransactionContext`<br>
  Executes the action, stores the rollback action.  It can be used to use the API with transactions, as hinted by its name.
  Try-with-resources should be used.
  The default action is to run the rollback actions in reverse order of which they are added, which restores the states of participants.
  `#commit` clears the rollback action queue, which means the states of participants will not be restored.


## Conjectures
These, while seems to make sense, needs statistics to be proven.
- It is much more likely that a constructed content does not have data rather than having data in all conditions.
- It is much more likely that an atomic transfer operation as defined by the controller consists of one and only mone action.

# Fabric: Transfer API

## Goals
- To facilitate the transfer of transferable between participants.
### Non-goals
- To impose constraints on the logic of transfers.
- To impose constraints on how participants store and represent their states.

## Definitions
- **Transfer**
  the relocation of transferable between multiple participants
- **Transferable**
  an arbitrary amount of instances of an arbitrary type with arbitrary data that can be transferred
- **Participant**
  an arbitrary entity that can be involved in transfers
- **Controller**
  an arbitrary entity which executes the logic of transfers
### Rationale
An API should only constrain things that are part of its goal.
Anything out of scope of the goal should not be constrained.
This ensures that independent systems can work together well without giving special treatments to other systems.
Implementations can have a greater freedom when implementing the API.

To achieve this, only essential things are specified here.
**Transfer** is the goal of this API and thus defined.
**Transferable** represents the information being transferred.
**Participant** represents the starting point(s) and ending point(s) of transfers.
**Controller** represents the consumer of this API.

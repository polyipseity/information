---
aliases:
  - COMP 3511 cloud computing
  - cloud computing
  - cloud computing types
tags:
  - flashcard/active/special/academia/HKUST/COMP_3511/cloud_computing
  - language/in/English
---

# cloud computing

Cloud computing delivers computing, storage, and applications as a service over a network, and it is a logical extension of [virtualization](virtualization.md). Virtualization abstracts one physical machine into several execution environments; cloud computing turns that abstraction into capacity a customer rents on demand, so a provider can sell slices of shared hardware.

What separates a cloud from an ordinary server is scale. A large provider such as Amazon EC2 runs millions of servers, tens of millions of virtual machines, and petabytes of storage reachable across the Internet, and charges by usage rather than by machine.

---

Flashcards for this section are as follows:

- cloud computing definition ::@:: A computing platform that delivers computing, storage, or application services on demand over a network.
- cloud computing and virtualization ::@:: Cloud computing is a logical extension of virtualization, which it uses as the base for its functionality.
- why virtualization matters for cloud computing ::@:: Running many isolated execution environments on shared hardware is what lets a provider sell computing capacity on demand.
- scale of a large cloud provider ::@:: A provider such as Amazon EC2 offers millions of servers, tens of millions of virtual machines, and petabytes of storage available across the Internet.
- cloud computing billing model ::@:: The customer pays based on usage rather than owning the hardware, so storage, computation, and application access are charged as they are consumed.

## deployment models

Clouds are classified by who can use them. A __public cloud__ is open through the Internet to anyone willing to pay. A __private cloud__ is run by a company for its own use. A __hybrid cloud__ combines both, so workloads can be placed where they fit best.

---

Flashcards for this section are as follows:

- public cloud ::@:: A cloud available through the Internet to anyone willing to pay for it.
- private cloud ::@:: A cloud run by a company for the company's own use.
- hybrid cloud ::@:: A cloud that includes both public and private cloud components.

## service models

Clouds are also classified by how much of the stack the provider manages. __Software as a service__ offers applications over the Internet, such as a word processor. __Platform as a service__ offers a ready-to-use software stack, such as a database server. __Infrastructure as a service__ offers servers or storage, such as storage for backup. Providers keep adding further services of the same kind, such as machine learning as a service.

---

Flashcards for this section are as follows:

- software as a service ::@:: One or more applications made available over the Internet, for example a word processor.
- platform as a service ::@:: A software stack ready for application use over the Internet, for example a database server.
- infrastructure as a service ::@:: Servers or storage made available over the Internet, for example storage used for backup.
- machine learning as a service ::@:: A further service type of the same kind, offering machine learning over the Internet rather than as software the customer installs.

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

Cloud computing sells computing, storage, and applications as a service over a network. It is a logical extension of [virtualization](virtualization.md): virtualization splits one physical machine into several execution environments, and a cloud rents that capacity out by the slice, on demand, from shared hardware.

Scale is what separates a cloud from an ordinary server. A large provider such as Amazon EC2 runs millions of servers, tens of millions of virtual machines, and petabytes of storage across the Internet, and bills by usage rather than by machine.

---

Flashcards for this section are as follows:

- cloud computing definition ::@:: A platform that offers computing, storage, or application services on demand over a network. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- cloud computing and virtualization ::@:: Cloud computing is a logical extension of virtualization. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- why virtualization matters for cloud computing ::@:: Running many isolated execution environments on shared hardware lets a provider sell capacity on demand. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- scale of a large cloud provider ::@:: Amazon EC2 offers millions of servers, tens of millions of virtual machines, and petabytes of storage across the Internet. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- cloud computing billing model ::@:: The customer pays for use rather than owning hardware, and storage, computation, and application access are charged as consumed. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

## deployment models

Clouds differ in who may use them. A __public cloud__ is open over the Internet to anyone who pays. A __private cloud__ serves one company's own use. A __hybrid cloud__ mixes the two, so a workload can sit where it fits.

---

Flashcards for this section are as follows:

- public cloud ::@:: A cloud open over the Internet to anyone willing to pay. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- private cloud ::@:: A cloud a company runs for its own use. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- hybrid cloud ::@:: A cloud with both public and private parts. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

## service models

The other classification is how much of the stack the provider manages. __Software as a service__ delivers applications over the Internet, such as a word processor. __Platform as a service__ supplies a ready-to-use software stack, for instance a database server. __Infrastructure as a service__ is servers or storage, such as storage kept for backup. Providers keep adding more services of that kind, such as machine learning as a service.

---

Flashcards for this section are as follows:

- software as a service ::@:: One or more applications offered over the Internet, for example a word processor. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- platform as a service ::@:: A software stack ready to use over the Internet, for example a database server. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- infrastructure as a service ::@:: Servers or storage offered over the Internet, for example storage kept for backup. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- machine learning as a service ::@:: A later service of the same kind, offering machine learning over the Internet, so the customer installs no software. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

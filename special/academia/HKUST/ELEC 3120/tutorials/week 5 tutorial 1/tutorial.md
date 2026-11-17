---
aliases:
  - ELEC 3120 week 5 tutorial 1 tutorial
  - ELEC3120 week 5 tutorial 1 tutorial
  - HKUST ELEC 3120 week 5 tutorial 1 tutorial
  - HKUST ELEC3120 week 5 tutorial 1 tutorial
tags:
  - flashcard/active/special/academia/HKUST/ELEC_3120/tutorials/week_5_tutorial_1/tutorial
  - language/in/English
---

# tutorial

- HKUST ELEC 3120 week 5 tutorial 1
- parent: [week 5 tutorial 1](index.md)

## agent code review

Codex, a coding agent, reviews its own change. It compares the diff with the intent stated in the pull request, reads the codebase and its dependencies, and runs the code and its tests. A static analysis tool reads only the code, so it passes a change that is locally clean but does not do what was asked.

---

Flashcards for this section are as follows:

- how does an agent's code review differ from a static analysis tool? ::@:: It matches the stated intent of the change against the diff, reads the codebase and its dependencies, and runs the code and its tests.
- what does the agent compare the diff against? ::@:: The intent stated in the pull request.

## packet capture

`capture_packets.sh` captures a transfer between two virtual machines. The server machine receives on `10.0.1.1` port `3120` into a path given on the command line. The client machine is given the source file to send. `start <name>.pcap` begins the capture, `stop <name>.pcap` ends it once the transfer is done, and `analyze <name>.pcap` hands the file to Wireshark, which reports User Datagram Protocol traffic between `10.0.1.2` and `10.0.1.1`. Each packet carries the project's own header inside the payload.

---

Flashcards for this section are as follows:

- `capture_packets.sh`: which subcommand starts a capture, and which one opens it for analysis? ::@:: `start <name>.pcap` starts it, and `analyze <name>.pcap` opens it in Wireshark.
- in a captured transfer, which protocol does Wireshark report, and where does the project's header sit? ::@:: User Datagram Protocol between the two virtual machines; the project's own header sits inside the payload.

## protocol dissector

Wireshark reads the project's header through a Lua dissector, `tcp.lua`. It declares a protocol and one field per header item: an identifier, a source port, a destination port, a sequence number, an acknowledgement number, a header length, a packet length, a set of flags, an advertised window, an extension length, and the extension data. The declarations turn the payload into the named rows Wireshark shows.

---

Flashcards for this section are as follows:

- what does a Lua dissector such as `tcp.lua` give Wireshark? ::@:: The protocol's name and one field per header item, so a payload of bytes is shown as named rows and values.
- name the project's header fields in order, as the dissector declares them. ::@:: An identifier, a source port, a destination port, a sequence number, an acknowledgement number, a header length, a packet length, flags, an advertised window, an extension length, and the extension data.

## validation tests

Two tests check the implementation from outside, over loopback sockets, and read the packets it sends. The duplicate acknowledgement test sends a chosen number of duplicate acknowledgements and looks for the retransmission they should provoke. The flow control test sends a stream under a chosen advertised window and caps the transfer at a packet limit. It checks that the sender stops at the window and adapts when the window changes.

---

Flashcards for this section are as follows:

- how do the tests read what the implementation sent? ::@:: They drive it over loopback sockets and read the packets.
- flow control test: what does it vary, and what does it check about the sender? ::@:: The advertised window and the packet limit; the sender stops at the window and adapts when the window changes.

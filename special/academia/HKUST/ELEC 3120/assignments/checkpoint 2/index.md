---
aliases:
  - ELEC 3120 checkpoint 2
  - ELEC3120 checkpoint 2
  - HKUST ELEC 3120 checkpoint 2
  - HKUST ELEC3120 checkpoint 2
tags:
  - date/2026/10/09
  - flashcard/active/special/academia/HKUST/ELEC_3120/assignments/checkpoint_2/index
  - language/in/English
---

# checkpoint 2

- HKUST ELEC 3120

---

- title: Checkpoint 2: TCP Basics
- due: 2026-10-09T23:59:59+08:00
- points: \[missing\]
- submitting: \[missing\]

---

Tentative release: Monday 21/09

Tentative due date: 09/10 23:59

## late policy

- You have free 4 late days in total.
- You can use late days for assignments. A late day extends the deadline 24 hours.
- Once you have used all 4 late days, the penalty is 20% for each additional late day (5 days later there will be no points).
- Remember that any questions should go to Ed instead of emailing TAs or the professor.

## introduction

In this checkpoint, you need to implement a basic TCP with:

- Sequence number and acknowledgement number, and
- Sliding window.

The starter code is provided for you which is a stop-and-wait implementation built on UDP. You need to implement the seq/ack numbering and sliding window based on it.

## starter code

Compared to checkpoint 1, we provide more codes for you. You can use `git pull` to get the latest codes from our course Github repository.

```sh
git pull origin main
```

And switch to the `main` branch.

```sh
git checkout main
```

### `server.cc` and `client.cc`

The two sample applications for server and client.

### `foggy_tcp.cc`

The API exposed to application is defined in this file. There are four core functions whose signatures should not be changed: `foggy_socket()`, `foggy_close()`, `foggy_read()`, and `foggy_write()`. An application requests a new foggy-TCP socket by calling the foggy_socket function. The socket created in `foggy_socket()` is actually a UDP socket and our job is to enhance it to TCP.

### `foggy_backend.cc`

This file implements foggy-TCP's core logic which runs in a separate backend thread. This is important as TCP must be able to work independently from the application (i.e., receiving, acknowledging and retransmitting packets).

### `foggy_function.cc`

This file implements foggy-TCP's function logics. Most of your implementations may be here.

### `foggy_packet.cc`

This file implements helper functions to create and manipulate packets. Please do not modify this file.

## run the starter code

In this checkpoint and the following you need to use your own TCP (foggy-tcp) instead of system TCP. So use the following command to build foggy-tcp.

```sh
make foggy
```

In the server VM, at the `/vagrant/foggytcp` folder, run the server with the following command:

```sh
./server 10.0.1.1 3120 test.out
```

In the client VM, at the `/vagrant/foggytcp` folder, run the client with the following command:

```sh
./client 10.0.1.1 3120 src/client.cc
```

Now you have successfully transmitted the `client.cc` file from the client to the server, named as `test.out`.

## how to debug

A bash script `capture_packets.sh` is provided for you to capture and analyze network packets.

### packet capture

Converting file `capture_packets.sh` to Unix format.

```sh
sudo apt-get install dos2unix
dos2unix capture_packets.sh
```

Start packet capture.

```sh
sudo ./capture_packets.sh start <name>.pcap
```

Stop packet capture.

```sh
sudo ./capture_packets.sh stop <name>.pcap
```

### packet analyse

#### packet analyse using the bash script

```sh
sudo apt-get install tshark
sudo ./capture_packets.sh analyze <name>.pcap
```

Then you should see something like this, the first line being the command you ran:

```text
sudo ./capture_packets.sh analyze server.pcap
Running as user "root" and group "root". This could be dangerous.
tcp.lua is successfully loaded
frame.time_relative,ip.src,cmutcp.source_port,ip.dst,cmutcp.destination_port,cmutcp.seq_num,cmutcp.ack_num,cmutcp.hlen,cmutcp.plen,cmutcp.flags,cmutcp.advertised_window,cmutcp.extension_length
0.000000000,10.0.1.2,50978,10.0.1.1,3120,0,0,33,1400,4,65535,0
0.000323000,10.0.1.1,3120,10.0.1.2,50978,0,1367,33,33,4,64168,0
0.001024000,10.0.1.2,50978,10.0.1.1,3120,1367,0,33,1205,4,65535,0
0.001882000,10.0.1.1,3120,10.0.1.2,50978,0,2539,33,33,4,62996,0
```

#### packet analyse using Wireshark

Wireshark is a powerful network packet capture and analysis tool. Download here. After installation, copy the lua file `tcp.lua` to the directory for wireshark plugins, for example: `E:\Applications\Wireshark\plugins`. Then start wireshark and open the captured file `<name>.pacp`. Now you can analyze the packets with a beautiful user interface.

The same four packets appear as a packet list:

| No. | Time | Source | Destination | Protocol | Length | Sequence Number | ACK Number | Header Length | Packet Length |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.000000 | 10.0.1.2 | 10.0.1.1 | CMU TCP | 1442 | 0 | 0 | 33 | 1400 |
| 2 | 0.000323 | 10.0.1.1 | 10.0.1.2 | CMU TCP | 75 | 0 | 1367 | 33 | 33 |
| 3 | 0.001024 | 10.0.1.2 | 10.0.1.1 | CMU TCP | 1247 | 1367 | 0 | 33 | 1205 |
| 4 | 0.001882 | 10.0.1.1 | 10.0.1.2 | CMU TCP | 75 | 0 | 2539 | 33 | 33 |

## what to submit

Your implementation should be in the following files: `foggy_function.cc`, `foggy_tcp.cc`, `foggy_function.h` and `foggy_tcp.h`. You can run the `submit.py` at the root of the project which will generate a `submit.zip` file including these four files, then submit the `submit.zip` file to Gradescope. The autograder will copy those four files you submitted to the starter codes and do the testing.

## attachments

- \[missing\]

## submission

- submission

## solution

- \[missing\]

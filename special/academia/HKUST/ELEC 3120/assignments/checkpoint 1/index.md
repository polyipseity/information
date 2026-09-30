---
aliases:
  - ELEC 3120 checkpoint 1
  - ELEC3120 checkpoint 1
  - HKUST ELEC 3120 checkpoint 1
  - HKUST ELEC3120 checkpoint 1
tags:
  - date/2026/10/02
  - flashcard/active/special/academia/HKUST/ELEC_3120/assignments/checkpoint_1/index
  - language/in/English
---

# checkpoint 1

- HKUST ELEC 3120

---

- title: Checkpoint 1: Kickoff
- due: 2026-10-02T23:59:59+08:00
- points: \[missing\]
- submitting: \[missing\]
- note: due three weeks after release, a special arrangement for the add/drop period rather than the usual two-week interval
- note: submissions stay open beyond the deadline, and no slip days are counted against it
- note: homework 1 falls due at the same time
- note: the later checkpoints build on this one, so it is worth finishing early

---

Tentative release: Monday 07/09

Tentative due date: 02/10 23:59

## late policy

- You have free 4 late days in total.
- You can use late days for assignments. A late day extends the deadline 24 hours.
- Once you have used all 4 late days, the penalty is 20% for each additional late day (5 days later there will be no points).
- Remember that any questions should go to Ed instead of emailing TAs or the professor.

## validate your GitHub student status

Please do it as soon as possible. It may take a few days to validate your status. Then you can use Copilot for free. You may refer to this guide.

## create a __PRIVATE__ repo of your project

Clone the repo to your local machine.

```sh
git clone https://github.com/HKUST-Network/foggytcp.git
```

_Reminder: Use git to clone the repo instead of download as a zip. Otherwise you cannot track the changes._

## install Vagrant and VirtualBox

You can use Vagrant and VirtualBox to automatically setup the environment. Different OSes require different installation steps.

If you are using Windows Subsystem for Linux (Linux), please refer to the installation steps for Linux. I also recommend you to do in that way -- Linux is an important tool for developers. Otherwise, follow the instructions below.

- Install Vagrant
- Install VirtualBox

_FAQ: Where is the terminal on my laptop?_ The best way to access the terminal is in Visual Studio Code. This is the most popular IDE for developers. Under the View menu, you can find the Terminal option.

## setup the environment

Once you have both Vagrant and VirtualBox installed, navigate inside this repo and run:

```sh
# In your project root folder where your Vagrantfile is located
vagrant up
# builds the server and client containers using VirtualBox.
```

After the containers are built, you can access the client and server containers using the following commands:

```sh
vagrant ssh client
vagrant ssh server
# connects to either the client or server using SSH.
```

_You will need to open two terminals to connect to server and client separately._

Vagrant keeps all files synchronized between your host machine and the two containers. In other words, the code will update automatically on the containers as you edit it on your computer. Similarly, debugging files and other files generated on the containers will automatically appear on your host machine.

### DNS domain issue

If your vagrant VMs fail to connect to the Internet and execute commands such as "sudo apt-get install", please use the following command within your VMs:

```sh
sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
```

## run the server and client

### build the binaries

```sh
# In the server VM
cd /vagrant/foggytcp
mkdir build
make system
```

You will see the binaries `server` and `client` in the `foggytcp` folder.

Remember, each time when you modify the code, you need to rebuild the binaries.

### read and understand the `server.cc` and `client.cc`

The `server.cc` and `client.cc` are the main files for the server and client respectively.

### send a file from the client to the server

In the server VM, at the `/vagrant/foggytcp` folder, run the server with the following command:

```sh
./server 10.0.1.1 3120 test.out
```

In the client VM, at the `/vagrant/foggytcp` folder, run the client with the following command:

```sh
./client 10.0.1.1 3120 src/client.cc
```

Now you have successfully transmitted the `client.cc` file from the client to the server, named as `test.out`.

### set traffic control manually

`tcconfig` can be used to manually set traffic control between client VM and server VM. Use the following command to install it:

```sh
sudo pip install tcconfig
```

Then you need to check the network interface name of your VM:

```sh
ifconfig
```

Then you can set traffic control to this interface. For example, use the following command on the client side to set one-way latency to be 100ms, replacing `<interface>` with the name you found:

```sh
sudo tcset <interface> --delay 100ms
```

And use the following command to see your settings:

```sh
sudo tcshow <interface>
```

Please refer to the tcconfig documents for more usages.

## what to submit

### codes

This checkpoint is about setting up the environment and understanding the code. You do not need to modify the code for this checkpoint. We hope that you can familiarize yourself with the submission procedure on Gradescope.

1. Modify any place in the `*.cc` or `*.h` (it can even be adding a new space).
2. Commit your code. If you're using VS Code, follow this video to commit the changes (from 4m49s to 6m22s).
3. Run the `submit.py` at the root of the project. It will generate a `submit.zip` file.

    ```sh
    python submit.py
    ```

4. Submit the `submit.zip` file to Gradescope.

### report

You need to measure the file transmission time for

- Different file sizes
- Different bandwidths
- Different delays

and plot them in three figures. Remember to fix other two parameters while changing one and make your plots __reader-friendly__. In the report, you need to follow the hypothesis-experiment-conclusion structure:

- __Hypothesis.__ Before running experiments, what is your expected results? Why?
- __Experiment.__ Measure the file transmission time under different conditions and plot your results.
- __Conclusion.__ Does you experiment results match your expectations? What may cause the gap between them? If your predictions are totally different from your resutls, please hypothesize as to why your predictions were wrong.

The following parameter configurations are for your reference. You are free to test with other configurations to verify your hypothesis.

__Test 1__:

- Bandwidth = 10Mbps
- Delay = 10ms
- Filesize = 1KB, 5KB, 25KB, 100KB, 1MB, 10MB

To create a file with a desired size:

```sh
fallocate -x -l 1M 1M.txt
```

__Test 2__:

- Dealy = 10ms
- Filesize = 1MB
- Bandwidth = 1Mbps, 5Mbps, 10Mbps, 20Mbps

__Test 3__:

- Bandwidth = 10Mbps
- Filesize = 1MB
- Delay = 0ms, 5ms, 10ms, 20ms, 50ms, 100ms

## attachments

- \[missing\]

## submission

- submission

## solution

- \[missing\]

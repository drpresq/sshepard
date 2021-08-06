# SSHepherd - Quick Start

SSHepherd is easy to use right out-of-the-box by following the general usage below.

## General Usage

```
usage: sshepherd [-h] [-a {list-users,add-users,run-command}]
                [-t TARGETS [TARGETS ...]] [-p PATH]
                [-c COMMAND [COMMAND ...]]

SSHepherd - herd your flock of ssh hosts

optional arguments:
  -h, --help            show this help message and exit
  -a {list-users,add-users,run-command}, --action {list-users,add-users,run-command}
                        
                        Action to be carried out on targets
                        
  -t TARGETS [TARGETS ...], --targets TARGETS [TARGETS ...]
                        
                        List of ip addresses/hostnames to perform action upon
                        
  -p PATH, --path PATH  
                        Path to New User SSH Public Keys. SSH Key names must conform to the following formats:
				<username>.pub or <username>_somethingelse.pub
                        
  -c COMMAND [COMMAND ...], --command COMMAND [COMMAND ...]
                        
                        Commands to be run on host separated by semicolons
                        

    Common Usage:
	sshepherd -a list-users -t 192.168.1.1 192.168.1.2				            Returns a list of users by IP
	sshepherd -a add-users -t 192.168.1.1 -p /home/user/pub-keys			    Add users to each target based on key name
	sshepherd -a run-command -t 192.168.1.1 -c sudo whoami; cat /etc/passwd		Runs the two commands on each target
```

## Command Option Detail

* **-a, --action** : (Mandatory) Choose which action you'd like SSHepherd to perform *all actions require the -t/--targets argument*:
    
    - list-users : Connects to each target host and returns a list, by IP, of user home folders
    - add-users : Connects to each target host and attempts to create new user accounts based on provided ssh public keys. *Requires -p/--path argument*.
    - run-command : Connects to each target host and attempts to run any arbitrary commands. *Requires -c/--command argument*.
    
* **-t, --targets** : (Mandatory) A space delimited list of IP addresses and/or hostnames you wish SSHepherd to perform the identified action on:

    - Single Target Example :  -t 192.168.1.1
    - Multi-Target Example : -t 192.168.0.1 192.168.1.5 192.168.0.15 192.168.1.11

* **-p, --path** : (Used with add-user action) Full directory path to the location of your new user public ssh keys:

    - Example : -p /home/user/key-folder

* **-c, --command** : (Used with run-command action) A semi-colon delimited list of commands you wish to perform on each target:

    - Single Command Example : -c sudo whoami
    - Multi-Command Example : -c sudo whoami; cat /etc/passwd

## Limitations

SSHepherd makes the following assumptions:

1. You have an openssh-based ssh client installed and callable by `ssh`
2. You have a private key installed in your profile at `~/.ssh/id_rsa`
3. Your user account has sudo privilege on all target hosts
4. Your target host `/etc/sudoers` file is set to not prompt for a password: (i.e. `%sudo	ALL=(ALL:ALL) NOPASSWD:ALL`)
# SSHepherd - Herd Your Flock!

<p align="center">
<img alt="SSHepherd - Herd Your Flock!" src="media/sshepard.png">
</p>

## Description

SSHepherd eases integration of new user accounts for SSH hosts without centralized user management by:

- Creating the new user account on the target host
- Adding them to security groups as applicable
- Placing ssh public keys as applicable

## Features

SSHepherd is also capable of some other user management features:

- Take an inventory of users on each system
- Delete users from system groups
- A variety of functions across system groups:
    - Delete, lock and unlock users
    - Update ssh keys
    - Reset passwords
    - Run arbitrary commands

## Installation

```
git clone https://github.com/drpresq/sshepherd.git
pip3 install ./sshepherd
```
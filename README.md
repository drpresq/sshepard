# SSHepard: Automated SSH Host Management

## Description

SSHepard eases integration of new user accounts for SSH hosts without centralized user management by:
* Creating the new user account on the target host
* Adding them to security groups as applicable
* Placing ssh public keys as applicable

## Features

SSHepard is also capable of some other user management features:
* Take an inventory of users on each system
* Delete users from system groups
* A variety of functions across system groups:
    * delete, lock and unlock users
    * Update ssh keys
    * reset passwords
    * run arbitrary commands
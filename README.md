# Vagrant-custom-MLpython
These automation script will enable a VM envirolment that has the following build in:
- Ubuntu 18.04 latest
- Miniconda >4.0 with python 3.7
- Conda dev36 env with python 3.6, pandas, TF|keras without GPU support
- Docker and Docker Compose

preRequisites:
I'm still trying to figureout how to automated this step using powershell for window
for now please do:
install Virtualbox and its extension pack:
https://download.virtualbox.org/virtualbox/6.1.4/VirtualBox-6.1.4-136177-Win.exe
https://download.virtualbox.org/virtualbox/6.1.4/Oracle_VM_VirtualBox_Extension_Pack-6.1.4.vbox-extpack
  1. run virtualbox.exe file and install VirtualBox-6 for window(with all default options)
  2. open virtualbox then select: 
     Tools -> Preferences -> Extensions -> 
	 addextention(+ button on the right)-> brown to VMBox extension 
	 -> install

Install Vagrant provision package controller (it's the parent form of Terraform)
https://www.vagrantup.com/downloads.html - install with default options

While you're at it, you might want to optionally install Git
https://git-scm.com/

Importance: please turn on Intel virtual x or Amd virtual u technology in your bios
and then when you are in window
open control panel -> programs -> turn window features on or off
or search for 'turn window features on or off' in start menu :)
  1. check on Hyper-V - this will check all option under Hyper-V
  2. expand Hyper-V -> expand Hyper-V Platform -> uncheck Hyper-V Hypervisor
Note: so you have everything under Hyper-V selected but Hyper-V Hypervisor option

Prepare for running:
1. open PowerShell and enter the following commands
1.1 vagrant plugin install vagrant-disksize
1.2 vagrant plugin install vagrant-docker-compose
Note: you only need to enter the above commands on the first vagrant run

The following steps are need all the time 
...still open powershell
2. Brown to this location where you see 'me' and the Vagrantfile
3. type in:
   vagrant up
   - wait until you have the control back then
   vagrant ssh
   you are ssh to your virtual machine nice!
   type "exit" to go back to window
   and ALWAY ...  ALWAY remember to turn off your VM by using virtualbox, 
   or by type "vagrant halt" in powershell

Trouble shooting note: if when you run vagrant up and you see a timeout warning
please open the Vagrantfile and go to line 5 where you see "bridge:" to change the name of your machine network connector
the easy way is to find what you need is - open virtualbox -> select docker-test1 (this is the VM we trying to create and ssh to)
-> setting -> networks -> adapter 2 -> expand "name" and replace what inside line 5 with the wireless adapter that you found

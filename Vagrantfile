Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_version = "1.0.0"
  config.vm.network "forwarded_port", guest: 8888, host: 8888
  #config.vm.network  "public_network", bridge: "Realtek 8822BE Wireless LAN 802.11ac PCI-E NIC"
  config.vm.network  "public_network", bridge: "Hyper-V Virtual Ethernet Adapter"
  config.vm.boot_timeout = 400
  config.disksize.size = '50GB'
  config.vm.synced_folder "./share", "/vagrant"
  # following config is for virtualbox setting
  config.vm.provider "virtualbox" do |v|
    v.name = 'docker-test1'
    v.customize ["modifyvm", :id, 
    #	         "--natdnshostresolver1", "on",
    #		     "--natdnsproxy1", "on",
	             "--cpus", "1",
				 "--cpuexecutioncap", "95",
  				 "--memory", "4096"
  	            ]
  end
  config.vm.provision :shell, path: "./share/bootstrap.sh"
  config.vm.provision :docker
  config.vm.provision :docker_compose
  config.vm.provision :shell, path: "./share/bootstrap_install_dev36.sh" 
end
Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/xenial64"

  # Create a forwarded port mapping
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Private network allows host-only access to the machine using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Public network, which generally matched to bridged network, which
  # make the machine appear as another physical device on your network.
  # config.vm.network "public_network"
  
  config.vm.synced_folder ".", "/home/vagrant/work"
  # config.vm.synced_folder ".", "/vagrant/", :nfs => { }:mount_options =>["dmode=777", "fmode=666"] }

end

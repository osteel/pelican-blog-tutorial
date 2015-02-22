# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Used box
  config.vm.box = "ubuntu/trusty32"

  config.vm.define "local" do |local|
    # Accessing "localhost:8000" will access port 8000 on the guest machine.
    local.vm.network :forwarded_port, guest: 8000, host: 8000, auto_correct: true

    # Copy Vagrant's ssh private key over
    local.vm.provision "file", source: "~/.vagrant.d/insecure_private_key", destination: "~/.ssh/insecure_private_key"

    # Install stuff
    local.vm.provision :shell, :path => ".provision/bootstrap.sh", privileged: false
  end

  config.vm.define "server" do |server|
    # Private IP
    server.vm.network :private_network, ip: "192.168.72.3"
  end

end
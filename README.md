#Pelican blog tutorial

Repository to illustrate the [Install and deploy a Pelican blog using Fabric with no Python background](http://blog.osteel.me/posts/2015/02/22/install-and-deploy-a-pelican-blog-using-fabric-with-no-python-background.html "Install and deploy a Pelican blog using Fabric with no Python background") series.

Its aim is to quickly get a Pelican blog running locally and to provide an easy way to test the provisionning of a server and the publication of content with Fabric.

##Get it running

Clone the project:

    git clone git@github.com:osteel/pelican-blog-tutorial.git

Download VirtualBox at [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads "VirtualBox - Downloads") (*"platform packages"*) and install it.  
Download Vagrant at [https://www.vagrantup.com/downloads.html](https://www.vagrantup.com/downloads.html "Vagrant - Downloads") and install it.

The Vagrantfile is set up to use the [Multi-Machine](https://docs.vagrantup.com/v2/multi-machine/index.html "Vagrant documentation - Multi-Machine") feature. It manages two virtual machines: one that will be the *"local"* one, and another that is going to be used to simulate a remote server.

From the project root, run:

    vagrant up local

This will start and provision a VM with everything required to run Pelican locally.


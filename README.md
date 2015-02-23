#Pelican blog tutorial

Repository to illustrate the [Install and deploy a Pelican blog using Fabric](http://blog.osteel.me/posts/2015/02/24/install-and-deploy-a-pelican-blog-using-fabric-part-1-local-environment.html "Install and deploy a Pelican blog using Fabric") series.

Its aim is to quickly get a Pelican blog running locally and to provide an easy way to test the provisionning of a server and the publication of content with Fabric.

##Get it running

Clone the project:

    git clone git@github.com:osteel/pelican-blog-tutorial.git

Change the origin for your own repository and push.

Open *"fabfile.py"* and assign your repository to the *"git_repository"* variable (e.g. *"git@github.com:username/my-blog.git"*).

Download VirtualBox at [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads "VirtualBox - Downloads") (*"platform packages"*) and install it.  
Download Vagrant at [https://www.vagrantup.com/downloads.html](https://www.vagrantup.com/downloads.html "Vagrant - Downloads") and install it.

The Vagrantfile is set up to use the [Multi-Machine](https://docs.vagrantup.com/v2/multi-machine/index.html "Vagrant documentation - Multi-Machine") feature. It manages two virtual machines: one that will be the *"local"* one, and another that is going to be used to simulate a remote server.

From the project root, run:

    vagrant up local

This will start and provision a VM with everything required to run Pelican locally.

From a new terminal, start the *"server"* machine:

    vagrant up server

*ssh* the *"local"* machine and run:

    cd /vagrant
    fab provision
    fab publish

`fab provision` will *ssh* the *"server"* machine to install the required packages and set up nginx so that the blog will be accessible at *http://my-blog.local.com*.

`fab publish` will pull the files from your Git repository, install the blog's dependencies and generate the HTML content.

The first time you run it, it will create a ssh key pair for you and ask you to add the private key to your repository. Do so and hit *return* to continue the process.

Add this line to your host machine's *"hosts"* file:

    192.168.72.3    my-blog.local.com

Save and visit [http://my-blog.local.com](http://my-blog.local.com).

Please see the [complete tutorial](http://blog.osteel.me/posts/2015/02/24/install-and-deploy-a-pelican-blog-using-fabric-part-1-local-environment.html "Install and deploy a Pelican blog using Fabric") for a full explanation.
#!/usr/bin/env bash

# update stuff
sudo apt-get update

# git
sudo apt-get install -y git-core

# make
#sudo apt-get install make

# python-dev
#sudo apt-get install -y python-dev

# pip
wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py -P /tmp/
sudo python /tmp/get-pip.py
rm /tmp/get-pip.py

# python virtualenv & virtualenvwrapper
sudo pip install virtualenv
sudo pip install virtualenvwrapper

# change virtual environments location
echo '' >> /home/vagrant/.bashrc
echo '# change virtual environments location' >> /home/vagrant/.bashrc
echo 'export WORKON_HOME=$HOME/.virtualenvs' >> /home/vagrant/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> /home/vagrant/.bashrc

# reload profile
source ~/.bashrc

# fabric
sudo pip install Fabric

# curl
#sudo apt-get -y install curl

# RVM
#curl -L https://get.rvm.io | bash -s stable
#source ~/.rvm/scripts/rvm
#rvm requirements

# ruby
#rvm install ruby
#rvm use ruby --default

# sass
#gem install sass

# compass
# then, to use it, update the scss files, go to the root dir, and type:
# compass compile
#gem install compass

# symlink /var/www => /vagrant
#ln -s /vagrant /var/www

# change current directory
#cd /var/www




# create blog directory
#mkdir blog

#cd blog

# create and activate a virtual environment. From now on, run 'workon blog'
# to activate the virtual environment
#mkvirtualenv blog

# install pelican
#pip install pelican

# install Markdown
#pip install Markdown

# exit virtual environment
#deactivate
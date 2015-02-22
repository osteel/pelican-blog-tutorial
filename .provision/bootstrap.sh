#!/usr/bin/env bash

# update stuff
sudo apt-get update

# git
sudo apt-get install -y git-core

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

# create and activate a virtual environment. From now on, run 'workon blog'
# to activate the virtual environment
mkvirtualenv blog

# install pip dependencies
pip install -r requirements.txt

# exit virtual environment
deactivate
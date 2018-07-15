#Install python3 libs
apt-get install -y libatlas-base-dev python3-dev python3-pip python3-pillow python3-numpy python3-pandas 
sudo pip3 install --yes --upgrade pip
sudo pip3 install --yes jupyter
sudo ipython3 kernelspec install-self
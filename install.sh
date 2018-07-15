#Install python3 libs
apt-get install -y libatlas-base-dev python3-dev python3-pip python3-pillow python3-numpy python3-pandas 
sudo pip3 install --upgrade pip
sudo pip3 install jupyter
sudo ipython3 kernelspec install-self

#Download and build the rpi-rgb-led-matrix library and build it
sudo git clone https://github.com/hzeller/rpi-rgb-led-matrix.git
cd rpi-rgb-led-matrix
sudo make
cd bindings/python/
sudo make build-python PYTHON=$(which python3)
sudo make install-python PYTHON=$(which python3)


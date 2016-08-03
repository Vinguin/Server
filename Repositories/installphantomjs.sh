# Dieses Script installiert Phantomjs auf dem Rechner.

sudo apt-get update
sudo apt-get install -y build-essential chrpath libssl-dev libxft-dev


sudo apt-get install -y libfreetype6 libfreetype6-dev
sudo apt-get install -y libfontconfig1 libfontconfig1-dev

cd ~
export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"
wget "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2"
sudo tar xvjf $PHANTOM_JS.tar.bz2

rm $PHANTOM_JS.tar.bz2

sudo mv $PHANTOM_JS /usr/local/share
sudo ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin


phantomjs --version

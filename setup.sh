#!/bin/bash
GREEN='\033[0;32m'
WHITE='\033[0m'
ORANGE='\033[0;33m'
echo "Do you wish to install Acorn? If so, place the Acorn folder on your Desktop to begin."
echo "Yes (y), No (n): "
read answer
if echo "$answer" | grep -q "^y" ;then
	echo -e "${GREEN}Setting up Acorn...${WHITE}"
else
	echo "No"
	exit
fi

cd ~
mkdir bin
mv ~/Desktop/Acorn ~/bin/

echo -e "${ORANGE}Almost finished, setting up command shortcut...${WHITE}"

echo "cocoa(){
CWPD=\"\$PWD\";
cd ~/bin/Acorn/src/;
python3.6 Driver.py \$CWPD/\$1;
cd \$CWPD;
}" >> .bash_profile


source ~/.bash_profile
echo -e "${GREEN}All done!${WHITE}"


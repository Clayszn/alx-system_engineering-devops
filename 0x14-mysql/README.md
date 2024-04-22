0x14-mysql
1- copy the key from msql.dev paste in a file signature.key

# Run this command to check if key is OK
sudo apt-key add signature.key
# input
sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 &&  sudo ./mysql57 

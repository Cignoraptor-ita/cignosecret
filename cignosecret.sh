echo " "

echo -e "\e[01;32m=========\e[00;31m::::::::::\e[01;32m=========\e[00m"
echo -e "\e[00;33m"
cat swan.txt
echo -e "\e[00m"
echo " "
PS3="Choose action:"

select opt in "INFO" "PLAY" "LEVEL HELP"
do
    case "$opt" in
        'INFO')
echo " "
echo "Cignosecret is a Open Source Intelligence, Forensics and crypto wargame" 
echo " "
echo "There are 15 levels"
echo " "
echo -e "Initially created for testing the \e[00;34mCIGNO-FRAMEWORK\e[00m (Social engineering oriented pentest and OSINT tool)"
echo " "
echo -e "\e[01;32mCoded by Cignoraptor\e[00m -- cignoraptor@easy.com"
echo " "
        ;;
        'PLAY')
bash avvio.sh
        ;;
        'LEVEL HELP')
bash help.sh
        break;
 esac
done

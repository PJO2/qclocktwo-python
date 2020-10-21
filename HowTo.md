
# Création d'un horloge à mots

Matériel :
- Un raspberry pi zéro W
- Un ruban de Leds
- Une photo résistance
- Un condensateur 47µF (entre 10 et 100)


# Préparation Raspberry

Récupération de l'OS [sur le site officiel](https://www.raspberrypi.org/downloads/raspberry-pi-os/)
Prendre la version Buster lite, (Minimal image based on Debian Buster)

Transférer l'image sur la flash grâce à [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/)
Edition des fichiers suivants dans le file system éditable (/boot)

 - ssh: créer un fichier vide
 - wpa_supplicant.conf : créer le fichier de destination :

    ```
    ctrl_interface=DIR=/run/wpa_supplicant     GROUP=netdev
    update_config=1
    country=FR
    
    network={
        ssid="xxx"
        psk="xxxx"
    }

- cmdline.txt : insertion de `modules-load=dwc2,g_ether` entre root et quit 
- config.txt : ajout de `dtoverlay=dwc2` en fin de fichier


Transférer la flash sur le raspberry zero.
Brancher le port USB du raspberry sur un port USB du PC (ne pas brancher le port power) et démarrer le raspberry (c'est assez long)

![branchement](https://github.com/PJO2/qclocktwo/raw/master/Raspberry-Pi-Zero-Ethernet-Gadget-Pi-Zero-Plugged-Into-Computer.jpg)

## Préparation PC

Pendant le boot du raspberry, installer le service Bonjour sur le PC, à partir du site [d'apple](https://support.apple.com/kb/DL999)

Pendant le démarrage,  le raspberry installe un driver RNIS gadget. Ca ne marche pas toujours et on peut se retrouver avec un driver de t

## Possibilité de passer en systemd
avec le tutoriel [https://hackaday.io/project/162164/instructions](ici)

Seul modifcation LinkLocalAddress=yes 


<!--stackedit_data:
eyJoaXN0b3J5IjpbODgxMTY3NzYzXX0=
-->
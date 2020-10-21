
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

Pendant le boot du raspberry, installer le service Bonjour sur le PC, à partir du site [d'apple](https://support.apple.com/kb/DL999). La version 2.0.2 est ancienne mais suffisante.

Pendant le démarrage,  le raspberry installe un driver RNIS gadget. Ca ne marche pas toujours et on peut se retrouver avec un driver de type Serial.
Dans ce cas, télécharger le driver ici et l'installer à la main (ie en cliquant sur le .inf)
[http://web1.moddevices.com/shared/mod-duo-rndis.zip](http://web1.moddevices.com/shared/mod-duo-rndis.zip)

Bref, il faut arriver à ça :
![drivers](https://github.com/PJO2/qclocktwo/raw/master/driver%20gadget.png)

Ainsi, on peut se connecter au raspberry, soit par le wifi, soit par le port USB à l'adresse raspberry.local (c'est le service bonjour qui résout ce nom), par ssh pi@raspberry.local.


## Utilisation de file system RAM

Pour éviter les écritures en flash, certains répertoires sont déplacés vers des file systems en RAM (format tmpfs).
Le petit script ci-dessous fait le boulot :

```
cat >> /etc/fstab <<EOF  
tmpfs /tmp tmpfs defaults,noatime,nosuid,size=10m 0 0  
tmpfs /var/log tmpfs defaults,noatime,nosuid,mode=0755,size=25m 0 0  
tmpfs /var/run tmpfs defaults,noatime,nosuid,mode=0755,size=2m 0 0  
EOF

rm -r /var/tmp  
ln -s /var/tmp /tmp  
ln -s /var/spool/mqueue /tmp
```


## Possibilité de passer en systemd
avec le tutoriel [https://hackaday.io/project/162164/instructions](ici)

Seule modification LinkLocalAddress=yes au lieu de IPv4 pour utiliser IPv6 en link local.

Il reste un pb à régler, `/etc/resolv.conf`  a été déplacé vers un file system en tmpfs sur lequel le répertoire `resolve` n'existe pas. DHCP ne modifie donc pas ce fichier et se retrouve sans DNS. Il faut utiliser un service pour le créer. 
On peut s'inspirer de `/etc/systemd/system/dbus-fi.w1.wpa_supplicant1.service` ou de `/etc/systemd/system/multi-user.target.wants/raspberrypi-net-mods.service` pour démarrer un service avant le réseau.


## Installation des librairies

Nous utilisons 2 librairies : 

- rpi.GPIO pour le pilotage des broches du GPIO
- neopixel : pour le pilotage du ruban de leds ws2813

```
apt install rpi.gpio
apt install python3-pip
pip3 install rpi_ws281x adafruit-circuitpython-neopixel

```
## Branchements

Conformément à l'image
![drivers](https://github.com/PJO2/qclocktwo/raw/master/branchement.png)


## mise à l'heure

Le raspberry se met à l'heure via NTP. Il reste à lui configurer le bon fuseau horaire.
raspi-config s'en charge : 
raspi-config
   - 4 localisation
       - I2 Change Time Zone
            - choisir Europe/Paris


## lecture de la luminosité

Le raspberry ne semble pas posséder d'entrée analogique, ce qui aurait été pratique pour mesurer la photo résistance. Le hack suivant nous montre un moyen de s'en passer [https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading).
[https://iot4beginners.com/measure-the-intensity-of-light-using-a-photocell/](https://iot4beginners.com/measure-the-intensity-of-light-using-a-photocell/)


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg3ODM3MjQyMCwxMTQyMDUwMzExLC0xMD
gxMTcwMDQyLDIwMzM3NTIxNTksLTM5OTM4MzMzNF19
-->
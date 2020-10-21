
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

Il reste un pb à régler, `/etc/resolv.conf`  a été déplacé vers un file system en tmpfs sur lequel le répertoire `resolve` n'existe pas. Il faut utiliser un service pour le créer 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5OTQ0MTUwNzJdfQ==
-->
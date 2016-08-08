# ShouEn
install
    ubuntu desktop
    xampp
        reboot start
            sudo ln -s /opt/lampp/lampp /etc/init.d/lampp
            sudo update-rc.d lampp start 80 2 3 4 5 . stop 30 0 1 6 .
        phpmyadmin
            Edit the etc/extra/httpd-xampp.conf file in your XAMPP installation directory.
            Within this file, find the line below and update it to remove 'phpmyadmin' from the list of locations.
             <LocationMatch "^/(?i:(?:xampp|security|licenses|phpmyadmin|webalizer|server-status|server-info))">
    python3
    mysql connector python
    pyserial
    create mysql table
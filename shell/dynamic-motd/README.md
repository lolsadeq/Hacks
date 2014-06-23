# Debian Wheezy Dynamic MOTD

The current stable version of Debian, which is codenamed Wheezy, does not
include the facilities to generate a dynamic message-of-the-day (MOTD). The
shell scripts in this folder will allow you to do that.

Follow these steps:

    sudo apt-get install figlet uptimed
    sudo mkdir /etc/update-motd.d/
    cd /etc/update-motd.d/
    sudo touch 00-header
    sudo touch 10-sysinfo
    sudo touch 90-footer
    sudo chmod /etc/update-motd.d/*
    sudo rm /etc/motd
    sudo ln -s /var/run/motd /etc/motd

Now copy the contents of `00-header`, `10-sysinfo`, and `90-footer` to
`/etc/update-motd.d/` on your server!

Edit the file `/etc/pam.d/sshd` and comment out the line that reads:

    session    optional     pam_motd.so  motd=/run/motd.dynamic noupdate

Edit the file `/etc/ssh/sshd_config` and edit the settings `PrintMotd` and
`PrintLastLog` so that they look like this:

    PrintMotd no
    PrintLastLog no

Finally, remove the file `/var/run/motd.dynamic` and reboot your system.

Have lots of fun!

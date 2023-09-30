# (c) 2023 Luana Neder
# Licensed under MIT license
# run at your own risk, this may break your system
# run with sh, I cant add a shebang bc env is part of coreutils and you won't have that during a period of time
# make a snapshot with snapper before: 'sudo snapper create --description 'before-uutils' --userdata important=yes -t pre'
# and after: 'sudo snapper create --description 'after-uutils' --userdata important=yes -t post --pre-number [NUMBER OF THE SNAPSHOT THAT WAS MADE BY THE PREVIOUS SNAPPER RUN, CHECK WITH 'sudo snapper list']'
# before running this, install uutils to /usr/bin  (compile and copy the generated coreutils binary to /usr/bin)
# Run this first with sudo sh, then run 'sudo rpm -e --allmatches --nodeps coreutils', and then run this with sudo sh once again.
# Only reboot AFTER running this after you remove coreutils with rpm.
# Remember to install the empty .rpm coreutils metapackage with zypper and then addlock coreutils and coreutils-single on zypper.

commandsuu="[ arch b2sum b3sum base32 base64 basename basenc cat chgrp chmod chown chroot cksum comm cp csplit cut date dd df dir dircolors dirname du echo env expand expr factor false fmt fold groups hashsum head hostid hostname id install join kill link ln logname ls md5sum mkdir mkfifo mknod mktemp more mv nice nl nohup nproc numfmt od paste pathchk pinky pr printenv printf ptx pwd readlink realpath relpath rm rmdir seq sha1sum sha224sum sha256sum sha3-224sum sha3-256sum sha3-384sum sha3-512sum sha384sum sha3sum sha512sum shake128sum shake256sum shred shuf sleep sort split stat stdbuf stty sum sync tac tail tee test timeout touch tr true truncate tsort tty uname unexpand uniq unlink uptime users vdir wc who whoami yes"

coreutils echo "Run this first with sudo sh, then run 'sudo rpm -e --allmatches --nodeps coreutils', and then run this with sudo sh once again."
coreutils echo "Only reboot AFTER running this after you remove coreutils with rpm."
coreutils echo "Remember to install the empty .rpm coreutils metapackage with zypper and then addlock coreutils and coreutils-single on zypper."

for i in $commandsuu; do
    coreutils rm -f /usr/bin/$i
    coreutils ln -s /usr/bin/coreutils /usr/bin/$i
done

echo done
commandsuu="coreutils base32 base64 basename basenc cat cksum comm cp csplit cut date dd df dir dircolors dirname du echo env expand expr factor false fmt fold hashsum md5sum sha1sum sha224sum sha256sum sha384sum sha512sum sha3sum sha3-224sum sha3-256sum sha3-384sum sha3-512sum shake128sum shake256sum b2sum b3sum head join link ln ls mkdir mktemp more mv nl numfmt od paste pr printenv printf ptx pwd readlink realpath relpath rm rmdir seq shred shuf sleep sort split sum tac tail tee touch tr true truncate tsort unexpand uniq unlink test vdir wc yes"



for i in $commandsuu; do
    cargo run completion $i bash > /usr/share/bash-completion/completions/$i
    cargo run completion $i zsh > /usr/share/zsh/site-functions/_$i
done

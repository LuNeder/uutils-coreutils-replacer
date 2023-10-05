#
# spec file for package coreutils
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           coreutils
Version:        9999.99.99
Release:        0
Summary:        Empty package to make zypper think GNU coreutils is installed if you use uutils
License:        MIT
URL:            https://luana.dev.br/
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Provides:       fileutils = %{version}
Provides:       mktemp = %{version}
Provides:       sh-utils = %{version}
Provides:       stat = %{version}
Provides:       textutils = %{version}
Provides:       /usr/bin/[
Provides:       /usr/bin/arch
Provides:       /usr/bin/b2sum
Provides:       /usr/bin/b3sum
Provides:       /usr/bin/base32
Provides:       /usr/bin/base64
Provides:       /usr/bin/basename
Provides:       /usr/bin/basenc
Provides:       /usr/bin/cat
Provides:       /bin/cat
Provides:       /usr/bin/chgrp
Provides:       /usr/bin/chmod
Provides:       /usr/bin/chown
Provides:       /usr/bin/chroot
Provides:       /usr/bin/cksum
Provides:       /usr/bin/comm
Provides:       /usr/bin/cp
Provides:       /usr/bin/csplit
Provides:       /usr/bin/cut
Provides:       /usr/bin/date
Provides:       /usr/bin/dd
Provides:       /usr/bin/df
Provides:       /usr/bin/dir
Provides:       /usr/bin/dircolors
Provides:       /usr/bin/dirname
Provides:       /usr/bin/du
Provides:       /usr/bin/echo
Provides:       /usr/bin/env
Provides:       /usr/bin/expand
Provides:       /usr/bin/expr
Provides:       /usr/bin/factor
Provides:       /usr/bin/false
Provides:       /usr/bin/fmt
Provides:       /usr/bin/fold
Provides:       /usr/bin/groups
Provides:       /usr/bin/hashsum
Provides:       /usr/bin/head
Provides:       /usr/bin/hostid
Provides:       /usr/bin/hostname
Provides:       /usr/bin/id
Provides:       /usr/bin/install
Provides:       /usr/bin/join
Provides:       /usr/bin/kill
Provides:       /usr/bin/link
Provides:       /usr/bin/ln
Provides:       /usr/bin/logname
Provides:       /usr/bin/ls
Provides:       /usr/bin/md5sum
Provides:       /usr/bin/mkdir
Provides:       /usr/bin/mkfifo
Provides:       /usr/bin/mknod
Provides:       /usr/bin/mktemp
Provides:       /usr/bin/more
Provides:       /usr/bin/mv
Provides:       /usr/bin/nice
Provides:       /usr/bin/nl
Provides:       /usr/bin/nohup
Provides:       /usr/bin/nproc
Provides:       /usr/bin/numfmt
Provides:       /usr/bin/od
Provides:       /usr/bin/paste
Provides:       /usr/bin/pathchk
Provides:       /usr/bin/pinky
Provides:       /usr/bin/pr
Provides:       /usr/bin/printenv
Provides:       /usr/bin/printf
Provides:       /usr/bin/ptx
Provides:       /usr/bin/pwd
Provides:       /usr/bin/readlink
Provides:       /usr/bin/realpath
Provides:       /usr/bin/relpath
Provides:       /usr/bin/rm
Provides:       /usr/bin/rmdir
Provides:       /usr/bin/seq
Provides:       /usr/bin/sha1sum
Provides:       /usr/bin/sha224sum
Provides:       /usr/bin/sha256sum
Provides:       /usr/bin/sha3-224sum
Provides:       /usr/bin/sha3-256sum
Provides:       /usr/bin/sha3-384sum
Provides:       /usr/bin/sha3-512sum
Provides:       /usr/bin/sha384sum
Provides:       /usr/bin/sha3sum
Provides:       /usr/bin/sha512sum
Provides:       /usr/bin/shake128sum
Provides:       /usr/bin/shake256sum
Provides:       /usr/bin/shred
Provides:       /usr/bin/shuf
Provides:       /usr/bin/sleep
Provides:       /usr/bin/sort
Provides:       /usr/bin/split
Provides:       /usr/bin/stat
Provides:       /usr/bin/stdbuf
Provides:       /usr/bin/stty
Provides:       /usr/bin/sum
Provides:       /usr/bin/sync
Provides:       /usr/bin/tac
Provides:       /usr/bin/tail
Provides:       /usr/bin/tee
Provides:       /usr/bin/test
Provides:       /usr/bin/timeout
Provides:       /usr/bin/touch
Provides:       /usr/bin/tr
Provides:       /usr/bin/true
Provides:       /usr/bin/truncate
Provides:       /usr/bin/tsort
Provides:       /usr/bin/tty
Provides:       /usr/bin/uname
Provides:       /usr/bin/unexpand
Provides:       /usr/bin/uniq
Provides:       /usr/bin/unlink
Provides:       /usr/bin/uptime
Provides:       /usr/bin/users
Provides:       /usr/bin/vdir
Provides:       /usr/bin/wc
Provides:       /usr/bin/who
Provides:       /usr/bin/whoami
Provides:       /usr/bin/yes

     

%description
Empty package to make zypper think GNU coreutils is installed if you use uutils

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/tmp
cp %{name} $RPM_BUILD_ROOT/tmp
echo haha goodbye gnu

%files
/tmp/%{name}

%changelog
* Sat Sep  30 2023 Luana Neder <luana@luana.dev.br> - 9999.99.99
- First version being packaged
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
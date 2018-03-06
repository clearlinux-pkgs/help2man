#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF0DC8E00B28C5995 (bod@debian.org)
#
Name     : help2man
Version  : 1.47.6
Release  : 10
URL      : https://mirrors.kernel.org/gnu/help2man/help2man-1.47.6.tar.xz
Source0  : https://mirrors.kernel.org/gnu/help2man/help2man-1.47.6.tar.xz
Source99 : https://mirrors.kernel.org/gnu/help2man/help2man-1.47.6.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: help2man-bin
Requires: help2man-doc

%description
help2man is a script to create simple man pages from the --help and
--version output of programs.

%package bin
Summary: bin components for the help2man package.
Group: Binaries

%description bin
bin components for the help2man package.


%package doc
Summary: doc components for the help2man package.
Group: Documentation

%description doc
doc components for the help2man package.


%prep
%setup -q -n help2man-1.47.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1520311529
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1520311529
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/help2man

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

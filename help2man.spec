#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : help2man
Version  : 1.47.3
Release  : 3
URL      : http://ftp.gnu.org/gnu/help2man/help2man-1.47.3.tar.xz
Source0  : http://ftp.gnu.org/gnu/help2man/help2man-1.47.3.tar.xz
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
%setup -q -n help2man-1.47.3

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
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

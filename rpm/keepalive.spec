Name:       libkeepalive
Summary:    CPU and display keepalive and scheduling library
Version:    1.1.0
Release:    1
Group:      System/System Control
License:    LGPLv2.1
URL:        https://github.com/nemomobile/nemo-keepalive
Source0:    %{name}-%{version}.tar.bz2
Requires:   dsme
Requires:   mce
Requires:   libiphb >= 1.2.0
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  mce-headers
BuildRequires:  pkgconfig(dsme) >= 0.58
BuildRequires:  pkgconfig(libiphb) >= 1.2.0

%description
CPU and display keepalive and scheduling library

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*
%dir %{_libdir}/qt5/qml/org/nemomobile
%{_libdir}/qt5/qml/org/nemomobile/*

#----------------------------------------------------------------
%package devel
Summary:    Development headers for libkeepalive
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development package for CPU and display keepalive and scheduling library

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/keepalive.pc
%dir %{_includedir}/keepalive
%{_includedir}/keepalive/*.h

#----------------------------------------------------------------
%package examples
Summary:    Example applications for libkeepalive
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description examples
Examples of CPU and display keepalive and scheduling library

%files examples
%defattr(-,root,root,-)
%{_libdir}/qt5/bin/backgroundactivity_periodic
%{_libdir}/qt5/bin/backgroundactivity_linger
%{_libdir}/qt5/bin/displayblanking
%{_libdir}/qt5/examples/keepalive/*.qml

%package tests
Summary:    Tests for libkeepalive
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description tests
%{summary}.
%files tests
%defattr(-,root,root,-)
/opt/tests/nemo-keepalive/*


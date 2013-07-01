Name:           multipath-tools
BuildRequires:  device-mapper-devel
BuildRequires:  libaio-devel
BuildRequires:  readline-devel
Url:            http://christophe.varoqui.free.fr/
Requires:       device-mapper
Requires:       kpartx
Requires(pre):  coreutils grep
Version:        0.4.9
Release:        0
Summary:        Tools to Manage Multipathed Devices with the device-mapper
License:        BSD-3-Clause ; GPL-2.0+ ; LGPL-2.1+ ; MIT
Group:          System/Base
Source:         multipath-tools-%{version}.tar.bz2
Source1001: 	multipath-tools.manifest
%description
This package provides the tools to manage multipathed devices by
instructing the device-mapper multipath module what to do. The tools
are:

- multipath: scans the system for multipathed devices, assembles
   them, and updates the device-mapper's maps

- multipathd: waits for maps events then execs multipath

- devmap-name: provides a meaningful device name to udev for devmaps

- kpartx: maps linear devmaps to device partitions, which makes
multipath maps partionable



%package -n kpartx
Summary:        Manages partition tables on device-mapper devices
Group:          System/Base
Requires:       device-mapper

%description -n kpartx
The kpartx program maps linear devmaps to device partitions, which
makes multipath maps partionable.



Authors:
--------
    Christophe Varoqui <christophe.varoqui@free.fr>

%prep
%setup -q -n multipath-tools-%{version}
cp %{SOURCE1001} .
%build
cd kpartx
make CC="%__cc" OPTFLAGS="$RPM_OPT_FLAGS" LIB=%_libdir

%install
pushd kpartx
make DESTDIR=$RPM_BUILD_ROOT LIB=%_libdir install
popd


%clean
rm -rf $RPM_BUILD_ROOT;

%files
%manifest %{name}.manifest
%defattr(-,root,root)

%files -n kpartx
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%config /usr/lib/udev/rules.d/kpartx.rules
/sbin/kpartx
%dir /lib/udev
/lib/udev/kpartx_id
%{_mandir}/man8/kpartx.8*

%changelog

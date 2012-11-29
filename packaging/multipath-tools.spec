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
%build
make CC="%__cc" OPTFLAGS="$RPM_OPT_FLAGS" LIB=%_lib

%install
make DESTDIR=$RPM_BUILD_ROOT LIB=%_libdir install
mkdir -p $RPM_BUILD_ROOT/var/cache/multipath/
rm $RPM_BUILD_ROOT/usr/include/mpath_persist.h
rm $RPM_BUILD_ROOT/%_lib/libmpathpersist.so

%clean
rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-,root,root)
%license COPYING
%doc multipath.conf*
%dir /etc/udev
%dir /etc/udev/rules.d
%config /etc/init.d/multipathd
%config /etc/init.d/boot.multipath
%config /etc/udev/rules.d/71-multipath.rules
/%{_lib}/libmultipath.so.0
/%{_lib}/libmpathpersist.so.0
/%{_lib}/multipath
/sbin/multipath
/sbin/multipathd
/sbin/mpathpersist
%attr (0700, root, root) /var/cache/multipath
%dir /lib/mkinitrd
%dir /lib/mkinitrd/scripts
/lib/mkinitrd/scripts/boot-multipath.sh
/lib/mkinitrd/scripts/setup-multipath.sh
/lib/mkinitrd/scripts/boot-multipathd.sh
/lib/mkinitrd/scripts/boot-killmultipathd.sh
%dir /lib/systemd/system
/lib/systemd/system/multipathd.service
%{_mandir}/man8/multipath.8*
%{_mandir}/man5/multipath.conf.5*
%{_mandir}/man8/multipathd.8*
%{_mandir}/man8/mpathpersist.8*
%{_mandir}/man3/mpath_persistent_*

%files -n kpartx
%defattr(-,root,root)
%dir /etc/udev
%dir /etc/udev/rules.d
%config /etc/udev/rules.d/70-kpartx.rules
/sbin/kpartx
%dir /lib/udev
/lib/udev/kpartx_id
%dir /lib/mkinitrd
%dir /lib/mkinitrd/scripts
%{_mandir}/man8/kpartx.8*

%changelog

Name:		qemu-ga-static
Version:	3.1.0
Release:	1
Summary:	Static QEMU Guest Agent
License:	GPL
Source0:	.

%description
Static QEMU Guest Agent with init.d-startup and
default method isa-serial for RHEL, CentOS, Fedora

%install
cd %{SOURCE0}
cp -rp usr etc %{buildroot}/

%post
chkconfig qemu-ga on
service qemu-ga start

%preun
service qemu-ga stop
chkconfig qemu-ga on

%files
/usr/local/bin/qemu-ga
/usr/local/etc/qemu/qemu-ga.conf
/etc/init.d/qemu-ga


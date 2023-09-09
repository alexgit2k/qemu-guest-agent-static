# QEMU Guest Agent Static

Statically compiled version of QEMU Guest Agent with init.d-startup and default method isa-serial for RHEL, CentOS, Fedora

## Install

```
rpm -i qemu-ga-static-*.rpm
```

## KVM-Parameters

```
-chardev socket,path=/var/run/qemu-server/123.qga,server,nowait,id=qga0
-device isa-serial,chardev=qga0
```

## RPM-Build

```
rpmbuild -bb qemu-ga-static.spec --define "_sourcedir $PWD"
```

## QEMU-Build

```
./configure --disable-xen --target-list="x86_64-softmmu x86_64-linux-user" --enable-guest-agent --prefix=/usr/local --static
make qemu-ga
strip qemu-ga
```

## Build-Environment CentOS 7

```
# Development tools and libraries
yum groupinstall 'Development Tools'
yum install glibc-static glib2-static pcre-static zlib-static pixman-devel

# Use new development-versions with Software Collections
yum install centos-release-scl
yum install devtoolset-8
scl enable devtoolset-8 bash
```

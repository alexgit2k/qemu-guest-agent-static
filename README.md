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
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig PKG_CONFIG_LIBDIR=/usr/local/lib/pkgconfig
./configure --disable-xen --target-list="x86_64-softmmu x86_64-linux-user" --enable-guest-agent --prefix=/usr/local --static
make qemu-ga
strip qemu-ga
```

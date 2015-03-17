%define   _base node
%define   _dist_ver %(sh /usr/lib/rpm/redhat/dist.sh)

Name:          %{_base}js-svcops
Version:       0.10.37
Release:       1%{_dist_ver}
Summary:       Node.js is a server-side JavaScript environment that uses an asynchronous event-driven model.
Packager:      Chris Kolosiwsky <ckolos@mozilla.com> (adapted from  Kazuhisa Hara <kazuhisya@gmail.com> )
Group:         Development/Libraries
License:       MIT License
URL:           http://nodejs.org
Source0:       %{url}/dist/v%{version}/%{_base}-v%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-tmp
Prefix:        /usr
BuildRequires: redhat-rpm-config
BuildRequires: tar
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: libstdc++-devel
BuildRequires: zlib-devel
BuildRequires: gzip
BuildRequires: python

%description
Node.js is a server-side JavaScript environment that uses an asynchronous event-driven model.
This allows Node.js to get excellent performance based on the architectures of many Internet applications.

%prep
rm -rf $RPM_SOURCE_DIR/%{_base}-v%{version}
%setup -q -n %{_base}-v%{version}

%build
%define _node_arch %{nil}
%ifarch x86_64
  %define _node_arch x64
%endif
%ifarch i386 i686
  %define _node_arch x86
%endif
if [ -z %{_node_arch} ];then
  echo "bad arch"
  exit 1
fi

./configure \
    --shared-openssl \
    --shared-openssl-includes=%{_includedir} \
    --shared-zlib \
    --shared-zlib-includes=%{_includedir}
make binary %{?_smp_mflags}

pushd $RPM_SOURCE_DIR
mv $RPM_BUILD_DIR/%{_base}-v%{version}/%{_base}-v%{version}-linux-%{_node_arch}.tar.gz .
rm  -rf %{_base}-v%{version}
tar zxvf %{_base}-v%{version}-linux-%{_node_arch}.tar.gz
popd

%install
rm -rf $RPM_BUILD_ROOT
mkdir  -p $RPM_BUILD_ROOT/usr
cp -Rp $RPM_SOURCE_DIR/%{_base}-v%{version}-linux-%{_node_arch}/* $RPM_BUILD_ROOT/usr/
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/%{_base}-v%{version}/

for file in ChangeLog LICENSE README.md ; do
    mv $RPM_BUILD_ROOT/usr/$file $RPM_BUILD_ROOT/usr/share/doc/%{_base}-v%{version}/
done
mkdir -p $RPM_BUILD_ROOT/usr/share/%{_base}js
mv $RPM_SOURCE_DIR/%{_base}-v%{version}-linux-%{_node_arch}.tar.gz $RPM_BUILD_ROOT/usr/share/%{_base}js/

# prefix all manpages with "npm-"
pushd $RPM_BUILD_ROOT/usr/lib/node_modules/npm/man/
for dir in *; do
    mkdir -p $RPM_BUILD_ROOT/usr/share/man/$dir
    pushd $dir
    for page in *; do
        if [[ $page != npm* ]]; then
        mv $page npm-$page
    fi
    done
    popd
    cp $dir/* $RPM_BUILD_ROOT/usr/share/man/$dir
done
popd

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_SOURCE_DIR/%{_base}-v%{version}-linux-%{_node_arch}

%files
%defattr(-,root,root,-)
%{_prefix}/lib/node_modules/npm
%{_prefix}/share/doc/%{_base}-v%{version}
%{_includedir}/node
%{_prefix}/share/%{_base}js/%{_base}-v%{version}-linux-%{_node_arch}.tar.gz
%defattr(755,root,root)
%{_bindir}/node
%{_bindir}/npm

%doc
/usr/share/man/man1
/usr/share/man/man3
/usr/share/man/man5
/usr/share/man/man7

%changelog
* Fri Mar 16 2015 Benson Wong <bwong@mozilla.com>
- Updated to nodejs version 0.10.37
* Fri Feb 13 2015 Benson Wong <bwong@mozilla.com>
- Updated to nodejs version 0.10.36
* Wed Sep 18 2014 Benson Wong <bwong@mozilla.com>
- Updated to nodejs version 0.10.32
- Removed support for el5
- fixed naming of SRPM for el7
* Wed Sep 10 2014 Benson Wong <bwong@mozilla.com>
- Updated to nodejs version 0.10.30
* Thu May  8 2014 Chris Kolosiwsky <ckolos@mozilla.com>
- Updated to match upstream; applied all previously made changes

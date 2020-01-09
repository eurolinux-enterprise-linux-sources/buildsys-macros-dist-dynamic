%define major_release 7

Name:		buildsys-macros-dist-dynamic
Version:	0.%{major_release}
Release:	4%{?dist}
Summary:	RPM dist macro for the build system

Group:		Development/Buildsystem
License:	GPL
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Source0:	macros.distag_dynamic

BuildRequires:	coreutils
BuildArch:	noarch

Provides:	buildsys-macros-dist
Requires:	bash
Requires:	rpm-build

%description
This package provides the dist macro for the build system.

The macro in this package is special.  It looks in:
~/rpmbuild/SRPMS
/builddir/build/originals

for the last '*.src.rpm' and determines the dist macro from
what it finds there.

%install
rm -rf %{buildroot}
install -D -m 644 -p $RPM_SOURCE_DIR/macros.distag_dynamic %{buildroot}/etc/rpm/macros.disttag


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/etc/rpm/macros.disttag


%changelog
* Wed Jan 28 2015 Pat Riehecky <riehecky@fnal.gov>
- fixed elifs

* Wed Jan 28 2015 Pat Riehecky <riehecky@fnal.gov>
- PRJTASK0026710, now supports sl{rhel}_x

* Mon Sep 15 2014 Pat Riehecky <riehecky@fnal.gov>
- Now supports the .ep6.el7 macro from jboss (I think)

* Tue May 21 2013 Pat Riehecky <riehecky@fnal.gov>
- Initial build for SL7

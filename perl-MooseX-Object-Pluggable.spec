
%define realname   MooseX-Object-Pluggable
%define version    0.0011
%define release    5

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Make your classes pluggable
Source:     http://www.cpan.org/modules/by-module/MooseX/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Pluggable::Object)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
This module is meant to be loaded as a role from Moose-based classes it
will add five methods and four attributes to assist you with the loading
and handling of plugins and extensions for plugins. I understand that this
may pollute your namespace, however I took great care in using the least
ambiguous names possible.





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.0011-3mdv2011.0
+ Revision: 655108
- rebuild for updated spec-helper

* Mon May 03 2010 Jérôme Quelin <jquelin@mandriva.org> 0.0011-2mdv2011.0
+ Revision: 541803
- rebuild

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.0011-1mdv2010.0
+ Revision: 369778
- update to new version 0.0011

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.0009-1mdv2009.1
+ Revision: 314340
- new version

* Wed Dec 03 2008 Jérôme Quelin <jquelin@mandriva.org> 0.0008-1mdv2009.1
+ Revision: 309774
- import perl-MooseX-Object-Pluggable


* Wed Dec 03 2008 cpan2dist 0.0008-1mdv
- initial mdv release, generated with cpan2dist



%define realname   MooseX-Object-Pluggable
%define version    0.0011
%define release    %mkrel 2

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



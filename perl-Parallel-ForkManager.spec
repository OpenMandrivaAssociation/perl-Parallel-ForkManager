%define module Parallel-ForkManager

Summary:	Simple parallel processing fork manager
Name:		perl-%{module}
Version:	0.7.5
Release:	%mkrel 1
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Parallel-ForkManager/
Source0:	http://www.cpan.org/modules/by-module/Parallel/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module is intended for use in operations that can be done in parallel
where the number of processes to be forked off should be limited. Typical
use is a downloader which will be retrieving hundreds/thousands of files.

%prep

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*


%define upstream_name    Parallel-ForkManager
%define upstream_version 0.7.6

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Simple parallel processing fork manager
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Parallel-ForkManager/
Source0:	http://www.cpan.org/modules/by-module/Parallel/%{upstream_name}-%{version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module is intended for use in operations that can be done in parallel
where the number of processes to be forked off should be limited. Typical
use is a downloader which will be retrieving hundreds/thousands of files.

%prep

%setup -q -n %{upstream_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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

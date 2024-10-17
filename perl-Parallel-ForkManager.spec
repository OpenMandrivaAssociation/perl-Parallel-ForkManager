%define upstream_name    Parallel-ForkManager
%define upstream_version 1.06
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Simple parallel processing fork manager
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/Parallel-ForkManager/
Source0:	http://www.cpan.org/modules/by-module/Parallel/Parallel-ForkManager-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module is intended for use in operations that can be done in parallel
where the number of processes to be forked off should be limited. Typical
use is a downloader which will be retrieving hundreds/thousands of files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.7.9-2mdv2011.0
+ Revision: 657818
- rebuild for updated spec-helper

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.7.9-1mdv2011.0
+ Revision: 596636
- update to 0.7.9

* Tue Aug 17 2010 Jérôme Quelin <jquelin@mandriva.org> 0.7.6-1mdv2011.0
+ Revision: 570745
- update to 0.7.6

* Sun Jun 21 2009 Oden Eriksson <oeriksson@mandriva.com> 0.7.5-1mdv2010.0
+ Revision: 387611
- import perl-Parallel-ForkManager


* Sun Jun 21 2009 Oden Eriksson <oeriksson@mandriva.com> 0.7.5-1mdv2009.0
- initial Mandriva package




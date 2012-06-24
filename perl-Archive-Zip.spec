#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Archive
%define		pnam	Zip
Summary:	Archive::Zip - module for manipulation of ZIP archives
Summary(pl):	Archive::Zip - modu� do manipulacji archiwami ZIP
Name:		perl-Archive-Zip
Version:	1.05
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	33ee624c7be5b35c635b9e6831d076bd
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Compress-Zlib >= 1.14
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Archive::Zip module allows a Perl program to create, manipulate,
read, and write ZIP archive files.

%description -l pl
Modu� Archive::Zip udost�pnia programom w Perlu mo�liwo�� tworzenia,
manipulowania, czytania i zapisywania archiw�w ZIP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README TODO docs/*
%attr(755,root,root) %{_bindir}/crc32
%dir %{perl_vendorlib}/Archive/Zip
%{perl_vendorlib}/Archive/Zip/*.pm
%{perl_vendorlib}/Archive/Zip.pm
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*

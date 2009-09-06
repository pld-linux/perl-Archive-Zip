#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Archive
%define		pnam	Zip
Summary:	Archive::Zip - module for manipulation of ZIP archives
Summary(pl.UTF-8):	Archive::Zip - moduł do manipulacji archiwami ZIP
Name:		perl-Archive-Zip
Version:	1.30
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Archive/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	40153666e7538b410e001aa8a810e702
URL:		http://search.cpan.org/dist/Archive-Zip/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl-Compress-Zlib >= 1.14
BuildRequires:	perl-File-Which >= 0.05
BuildRequires:	perl-Test-Simple >= 0.42
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Archive::Zip module allows a Perl program to create, manipulate,
read, and write ZIP archive files.

%description -l pl.UTF-8
Moduł Archive::Zip udostępnia programom w Perlu możliwość tworzenia,
manipulowania, czytania i zapisywania archiwów ZIP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/crc32
%dir %{perl_vendorlib}/Archive/Zip
%{perl_vendorlib}/Archive/Zip/*.pm
%{perl_vendorlib}/Archive/Zip.pm
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*

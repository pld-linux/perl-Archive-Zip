%include	/usr/lib/rpm/macros.perl
%define		pdir	Archive
%define		pnam	Zip
Summary:	Archive::Zip perl module
Summary(pl):	Modu³ perla Archive::Zip
Name:		perl-Archive-Zip
Version:	1.01
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Archive::Zip - module for manipulation of zip archives.

%description -l pl
Archive::Zip - modu³ do manipulacji archiwami zip.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO docs/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*.gz
%{_mandir}/man3/*
%attr(755,root,root) %{_bindir}/crc32
%dir %{perl_sitelib}/Archive/Zip
%{perl_sitelib}/Archive/Zip/*.pm
%{perl_sitelib}/Archive/Zip.pm

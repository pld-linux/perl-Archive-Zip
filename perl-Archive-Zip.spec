%include	/usr/lib/rpm/macros.perl
%define		pdir	Archive
%define		pnam	Zip
Summary:	Archive::Zip - module for manipulation of ZIP archives
Summary(pl):	Archive::Zip - modu³ do manipulacji archiwami ZIP
Name:		perl-Archive-Zip
Version:	1.02
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Archive::Zip module allows a Perl program to create, manipulate,
read, and write ZIP archive files.

%description -l pl
Modu³ Archive::Zip udostêpnia programom w Perlu mo¿liwo¶æ tworzenia,
manipulowania, czytania i zapisywania archiwów ZIP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

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
%dir %{perl_sitelib}/Archive/Zip
%{perl_sitelib}/Archive/Zip/*.pm
%{perl_sitelib}/Archive/Zip.pm
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*

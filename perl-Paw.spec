# $Revision: 1.6 $
%include	/usr/lib/rpm/macros.perl
Summary:	Paw perl module
Summary(pl):	Modu³ perla Paw
Name:		perl-Paw
Version:	0.52
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	 ftp://ftp.perl.org/pub/CPAN/authors/id/U/UG/UGANSERT/Paw-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Curses
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl Paw modules.

%description -l pl
Modu³ perla Paw.

%prep
%setup -q -n Paw-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -r Paw/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_sitelib}/Paw
%{perl_sitelib}/Paw/*.pm
%{perl_sitelib}/Paw/*.pod
%{perl_sitelib}/Paw.pm
%{_examplesdir}/%{name}-%{version}

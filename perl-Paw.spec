# $Revision: 1.8 $
%include	/usr/lib/rpm/macros.perl
Summary:	Paw perl module
Summary(pl):	Modu� perla Paw
Name:		perl-Paw
Version:	0.52
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(is):	�r�unart�l/Forritunarm�l/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	��ȯ/����/Perl
Group(no):	Utvikling/Programmeringsspr�k/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Group(sl):	Razvoj/Jeziki/Perl
Group(sv):	Utveckling/Spr�k/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/authors/id/U/UG/UGANSERT/Paw-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Curses
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl Paw modules.

%description -l pl
Modu� perla Paw.

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

%include	/usr/lib/rpm/macros.perl
%define		pnam	Paw
Summary:	Paw Perl module
Summary(cs):	Modul Paw pro Perl
Summary(da):	Perlmodul Paw
Summary(de):	Paw Perl Modul
Summary(es):	M�dulo de Perl Paw
Summary(fr):	Module Perl Paw
Summary(it):	Modulo di Perl Paw
Summary(ja):	Paw Perl �⥸�塼��
Summary(ko):	Paw �� ����
Summary(no):	Perlmodul Paw
Summary(pl):	Modu� Perla Paw
Summary(pt):	M�dulo de Perl Paw
Summary(pt_BR):	M�dulo Perl Paw
Summary(ru):	������ ��� Perl Paw
Summary(sv):	Paw Perlmodul
Summary(uk):	������ ��� Perl Paw
Summary(zh_CN):	Paw Perl ģ��
Name:		perl-Paw
Version:	0.52
Release:	4
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/authors/id/U/UG/UGANSERT/%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Curses
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl Paw modules.

%description -l pl
Modu� perla Paw.

%prep
%setup -q -n %{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_mandir}/{,de/}man3

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -f Paw/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cd $RPM_BUILD_ROOT%{perl_sitelib}/Paw
mv Paw-de.pod Paw.pod
pod2man --section=3pm Paw.pod >$RPM_BUILD_ROOT%{_mandir}/de/man3/Paw.3pm
rm -f Paw.pod

for i in *-de.pod; do
	n=`echo $i | sed 's/-de\.pod$//'`
	mv $i $n.pod
	pod2man --section=3pm $n.pod >$RPM_BUILD_ROOT%{_mandir}/de/man3/Paw::$n.3pm
done
rm -f *.pod

for i in *.pm; do
	if grep '^=head' $i >/dev/null; then
		n=`echo $i | sed 's/\.pm$//'`
        	pod2man --section=3pm $i >$RPM_BUILD_ROOT%{_mandir}/man3/Paw::$n.3pm
	fi
done

cd ..
pod2man --section=3pm Paw.pm >$RPM_BUILD_ROOT%{_mandir}/man3/Paw.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes.txt
%dir %{perl_sitelib}/Paw
%{perl_sitelib}/Paw/*.pm
%{perl_sitelib}/Paw.pm
%{_mandir}/man3/*
%lang(de) %{_mandir}/de/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl

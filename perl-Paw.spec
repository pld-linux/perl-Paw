#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Paw
Summary:	Paw Perl module
Summary(cs):	Modul Paw pro Perl
Summary(da):	Perlmodul Paw
Summary(de):	Paw Perl Modul
Summary(es):	Módulo de Perl Paw
Summary(fr):	Module Perl Paw
Summary(it):	Modulo di Perl Paw
Summary(ja):	Paw Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Paw ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Paw
Summary(pl):	Modu³ Perla Paw
Summary(pt):	Módulo de Perl Paw
Summary(pt_BR):	Módulo Perl Paw
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Paw
Summary(sv):	Paw Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Paw
Summary(zh_CN):	Paw Perl Ä£¿é
Name:		perl-Paw
Version:	0.54
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/U/UG/UGANSERT/%{pnam}-%{version}.tar.gz
# Source0-md5:	1bdc9ec343614dc345f8c602f716f777
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Curses
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Perl Paw modules.

%description -l pl
Modu³ perla Paw.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_mandir}/{,de/}man3

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -f Paw/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT%{perl_vendorlib}/Paw/examples

cd $RPM_BUILD_ROOT%{perl_vendorlib}/Paw
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
%dir %{perl_vendorlib}/Paw
%{perl_vendorlib}/Paw/*.pm
%{perl_vendorlib}/Paw.pm
%{_mandir}/man3/*
%lang(de) %{_mandir}/de/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl

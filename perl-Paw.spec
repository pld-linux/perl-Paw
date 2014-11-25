#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pnam	Paw
%include	/usr/lib/rpm/macros.perl
Summary:	Paw Perl module
Summary(cs.UTF-8):	Modul Paw pro Perl
Summary(da.UTF-8):	Perlmodul Paw
Summary(de.UTF-8):	Paw Perl Modul
Summary(es.UTF-8):	Módulo de Perl Paw
Summary(fr.UTF-8):	Module Perl Paw
Summary(it.UTF-8):	Modulo di Perl Paw
Summary(ja.UTF-8):	Paw Perl モジュール
Summary(ko.UTF-8):	Paw 펄 모줄
Summary(nb.UTF-8):	Perlmodul Paw
Summary(pl.UTF-8):	Moduł Perla Paw
Summary(pt.UTF-8):	Módulo de Perl Paw
Summary(pt_BR.UTF-8):	Módulo Perl Paw
Summary(ru.UTF-8):	Модуль для Perl Paw
Summary(sv.UTF-8):	Paw Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Paw
Summary(zh_CN.UTF-8):	Paw Perl 模块
Name:		perl-Paw
Version:	0.54
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/U/UG/UGANSERT/%{pnam}-%{version}.tar.gz
# Source0-md5:	1bdc9ec343614dc345f8c602f716f777
URL:		http://search.cpan.org/dist/Paw/
BuildRequires:	perl-Curses
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl Paw modules.

%description -l pl.UTF-8
Moduł Perla Paw.

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

#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Parse
%define		pnam	Lex
Summary:	perlmodule
#Summary(pl):	
Name:		perl-Parse-Lex
Version:	2.15
Release:	0.1
License:	x
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/P/PV/PVERD/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	aeb0bb36454485d28214aad0907d5c92
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description


# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes doc README
%{perl_vendorlib}/Parse/*.pm
#%{perl_vendorlib}/Parse/Lex/
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

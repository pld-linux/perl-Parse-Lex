#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Parse
%define		pnam	Lex
Summary:	Parse::Lex - generator of lexical analyzers
Summary(pl.UTF-8):	Parse::Lex - generator analizatorów leksykalnych
Name:		perl-Parse-Lex
Version:	2.15
Release:	0.2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/P/PV/PVERD/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	aeb0bb36454485d28214aad0907d5c92
Patch0:		%{name}-strict.patch
URL:		http://search.cpan.org/dist/ParseLex/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The classes Parse::Lex and Parse::CLex create lexical analyzers.

%description -l pl.UTF-8
Klasy Parse::Lex i Parse::CLex tworzą analizatory leksykalne.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}
%patch -P0 -p1

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
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

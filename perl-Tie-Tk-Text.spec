#
# Conditional build:
%bcond_with	tests		# perform "make test", requires DISPLAY

%define		pdir	Tie
%define		pnam	Tk-Text
Summary:	Tie::Tk::Text - Access Tk text widgets as arrays
Name:		perl-Tie-Tk-Text
Version:	0.92
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Tie/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9e2064a300a46f2df81df5383c24f068
URL:		http://search.cpan.org/dist/Tie-Tk-Text/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Tk
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module defines a class for tie()ing Tk text widgets to an array,
allowing them to be accessed as if they were an array of lines.

It's not expected that anyone will actually want to populate and
manipulate their text widgets this way, though you are of course free
to do so. This module was created to make text widgets accessible to
functions that expect an array reference as their input. (e.g.
Algorithm::Diff::sdiff) You can do that with read-only support (FETCH
and FETCHSIZE). All of the methods (PUSH, POP, STORE, etc.) are
included for completeness.

Note: This documentation refers to "Tk text" widgets rather than
"Tk::Text" ones. That's because it supports anything that uses the
same API as a Tk text widget. It works with Perl/Tk and Tkx and should
work with Tcl::Tk as well.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT
./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Tie/Tk
%{perl_vendorlib}/Tie/Tk/Text.pm
%{_mandir}/man3/Tie::Tk::Text.3pm*

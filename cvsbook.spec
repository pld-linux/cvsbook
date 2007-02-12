Summary:	CVS book
Summary(pl.UTF-8):	Książka o CVS-ie
Name:		cvsbook
Version:	1.21
Release:	1
License:	GPL v2
Group:		Documentation
Source0:	http://cvsbook.red-bean.com/%{name}-%{version}-texi.tar.gz
# Source0-md5:	9bcfccd92dd153d1c3e928b948c091a4
Patch0:		%{name}-dir.patch
URL:		http://cvsbook.red-bean.com/
BuildRequires:	texinfo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of free chapters "Open Source development with CVS" book about
using CVS (Concurrent Versions System) for collaboration and version
control. It covers everything from CVS installation and basic
concepts all the way to advanced usage and administration. It is
intended for anyone who uses or plans to use CVS.

%description -l pl.UTF-8
Zbiór wolnodostępnych rozdziałów książki "Open Source development with
CVS" (rozwijanie oprogramowania o otwartych źródłach przy użyciu
CVS-u) o korzystaniu z CVS-u do wspólnej pracy i kontroli wersji.
Pokrywa wszystko od instalacji CVS-u i podstawowych idei do
zaawansowanych zastosowań i administracji. Jest przeznaczony dla
każdego, kto używa lub planuje używać CVS-u.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}
makeinfo --no-split --fill-column=72 main.texi
install cvsbook.info $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc TODO
%{_infodir}/cvsbook.info*

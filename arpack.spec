Summary:	Subroutines for solving large scale eigenvalue problems.
Summary(pl):	Rozwi±zywanie zagadnienia w³asnego dla du¿ych macierzy.
Name:		arpack
Version:	2.1
Release:	1
License:	Freely distributable
Group:		Development/Libraries
URL:		http://www.caam.rice.edu/software/ARPACK/
Source0:	http://www.caam.rice.edu/software/ARPACK/SRC/%{name}96.tar.gz
Source1:	http://www.caam.rice.edu/software/ARPACK/SRC/patch.tar.gz
Patch0:		%{name}-automake_support.patch
BuildRequires:	gcc-g77
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool	>= 1:1.4.2-9
Requires:	lapack
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ARPACK software is capable of solving large scale symmetric,
nonsymmetric, and generalized eigenproblems from significant
application areas. The software is designed to compute a few (k)
eigenvalues with user specified features such as those of largest real
part or largest magnitude. Storage requirements are on the order of
n*k locations. No auxiliary storage is required. A set of Schur basis
vectors for the desired k-dimensional eigen-space is computed which is
numerically orthogonal to working precision. Numerically accurate
eigenvectors are available on request.

%description -l pl
Rozwi±zywanie zagadnienia w³asnego (symetrycznego, niesymetrycznego,
ogólnego) dla du¿ych macierzy. Macierz mo¿e byæ dowolna, przy czym
procedury dzia³aj± szczególnie dobrze w przypadku du¿ych macierzy
rzadkich b±d¼ macierzy ze znan± struktur±.

%package devel
Summary:	ARPACK header files.
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	lapack-devel

%description devel
ARPACK header files.

%description devel -l pl
Pliki nag³ówkowe ARPACK.

%package static
Summary:	Static ARPACK libraries.
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static ARPACK libraries.

%description static -l pl
Biblioteki statyczne ARPACK.

%prep
%setup -q -a1 -n ARPACK
%patch -p1

%build
rm -f ltmain.sh missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

# libtool 1.4d requires --tag for g77, libtool 1.4.2 fails when --tag is passed
LTTAG=""
grep -q -e '--tag' `which libtool` && LTTAG="--tag=F77"

%{__make} LTTAG="$LTTAG"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libarpack.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libarpack.so
%{_libdir}/libarpack.la

%files static
%defattr(644,root,root,755)
%{_libdir}/libarpack.a

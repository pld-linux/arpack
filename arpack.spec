#
# Conditional build:
%bcond_with	acml	# With ACML version of BLAS instead of NETLIB implementation
Summary:	Subroutines for solving large scale eigenvalue problems
Summary(pl):	Rozwi±zywanie zagadnienia w³asnego dla du¿ych macierzy
Name:		arpack
Version:	2.1
Release:	3%{?with_acml:ACML}
License:	Freely distributable
Group:		Libraries
Source0:	http://www.caam.rice.edu/software/ARPACK/SRC/%{name}96.tar.gz
# Source0-md5:	fffaa970198b285676f4156cebc8626e
Source1:	http://www.caam.rice.edu/software/ARPACK/SRC/patch.tar.gz
# Source1-md5:	14830d758f195f272b8594a493501fa2
Source2:	http://www.caam.rice.edu/software/ARPACK/SRC/ug.ps.gz
# Source2-md5:	79cc51e4812c75873adafcad2185842e
Source3:	http://www.caam.rice.edu/software/ARPACK/SRC/P57_58.ps.gz
# Source3-md5:	b86d77199f989fc438acaf7ac0433e76
Source4:	http://www.caam.rice.edu/software/ARPACK/SRC/P61_62.ps.gz
# Source4-md5:	d116887acb3d61fecf645c2d37d4d517
Patch0:		%{name}-automake_support.patch
URL:		http://www.caam.rice.edu/software/ARPACK/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-g77
BuildRequires:	libtool	>= 2:1.5
%{!?with_acml:BuildRequires:	blas-devel}
%{?with_acml:ExclusiveArch:	amd64}
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
rzadkich b±d¼ macierzy ze znan± struktur±. Biblioteka s³u¿y do
obliczenia kilku (k) warto¶ci w³asnych o zadanych z góry w³asno¶ciach,
takich jak najwiêksza (najmniejsza) czê¶æ rzeczywista albo najwiêkszy
(najmniejszy) modu³. Wymagania pamiêciowe s± rzedu n*k, ¿adna
dodatkowa pamiêæ (np. dyskowa) nie jest wymagana.

%package devel
Summary:	ARPACK development files
Summary(pl):	Pliki programistyczne ARPACK
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{!?with_acml:Requires:	blas-devel}

%description devel
ARPACK development files.

%description devel -l pl
Pliki programistyczne ARPACK.

%package static
Summary:	Static ARPACK library
Summary(pl):	Statyczna biblioteka ARPACK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
%{!?with_acml:Requires:	blas-static}

%description static
Static ARPACK library.

%description static -l pl
Statyczna biblioteka ARPACK.

%prep
%setup -q -n ARPACK -b1
%patch -p1
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	LDFLAGS=%{?with_acml:-lacml}%{!?with_acml:-lblas}


%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc DOCUMENTS/*.doc *.ps.gz
%{_libdir}/libarpack.la

%files static
%defattr(644,root,root,755)
%{_libdir}/libarpack.a

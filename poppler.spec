#
# Conditional build:
%bcond_with	cairo	# enable Cairo backend
#
Summary:	PDF rendering library
Summary(pl):	Biblioteka renderuj±ca PDF
Name:		poppler
Version:	0.1.1
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
# Source0-md5:	d10982c93a1ccee79a14bb277f94990a
Patch0:		%{name}-link.patch
URL:		http://poppler.freedesktop.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
%{?with_cairo:BuildRequires:	cairo-devel >= 0.3.0}
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
%{?with_cairo:Requires:	cairo >= 0.3.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A common PDF rendering library for integrating PDF viewing into
desktop applications (based on the xpdf-3.0 code base).

%description -l pl
Wspólna biblioteka renderuj±ca PDF do integrowania ogl±dania PDF w
aplikacjach desktopowych (oparta na kodzie xpdf-3.0).

%package devel
Summary:	Poppler header files
Summary(pl):	Pliki nag³ówkowe biblioteki Poppler
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_cairo:Requires:	cairo-devel >= 0.3.0}
Requires:	fontconfig-devel
Requires:	freetype-devel >= 2.0
Requires:	libstdc++-devel

%description devel
Header files for the Poppler library.

%description devel -l pl
Pliki nag³ówkowe biblioteki Poppler.

%package static
Summary:	Poppler static libraries
Summary(pl):	Statyczne biblioteki Poppler
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Poppler static libraries.

%description static -l pl
Statyczne biblioteki Poppler.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_cairo:--disable-cairo-output} \
	--enable-a4-paper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/poppler
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

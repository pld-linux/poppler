#
# Conditional build:
%bcond_without	cairo	# disable Cairo backend
%bcond_without	qt	# disable qt wrapper
#
%define		cairo_ver	1.0.0
#
Summary:	PDF rendering library
Summary(pl):	Biblioteka renderuj±ca PDF
Name:		poppler
Version:	0.4.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
# Source0-md5:	beb1eea135a3c5b679a7a22d01a500c0
Patch0:		%{name}-link.patch
Patch1:		%{name}-freetype_includes.patch
URL:		http://poppler.freedesktop.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
%{?with_cairo:BuildRequires:	cairo-devel >= %{cairo_ver}}
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
%{?with_qt:BuildRequires:	qt-devel}
%{?with_cairo:Requires:	cairo >= %{cairo_ver}}
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
%{?with_cairo:Requires:	cairo-devel >= %{cairo_ver}}
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

%package glib
Summary:	GLib wrapper for poppler
Summary(pl):	Wrapper GLib dla popplera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description glib
GLib wrapper for poppler.

%description glib -l pl
Wrapper GLib dla popplera.

%package glib-devel
Summary:	Header files for GLib wrapper for poppler
Summary(pl):	Pliki nag³ówkowe wrappera GLib dla popplera
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-glib = %{version}-%{release}
Requires:	gtk+2-devel >= 2.0.0

%description glib-devel
Header files for GLib wrapper for poppler.

%description glib-devel -l pl
Pliki nag³ówkowe wrappera GLib dla popplera.

%package glib-static
Summary:	Static version of GLib wrapper for poppler
Summary(pl):	Statyczna wersja wrappera GLib dla popplera
Group:		Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}

%description glib-static
Static version of GLib wrapper for poppler.

%description glib-static -l pl
Statyczna wersja wrappera GLib dla popplera.

%package qt
Summary:	Qt wrapper for poppler
Summary(pl):	Wrapper Qt dla popplera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description qt
Qt wrapper for poppler.

%description qt -l pl
Wrapper Qt dla popplera.

%package qt-devel
Summary:	Header files for Qt wrapper for poppler
Summary(pl):	Pliki nag³ówkowe wrappera Qt dla popplera
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt = %{version}-%{release}
Requires:	qt-devel

%description qt-devel
Header files for Qt wrapper for poppler.

%description qt-devel -l pl
Pliki nag³ówkowe wrappera Qt dla popplera.

%package qt-static
Summary:	Static version of Qt wrapper for poppler
Summary(pl):	Statyczna wersja wrappera Qt dla popplera
Group:		Development/Libraries
Requires:	%{name}-qt-devel = %{version}-%{release}

%description qt-static
Static version of Qt wrapper for poppler.

%description qt-static -l pl
Statyczna wersja wrappera Qt dla popplera.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	QTLIB=%{_libdir} \
	%{!?with_cairo:--disable-cairo-output} \
	%{!?with_qt:--disable-poppler-qt} \
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

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%post	qt -p /sbin/ldconfig
%postun	qt -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_libdir}/libpoppler.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler.so
%{_libdir}/libpoppler.la
%{_includedir}/poppler
%exclude %{_includedir}/poppler/glib
%{?with_qt:%exclude %{_includedir}/poppler/poppler-qt.h}
%{_pkgconfigdir}/poppler.pc
%{?with_cairo:%{_pkgconfigdir}/poppler-cairo.pc}
%{_pkgconfigdir}/poppler-splash.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpoppler.a

%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-glib.so.*.*.*

%files glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-glib.so
%{_libdir}/libpoppler-glib.la
%{_includedir}/poppler/glib
%{_pkgconfigdir}/poppler-glib.pc

%files glib-static
%defattr(644,root,root,755)
%{_libdir}/libpoppler-glib.a

%if %{with qt}
%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-qt.so.*.*.*

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-qt.so
%{_libdir}/libpoppler-qt.la
%{_includedir}/poppler/poppler-qt.h
%{_pkgconfigdir}/poppler-qt.pc

%files qt-static
%defattr(644,root,root,755)
%{_libdir}/libpoppler-qt.a
%endif

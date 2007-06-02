#
# Conditional build:
%bcond_without	apidocs # disable gtk-doc 
%bcond_without	cairo	# disable Cairo backend
%bcond_without	qt	# disable qt wrapper
%bcond_without	qt4	# disable qt4 wrapper
#
%define		cairo_ver	1.0.0
#
Summary:	PDF rendering library
Summary(pl.UTF-8):	Biblioteka renderująca PDF
Name:		poppler
Version:	0.5.9
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
# Source0-md5:	8d1ac008614c0e413bcac95b8102fa07
Patch0:		%{name}-qt_m4.patch
URL:		http://poppler.freedesktop.org/
%{?with_qt4:BuildRequires:	QtGui-devel >= 4.1.0}
%{?with_qt4:BuildRequires:	QtXml-devel >= 4.1.0}
%{?with_qt4:BuildRequires:	QtTest-devel >= 4.1.0}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
%{?with_cairo:BuildRequires:	cairo-devel >= %{cairo_ver}}
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.8.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.0}
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
%{?with_qt:BuildRequires:	qt-devel >= 3.0}
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A common PDF rendering library for integrating PDF viewing into
desktop applications (based on the xpdf-3.0 code base).

%description -l pl.UTF-8
Wspólna biblioteka renderująca PDF do integrowania oglądania PDF w
aplikacjach desktopowych (oparta na kodzie xpdf-3.0).

%package devel
Summary:	Poppler header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Poppler
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fontconfig-devel
Requires:	freetype-devel >= 2.0
Requires:	libstdc++-devel

%description devel
Header files for the Poppler library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Poppler.

%package static
Summary:	Poppler static libraries
Summary(pl.UTF-8):	Statyczne biblioteki Poppler
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Poppler static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Poppler.

%package glib
Summary:	GLib wrapper for poppler
Summary(pl.UTF-8):	Wrapper GLib dla popplera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_cairo:Requires:	cairo >= %{cairo_ver}}
Requires:	gtk+2 >= 2:2.8.0

%description glib
GLib wrapper for poppler.

%description glib -l pl.UTF-8
Wrapper GLib dla popplera.

%package glib-devel
Summary:	Header files for GLib wrapper for poppler
Summary(pl.UTF-8):	Pliki nagłówkowe wrappera GLib dla popplera
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-glib = %{version}-%{release}
%{?with_cairo:Requires:	cairo-devel >= %{cairo_ver}}
Requires:	gtk+2-devel >= 2:2.8.0

%description glib-devel
Header files for GLib wrapper for poppler.

%description glib-devel -l pl.UTF-8
Pliki nagłówkowe wrappera GLib dla popplera.

%package glib-static
Summary:	Static version of GLib wrapper for poppler
Summary(pl.UTF-8):	Statyczna wersja wrappera GLib dla popplera
Group:		Development/Libraries
Requires:	%{name}-glib-devel = %{version}-%{release}

%description glib-static
Static version of GLib wrapper for poppler.

%description glib-static -l pl.UTF-8
Statyczna wersja wrappera GLib dla popplera.

%package qt
Summary:	Qt wrapper for poppler
Summary(pl.UTF-8):	Wrapper Qt dla popplera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description qt
Qt wrapper for poppler.

%description qt -l pl.UTF-8
Wrapper Qt dla popplera.

%package qt-devel
Summary:	Header files for Qt wrapper for poppler
Summary(pl.UTF-8):	Pliki nagłówkowe wrappera Qt dla popplera
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt = %{version}-%{release}
Requires:	qt-devel

%description qt-devel
Header files for Qt wrapper for poppler.

%description qt-devel -l pl.UTF-8
Pliki nagłówkowe wrappera Qt dla popplera.

%package qt-static
Summary:	Static version of Qt wrapper for poppler
Summary(pl.UTF-8):	Statyczna wersja wrappera Qt dla popplera
Group:		Development/Libraries
Requires:	%{name}-qt-devel = %{version}-%{release}

%description qt-static
Static version of Qt wrapper for poppler.

%description qt-static -l pl.UTF-8
Statyczna wersja wrappera Qt dla popplera.

%package Qt
Summary:	Qt4 wrapper for poppler
Summary(pl.UTF-8):	Wrapper Qt4 dla popplera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description Qt
Qt4 wrapper for poppler.

%description Qt -l pl.UTF-8
Wrapper Qt4 dla popplera.

%package Qt-devel
Summary:	Header files for Qt4 wrapper for poppler
Summary(pl.UTF-8):	Pliki nagłówkowe wrappera Qt4 dla popplera
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-Qt = %{version}-%{release}
Requires:	QtGui-devel
Requires:	QtXml-devel

%description Qt-devel
Header files for Qt4 wrapper for poppler.

%description Qt-devel -l pl.UTF-8
Pliki nagłówkowe wrapper Qt4 dla popplera.

%package Qt-static
Summary:	Static version of Qt4 wrapper for poppler
Summary(pl.UTF-8):	Statyczna wersja wrappera Qt4 dla popplera
Group:		Development/Libraries
Requires:	%{name}-Qt-devel = %{version}-%{release}

%description Qt-static
Static version of Qt4 wrapper for poppler.

%description Qt-static -l pl.UTF-8
Statyczna wersja wrappera Qt4 dla popplera.

%package progs
Summary:	Set of tools for viewing information and converting PDF files
Summary(pl.UTF-8):	Zestaw narzędzi do wyświetlania informacji i konwertowania plików PDF
Group:		Applications/Publishing
Provides:	pdftops
Obsoletes:	pdftohtml
Obsoletes:	pdftohtml-pdftops
Obsoletes:	xpdf-tools
Obsoletes:	poppler-utils

%description progs
Package contains utilites for PDF files. These utilities allow to
- extract information about PDF files
- extract images from PDF files
- convert PDF files to HTML, plain text and PS formats

%description progs -l pl.UTF-8
Pakiet zawiera zestaw narzędzi do plików PDF. Programy te umożliwiają
- wyświetlanie informacji o plikach PDF
- wydobywanie obrazków z plików PDF
- konwersję plików PDF do formatów takich jak HTML, PS czy też czystego
  tekstu

%prep
%setup -q
%patch0 -p1

%build
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf} -f
%{__autoheader}
%{__automake}
%configure \
	%{!?with_cairo:--disable-cairo-output} \
	%{!?with_qt:--disable-poppler-qt} \
	%{!?with_qt4:--disable-poppler-qt4} \
	--enable-a4-paper \
	%{?with_apidocs:--enable-gtk-doc} \
	--enable-xpdf-headers \
	--enable-zlib \
	--with-html-dir=%{_gtkdocdir}
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

%post	Qt -p /sbin/ldconfig
%postun	Qt -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_libdir}/libpoppler.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler.so
%{_libdir}/libpoppler.la
%dir %{_includedir}/poppler
%{_includedir}/poppler/poppler-config.h
%{_includedir}/poppler/[ABCDEFGJLNOPSTUX]*.h
%{_includedir}/poppler/Function.cc
%{_includedir}/poppler/goo
%{_includedir}/poppler/splash
%exclude %{_includedir}/poppler/glib
%{_pkgconfigdir}/poppler.pc
%{?with_cairo:%{_pkgconfigdir}/poppler-cairo.pc}
%{_pkgconfigdir}/poppler-splash.pc

%{_gtkdocdir}/poppler

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
%{_includedir}/poppler/qt3
%{_pkgconfigdir}/poppler-qt.pc

%files qt-static
%defattr(644,root,root,755)
%{_libdir}/libpoppler-qt.a
%endif

%if %{with qt4}
%files Qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-qt4.so.*.*.*

%files Qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-qt4.so
%{_libdir}/libpoppler-qt4.la
%{_includedir}/poppler/qt4
%{_pkgconfigdir}/poppler-qt4.pc

%files Qt-static
%defattr(644,root,root,755)
%{_libdir}/libpoppler-qt4.a
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdf*
%{_mandir}/man1/pdf*

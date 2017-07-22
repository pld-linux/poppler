#
# Conditional build:
%bcond_without	apidocs # disable gtk-doc
%bcond_without	cairo	# disable Cairo backend
%bcond_without	qt4	# disable qt4 wrapper
%bcond_without	qt5	# disable qt5 wrapper
%bcond_without	cpp	# disable cpp wrapper
%bcond_without	glib	# disable glib wrapper

%define		cairo_ver	1.10.0
%define		qt4_ver		4.7.0
%define		qt5_ver		5.0.0
Summary:	PDF rendering library
Summary(pl.UTF-8):	Biblioteka renderująca PDF
Name:		poppler
Version:	0.56.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://poppler.freedesktop.org/%{name}-%{version}.tar.xz
# Source0-md5:	31260c06e139d7270be4567cc8a4af97
URL:		https://poppler.freedesktop.org/
%{?with_qt5:BuildRequires:	Qt5Core-devel >= %{qt5_ver}}
%{?with_qt5:BuildRequires:	Qt5Gui-devel >= %{qt5_ver}}
%{?with_qt5:BuildRequires:	Qt5Test-devel >= %{qt5_ver}}
%{?with_qt5:BuildRequires:	Qt5Widgets-devel >= %{qt5_ver}}
%{?with_qt5:BuildRequires:	Qt5Xml-devel >= %{qt5_ver}}
%{?with_qt4:BuildRequires:	QtCore-devel >= %{qt4_ver}}
%{?with_qt4:BuildRequires:	QtGui-devel >= %{qt4_ver}}
%{?with_qt4:BuildRequires:	QtTest-devel >= %{qt4_ver}}
%{?with_qt4:BuildRequires:	QtXml-devel >= %{qt4_ver}}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.7
%{?with_cairo:BuildRequires:	cairo-devel >= %{cairo_ver}}
BuildRequires:	curl-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	fontconfig-devel >= 2.0.0
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gettext-tools
%{?with_glib:BuildRequires:	glib2-devel >= 1:2.41}
BuildRequires:	gobject-introspection-devel >= 0.6.7
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.14}
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	nss-devel >= 3
BuildRequires:	openjpeg2-devel >= 2
BuildRequires:	pkgconfig >= 1:0.18
# wanted cairo backends
BuildRequires:	pkgconfig(cairo-pdf) >= %{cairo_ver}
BuildRequires:	pkgconfig(cairo-ps) >= %{cairo_ver}
BuildRequires:	pkgconfig(cairo-svg) >= %{cairo_ver}
%{?with_qt4:BuildRequires:	qt4-build >= %{qt4_ver}}
%{?with_qt5:BuildRequires:	qt5-build >= %{qt5_ver}}
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	which
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	openjpeg2 >= 2
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
Requires:	curl-devel
Requires:	lcms2-devel >= 2
Requires:	libstdc++-devel >= 6:4.7
Requires:	nss-devel >= 3

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

%package apidocs
Summary:	Poppler library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki Poppler
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Poppler library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Poppler.

%package cpp
Summary:	Cpp wrapper for poppler
Summary(pl.UTF-8):	Wrapper cpp dla popplera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description cpp
Cpp wrapper for poppler.

%description cpp -l pl.UTF-8
Wrapper cpp dla popplera.

%package cpp-devel
Summary:	Header files for cpp wrapper for poppler
Summary(pl.UTF-8):	Pliki nagłówkowe wrappera cpp dla popplera
Group:		Development/Libraries
Requires:	%{name}-cpp = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description cpp-devel
Header files for cpp wrapper for poppler.

%description cpp-devel -l pl.UTF-8
Pliki nagłówkowe wrappera cpp dla popplera.

%package cpp-static
Summary:	Static version of cpp wrapper for poppler
Summary(pl.UTF-8):	Statyczna wersja wrappera cpp dla popplera
Group:		Development/Libraries
Requires:	%{name}-cpp-devel = %{version}-%{release}

%description cpp-static
Static version of cpp wrapper for poppler.

%description cpp-static -l pl.UTF-8
Statyczna wersja wrappera cpp dla popplera.

%package glib
Summary:	GLib wrapper for poppler
Summary(pl.UTF-8):	Wrapper GLib dla popplera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_cairo:Requires:	cairo >= %{cairo_ver}}
Requires:	glib2 >= 1:2.41

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
Requires:	glib2-devel >= 1:2.41

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

%package qt4
Summary:	Qt4 wrapper for poppler
Summary(pl.UTF-8):	Wrapper Qt4 dla popplera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore >= %{qt4_ver}
Requires:	QtGui >= %{qt4_ver}
Requires:	QtXml >= %{qt4_ver}
Provides:	poppler-Qt = %{version}-%{release}
Obsoletes:	poppler-Qt < 0.24.4-2
Obsoletes:	poppler-qt

%description qt4
Qt4 wrapper for poppler.

%description qt4 -l pl.UTF-8
Wrapper Qt4 dla popplera.

%package qt4-devel
Summary:	Header files for Qt4 wrapper for poppler
Summary(pl.UTF-8):	Pliki nagłówkowe wrappera Qt4 dla popplera
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt4 = %{version}-%{release}
Requires:	QtCore-devel >= %{qt4_ver}
Requires:	QtGui-devel >= %{qt4_ver}
Requires:	QtXml-devel >= %{qt4_ver}
Provides:	poppler-Qt-devel = %{version}-%{release}
Obsoletes:	poppler-Qt-devel < 0.24.4-2
Obsoletes:	poppler-qt-devel

%description qt4-devel
Header files for Qt4 wrapper for poppler.

%description qt4-devel -l pl.UTF-8
Pliki nagłówkowe wrapper Qt4 dla popplera.

%package qt4-static
Summary:	Static version of Qt4 wrapper for poppler
Summary(pl.UTF-8):	Statyczna wersja wrappera Qt4 dla popplera
Group:		Development/Libraries
Requires:	%{name}-qt4-devel = %{version}-%{release}
Provides:	poppler-Qt-static = %{version}-%{release}
Obsoletes:	poppler-Qt-static < 0.24.4-2
Obsoletes:	poppler-qt-static

%description qt4-static
Static version of Qt4 wrapper for poppler.

%description qt4-static -l pl.UTF-8
Statyczna wersja wrappera Qt4 dla popplera.

%package qt5
Summary:	Qt5 wrapper for poppler
Summary(pl.UTF-8):	Wrapper Qt5 dla popplera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description qt5
Qt5 wrapper for poppler.

%description qt5 -l pl.UTF-8
Wrapper Qt5 dla popplera.

%package qt5-devel
Summary:	Header files for Qt5 wrapper for poppler
Summary(pl.UTF-8):	Pliki nagłówkowe wrappera Qt5 dla popplera
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt5 = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qt5_ver}
Requires:	Qt5Gui-devel >= %{qt5_ver}
Requires:	Qt5Widgets-devel >= %{qt5_ver}
Requires:	Qt5Xml-devel >= %{qt5_ver}

%description qt5-devel
Header files for Qt5 wrapper for poppler.

%description qt5-devel -l pl.UTF-8
Pliki nagłówkowe wrapper Qt5 dla popplera.

%package qt5-static
Summary:	Static version of Qt5 wrapper for poppler
Summary(pl.UTF-8):	Statyczna wersja wrappera Qt5 dla popplera
Group:		Development/Libraries
Requires:	%{name}-qt5-devel = %{version}-%{release}

%description qt5-static
Static version of Qt5 wrapper for poppler.

%description qt5-static -l pl.UTF-8
Statyczna wersja wrappera Qt5 dla popplera.

%package progs
Summary:	Set of tools for viewing information and converting PDF files
Summary(pl.UTF-8):	Zestaw narzędzi do wyświetlania informacji i konwertowania plików PDF
Group:		Applications/Publishing
Provides:	pdftops
Obsoletes:	pdftohtml
Obsoletes:	pdftohtml-pdftops
Obsoletes:	poppler-utils
Obsoletes:	xpdf-tools

%description progs
Package contains utilites for PDF files. These utilities allow to
- extract information about PDF files,
- extract images from PDF files,
- convert PDF files to HTML, plain text and PS formats.

%description progs -l pl.UTF-8
Pakiet zawiera zestaw narzędzi do plików PDF. Programy te umożliwiają
- wyświetlanie informacji o plikach PDF,
- wydobywanie obrazków z plików PDF,
- konwersję plików PDF do formatów takich jak HTML, PS czy też
  czystego tekstu.

%prep
%setup -q

%build
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf} -f
%{__autoheader}
%{__automake}
%configure \
	--disable-gtk-test \
	--enable-libcurl \
	%{?with_apidocs:--enable-gtk-doc} \
	%{!?with_cairo:--disable-cairo-output} \
	%{!?with_cpp:--disable-poppler-cpp} \
	%{!?with_glib:--disable-poppler-glib} \
	%{!?with_qt4:--disable-poppler-qt4} \
	%{!?with_qt5:--disable-poppler-qt5} \
	--disable-silent-rules \
	--enable-xpdf-headers \
	--enable-zlib \
	--enable-dependency-tracking \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{without apidocs}
# why it still installs them, brr
%{__rm} -rf $RPM_BUILD_ROOT%{_gtkdocdir}/poppler
%endif

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	cpp -p /sbin/ldconfig
%postun	cpp -p /sbin/ldconfig

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%post	qt4 -p /sbin/ldconfig
%postun	qt4 -p /sbin/ldconfig

%post	qt5 -p /sbin/ldconfig
%postun	qt5 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_libdir}/libpoppler.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpoppler.so.67

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler.so
%dir %{_includedir}/poppler
%{_includedir}/poppler/poppler-config.h
%{_includedir}/poppler/[ABCDEFGHJLMNOPRSTUVX]*.h
%{_includedir}/poppler/fofi
%{_includedir}/poppler/goo
%{_includedir}/poppler/splash
%{_pkgconfigdir}/poppler.pc
%{?with_cairo:%{_pkgconfigdir}/poppler-cairo.pc}
%{_pkgconfigdir}/poppler-splash.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpoppler.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/poppler
%endif

%if %{with cpp}
%files cpp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpoppler-cpp.so.0

%files cpp-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-cpp.so
%{_includedir}/poppler/cpp
%{_pkgconfigdir}/poppler-cpp.pc

%files cpp-static
%defattr(644,root,root,755)
%{_libdir}/libpoppler-cpp.a
%endif

%if %{with glib}
%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpoppler-glib.so.8
%{_libdir}/girepository-1.0/Poppler-0.18.typelib

%files glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-glib.so
%{_includedir}/poppler/glib
%{_pkgconfigdir}/poppler-glib.pc
%{_datadir}/gir-1.0/Poppler-0.18.gir

%files glib-static
%defattr(644,root,root,755)
%{_libdir}/libpoppler-glib.a
%endif

%if %{with qt4}
%files qt4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-qt4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpoppler-qt4.so.4

%files qt4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-qt4.so
%{_includedir}/poppler/qt4
%{_pkgconfigdir}/poppler-qt4.pc

%files qt4-static
%defattr(644,root,root,755)
%{_libdir}/libpoppler-qt4.a
%endif

%if %{with qt5}
%files qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-qt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpoppler-qt5.so.1

%files qt5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-qt5.so
%{_includedir}/poppler/qt5
%{_pkgconfigdir}/poppler-qt5.pc

%files qt5-static
%defattr(644,root,root,755)
%{_libdir}/libpoppler-qt5.a
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfdetach
%attr(755,root,root) %{_bindir}/pdffonts
%attr(755,root,root) %{_bindir}/pdfimages
%attr(755,root,root) %{_bindir}/pdfinfo
%attr(755,root,root) %{_bindir}/pdfseparate
%attr(755,root,root) %{_bindir}/pdfsig
%attr(755,root,root) %{_bindir}/pdftocairo
%attr(755,root,root) %{_bindir}/pdftohtml
%attr(755,root,root) %{_bindir}/pdftoppm
%attr(755,root,root) %{_bindir}/pdftops
%attr(755,root,root) %{_bindir}/pdftotext
%attr(755,root,root) %{_bindir}/pdfunite
%{_mandir}/man1/pdfdetach.1*
%{_mandir}/man1/pdffonts.1*
%{_mandir}/man1/pdfimages.1*
%{_mandir}/man1/pdfinfo.1*
%{_mandir}/man1/pdfseparate.1*
%{_mandir}/man1/pdfsig.1*
%{_mandir}/man1/pdftocairo.1*
%{_mandir}/man1/pdftohtml.1*
%{_mandir}/man1/pdftoppm.1*
%{_mandir}/man1/pdftops.1*
%{_mandir}/man1/pdftotext.1*
%{_mandir}/man1/pdfunite.1*

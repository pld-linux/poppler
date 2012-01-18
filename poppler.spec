#
# Conditional build:
%bcond_without	apidocs # disable gtk-doc
%bcond_without	cairo	# disable Cairo backend
%bcond_without	qt4	# disable qt4 wrapper
%bcond_without	cpp	# disable cpp wrapper
%bcond_without	glib	# disable glib wrapper
#
%define		cairo_ver	1.10.0
#
Summary:	PDF rendering library
Summary(pl.UTF-8):	Biblioteka renderująca PDF
Name:		poppler
Version:	0.18.3
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
# Source0-md5:	d70d2d63d8acd29c97185f7e5f09c9b4
URL:		http://poppler.freedesktop.org/
%{?with_qt4:BuildRequires:	QtGui-devel >= 4.4.0}
%{?with_qt4:BuildRequires:	QtTest-devel >= 4.4.0}
%{?with_qt4:BuildRequires:	QtXml-devel >= 4.4.0}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
%{?with_cairo:BuildRequires:	cairo-devel >= %{cairo_ver}}
BuildRequires:	curl-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	fontconfig-devel >= 2.0.0
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gettext-devel
%{?with_glib:BuildRequires:	glib2-devel >= 1:2.18.0}
BuildRequires:	gobject-introspection-devel >= 0.6.7
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.14}
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	openjpeg-devel
BuildRequires:	pkgconfig >= 1:0.18
%{?with_qt4:BuildRequires:	qt4-build}
BuildRequires:	sed >= 4.0
BuildRequires:	which
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
Requires:	curl-devel
Requires:	fontconfig-devel >= 2.0.0
Requires:	freetype-devel >= 2.0
Requires:	lcms-devel
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libstdc++-devel
Requires:	libtiff-devel
Requires:	openjpeg-devel
Requires:	zlib-devel

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
Requires:	glib2 >= 1:2.18.0

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
Requires:	glib2-devel >= 1:2.18.0

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

%package Qt
Summary:	Qt4 wrapper for poppler
Summary(pl.UTF-8):	Wrapper Qt4 dla popplera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtGui >= 4.4.0
Requires:	QtXml >= 4.4.0
Obsoletes:	poppler-qt

%description Qt
Qt4 wrapper for poppler.

%description Qt -l pl.UTF-8
Wrapper Qt4 dla popplera.

%package Qt-devel
Summary:	Header files for Qt4 wrapper for poppler
Summary(pl.UTF-8):	Pliki nagłówkowe wrappera Qt4 dla popplera
Group:		Development/Libraries
Requires:	%{name}-Qt = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	QtGui-devel >= 4.4.0
Requires:	QtXml-devel >= 4.4.0
Obsoletes:	poppler-qt-devel

%description Qt-devel
Header files for Qt4 wrapper for poppler.

%description Qt-devel -l pl.UTF-8
Pliki nagłówkowe wrapper Qt4 dla popplera.

%package Qt-static
Summary:	Static version of Qt4 wrapper for poppler
Summary(pl.UTF-8):	Statyczna wersja wrappera Qt4 dla popplera
Group:		Development/Libraries
Requires:	%{name}-Qt-devel = %{version}-%{release}
Obsoletes:	poppler-qt-static

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
%{__rm} -rf $RPM_BUILD_ROOT%{_gtkdocdir}/poppler || :
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

%post	Qt -p /sbin/ldconfig
%postun	Qt -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_libdir}/libpoppler.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpoppler.so.19

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
%files Qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-qt4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpoppler-qt4.so.3

%files Qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-qt4.so
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

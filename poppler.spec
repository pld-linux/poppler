Summary:	PDF rendering library
Name:		poppler
Version:	0.1.1
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
# Source0-md5:	d10982c93a1ccee79a14bb277f94990a
URL:		http://poppler.freedesktop.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A common PDF rendering library for integrating PDF viewing into
desktop applications (based on the xpdf-3.0 code base).

%package devel
Summary:	Poppler header files and development documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for the Poppler library.

%package static
Summary:	Poppler static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Poppler static libraries.

%prep
%setup -q

%build
%configure --disable-cairo-output
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/ldconfig
%postun	-p	/sbin/ldconfig

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

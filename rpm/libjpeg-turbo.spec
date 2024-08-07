Summary: A library for manipulating JPEG image format files
Name: libjpeg-turbo
Version: 3.0.3
Release: 1
License: IJG
URL: https://libjpeg-turbo.org/

Source0: %{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: libtool
BuildRequires: nasm

%description
The libjpeg package contains a library of functions for manipulating
JPEG images, as well as simple client programs for accessing the
libjpeg functions.  Libjpeg client programs include cjpeg, djpeg,
jpegtran, rdjpgcom and wrjpgcom.  Cjpeg compresses an image file into
JPEG format.  Djpeg decompresses a JPEG file into a regular image
file.  Jpegtran can perform various useful transformations on JPEG
files.  Rdjpgcom displays any text comments included in a JPEG file.
Wrjpgcom inserts text comments into a JPEG file.

%package devel
Summary: Development tools for programs which will use the libjpeg library
Requires: libjpeg-turbo = %{version}-%{release}
Provides: libjpeg-devel

%description devel
The libjpeg-devel package includes the header files and documentation
necessary for developing programs which will manipulate JPEG files using
the libjpeg library.

If you are going to develop programs which will manipulate JPEG images,
you should install libjpeg-devel.  You'll also need to have the libjpeg
package installed.

%package static
Summary: Static JPEG image format file library
Requires: libjpeg-turbo-devel = %{version}-%{release}
Provides: libjpeg-static

%description static
The libjpeg-static package contains the statically linkable version of libjpeg.
Linking to static libraries is discouraged for most applications, but it is
necessary for some boot packages.

%package tools
Summary: Client programs which use the libjpeg-turbo library
Requires: %{name} = %{version}-%{release}

%description tools
The libjpeg-turbo-tools package contains client programs for libjpeg-turbo.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
Man pages and developer documentation for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%cmake -DBUILD="$(sed 's/+.*//' <<<"%{version}")"

%cmake_build

%install
%cmake_install

mv $RPM_BUILD_ROOT%{_docdir}/%{name}{,-%{version}}
cp -r doc/html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html
rm $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/{LICENSE.md,README.ijg}
ln -s ../../licenses/%{name}-%{version}/README.ijg \
   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/README.ijg

%ifarch %{ix86} x86_64
%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test %{?_smp_mflags}
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE.md README.ijg
%{_libdir}/libjpeg.so.*
%{_libdir}/libturbojpeg.so.*

%files devel
%{_libdir}/libjpeg.so
%{_libdir}/libturbojpeg.so
%{_libdir}/pkgconfig/libjpeg.pc
%{_libdir}/pkgconfig/libturbojpeg.pc
%{_libdir}/cmake/libjpeg-turbo/*.cmake
/usr/include/*.h

%files static
%{_libdir}/*.a

%files tools
%{_bindir}/*

%files doc
%{_mandir}/man1/*
%{_docdir}/%{name}-%{version}

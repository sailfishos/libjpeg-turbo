Summary: A library for manipulating JPEG image format files
Name: libjpeg-turbo
Version: 1.5.3
Release: 0
License: IJG
Group: System/Libraries
URL: http://www.libjpeg-turbo.org/

Source0: %{name}-%{version}.tar.gz

BuildRequires: autoconf libtool nasm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
Group: Development/Libraries
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
Group: Development/Libraries
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
You'll also need to have the libjpeg-turbo package installed.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
Man pages and developer documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
autoreconf -fiv
%configure --enable-shared --enable-static

make libdir=%{_libdir} %{?_smp_mflags}

LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH make test

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

mv $RPM_BUILD_ROOT%{_docdir}/%{name}{,-%{version}}
cp -r doc/html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html
rm $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/{LICENSE.md,README.ijg}
ln -s ../../licenses/%{name}-%{version}/README.ijg \
   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/README.ijg

# We don't ship .la files.
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE.md README.ijg
%{_libdir}/libjpeg.so.*
%{_libdir}/libturbojpeg.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libjpeg.so
%{_libdir}/libturbojpeg.so
%{_libdir}/pkgconfig/libjpeg.pc
%{_libdir}/pkgconfig/libturbojpeg.pc
/usr/include/*.h

%files static
%defattr(-,root,root)
%{_libdir}/*.a

%files tools
%{_bindir}/*

%files doc
%defattr(-,root,root)
%{_mandir}/man1/*
%{_docdir}/%{name}-%{version}

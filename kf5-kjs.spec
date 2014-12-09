# TODO:
# - dir /usr/include/KF5 not packaged
# /usr/share/kf5 not packaged
%define		kdeframever	5.4
%define		qtver		5.3.2
%define		kfname		kjs

Summary:	Javascript engine
Name:		kf5-%{kfname}
Version:	5.4.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/portingAids/%{kfname}-%{version}.tar.xz
# Source0-md5:	c8066f2d86bb1230b676582198a923ea
Patch0:		kf5-kjs-absolute.patch
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	pcre-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
This library provides an ECMAScript compatible interpreter. The ECMA
standard is based on well known scripting languages such as Netscape's
JavaScript and Microsoft's JScript.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/kjs5
%dir %{_datadir}/kf5/kjs
%{_datadir}/kf5/kjs/create_hash_table
%attr(755,root,root) %ghost %{_libdir}/libKF5JS.so.5
%attr(755,root,root) %{_libdir}/libKF5JS.so.5.4.0
%attr(755,root,root) %ghost %{_libdir}/libKF5JSApi.so.5
%attr(755,root,root) %{_libdir}/libKF5JSApi.so.5.4.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/kjs
%{_includedir}/KF5/wtf
%{_includedir}/KF5/kjs_version.h
%{_libdir}/cmake/KF5JS
%attr(755,root,root) %{_libdir}/libKF5JS.so
%attr(755,root,root) %{_libdir}/libKF5JSApi.so
%{qt5dir}/mkspecs/modules/qt_KJS.pri
%{qt5dir}/mkspecs/modules/qt_KJSApi.pri

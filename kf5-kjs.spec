%define		kdeframever	5.84
%define		qtver		5.9.0
%define		kfname		kjs

Summary:	Javascript engine
Name:		kf5-%{kfname}
Version:	5.84.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/portingAids/%{kfname}-%{version}.tar.xz
# Source0-md5:	b2d205f7f7f18e60ea7a346da8768b51
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	ninja
BuildRequires:	pcre-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
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

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
%ghost %{_libdir}/libKF5JS.so.5
%attr(755,root,root) %{_libdir}/libKF5JS.so.*.*
%ghost %{_libdir}/libKF5JSApi.so.5
%attr(755,root,root) %{_libdir}/libKF5JSApi.so.*.*
%{_mandir}/man1/kjs5.1*
%lang(ca) /usr/share/man/ca/man1/kjs5.1*
%lang(de) /usr/share/man/de/man1/kjs5.1*
%lang(es) /usr/share/man/es/man1/kjs5.1*
%lang(it) /usr/share/man/it/man1/kjs5.1*
%lang(nl) /usr/share/man/nl/man1/kjs5.1*
%lang(pt) /usr/share/man/pt/man1/kjs5.1*
%lang(pt_BR) /usr/share/man/pt_BR/man1/kjs5.1*
%lang(sv) /usr/share/man/sv/man1/kjs5.1*
%lang(uk) /usr/share/man/uk/man1/kjs5.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/kjs
%{_includedir}/KF5/wtf
%{_includedir}/KF5/kjs_version.h
%{_libdir}/cmake/KF5JS
%{_libdir}/libKF5JS.so
%{_libdir}/libKF5JSApi.so
%{qt5dir}/mkspecs/modules/qt_KJS.pri
%{qt5dir}/mkspecs/modules/qt_KJSApi.pri

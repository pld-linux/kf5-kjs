# TODO:
# - dir /usr/include/KF5 not packaged
# /usr/share/kf5 not packaged
%define         _state          stable
%define		orgname		kjs

Summary:	Javascript engine
Name:		kf5-%{orgname}
Version:	5.0.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/frameworks/%{version}/portingAids/%{orgname}-%{version}.tar.xz
# Source0-md5:	d2736660739061a94e52c9695e51e000
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	pcre-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	qt5-linguist
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
This library provides an ECMAScript compatible interpreter. The ECMA
standard is based on well known scripting languages such as Netscape's
JavaScript and Microsoft's JScript.

%package devel
Summary:	Header files for %{orgname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{orgname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{orgname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{orgname}.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DBIN_INSTALL_DIR=%{_bindir} \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DPLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQT_PLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQML_INSTALL_DIR=%{qt5dir}/qml \
	-DIMPORTS_INSTALL_DIR=%{qt5dirs}/imports \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_LIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_INCLUDE_INSTALL_DIR=%{_includedir} \
	-DECM_MKSPECS_INSTALL_DIR=%{qt5dir}/mkspecs/modules \
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
%attr(755,root,root) %{_libdir}/libKF5JS.so.5.0.0
%attr(755,root,root) %ghost %{_libdir}/libKF5JSApi.so.5
%attr(755,root,root) %{_libdir}/libKF5JSApi.so.5.0.0

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

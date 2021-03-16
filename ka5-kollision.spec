%define		kdeappsver	20.12.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kollision
Summary:	kollision
Name:		ka5-%{kaname}
Version:	20.12.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	79d626cf91f511745b6fe96088b85b52
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kollision is a simple ball dodging game.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/nn
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kollision
%{_desktopdir}/org.kde.kollision.desktop
%{_iconsdir}/hicolor/128x128/apps/kollision.png
%{_iconsdir}/hicolor/16x16/apps/kollision.png
%{_iconsdir}/hicolor/22x22/apps/kollision.png
%{_iconsdir}/hicolor/32x32/apps/kollision.png
%{_iconsdir}/hicolor/48x48/apps/kollision.png
%{_iconsdir}/hicolor/64x64/apps/kollision.png
%{_iconsdir}/oxygen/128x128/apps/kollision.png
%{_iconsdir}/oxygen/16x16/apps/kollision.png
%{_iconsdir}/oxygen/22x22/apps/kollision.png
%{_iconsdir}/oxygen/32x32/apps/kollision.png
%{_iconsdir}/oxygen/48x48/apps/kollision.png
%{_iconsdir}/oxygen/64x64/apps/kollision.png
%{_datadir}/kollision
%{_datadir}/metainfo/org.kde.kollision.appdata.xml

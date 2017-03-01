%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kinfocenter
# (tpg) add this to obsolete old kinfocenter from kde-workspace
Epoch: 2
Version: 5.9.3
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
Summary: KDE Plasma 5 Info Center
URL: http://kde.org/
License: GPL
Group: System/Libraries
#Patch0: kinfocenter-5.5.3-set-logo-to-128-size.patch
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Wayland)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(libraw1394)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(libraw1394)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Test)
Conflicts: kinfocenter < %{version}
Obsoletes: kinfocenter < 2:4.11.22-9
Obsoletes: about-distro
%rename kinfocenter5

%description
KDE Plasma 5 Info Center.

%prep
%setup -qn %{name}-%(echo %{version} |cut -d. -f1-3)
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kcm-about-distro || touch kcm-about-distro.lang
%find_lang kcm_energyinfo || touch kcm_energyinfo.lang
%find_lang kcm_fileindexermonitor || touch kcm_fileindexermonitor.lang
%find_lang kcm_memory || touch kcm_memory.lang
%find_lang kcm_pci || touch kcm_pci.lang
%find_lang kcmdevinfo || touch kcmdevinfo.lang
%find_lang kcminfo || touch kcminfo.lang
%find_lang kcmnic || touch kcmnic.lang
%find_lang kcmopengl || touch kcmopengl.lang
%find_lang kcmsamba || touch kcmsamba.lang
%find_lang kcmusb || touch kcmusb.lang
%find_lang kcmview1394 || touch kcmview1394.lang
%find_lang kinfocenter || touch kinfocenter.lang
cat *.lang >%{name}-all.lang

%files -f %{name}-all.lang
%{_sysconfdir}/xdg/menus/kinfocenter.menu
%{_bindir}/kinfocenter
%{_libdir}/qt5/plugins/kcm_about_distro.so
%{_libdir}/qt5/plugins/kcm_devinfo.so
%{_libdir}/qt5/plugins/kcm_info.so
%{_libdir}/qt5/plugins/kcm_memory.so
%{_libdir}/qt5/plugins/kcm_nic.so
%{_libdir}/qt5/plugins/kcm_opengl.so
%{_libdir}/qt5/plugins/kcm_pci.so
%{_libdir}/qt5/plugins/kcm_samba.so
%{_libdir}/qt5/plugins/kcm_usb.so
%{_libdir}/qt5/plugins/kcm_view1394.so
%{_libdir}/qt5/plugins/kcms/kcm_energyinfo.so
%{_datadir}/kpackage/kcms/kcm_energyinfo/contents/ui/*.qml
%{_datadir}/kpackage/kcms/kcm_energyinfo/metadata.*
%{_libdir}/qt5/plugins/kcms/kcm_fileindexermonitor.so
%{_datadir}/kpackage/kcms/kcm_fileindexermonitor/contents/ui/*.qml
%{_datadir}/kpackage/kcms/kcm_fileindexermonitor/contents/ui/*.js
%{_datadir}/kpackage/kcms/kcm_fileindexermonitor/metadata.*
%{_datadir}/applications/org.kde.kinfocenter.desktop
%{_datadir}/desktop-directories/kinfocenter.directory
%{_datadir}/kcmusb
%{_datadir}/kcmview1394
%{_datadir}/kservicetypes5/kinfocentercategory.desktop
%{_datadir}/kxmlgui5/kinfocenter
%{_datadir}/kservices5/*
%doc %{_docdir}/HTML/*/kinfocenter

%define realname kinfocenter
%define major 5
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: %{realname}%{major}
Version: 5.5.3
Release: 1
Source0: hhttp://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{realname}-%{version}.tar.xz
Summary: KDE Plasma 5 Info Center
URL: http://kde.org/
License: GPL
Group: System/Libraries
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
Conflicts: kinfocenter < 5.3.1
Obsoletes: about-distro

%description
KDE Plasma 5 Info Center.

%prep
%setup -qn %{realname}-%(echo %{version} |cut -d. -f1-3)
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kcm-about-distro
%find_lang kcm_energyinfo
%find_lang kcm_fileindexermonitor
%find_lang kcm_memory
%find_lang kcm_pci
%find_lang kcmdevinfo
%find_lang kcminfo
%find_lang kcmnic
%find_lang kcmopengl
%find_lang kcmsamba
%find_lang kcmusb
%find_lang kcmview1394
%find_lang kinfocenter
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
%{_datadir}/kpackage/kcms/kcm_energyinfo/metadata.desktop
%{_libdir}/qt5/plugins/kcms/kcm_fileindexermonitor.so
%{_datadir}/kpackage/kcms/kcm_fileindexermonitor/contents/ui/*.qml
%{_datadir}/kpackage/kcms/kcm_fileindexermonitor/contents/ui/*.js
%{_datadir}/kpackage/kcms/kcm_fileindexermonitor/metadata.desktop
%{_datadir}/applications/org.kde.kinfocenter.desktop
%{_datadir}/desktop-directories/kinfocenter.directory
%{_datadir}/kcmusb
%{_datadir}/kcmview1394
%{_datadir}/kservicetypes5/kinfocentercategory.desktop
%{_datadir}/kxmlgui5/kinfocenter
%{_datadir}/kservices5/*
%doc %{_docdir}/HTML/*/kinfocenter

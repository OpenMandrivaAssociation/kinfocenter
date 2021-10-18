%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kinfocenter
Version:	5.23.0
Release: 2
Source0: http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
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
BuildRequires: cmake(KF5Declarative)
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
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: kirigami
BuildRequires: systemsettings
BuildRequires: vulkan-tools
BuildRequires: wayland-utils
Requires: kirigami
Requires: systemsettings
Requires: vulkan-tools
Requires: wayland-utils
Conflicts: kinfocenter < %{version}
Obsoletes: kinfocenter < 2:4.11.22-9
Obsoletes: about-distro
%rename kinfocenter5

%description
KDE Plasma 5 Info Center.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kcm-about-distro || touch kcm-about-distro.lang
%find_lang kcm_about-distro || touch kcm_about-distro.lang
%find_lang kcm_energyinfo || touch kcm_energyinfo.lang
%find_lang kcm_memory || touch kcm_memory.lang
%find_lang kcm_nic || touch kcm_nic.lang
%find_lang kcm_cpu || touch kcm_cpu.lang
%find_lang kcm_pci || touch kcm_pci.lang
%find_lang kcm_interrupts || touch kcm_interrupts.lang
%find_lang kcm_vulkan || touch kcm_vulkan.lang
%find_lang kcm_wayland || touch kcm_wayland.lang
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
%{_libdir}/qt5/plugins/kcm_devinfo.so
%{_libdir}/qt5/plugins/kcm_info.so
%{_libdir}/qt5/plugins/kcm_memory.so
%{_libdir}/qt5/plugins/kcm_opengl.so
%{_libdir}/qt5/plugins/kcm_pci.so
%{_libdir}/qt5/plugins/kcm_usb.so
%{_libdir}/qt5/plugins/kcm_view1394.so
%{_libdir}/qt5/plugins/kcms/kcm_energyinfo.so
%{_libdir}/qt5/plugins/kcms/kcm_nic.so
%{_libdir}/qt5/plugins/kcms/kcm_samba.so
%{_datadir}/kpackage/kcms/kcm_nic
%{_datadir}/kpackage/kcms/kcmsamba
%{_datadir}/kpackage/kcms/kcm_energyinfo/contents/ui/*.qml
%{_datadir}/kpackage/kcms/kcm_energyinfo/metadata.*
%{_datadir}/metainfo/org.kde.kinfocenter.appdata.xml
%{_datadir}/applications/org.kde.kinfocenter.desktop
%{_datadir}/desktop-directories/kinfocenter.directory
%{_datadir}/kservicetypes5/kinfocentercategory.desktop
%{_datadir}/kservices5/*
%doc %{_docdir}/HTML/*/kinfocenter
%{_libdir}/qt5/plugins/kcms/kcm_about-distro.so
%{_libdir}/qt5/plugins/kcms/kcm_cpu.so
%{_libdir}/qt5/plugins/kcms/kcm_interrupts.so
%{_libdir}/qt5/plugins/kcms/kcm_vulkan.so
%{_libdir}/qt5/plugins/kcms/kcm_wayland.so
%{_libdir}/qt5/qml/org/kde/kinfocenter
%{_datadir}/kinfocenter/categories/basicinformation.desktop
%{_datadir}/kinfocenter/categories/detailedinformation.desktop
%{_datadir}/kinfocenter/categories/deviceinfocategory.desktop
%{_datadir}/kinfocenter/categories/graphicalinfocategory.desktop
%{_datadir}/kinfocenter/categories/lostfoundcategory.desktop
%{_datadir}/kinfocenter/categories/networkinfocategory.desktop
%{_datadir}/kpackage/kcms/kcm_about-distro
%{_datadir}/kpackage/kcms/kcm_cpu
%{_datadir}/kpackage/kcms/kcm_interrupts
%{_datadir}/kpackage/kcms/kcm_vulkan
%{_datadir}/kpackage/kcms/kcm_wayland

%define realname kinfocenter
%define major 5
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: %{realname}%{major}
Version: 5.1.1
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{realname}-%{version}.tar.xz
Summary: KDE Plasma 5 Info Center
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(OpenGL)
BuildRequires: pkgconfig(glesv2)
BuildRequires: cmake(EGL)
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
BuildRequires: ninja

%description
KDE Plasma 5 Info Center

%prep
%setup -qn %{realname}-%(echo %{version} |cut -d. -f1-3)
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}
%find_lang kcm_infobase
%find_lang kcm_infosummary
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
%{_libdir}/plugins/devinfo.so
%{_libdir}/plugins/kcm_info.so
%{_libdir}/plugins/kcm_infosummary.so
%{_libdir}/plugins/kcm_memory.so
%{_libdir}/plugins/kcm_nic.so
%{_libdir}/plugins/kcm_opengl.so
%{_libdir}/plugins/kcm_pci.so
%{_libdir}/plugins/kcm_samba.so
%{_libdir}/plugins/kcm_usb.so
%{_libdir}/plugins/kcm_view1394.so
%{_datadir}/applications/kinfocenter.desktop
%{_datadir}/desktop-directories/kinfocenter.directory
%{_datadir}/kcmusb
%{_datadir}/kcmview1394
%{_datadir}/kservicetypes5/kinfocentercategory.desktop
%{_datadir}/kxmlgui5/kinfocenter
%{_datadir}/kservices5/*
%doc %{_docdir}/HTML/en/kinfocenter

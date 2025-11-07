Summary:	Image viewer for Wayland
Name:		swayimg
Version:	4.5
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/artemsen/swayimg/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7ec1fb47687a0d4caf084be580a87df1
URL:		https://github.com/artemsen/swayimg
BuildRequires:	OpenEXR-devel >= 3.1
BuildRequires:	bash-completion-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	giflib-devel
BuildRequires:	json-c-devel
BuildRequires:	libdrm-devel
BuildRequires:	libavif-devel
BuildRequires:	libexif-devel
BuildRequires:	libheif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libjxl-devel
BuildRequires:	libpng-devel
BuildRequires:	libraw-devel
BuildRequires:	librsvg-devel >= 2.46
BuildRequires:	libsixel-devel
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libwebp-devel
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	scdoc
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.35
BuildRequires:	xorg-lib-libxkbcommon-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	OpenEXR >= 3.1
Requires:	hicolor-icon-theme
Requires:	librsvg >= 2.46
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fully customizable and lightweight image viewer for Wayland based
display servers.

%prep
%setup -q

%build
%meson \
	-Dversion=%{version} \
	-Dzsh=enabled
%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/swayimg
%dir %{_datadir}/swayimg
%{_datadir}/swayimg/swayimgrc
%{_desktopdir}/swayimg.desktop
%{_iconsdir}/hicolor/*x*/apps/swayimg.png
%{_mandir}/man1/swayimg.1*
%{_mandir}/man5/swayimgrc.5*
%{bash_compdir}/swayimg
%{zsh_compdir}/_swayimg

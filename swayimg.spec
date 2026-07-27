Summary:	Image viewer for Wayland
Name:		swayimg
Version:	5.5
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/artemsen/swayimg/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1961cdbbd1a259a5f96dd839b9627ada
URL:		https://github.com/artemsen/swayimg
BuildRequires:	OpenEXR-devel >= 3.4
BuildRequires:	bash-completion-devel
BuildRequires:	exiv2-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	giflib-devel
BuildRequires:	libavif-devel >= 1.0
BuildRequires:	libdrm-devel
BuildRequires:	libheif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libjxl-devel
BuildRequires:	libpng-devel
BuildRequires:	libraw-devel
BuildRequires:	librsvg-devel >= 2.46
BuildRequires:	libsixel-devel
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libwebp-devel
BuildRequires:	luajit-devel
BuildRequires:	meson >= 1.1
BuildRequires:	ninja
BuildRequires:	openjpeg2-devel
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	python3-modules
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.35
BuildRequires:	xorg-lib-libxkbcommon-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	OpenEXR >= 3.4
Requires:	hicolor-icon-theme
Requires:	libavif >= 1.0
Requires:	librsvg >= 2.46
ExclusiveArch:	%{ix86} %{x8664} %{arm} aarch64 mips mips64 mipsel ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fully customizable and lightweight image viewer for Wayland based
display servers.

%prep
%setup -q

%build
%meson \
	-Ddoc=false \
	-Dlicense=false \
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
%doc CONFIG.md LICENSE README.md USAGE.md
%attr(755,root,root) %{_bindir}/swayimg
%dir %{_datadir}/swayimg
%{_datadir}/swayimg/example.lua
%{_datadir}/swayimg/swayimg.lua
%{_desktopdir}/swayimg.desktop
%{_iconsdir}/hicolor/*x*/apps/swayimg.png
%{_mandir}/man1/swayimg.1*
%{bash_compdir}/swayimg
%{zsh_compdir}/_swayimg

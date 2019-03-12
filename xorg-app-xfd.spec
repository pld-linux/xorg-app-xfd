Summary:	xfd application to display all characters in a font
Summary(pl.UTF-8):	Aplikacja xfd, wyświetlająca wszystkie znaki z fontu
Name:		xorg-app-xfd
Version:	1.1.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xfd-%{version}.tar.bz2
# Source0-md5:	f9c9f2b101a96d4b50c2a4ab9b5ab5b1
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	fontconfig-devel >= 2.0
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfd application displays all the characters in a font using either the
X11 core protocol or libXft2.

%description -l pl.UTF-8
Aplikacja xfd wyświetla wszystkie znaki z fontu przy użyciu
podstawowego protokołu X11 lub libXft2.

%prep
%setup -q -n xfd-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xfd
%{_datadir}/X11/app-defaults/Xfd
%{_mandir}/man1/xfd.1*

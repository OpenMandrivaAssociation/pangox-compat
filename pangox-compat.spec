%define	api_version	1.0
%define	lib_major	0
%define	libname		%mklibname pangox %{api_version} %{lib_major}
%define	devname		%mklibname -d pangox

%define	url_ver		%(echo %{version}|cut -d. -f1,2)

Summary:	Compatibility library providing the obsolete pangox library
Name:		pangox-compat
Version:	0.0.2
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.pango.org/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0) >= 2.31.0
BuildRequires:	pkgconfig(gmodule-no-export-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(x11)
Conflicts:	pango < 1.32.0

%description
This is a compatibility library providing the obsolete pangox library
that is not shipped by Pango itself anymore.

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Conflicts:	%{_lib}pango1.0_0 < 1.32.0

%description -n %{libname}
This is a compatibility library providing the obsolete pangox library
that is not shipped by Pango itself anymore.

%package -n %{devname}
Summary:	%{summary}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	%{_lib}pango1.0-devel < 1.32.0

%description -n %{devname}
This package includes the static libraries and header files
for the pangox package.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%config(noreplace) %{_sysconfdir}/pango/pangox.aliases

%files -n %{libname}
%{_libdir}/libpangox-%{api_version}.so.%{lib_major}*

%files -n %{devname}
%{_libdir}/libpangox-%{api_version}.so
%{_libdir}/pkgconfig/*
%{_includedir}/*



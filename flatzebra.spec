%define		major		2
%define		libname		%mklibname %{name} 0.1 %{major}
%define		develname	%mklibname %{name} -d

Name:		flatzebra
Version:	0.1.7
Release:	1
Summary:	A Generic Game Engine library for 2D double-buffering animation
Group:		System/Libraries
License:	GPLv2
URL:		http://sarrazip.com/dev/burgerspace.html
Source:		http://sarrazip.com/dev/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(zlib)

%description
Generic Game Engine library suitable for BurgerSpace, Afternoon Stalker
and Cosmosmash.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	flatzebra-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

rm -rf %{buildroot}%{_docdir}

%files -n %{libname}
%doc AUTHORS COPYING README INSTALL NEWS
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}-0.1
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

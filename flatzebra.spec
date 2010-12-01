%define major   2
%define libname %mklibname %name %major
%define develname %mklibname %name -d

Name:		flatzebra
Version:	0.1.5
Release:	%mkrel 2
Summary:	A Generic Game Engine library for 2D double-buffering animation
Group:		System/Libraries
License:	GPLv2
URL:		http://sarrazip.com/dev/burgerspace.html
Source:		http://sarrazip.com/dev/%{name}-%{version}.tar.gz
BuildRequires:	SDL1.2-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer1.2-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Generic Game Engine library suitable for BurgerSpace, Afternoon Stalker
and Cosmosmash.

%package -n %{libname}
Summary: Main library for %{name}
Group: System/Libraries
Obsoletes:  %mklibname %name 0.1_2

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary: Headers for developing programs that will use %{name}
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: flatzebra-devel = %{version}-%{release}
Obsoletes: %mklibname %name -d 0.1_2

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall

rm -rf %{buildroot}/%_docdir

%clean 
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README INSTALL NEWS
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/%name-0.1
%{_includedir}/%name-0.1/%name/*.h
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

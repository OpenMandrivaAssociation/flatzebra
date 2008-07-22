%define name flatzebra
%define version	0.1.1
%define release %mkrel 5

%define major   0.1_2
%define libname %mklibname %name %major
%define libnamedev %mklibname %name %major -d

Name:		%{name}
Summary:	A Generic Game Engine library for 2D double-buffering animation
Version:	%{version}
Release:	%{release}
Group:		System/Libraries
License:	GPL
URL:		http://www3.sympatico.ca/sarrazip/dev/burgerspace.html
Source:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	SDL1.2-devel
BuildRequires:	SDL_image1.2-devel
BuildRequires:	SDL_mixer1.2-devel
BuildRequires:	pkgconfig

%description
Generic Game Engine library suitable for BurgerSpace, Afternoon Stalker
and Cosmosmash.

%package -n %{libname}
Summary: Main library for %{name}
Group: System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{libnamedev}
Summary: Headers for developing programs that will use %{name}
Group: Development/C
Requires: %{libname} = %{version}
Provides: libflatzebra-devel = %{version}-%{release}
Provides: flatzebra-devel = %{version}-%{release}

%description -n %{libnamedev}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep

%setup -q

%build

%configure

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

rm -rf $RPM_BUILD_ROOT/%_docdir

%clean 
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README INSTALL NEWS
%{_libdir}/lib*.so.*

%files -n %{libnamedev}
%defattr(-,root,root)
%dir %{_includedir}/%name-0.1
%{_includedir}/%name-0.1/%name/*.h
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

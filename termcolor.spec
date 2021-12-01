%global debug_package %{nil}

Name:           termcolor
Version:        2.0.0
Release:        %autorelease
Summary:        Header-only C++ library for printing colored messages to the terminal

License:        BSD
URL:            https://github.com/ikalnytskyi/termcolor
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  sed

%description
Termcolor is a header-only C++ library for printing colored messages to the
terminal. Written just for fun with a help of the Force.

Termcolor uses ANSI color formatting, so you can use it on every system that is
used such terminals (most *nix systems, including Linux and Mac OS).

%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}
BuildArch:      noarch

%description devel
Termcolor is a header-only C++ library for printing colored messages to the
terminal. Written just for fun with a help of the Force.

Termcolor uses ANSI color formatting, so you can use it on every system that is
used such terminals (most *nix systems, including Linux and Mac OS).

%prep
%setup -q
sed -i -e 's/DESTINATION lib/DESTINATION lib64/' CMakeLists.txt


%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.rst
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/


%changelog
%autochangelog

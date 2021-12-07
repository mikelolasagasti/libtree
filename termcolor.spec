%global debug_package %{nil}

Name:           termcolor
Version:        2.0.0
Release:        %autorelease
Summary:        Header-only C++ library for printing colored messages to the terminal

License:        BSD
URL:            https://github.com/ikalnytskyi/termcolor
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
# https://github.com/ikalnytskyi/termcolor/pull/63
Patch0:         0001-Use-GNUInstallDirs-for-install-targets.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Termcolor is a header-only C++ library for printing colored messages to the
terminal. Written just for fun with a help of the Force.

Termcolor uses ANSI color formatting, so you can use it on every system that is
used such terminals (most *nix systems, including Linux and Mac OS).

%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}

%description devel
Termcolor is a header-only C++ library for printing colored messages to the
terminal. Written just for fun with a help of the Force.

Termcolor uses ANSI color formatting, so you can use it on every system that is
used such terminals (most *nix systems, including Linux and Mac OS).

%prep
%autosetup -p1

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

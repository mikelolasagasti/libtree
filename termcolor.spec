%global debug_package %{nil}

%global common_description %{expand:
Termcolor is a header-only C++ library for printing colored messages to the
terminal. Written just for fun with a help of the Force.

Termcolor uses ANSI color formatting, so you can use it on every system that is
used such terminals (most *nix systems, including Linux and Mac OS).}

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

%description %{common_description}

%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}
Requires:  cmake-filesystem

%description devel %{common_description}

%prep
%autosetup -p1

%build
%cmake -DTERMCOLOR_TESTS:BOOL=ON
%cmake_build

%install
%cmake_install

# test_termcolor is a visual test
# It should show colors, but mock will show without colors.
%check
%{_vpath_builddir}/test_termcolor

%files devel
%license LICENSE
%doc README.rst
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/


%changelog
%autochangelog

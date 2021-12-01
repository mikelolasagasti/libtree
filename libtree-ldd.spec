Name:           libtree-ldd
Version:        2.0.0
Release:        %autorelease
Summary:        Like ldd but as a tree


License:        MIT
URL:            https://github.com/haampie/libtree
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cxxopts-devel
BuildRequires:  elfio-devel
BuildRequires:  termcolor-devel

Provides:       %{_bindir}/libtree

%description
A tool that:
- turns ldd into a tree
- explains why shared libraries are found and why not
- optionally deploys executables and dependencies into a single directory

%prep
%autosetup -n libtree-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_mandir}/man1/libtree.1*
%{_bindir}/libtree
%doc README.md
%license LICENSE

%changelog
%autochangelog

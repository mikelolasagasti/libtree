Name:           libtree-ldd
Version:        2.0.0
Release:        %autorelease
Summary:        ldd as a tree


License:        MIT
URL:            https://github.com/haampie/libtree
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:  cxxopts-devel
BuildRequires:  elfio-devel

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
%{_mandir}/man1/%{name}*
%{_bindir}/%{name}
%doc CHANGELOG.md README.md
%license LICENSE

%changelog
* Mon Mar 08 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 4.0.0-1
- foo

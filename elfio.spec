%global debug_package %{nil}

Name:           elfio
Version:        3.9
Release:        1%{?dist}
Summary:        C++ library for reading and generating ELF files

License:        MIT
URL:            http://elfio.sourceforge.net/
Source0:        https://downloads.sf.net/elfio/elfio-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make

%description
ELFIO is a small, header-only C++ library that provides a simple interface for
reading and generating files in ELF binary format.

It is used as a standalone library - it is not dependent on any other product
or project. Adhering to ISO C++, it compiles on a wide variety of
architectures and compilers.

While the library is easy to use, some basic knowledge of the ELF binary
format is required. Such Information can easily be found on the Web.


%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}
BuildArch:      noarch

%description devel
ELFIO is a small, header-only C++ library that provides a simple interface for
reading and generating files in ELF binary format.

It is used as a standalone library - it is not dependent on any other product
or project. Adhering to ISO C++, it compiles on a wide variety of
architectures and compilers.

While the library is easy to use, some basic knowledge of the ELF binary
format is required. Such Information can easily be found on the Web.


%prep
%setup -q


%build
%cmake
%cmake_build

%install
%cmake_install
# Binaries are the examples and have too generic names: elfdump tutorial write_obj writer
#rm %{buildroot}%{_bindir}/*


#%%check
# Sanity check
#examples/elfdump/elfdump %{_bindir}/make

%files devel
%license COPYING
%doc AUTHORS doc/elfio.pdf README
%{_includedir}/elfio/
%{_datadir}/elfio/


%changelog
* Wed Sep 15 2021 Orion Poplawski <orion@nwra.com> - 3.9-1
- Update to 3.9

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Orion Poplawski <orion@nwra.com> - 3.8-1
- Update to 3.8

* Thu Sep 17 2020 Orion Poplawski <orion@nwra.com> - 3.7-1
- Update to 3.7

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Orion Poplawski <orion@nwra.com> - 3.6-1
- Update to 3.6

* Thu Feb 27 2020 Orion Poplawski <orion@nwra.com> - 3.5-1
- Update to 3.5

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Orion Poplawski <orion@nwra.com> - 3.4-1
- Update to 3.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 3.2-5
- Rebuild for protobuf 3.3.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Orion Poplawski <orion@cora.nwra.com> - 3.2-3
- Rebuild for protobuf 3.2.0

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 3.2-2
- Fix source url
- Add BR gcc-c++
- Add %%check
- Other cleanup

* Thu Nov 17 2016 Orion Poplawski <orion@cora.nwra.com> - 3.2-1
- Initial Fedora package

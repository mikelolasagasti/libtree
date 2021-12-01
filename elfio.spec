%global debug_package %{nil}

Name:           elfio
Version:        3.9
Release:        %autorelease
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
%autochangelog

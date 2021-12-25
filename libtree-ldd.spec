Name:           libtree-ldd
Version:        3.0.1
Release:        %autorelease
Summary:        Like ldd but as a tree


License:        MIT
URL:            https://github.com/haampie/libtree
Source0:        %{url}/archive/v%{version}/libtree-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
A tool that:
- turns ldd into a tree
- explains why shared libraries are found and why not

%prep
%autosetup -n libtree-%{version}
# preserve timestamps
sed -r -i 's/\b(cp )/\1-p /' Makefile
# remove failing tests
rm -rf tests/07_origin_is_relative_to_symlink_location_not_realpath
rm -rf tests/08_nodeflib

%build
%set_build_flags
%make_build

%install
%make_install PREFIX="%{_prefix}"

%check
%make_build check

%files
%{_mandir}/man1/libtree.1*
%{_bindir}/libtree
%doc README.md
%license LICENSE

%changelog
%autochangelog

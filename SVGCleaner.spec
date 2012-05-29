%define git	20120506

Name:		SVGCleaner
Summary:	Tool to clean up SVG files
Version:	0.1
Release:	0.git%{git}.2
License:	GPLv3+
Group:		Graphics
URL:		https://github.com/RazrFalcon/SVGCleaner
Source0:	%{name}-%{git}.tar.xz
BuildRequires:	qt4-devel
Requires:	p7zip

%description
Generally, SVG files produced by vector editors contain a lot of unused
elements and attributes that just blow up their size without providing better
visible quality.

SVG Cleaner could help you to clean up your SVG files from unnecessary data.
It has a lot of options for cleanup and optimization, works in batch mode,
provides threaded processing on the multicore processors and basically does two
things:
- removing elements and attributes that don't contribute to the final
rendering;
- making those elements and attributes in use more compact.

Images cleaned by SVG Cleaner are typically 10-60 percent smaller
than the original ones.

Important! The internal image viewer in SVG Cleaner uses the QtSvg module
for rendering SVG images. Qt supports only the static features of SVG 1.2 Tiny,
and that imposes a number of restrictions on rendering of advanced features.
For instance, elements such as clipPath, mask, filters etc. will not be
rendered at all.

%prep
%setup -q -n %{name}-%{git}
find . -type f -exec chmod -x {} \;

%build
%qmake_qt4
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%attr(0755,root,root) %{_bindir}/svgcleaner*
%{_datadir}/applications/svgcleaner.desktop
%{_iconsdir}/hicolor/scalable/apps/svgcleaner.svg
%{_datadir}/svgcleaner/
%doc README

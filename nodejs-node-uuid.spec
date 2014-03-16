%define		pkg	node-uuid
Summary:	RFC4122v4 UUID generator for Node.js
Name:		nodejs-%{pkg}
Version:	1.4.1
Release:	1
License:	MIT or GPL+
Group:		Development/Libraries
URL:		https://github.com/broofa/node-uuid
Source0:	http://registry.npmjs.org/node-uuid/-/%{pkg}-%{version}.tgz
# Source0-md5:	f7778f1bb34f4ea250b259388cd7ec13
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Obsoletes:	nodejs-uuid < 1.4.1-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple, fast generation of RFC4122v4 and non-RFC compact UUIDs. It
runs in node.js and many browsers.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -p uuid.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.md
%{nodejs_libdir}/%{pkg}

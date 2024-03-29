%define prerelease 84a4013f96e01fdd14b65d260a78b543e3702ee1
%define import_path code.google.com/p/go.net
%define gopath %{_libdir}/go
%define gosrc %{gopath}/src/%{import_path}
%define shortcommit %(c=%{prerelease}; echo ${c:0:12})

Summary:	Supplementary Go networking libraries
Name:		golang-net
Version:	0.1.git%{shortcommit}
Release:	12
License:	BSD
Group:		Development/Other
Url:		http://net.go.googlecode.com
Source0:	http://net.go.googlecode.com/archive/%{prerelease}.zip
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/dict) = %{version}-%{release}
Provides:       golang(%{import_path}/html) = %{version}-%{release}
Provides:       golang(%{import_path}/html/atom) = %{version}-%{release}
Provides:       golang(%{import_path}/idna) = %{version}-%{release}
Provides:       golang(%{import_path}/ipv4) = %{version}-%{release}
Provides:       golang(%{import_path}/ipv6) = %{version}-%{release}
Provides:       golang(%{import_path}/proxy) = %{version}-%{release}
Provides:       golang(%{import_path}/publicsuffix) = %{version}-%{release}
Provides:       golang(%{import_path}/spdy) = %{version}-%{release}
Provides:       golang(%{import_path}/websocket) = %{version}-%{release}

%package devel
BuildRequires:  golang >= 1.3.3
Requires:       golang >= 1.3.3
Summary:        Supplementary Go networking libraries

%description devel
Supplementary Go networking libraries devel part

%description
Supplementary Go networking libraries

%prep
cd %{_builddir}
rm -rf net.go-*
unzip %{SOURCE0}

%build
cd %{_builddir}/net.go-%{shortcommit}
#go build

%install
mkdir -p %{buildroot}%{gosrc}
cp -av %{_builddir}/net.go-%{shortcommit}/* %{buildroot}%{gosrc}/
rm -vf %{buildroot}%{gosrc}/LICENSE
rm -vf %{buildroot}%{gosrc}/README
rm -vf %{buildroot}%{gosrc}/AUTHORS
rm -vf %{buildroot}%{gosrc}/CONTRIBUTORS
rm -vf %{buildroot}%{gosrc}/PATENTS

%files
%doc net.go-%{shortcommit}/README
%doc net.go-%{shortcommit}/LICENSE

%files devel
%doc net.go-%{shortcommit}/LICENSE
%doc net.go-%{shortcommit}/README
%doc net.go-%{shortcommit}/AUTHORS
%doc net.go-%{shortcommit}/CONTRIBUTORS
%doc net.go-%{shortcommit}/PATENTS
%{gosrc}/*

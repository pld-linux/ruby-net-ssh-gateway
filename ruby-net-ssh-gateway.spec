#
# Conditional build:
%bcond_with	tests		# build without tests (not in gem)

%define	pkgname net-ssh-gateway
Summary:	A simple library to assist in establishing tunneled Net::SSH connections
Name:		ruby-%{pkgname}
Version:	2.0.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	1841d939c1c60e468d517da64e495e31
URL:		https://github.com/net-ssh/net-ssh-gateway
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-minitest
BuildRequires:	ruby-mocha
BuildRequires:	ruby-net-ssh >= 4.0.0
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple library to assist in establishing tunneled Net::SSH
connections.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%if %{with tests}
# No tests in gem
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGES.txt LICENSE.txt
%{ruby_vendorlibdir}/net/ssh/gateway.rb
%{ruby_vendorlibdir}/net/ssh/gateway
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

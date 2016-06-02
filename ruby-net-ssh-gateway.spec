#
# Conditional build:
%bcond_without	tests		# build without tests

%define	pkgname net-ssh-gateway
Summary:	A simple library to assist in establishing tunneled Net::SSH connections
Name:		ruby-%{pkgname}
Version:	1.2.0
Release:	3
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	7398dc8b2480c870eea3ccf1969f4913
URL:		http://net-ssh.rubyforge.org/gateway
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-minitest
BuildRequires:	ruby-mocha
BuildRequires:	ruby-net-ssh >= 2.6.5
BuildRequires:	ruby-rubygems
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
RUBYOPT="-Ilib -rrubygems" testrb test/*_test.rb
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
%doc README.rdoc CHANGES.txt LICENSE.txt
%{ruby_vendorlibdir}/net/ssh/gateway.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

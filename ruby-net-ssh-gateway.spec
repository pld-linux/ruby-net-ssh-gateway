#
# Conditional build:
%bcond_without	tests		# build without tests

%define	gem_name net-ssh-gateway
Summary:	A simple library to assist in establishing tunneled Net::SSH connections
Name:		ruby-%{gem_name}
Version:	1.1.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Source0-md5:	896b2b8ccca01edc72e145176a591665
URL:		http://net-ssh.rubyforge.org/gateway
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-minitest
BuildRequires:	ruby-mocha
BuildRequires:	ruby-net-ssh >= 1.99.1
BuildRequires:	ruby-rubygems
Requires:	ruby-net-ssh >= 1.99.1
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
%setup -q -n %{gem_name}-%{version}

%build
%if %{with tests}
RUBYOPT="-Ilib -rrubygems" testrb test/*_test.rb
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc CHANGELOG.rdoc
%{ruby_vendorlibdir}/net/ssh/gateway.rb

%define		module	rsa
Summary:	Pure-Python RSA implementation
Name:		python3-%{module}
Version:	4.7.2
Release:	5
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/rsa/
Source0:	https://files.pythonhosted.org/packages/source/r/rsa/%{module}-%{version}.tar.gz
# Source0-md5:	c21701cdd75c170f8d690f704a362c44
URL:		https://pypi.org/project/rsa/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python-RSA is a pure-Python RSA implementation. It supports encryption
and decryption, signing and verifying signatures, and key generation
according to PKCS#1 version 1.5. It can be used as a Python library as
well as on the commandline.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/pyrsa-decrypt
%attr(755,root,root) %{_bindir}/pyrsa-encrypt
%attr(755,root,root) %{_bindir}/pyrsa-keygen
%attr(755,root,root) %{_bindir}/pyrsa-priv2pub
%attr(755,root,root) %{_bindir}/pyrsa-sign
%attr(755,root,root) %{_bindir}/pyrsa-verify
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

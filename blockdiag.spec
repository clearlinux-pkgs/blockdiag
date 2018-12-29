#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : blockdiag
Version  : 1.5.4
Release  : 19
URL      : https://files.pythonhosted.org/packages/0f/bd/2bfaef223e428742313d7fba6edca1e6d21cd2867dbd758874f403d82cbf/blockdiag-1.5.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/0f/bd/2bfaef223e428742313d7fba6edca1e6d21cd2867dbd758874f403d82cbf/blockdiag-1.5.4.tar.gz
Summary  : blockdiag generates block-diagram image from text
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: blockdiag-bin = %{version}-%{release}
Requires: blockdiag-license = %{version}-%{release}
Requires: blockdiag-python = %{version}-%{release}
Requires: blockdiag-python3 = %{version}-%{release}
Requires: Pillow
Requires: docutils
Requires: funcparserlib
Requires: reportlab
Requires: setuptools
Requires: webcolors
BuildRequires : Pillow-python
BuildRequires : buildreq-distutils3
BuildRequires : docutils-python
BuildRequires : funcparserlib-python
BuildRequires : funcsigs-python
BuildRequires : nose-python
BuildRequires : pep8
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : reportlab-python
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : webcolors-python

%description
=====================
debian-logo-256color-palettealpha.png
--------------------------------------

%package bin
Summary: bin components for the blockdiag package.
Group: Binaries
Requires: blockdiag-license = %{version}-%{release}

%description bin
bin components for the blockdiag package.


%package license
Summary: license components for the blockdiag package.
Group: Default

%description license
license components for the blockdiag package.


%package python
Summary: python components for the blockdiag package.
Group: Default
Requires: blockdiag-python3 = %{version}-%{release}

%description python
python components for the blockdiag package.


%package python3
Summary: python3 components for the blockdiag package.
Group: Default
Requires: python3-core

%description python3
python3 components for the blockdiag package.


%prep
%setup -q -n blockdiag-1.5.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541276995
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/blockdiag
cp LICENSE %{buildroot}/usr/share/package-licenses/blockdiag/LICENSE
cp src/blockdiag/tests/VLGothic/LICENSE %{buildroot}/usr/share/package-licenses/blockdiag/src_blockdiag_tests_VLGothic_LICENSE
cp src/blockdiag/tests/VLGothic/LICENSE.en %{buildroot}/usr/share/package-licenses/blockdiag/src_blockdiag_tests_VLGothic_LICENSE.en
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/blockdiag

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/blockdiag/LICENSE
/usr/share/package-licenses/blockdiag/src_blockdiag_tests_VLGothic_LICENSE
/usr/share/package-licenses/blockdiag/src_blockdiag_tests_VLGothic_LICENSE.en

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : blockdiag
Version  : 1.5.3
Release  : 8
URL      : https://pypi.python.org/packages/source/b/blockdiag/blockdiag-1.5.3.tar.gz
Source0  : https://pypi.python.org/packages/source/b/blockdiag/blockdiag-1.5.3.tar.gz
Summary  : blockdiag generates block-diagram image from text
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: blockdiag-bin
Requires: blockdiag-python
BuildRequires : Pillow-python
BuildRequires : docutils-python
BuildRequires : funcparserlib-python
BuildRequires : funcsigs-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : reportlab-python
BuildRequires : setuptools
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

%description bin
bin components for the blockdiag package.


%package python
Summary: python components for the blockdiag package.
Group: Default
Requires: Pillow-python
Requires: docutils-python
Requires: funcparserlib-python
Requires: nose-python
Requires: pep8
Requires: reportlab-python
Requires: webcolors-python

%description python
python components for the blockdiag package.


%prep
%setup -q -n blockdiag-1.5.3

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/blockdiag

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : blockdiag
Version  : 2.0.1
Release  : 39
URL      : https://files.pythonhosted.org/packages/b6/1b/eab880ae3e6c7e24ae5adecc40ee7dd05c9ebb0dff6c39b52472844ce9b7/blockdiag-2.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b6/1b/eab880ae3e6c7e24ae5adecc40ee7dd05c9ebb0dff6c39b52472844ce9b7/blockdiag-2.0.1.tar.gz
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
BuildRequires : Pillow
BuildRequires : Pillow-python
BuildRequires : buildreq-distutils3
BuildRequires : docutils
BuildRequires : docutils-python
BuildRequires : funcparserlib
BuildRequires : funcparserlib-python
BuildRequires : funcsigs-python
BuildRequires : nose-python
BuildRequires : pep8
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : reportlab
BuildRequires : reportlab-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : webcolors
BuildRequires : webcolors-python

%description
`blockdiag` generate block-diagram image file from spec-text file.
.. image:: https://drone.io/bitbucket.org/blockdiag/blockdiag/status.png
:target: https://drone.io/bitbucket.org/blockdiag/blockdiag
:alt: drone.io CI build status

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
Provides: pypi(blockdiag)
Requires: pypi(funcparserlib)
Requires: pypi(pillow)
Requires: pypi(setuptools)
Requires: pypi(webcolors)

%description python3
python3 components for the blockdiag package.


%prep
%setup -q -n blockdiag-2.0.1
cd %{_builddir}/blockdiag-2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603388259
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/blockdiag
cp %{_builddir}/blockdiag-2.0.1/LICENSE %{buildroot}/usr/share/package-licenses/blockdiag/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/blockdiag-2.0.1/src/blockdiag/tests/VLGothic/LICENSE %{buildroot}/usr/share/package-licenses/blockdiag/af07a3a5218239724d3c4ad4f9e4746835129293
cp %{_builddir}/blockdiag-2.0.1/src/blockdiag/tests/VLGothic/LICENSE.en %{buildroot}/usr/share/package-licenses/blockdiag/25d28628ff8ea8da700469e7b9ce06e5faecfed0
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
/usr/share/package-licenses/blockdiag/25d28628ff8ea8da700469e7b9ce06e5faecfed0
/usr/share/package-licenses/blockdiag/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/blockdiag/af07a3a5218239724d3c4ad4f9e4746835129293

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

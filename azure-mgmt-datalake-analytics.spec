#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-mgmt-datalake-analytics
Version  : 0.6.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/6f/e9/91da6cea4cccb268237e7f16bddefb2dbb1507f75b78c13a79eae16eb1cc/azure-mgmt-datalake-analytics-0.6.0.zip
Source0  : https://files.pythonhosted.org/packages/6f/e9/91da6cea4cccb268237e7f16bddefb2dbb1507f75b78c13a79eae16eb1cc/azure-mgmt-datalake-analytics-0.6.0.zip
Summary  : Microsoft Azure Data Lake Analytics Management Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-mgmt-datalake-analytics-python = %{version}-%{release}
Requires: azure-mgmt-datalake-analytics-python3 = %{version}-%{release}
Requires: azure-common
Requires: msrestazure
BuildRequires : azure-common
BuildRequires : buildreq-distutils3
BuildRequires : msrestazure

%description
==============================
        
        This is the Microsoft Azure Data Lake Analytics Management Client Library.
        
        Azure Resource Manager (ARM) is the next generation of management APIs that
        replace the old Azure Service Management (ASM).
        
        This package has been tested with Python 2.7, 3.4, 3.5 and 3.6.
        
        For the older Azure Service Management (ASM) libraries, see

%package python
Summary: python components for the azure-mgmt-datalake-analytics package.
Group: Default
Requires: azure-mgmt-datalake-analytics-python3 = %{version}-%{release}

%description python
python components for the azure-mgmt-datalake-analytics package.


%package python3
Summary: python3 components for the azure-mgmt-datalake-analytics package.
Group: Default
Requires: python3-core
Provides: pypi(azure_mgmt_datalake_analytics)
Requires: pypi(azure_common)
Requires: pypi(azure_mgmt_datalake_nspkg)
Requires: pypi(msrestazure)

%description python3
python3 components for the azure-mgmt-datalake-analytics package.


%prep
%setup -q -n azure-mgmt-datalake-analytics-0.6.0
cd %{_builddir}/azure-mgmt-datalake-analytics-0.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588789966
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/__init__.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/__pycache__/__init__.cpython-38.pyc
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/mgmt/__init__.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/mgmt/__pycache__/__init__.cpython-38.pyc

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

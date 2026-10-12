%define module uv-dynamic-versioning
%define oname uv_dynamic_versioning

Name:		python-uv-dynamic-versioning
Version:	0.14.0
Release:	2
Summary:	Dynamic versioning based on VCS tags for uv/hatch project
License:	MIT
Group:		Development/Python
URL:		https://github.com/ninoseki/uv-dynamic-versioning
Source0:	https://github.com/ninoseki/uv-dynamic-versioning/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Dynamic versioning based on VCS tags for uv/hatch project

%files
%{_bindir}/%{module}
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info

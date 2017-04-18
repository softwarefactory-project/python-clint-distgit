%global srcname clint

Name:           python-%{srcname}
Version:        0.5.1
Release:        2%{?dist}
Summary:        A set of awesome tools for developing commandline applications

License:        ISC
URL:            https://github.com/kennethreitz/%{srcname}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Patch0:         0001-Adjust-imports-to-avoid-using-vendored-packages.patch
Patch1:         0002-Remove-vendored-packages.patch

BuildArch:      noarch

%description
Clint is a module filled with a set of awesome tools for developing commandline
applications. It supports colors, but detects if the session is a TTY, so
doesn't render the colors if you're piping stuff around. Automagically.


%package -n python2-%{srcname}
Summary:        %{summary}
Requires:       python-appdirs
Requires:       python2-args
Requires:       python-colorama
BuildRequires:  python-colorama
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Clint is a module filled with a set of awesome tools for developing commandline
applications. It supports colors, but detects if the session is a TTY, so
doesn't render the colors if you're piping stuff around. Automagically.


%package doc
Summary: Documentation for python-clint
BuildRequires:  python-sphinx

%description doc
Documentation for the python2-clint and python3-clint packages.
Clint is a module filled with a set of awesome tools for developing commandline
applications. It supports colors, but detects if the session is a TTY, so
doesn't render the colors if you're piping stuff around. Automagically.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%{__python2} setup.py build

make %{?_smp_mflags} -C docs html
make %{?_smp_mflags} -C docs man
rm docs/_build/html/.buildinfo


%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

install -p -D -T -m 0644 docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1


# check
# No tests are currently provided in a tagged release by upstream


%files -n python2-%{srcname}
%license LICENSE
%doc README.rst HISTORY.rst AUTHORS
%{python2_sitelib}/*


%files doc
%license LICENSE
%doc README.rst HISTORY.rst AUTHORS
%doc %{_mandir}/man1/%{srcname}.1*
%doc docs/_build/html


%changelog
* Wed Jul 13 2016 Jeremy Cline <jeremy@jcline.org> - 0.5.1-2
- Leave inter-sphinx inventory file in the doc package
- Explicitly depend on setuptools

* Tue Jul 05 2016 Jeremy Cline <jeremy@jcline.org> - 0.5.1-1
- Initial commit

%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ament-cmake-core
Version:        2.2.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ament_cmake_core package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       cmake3
Requires:       python%{python3_pkgversion}-catkin_pkg
Requires:       ros-rolling-ament-package
BuildRequires:  cmake3
BuildRequires:  python%{python3_pkgversion}-catkin_pkg
BuildRequires:  ros-rolling-ament-package
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The core of the ament buildsystem in CMake. Several subcomponents provide
specific funtionalities: * environment: provide prefix-level setup files *
environment_hooks: provide package-level setup files and environment hooks *
index: store information in an index and retrieve them without crawling *
package_templates: templates from the ament_package Python package *
symlink_install: use symlinks for CMake install commands

%prep
%autosetup -p1

%build
# Needed to bootstrap since the ros_workspace package does not yet exist.
export PYTHONPATH=/opt/ros/rolling/lib/python%{python3_version}/site-packages

# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# Needed to bootstrap since the ros_workspace package does not yet exist.
export PYTHONPATH=/opt/ros/rolling/lib/python%{python3_version}/site-packages

# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Needed to bootstrap since the ros_workspace package does not yet exist.
export PYTHONPATH=/opt/ros/rolling/lib/python%{python3_version}/site-packages

# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Wed Jun 21 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 2.2.1-1
- Autogenerated by Bloom

* Wed Jun 07 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 2.2.0-1
- Autogenerated by Bloom

* Wed Apr 26 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 2.1.0-1
- Autogenerated by Bloom

* Wed Apr 12 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 2.0.2-1
- Autogenerated by Bloom

* Tue Apr 11 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 2.0.1-1
- Autogenerated by Bloom

* Tue Apr 11 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 2.0.0-1
- Autogenerated by Bloom

* Fri Mar 24 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.5.3-6
- Autogenerated by Bloom

* Fri Mar 24 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.5.3-5
- Autogenerated by Bloom

* Tue Mar 21 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.5.3-4
- Autogenerated by Bloom


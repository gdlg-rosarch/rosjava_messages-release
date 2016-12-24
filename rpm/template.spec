Name:           ros-kinetic-rosjava-messages
Version:        0.3.0
Release:        0%{?dist}
Summary:        ROS rosjava_messages package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/rosjava_messages
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-genjava
Requires:       ros-kinetic-rosjava-build-tools
BuildRequires:  ros-kinetic-actionlib-msgs
BuildRequires:  ros-kinetic-ar-track-alvar-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-concert-msgs
BuildRequires:  ros-kinetic-concert-service-msgs
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-gateway-msgs
BuildRequires:  ros-kinetic-genjava
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-move-base-msgs
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-rocon-app-manager-msgs
BuildRequires:  ros-kinetic-rocon-device-msgs
BuildRequires:  ros-kinetic-rocon-interaction-msgs
BuildRequires:  ros-kinetic-rocon-service-pair-msgs
BuildRequires:  ros-kinetic-rocon-std-msgs
BuildRequires:  ros-kinetic-rocon-tutorial-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rosgraph-msgs
BuildRequires:  ros-kinetic-rosjava-build-tools
BuildRequires:  ros-kinetic-rosjava-test-msgs
BuildRequires:  ros-kinetic-scheduler-msgs
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-shape-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-stereo-msgs
BuildRequires:  ros-kinetic-tf2-msgs
BuildRequires:  ros-kinetic-trajectory-msgs
BuildRequires:  ros-kinetic-uuid-msgs
BuildRequires:  ros-kinetic-visualization-msgs
BuildRequires:  ros-kinetic-world-canvas-msgs
BuildRequires:  ros-kinetic-yocs-msgs

%description
Message generation for rosjava.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Dec 24 2016 Daniel Stonier <d.stonier@gmail.com> - 0.3.0-0
- Autogenerated by Bloom


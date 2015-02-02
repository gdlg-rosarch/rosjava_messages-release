Name:           ros-hydro-rosjava-messages
Version:        0.1.318
Release:        0%{?dist}
Summary:        ROS rosjava_messages package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/rosjava_messages
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-rosjava-bootstrap
Requires:       ros-hydro-rosjava-build-tools
BuildRequires:  ros-hydro-ackermann-msgs
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-actionlib-msgs
BuildRequires:  ros-hydro-actionlib-tutorials
BuildRequires:  ros-hydro-app-manager
BuildRequires:  ros-hydro-applanix-msgs
BuildRequires:  ros-hydro-apriltags-ros
BuildRequires:  ros-hydro-ar-track-alvar
BuildRequires:  ros-hydro-arbotix-msgs
BuildRequires:  ros-hydro-ardrone-autonomy
BuildRequires:  ros-hydro-asmach-tutorials
BuildRequires:  ros-hydro-audio-common-msgs
BuildRequires:  ros-hydro-axis-camera
BuildRequires:  ros-hydro-base-local-planner
BuildRequires:  ros-hydro-baxter-core-msgs
BuildRequires:  ros-hydro-baxter-maintenance-msgs
BuildRequires:  ros-hydro-bayesian-belief-networks
BuildRequires:  ros-hydro-blob
BuildRequires:  ros-hydro-bond
BuildRequires:  ros-hydro-brics-actuator
BuildRequires:  ros-hydro-bride-tutorials
BuildRequires:  ros-hydro-bwi-planning
BuildRequires:  ros-hydro-bwi-planning-common
BuildRequires:  ros-hydro-calibration-msgs
BuildRequires:  ros-hydro-capabilities
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-clearpath-base
BuildRequires:  ros-hydro-cmvision
BuildRequires:  ros-hydro-cob-base-drive-chain
BuildRequires:  ros-hydro-cob-camera-sensors
BuildRequires:  ros-hydro-cob-footprint-observer
BuildRequires:  ros-hydro-cob-grasp-generation
BuildRequires:  ros-hydro-cob-kinematics
BuildRequires:  ros-hydro-cob-light
BuildRequires:  ros-hydro-cob-lookat-action
BuildRequires:  ros-hydro-cob-object-detection-msgs
BuildRequires:  ros-hydro-cob-perception-msgs
BuildRequires:  ros-hydro-cob-phidgets
BuildRequires:  ros-hydro-cob-pick-place-action
BuildRequires:  ros-hydro-cob-relayboard
BuildRequires:  ros-hydro-cob-script-server
BuildRequires:  ros-hydro-cob-sound
BuildRequires:  ros-hydro-cob-srvs
BuildRequires:  ros-hydro-cob-trajectory-controller
BuildRequires:  ros-hydro-concert-msgs
BuildRequires:  ros-hydro-control-msgs
BuildRequires:  ros-hydro-control-toolbox
BuildRequires:  ros-hydro-controller-manager-msgs
BuildRequires:  ros-hydro-costmap-2d
BuildRequires:  ros-hydro-create-node
BuildRequires:  ros-hydro-data-vis-msgs
BuildRequires:  ros-hydro-designator-integration-msgs
BuildRequires:  ros-hydro-diagnostic-msgs
BuildRequires:  ros-hydro-dna-extraction-msgs
BuildRequires:  ros-hydro-driver-base
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-dynamic-tf-publisher
BuildRequires:  ros-hydro-dynamixel-controllers
BuildRequires:  ros-hydro-dynamixel-msgs
BuildRequires:  ros-hydro-ecto-ros
BuildRequires:  ros-hydro-epos-driver
BuildRequires:  ros-hydro-ethercat-hardware
BuildRequires:  ros-hydro-ethercat-trigger-controllers
BuildRequires:  ros-hydro-eusgazebo
BuildRequires:  ros-hydro-face-detector
BuildRequires:  ros-hydro-fingertip-pressure
BuildRequires:  ros-hydro-frontier-exploration
BuildRequires:  ros-hydro-fs100-motoman
BuildRequires:  ros-hydro-gateway-msgs
BuildRequires:  ros-hydro-gazebo-msgs
BuildRequires:  ros-hydro-gazebo-plugins
BuildRequires:  ros-hydro-gazebo-ros
BuildRequires:  ros-hydro-geographic-msgs
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-gps-common
BuildRequires:  ros-hydro-graft
BuildRequires:  ros-hydro-graph-msgs
BuildRequires:  ros-hydro-grasp-stability-msgs
BuildRequires:  ros-hydro-grasping-msgs
BuildRequires:  ros-hydro-grizzly-msgs
BuildRequires:  ros-hydro-handle-detector
BuildRequires:  ros-hydro-hector-mapping
BuildRequires:  ros-hydro-hector-nav-msgs
BuildRequires:  ros-hydro-hector-uav-msgs
BuildRequires:  ros-hydro-hector-worldmodel-msgs
BuildRequires:  ros-hydro-household-objects-database-msgs
BuildRequires:  ros-hydro-hrpsys-gazebo-msgs
BuildRequires:  ros-hydro-humanoid-nav-msgs
BuildRequires:  ros-hydro-iai-content-msgs
BuildRequires:  ros-hydro-iai-control-msgs
BuildRequires:  ros-hydro-iai-kinematics-msgs
BuildRequires:  ros-hydro-iai-robosherlock-actions
BuildRequires:  ros-hydro-iai-urdf-msgs
BuildRequires:  ros-hydro-image-cb-detector
BuildRequires:  ros-hydro-image-exposure-msgs
BuildRequires:  ros-hydro-image-view2
BuildRequires:  ros-hydro-industrial-msgs
BuildRequires:  ros-hydro-interaction-cursor-msgs
BuildRequires:  ros-hydro-interactive-marker-proxy
BuildRequires:  ros-hydro-jaco-msgs
BuildRequires:  ros-hydro-jsk-footstep-controller
BuildRequires:  ros-hydro-jsk-footstep-msgs
BuildRequires:  ros-hydro-jsk-gui-msgs
BuildRequires:  ros-hydro-jsk-hark-msgs
BuildRequires:  ros-hydro-jsk-network-tools
BuildRequires:  ros-hydro-jsk-pcl-ros
BuildRequires:  ros-hydro-jsk-perception
BuildRequires:  ros-hydro-jsk-pr2-startup
BuildRequires:  ros-hydro-jsk-recognition-msgs
BuildRequires:  ros-hydro-jsk-rviz-plugins
BuildRequires:  ros-hydro-jsk-topic-tools
BuildRequires:  ros-hydro-keyboard
BuildRequires:  ros-hydro-kingfisher-msgs
BuildRequires:  ros-hydro-kobuki-msgs
BuildRequires:  ros-hydro-kobuki-testsuite
BuildRequires:  ros-hydro-laser-assembler
BuildRequires:  ros-hydro-leap-motion
BuildRequires:  ros-hydro-linux-hardware
BuildRequires:  ros-hydro-lizi
BuildRequires:  ros-hydro-manipulation-msgs
BuildRequires:  ros-hydro-map-msgs
BuildRequires:  ros-hydro-map-store
BuildRequires:  ros-hydro-mavros
BuildRequires:  ros-hydro-microstrain-3dmgx2-imu
BuildRequires:  ros-hydro-ml-classifiers
BuildRequires:  ros-hydro-mln-robosherlock-msgs
BuildRequires:  ros-hydro-mongodb-store
BuildRequires:  ros-hydro-mongodb-store-msgs
BuildRequires:  ros-hydro-move-base
BuildRequires:  ros-hydro-move-base-msgs
BuildRequires:  ros-hydro-moveit-msgs
BuildRequires:  ros-hydro-moveit-simple-grasps
BuildRequires:  ros-hydro-multimaster-msgs-fkie
BuildRequires:  ros-hydro-multisense-ros
BuildRequires:  ros-hydro-nao-interaction-msgs
BuildRequires:  ros-hydro-naoqi-msgs
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-nav2d-msgs
BuildRequires:  ros-hydro-nav2d-navigator
BuildRequires:  ros-hydro-nav2d-operator
BuildRequires:  ros-hydro-ndt-map
BuildRequires:  ros-hydro-network-monitor-udp
BuildRequires:  ros-hydro-nmea-msgs
BuildRequires:  ros-hydro-nodelet
BuildRequires:  ros-hydro-novatel-msgs
BuildRequires:  ros-hydro-object-recognition-msgs
BuildRequires:  ros-hydro-octomap-msgs
BuildRequires:  ros-hydro-p2os-driver
BuildRequires:  ros-hydro-p2os-teleop
BuildRequires:  ros-hydro-p2os-urdf
BuildRequires:  ros-hydro-pano-ros
BuildRequires:  ros-hydro-pcl-msgs
BuildRequires:  ros-hydro-pddl-msgs
BuildRequires:  ros-hydro-people-msgs
BuildRequires:  ros-hydro-person-msgs
BuildRequires:  ros-hydro-play-motion-msgs
BuildRequires:  ros-hydro-polled-camera
BuildRequires:  ros-hydro-posedetection-msgs
BuildRequires:  ros-hydro-pr2-calibration-launch
BuildRequires:  ros-hydro-pr2-common-action-msgs
BuildRequires:  ros-hydro-pr2-controllers-msgs
BuildRequires:  ros-hydro-pr2-gazebo-plugins
BuildRequires:  ros-hydro-pr2-gripper-sensor-action
BuildRequires:  ros-hydro-pr2-gripper-sensor-msgs
BuildRequires:  ros-hydro-pr2-mechanism-controllers
BuildRequires:  ros-hydro-pr2-mechanism-msgs
BuildRequires:  ros-hydro-pr2-msgs
BuildRequires:  ros-hydro-pr2-power-board
BuildRequires:  ros-hydro-pr2-precise-trajectory
BuildRequires:  ros-hydro-pr2-self-test-msgs
BuildRequires:  ros-hydro-pr2-tilt-laser-interface
BuildRequires:  ros-hydro-program-queue
BuildRequires:  ros-hydro-ptu-control
BuildRequires:  ros-hydro-qt-tutorials
BuildRequires:  ros-hydro-r2-msgs
BuildRequires:  ros-hydro-razer-hydra
BuildRequires:  ros-hydro-resized-image-transport
BuildRequires:  ros-hydro-robot-localization
BuildRequires:  ros-hydro-roboteq-msgs
BuildRequires:  ros-hydro-robotnik-msgs
BuildRequires:  ros-hydro-rocon-app-manager-msgs
BuildRequires:  ros-hydro-rocon-interaction-msgs
BuildRequires:  ros-hydro-rocon-service-pair-msgs
BuildRequires:  ros-hydro-rocon-std-msgs
BuildRequires:  ros-hydro-romeo-dcm-msgs
BuildRequires:  ros-hydro-rosapi
BuildRequires:  ros-hydro-rosauth
BuildRequires:  ros-hydro-rosbridge-library
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-roscpp-tutorials
BuildRequires:  ros-hydro-roseus
BuildRequires:  ros-hydro-rosgraph-msgs
BuildRequires:  ros-hydro-rosjava-bootstrap
BuildRequires:  ros-hydro-rosjava-build-tools
BuildRequires:  ros-hydro-rospeex-msgs
BuildRequires:  ros-hydro-rospy-message-converter
BuildRequires:  ros-hydro-rospy-tutorials
BuildRequires:  ros-hydro-rosruby
BuildRequires:  ros-hydro-rosruby-messages
BuildRequires:  ros-hydro-rosruby-tutorials
BuildRequires:  ros-hydro-rosserial-arduino
BuildRequires:  ros-hydro-rosserial-msgs
BuildRequires:  ros-hydro-rosserial-windows
BuildRequires:  ros-hydro-rovio-shared
BuildRequires:  ros-hydro-rtmbuild
BuildRequires:  ros-hydro-rtt-ros-msgs
BuildRequires:  ros-hydro-s3000-laser
BuildRequires:  ros-hydro-saphari-msgs
BuildRequires:  ros-hydro-scanning-table-msgs
BuildRequires:  ros-hydro-scheduler-msgs
BuildRequires:  ros-hydro-schunk-sdh
BuildRequires:  ros-hydro-segbot-gui
BuildRequires:  ros-hydro-segbot-sensors
BuildRequires:  ros-hydro-segbot-simulation-apps
BuildRequires:  ros-hydro-segway-rmp
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-shape-msgs
BuildRequires:  ros-hydro-shared-serial
BuildRequires:  ros-hydro-sherlock-sim-msgs
BuildRequires:  ros-hydro-simple-robot-control
BuildRequires:  ros-hydro-smach-msgs
BuildRequires:  ros-hydro-smart-battery-msgs
BuildRequires:  ros-hydro-sound-play
BuildRequires:  ros-hydro-speech-recognition-msgs
BuildRequires:  ros-hydro-sr-edc-ethercat-drivers
BuildRequires:  ros-hydro-sr-robot-msgs
BuildRequires:  ros-hydro-sr-ronex-msgs
BuildRequires:  ros-hydro-statistics-msgs
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-std-srvs
BuildRequires:  ros-hydro-stdr-msgs
BuildRequires:  ros-hydro-stereo-msgs
BuildRequires:  ros-hydro-stereo-wall-detection
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-tf2-msgs
BuildRequires:  ros-hydro-theora-image-transport
BuildRequires:  ros-hydro-topic-proxy
BuildRequires:  ros-hydro-topic-tools
BuildRequires:  ros-hydro-trajectory-msgs
BuildRequires:  ros-hydro-turtle-actionlib
BuildRequires:  ros-hydro-turtlebot-actions
BuildRequires:  ros-hydro-turtlebot-calibration
BuildRequires:  ros-hydro-turtlebot-msgs
BuildRequires:  ros-hydro-turtlesim
BuildRequires:  ros-hydro-twist-mux-msgs
BuildRequires:  ros-hydro-um6
BuildRequires:  ros-hydro-underwater-sensor-msgs
BuildRequires:  ros-hydro-universal-teleop
BuildRequires:  ros-hydro-ur-msgs
BuildRequires:  ros-hydro-uuid-msgs
BuildRequires:  ros-hydro-velodyne-msgs
BuildRequires:  ros-hydro-view-controller-msgs
BuildRequires:  ros-hydro-visp-camera-calibration
BuildRequires:  ros-hydro-visp-hand2eye-calibration
BuildRequires:  ros-hydro-visp-tracker
BuildRequires:  ros-hydro-visualization-msgs
BuildRequires:  ros-hydro-wfov-camera-msgs
BuildRequires:  ros-hydro-wge100-camera
BuildRequires:  ros-hydro-wifi-ddwrt
BuildRequires:  ros-hydro-wireless-msgs
BuildRequires:  ros-hydro-yocs-msgs
BuildRequires:  ros-hydro-zeroconf-msgs

%description
Message generation for rosjava.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Feb 02 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.318-0
- Autogenerated by Bloom

* Sun Feb 01 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.317-0
- Autogenerated by Bloom


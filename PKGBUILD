# Script generated with Bloom
pkgdesc="ROS - Message generation for rosjava."
url='http://ros.org/wiki/rosjava_messages'

pkgname='ros-kinetic-rosjava-messages'
pkgver='0.3.0_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-actionlib-msgs'
'ros-kinetic-ar-track-alvar-msgs'
'ros-kinetic-catkin'
'ros-kinetic-concert-msgs'
'ros-kinetic-concert-service-msgs'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-gateway-msgs'
'ros-kinetic-genjava'
'ros-kinetic-geometry-msgs'
'ros-kinetic-move-base-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-rocon-app-manager-msgs'
'ros-kinetic-rocon-device-msgs'
'ros-kinetic-rocon-interaction-msgs'
'ros-kinetic-rocon-service-pair-msgs'
'ros-kinetic-rocon-std-msgs'
'ros-kinetic-rocon-tutorial-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-rosgraph-msgs'
'ros-kinetic-rosjava-build-tools'
'ros-kinetic-rosjava-test-msgs'
'ros-kinetic-scheduler-msgs'
'ros-kinetic-sensor-msgs'
'ros-kinetic-shape-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-stereo-msgs'
'ros-kinetic-tf2-msgs'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-uuid-msgs'
'ros-kinetic-visualization-msgs'
'ros-kinetic-world-canvas-msgs'
'ros-kinetic-yocs-msgs'
)

depends=('ros-kinetic-genjava'
'ros-kinetic-rosjava-build-tools'
)

conflicts=()
replaces=()

_dir=rosjava_messages
source=()
md5sums=()

prepare() {
    cp -R $startdir/rosjava_messages $srcdir/rosjava_messages
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}


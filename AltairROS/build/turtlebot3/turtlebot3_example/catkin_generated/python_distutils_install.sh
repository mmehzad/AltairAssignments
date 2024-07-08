#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/euphyzr/AltairROS/src/turtlebot3/turtlebot3_example"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/euphyzr/AltairROS/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/euphyzr/AltairROS/install/lib/python3/dist-packages:/home/euphyzr/AltairROS/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/euphyzr/AltairROS/build" \
    "/usr/bin/python3" \
    "/home/euphyzr/AltairROS/src/turtlebot3/turtlebot3_example/setup.py" \
     \
    build --build-base "/home/euphyzr/AltairROS/build/turtlebot3/turtlebot3_example" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/euphyzr/AltairROS/install" --install-scripts="/home/euphyzr/AltairROS/install/bin"

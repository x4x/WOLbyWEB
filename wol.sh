#! /bin/sh
### BEGIN INIT INFO
# Provides:          WOLbyWEB
# Required-Start:
# Required-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Starts & Stops My Programm
# Description:       Starts & Stops My Programm
### END INIT INFO

#Switch case fuer den ersten Parameter
case "$1" in
    start)
 #Aktion wenn start uebergeben wird
        echo "starting uwsgi WOL interface"
        uwsgi /opt/WOLbyWEB/uwsgi.ini &
        ;;

    stop)
 #Aktion wenn stop uebergeben wird
        echo "stopping uwsgi WOL interface (killall)"
        killall uwsgi
        ;;

    restart)
 #Aktion wenn restart uebergeben wird
        echo "restarting uwsgi WOL interface"
        killall uwsgi
        uwsgi /opt/WOLbyWEB/uwsgi.ini &
        ;;
 *)
 #Standard Aktion wenn start|stop|restart nicht passen
 echo "(start|stop|restart)"
 ;;
esac

exit 0

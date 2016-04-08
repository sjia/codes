#!/bin/bash
export JAVA_HOME="/software/java/jdk1.6.0_30"

NOW="$(date +'%Y-%m-%d-%H-%M')"
HIGHCPU="HighCpu-$NOW"
HIGHMEMORY="HighMemory-$NOW"
BOTHHIGH="BothHigh-$NOW"
PID=`ps aux |grep -i esp_services |grep -v grep |awk '{print $2}'`
THREADINFO=`top -b -p $PID -n 1 -H | sed -n -e '8p'`
PROCESSINFO=`top -b -p $PID -n 1 |sed -n -e '8p'`
PSUSAGE=`echo "$PROCESSINFO"|awk '{print $9}'`
THREADID=`echo "$THREADINFO"|awk '{print $1}'`
CPUUSAGE=`echo "$THREADINFO"|awk '{print $9}'`
MEMORYUSAGE=`echo "$THREADINFO"|awk '{print $10}'`
INTCPUUSAGE=`echo "$CPUUSAGE"|awk -F. '{print $1}'`
INTPSUSAGE=`echo "$PSUSAGE"|awk -F. '{print $1}'`
INTMEMORYUSAGE=`echo "$MEMORYUSAGE"|awk -F. '{print $1}'`
if [ $INTPSUSAGE -gt 95 ]; then
        LOG=`echo $HIGHCPU.log`
        MEMORYDUMP=`echo $HIGHCPU.hprof`
fi
if [ $INTMEMORYUSAGE -gt 90 ]; then
        LOG=`echo $HIGHMEMORY.log`
        MEMORYDUMP=`echo $HIGHMEMORY.hprof`
fi
if [ $INTPSUSAGE -gt 95 ]&&[ $INTMEMORYUSAGE -gt 90 ]; then
        LOG=`echo $BOTHHIGH.log`
        MEMORYDUMP=`echo $BOTHHIGH.hprof`
fi
if [ $INTPSUSAGE -gt 95 ]||[ $INTMEMORYUSAGE -gt 90 ]; then
        echo "==============================================" >> $LOG
        echo "current esp_service PID is: $PID" >> $LOG
        echo "===============CPU USAGE:$PSUSAGE==============">>$LOG
        echo "===============MEMORY USAGE:$MEMORYUSAGE==============">>$LOG
        echo "===============================================" >> $LOG
        echo "thread $THREADID has highest cup usage,cost $CPUUSAGE cpu usage " >> $LOG

        echo '===============================================' >> $LOG
        `$JAVA_HOME/bin/jstack -J-d64 $PID >> $LOG`
        echo '===============================================' >> $LOG
        echo 'List the number of loaded classes and how much space these classes used' >> $LOG
        `$JAVA_HOME/bin/jstat -class $PID >> $LOG`
        echo '================================================' >> $LOG
        echo 'The usage of three generation(yong,old,perm) objects in VM memory' >> $LOG
        `$JAVA_HOME/bin/jstat -gccapacity $PID >> $LOG`
        echo '================================================' >> $LOG
        echo 'The usage of heap space' >> $LOG
        `$JAVA_HOME/bin/jmap -heap $PID >> $LOG`
         echo '================================================' >> $LOG
        count=`ls *.hprof | wc -l`
        if [ $count -gt 4 ]; then
            echo 'memory dump files are more 3,will not do the dump operation' >> $LOG
        else
            echo 'dumping the memory info' >> $LOG
            $JAVA_HOME/bin/jmap -dump:format=b,file=$MEMORYDUMP $PID
        fi

fi

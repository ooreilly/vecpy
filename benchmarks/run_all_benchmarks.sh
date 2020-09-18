if [ $# != 1 ]; 
then
        echo "usage: ${0} <test> "
        echo "test : Run in test mode (1 or 0). Otherwise, run in benchmark mode."
        exit -1
fi
test=$1
if [ ${test} == "1" ];
then
        echo Test mode;
        dir=tests
        benchmarks="geometric-series trig"
else
        echo Benchmark mode;
        benchmarks="sum geometric-series trig array-sum"
        dir=data
fi
for dtype in float64 float32;
do
        for benchmark in $benchmarks;
        do
                for lib in numpy numexpr cupy skcuda vecpy; 
                do
                       make init benchmark test=${test} outputdir=${dir}/${benchmark}_${dtype} dtype=${dtype} lib=$lib benchmark=$benchmark
                done
        done
done

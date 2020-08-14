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
                       make init benchmark test=${test} outputdir=${dir}/${benchmark}_${dtype}
                       dtype=${dtype} lib=$lib benchmark=$benchmark
                done
        done
done

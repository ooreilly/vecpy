benchmarks="sum geometric-series trig array-sum"
for dtype in float64 float32;
do
        for benchmark in $benchmarks;
        do
                make plot outputdir=data/${benchmark}_${dtype} dtype=${dtype} benchmark=$benchmark
        done
done

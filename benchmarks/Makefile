py=python3
julia=julia
outputdir=data
plotdir=plots
lib=numpy
test=0
dtype=float32
test=0
benchmark=sum
sizes=200
begin=2
end=7
trials=100

all: init

init:
	mkdir -p $(outputdir) $(plotdir)

benchmark:
	$(py) benchmarks.py $(benchmark) $(lib) $(sizes) $(begin) $(end) $(trials) $(dtype) $(test) | tee $(outputdir)/$(lib).txt

experiment:
	$(py) benchmarks.py $(benchmark) $(lib) $(sizes) $(begin) $(end) $(trials) $(dtype) 0 

plot:
	$(py) plot.py $(outputdir)/*.txt $(plotdir)/$(benchmark)_$(dtype).svg




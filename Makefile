root=../vecpy/api
srcs:=$(wildcard $(root)/*.py)
bins := $(srcs:$(root)/%.py=%)
filt:=$(filter-out __init__, $(bins)) 
out := $(filt:%=docs/%.md)    

out : $(filt) 

% : docs/%.md 
	mydocstring $(root)/$@.py $@ -m -T=template.md > $<

copy-benchmarks:
	cp ${VECPY}/benchmarks/plots/* static/img/benchmarks/


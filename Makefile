all: clone build copy-benchmarks# cleanup

clone:
	git clone git@github.com:ooreilly/vecpy.git vecpy_tmp

build:
	bash docs.sh

copy-benchmarks:
	cp vecpy_tmp/benchmarks/plots/* static/img/benchmarks/

cleanup:
	rm -rf vecpy_tmp



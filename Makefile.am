AUTOMAKE_OPTIONS = foreign dist-bzip2 1.6

SUBDIRS = src examples
EXTRA_DIST = osmoappdesc.py

if ENABLE_VTY_TESTS
python-tests: $(BUILT_SOURCES)
	osmotestvty.py -p $(abs_top_srcdir) -w $(abs_builddir) -v
	osmotestconfig.py -p $(abs_top_srcdir) -w $(abs_builddir) -v
else
python-tests: $(BUILT_SOURCES)
	echo "Not running python-based tests (determined at configure-time)"
endif

check-local: $(BUILT_SOURCES)
	$(MAKE) $(AM_MAKEFLAGS) python-tests

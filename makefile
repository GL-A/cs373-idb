FILES :=                              \
    .gitignore												\
    .travis.yml												\
    makefile													\
    IDB2.log                       		\
    UML.pdf                        		\
    apiary.apib                     	\
    models.html                    		\
    app/models.py                     \
    app/tests.py                   		\

ifeq ($(CI), true)
    COVERAGE := coverage
    PYLINT   := pylint
else
    COVERAGE := coverage-3.5
		PYLINT   := pylint3
endif

.pylintrc:
	$(PYLINT) --disable=bad-whitespace,invalid-name,redefined-outer-name,line-too-long,missing-docstring,too-many-branches,too-many-locals,too-many-statements,pointless-string-statement --extension-pkg-whitelist=numpy --reports=n --generate-rcfile > $@

models.html: app/models.py
	pydoc3 -w models

IDB2.log:
	git log > IDB2.log

tests.out: .pylintrc app/tests.py
	-$(PYLINT) app/tests.py
	$(COVERAGE) run    --branch app/tests.py >  tests.out 2>&1
	$(COVERAGE) report -m                      >> tests.out
	cat tests.out

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f .pylintrc
	rm -f test.db
	rm -f tests.out
	rm -f  *.pyc
	rm -f  models.html
	rm -f  IDB2.log
	rm -rf __pycache__

config:
	git config -l

format:
	autopep8 -i app/models.py
	autopep8 -i app/tests.py

test:
	python app/tests.py

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

all: models.html IDB2.log tests.out check

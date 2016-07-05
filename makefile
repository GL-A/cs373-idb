FILES :=                              \
    IDB1.log                       		\
    UML.pdf                        		\
    apiary.apib                     	\
    models.html                    		\
    models.py                     		\
    tests.py                   				\

ifeq ($(CI), true)
    COVERAGE := coverage
    PYLINT   := pylint
else
    COVERAGE := coverage-3.5
		PYLINT   := pylint3
endif

models.html: models.py
	pydoc3 -w models

IDB1.log:
	git log > IDB1.log

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
	rm -f  *.pyc
	rm -f  models.html
	rm -f  IDB.log
	rm -rf __pycache__

config:
	git config -l

format:
	autopep8 -i models.py
	autopep8 -i test.py

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

all: models.html IDB1.log check

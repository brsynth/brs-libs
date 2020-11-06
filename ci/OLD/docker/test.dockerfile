ARG IMAGE
FROM ${IMAGE}

RUN conda update -n base -c defaults conda \
 && conda install -y -c conda-forge pyyaml

ARG HOME
WORKDIR ${HOME}

ADD recipe recipe

ARG PYTEST_FOLDER=/tmp/pytest
ADD ci/pytest $PYTEST_FOLDER
RUN python $PYTEST_FOLDER/parse_recipe.py > $PYTEST_FOLDER/build_configs.txt
RUN for pkg in `cat $PYTEST_FOLDER/build_configs.txt` ; do \
      conda create -n test_$pkg $pkg ; \
      conda env update -n test_$pkg --file $PYTEST_FOLDER/environment.yml ; \
    done

RUN apt-get update \
 && apt-get install -y make

RUN echo "#!/bin/sh" > /docker-entrypoint.sh
RUN echo "conda env list \
        | cut -d\" \" -f1 \
        | tail -n+4 \
        | grep test_ \
        | xargs -L 1 -I env \
        conda run -n env \$@" >> /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ARG PKG
ADD ci     ci
ADD extras extras
ADD tests  tests
ADD ${PKG} tests/${PKG}

WORKDIR ${HOME}/ci

ENTRYPOINT ["/docker-entrypoint.sh"]

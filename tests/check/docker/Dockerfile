# ARG IMAGE
# FROM ${IMAGE}
#
# ARG PKG
# COPY tests/check/requirements.txt requirements-test.txt
# COPY extras/requirements.txt requirements-src.txt
# # install requirements
# RUN python3 -m pip install --upgrade pip \
#  && python3 -m pip install --no-cache-dir --upgrade -r requirements-test.txt \
#  && python3 -m pip install --no-cache-dir --upgrade -r requirements-src.txt
#
# ARG HOME
# WORKDIR ${HOME}
#
# ADD ${PKG} ${PKG}
# ADD tests tests

ARG IMAGE
FROM ${IMAGE}

RUN conda update -n base -c defaults conda

COPY tests/check/environment.yml conda_env_check.yml
ARG PKG
RUN conda env create -n check --file conda_env_check.yml

ARG HOME
WORKDIR ${HOME}
ADD tests tests
ADD ${PKG} ${PKG}

ENTRYPOINT ["conda", "run", "-n", "check"]

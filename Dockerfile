# Token
#
# Build:
#
#    % docker build -t token
#
# Run:
#
#    % docker run -it --rm token brownie test
#
#    % docker run -it --rm --volume "$(pwd)":/token token brownie test --coverage
#

FROM minty/brownie:1.17.0

ENV HOME=/tmp

RUN apk add curl
RUN python -c "from brownie.project.compiler import install_solc;install_solc('0.8.10')"

COPY . /code

RUN chmod -R 777 /code
RUN chmod -R 777 /tmp

WORKDIR /code

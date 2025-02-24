FROM Python:3.11.4-slim
VOLUME /var/code
RUN pip install pytest
RUN pip install pytest-bdd
WORKDIR  /var/code
RUN apt-get update && apt-get install git -y

ENTRYPOINT [ "sleep infinity" ]
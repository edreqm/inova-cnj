FROM ubuntu:18.04

RUN apt update \
  && apt upgrade -y \
  && apt install git nodejs npm wget -y

RUN apt remove nodejs npm -y

RUN wget https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh \
  && bash install.sh

# Coloca nvm no path
RUN . /root/.bashrc \
  && nvm --version \
  && nvm install 14.4.0 \
  && npm --version \
  && node --version

ENV PATH /root/.nvm/versions/node/v14.4.0/bin:$PATH

RUN npm config set user 0 \
  && npm config set unsafe-perm true

RUN npm install -g @angular/cli
 
RUN node --version && ng --version

#RUN ng update @angular/cli

RUN groupadd -r inovacnj \
  && useradd --no-log-init -m -r -s /bin/bash -g inovacnj inovacnj

#USER inovacnj

#WORKDIR /home/inovacnj

RUN git clone https://github.com/edreqm/inova-cnj.git

WORKDIR inova-cnj/cubejs/frontend/minerador-processos

RUN npm install

CMD ng serve --port $PORT

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
  && nvm install 14.4.0 -g \
  && npm --version \
  && node --version \
  && npm config set user 0 \
  && npm config set unsafe-perm true \
  && npm install -g @angular/cli \
  && npm link @angular/cli
 
#RUN node --version && ng --version

RUN groupadd -r inovacnj \
  && useradd --no-log-init -m -r -s /bin/bash -g inovacnj inovacnj

USER inovacnj

WORKDIR /home/inovacnj

RUN wget https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh \
  && bash install.sh

ENV NVM_DIR /home/inovacnj/.nvm

RUN chmod +x $NVM_DIR/nvm.sh

RUN . $NVM_DIR/nvm.sh \
  && nvm --version \
  && nvm install 14.4.0

ENV PATH /home/inovacnj/.nvm/versions/node/v14.4.0/bin:$PATH

RUN  npm --version \ 
  && node --version

RUN npm install @angular/cli \
  && npm link @angular/cli

RUN ng --version

RUN git clone https://github.com/edreqm/inova-cnj.git

WORKDIR inova-cnj/cubejs/frontend/minerador-processos

RUN npm install

CMD ng serve --port $PORT --host 0.0.0.0 --disableHostCheck true --liveReload false

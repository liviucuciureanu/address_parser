FROM python:3.9

RUN apt-get update && \
  apt-get install --yes \
  curl \
  autoconf \
  automake \
  libtool \
  git \
  pkg-config

WORKDIR /app

RUN git clone https://github.com/openvenues/libpostal

WORKDIR /app/libpostal

RUN git clone https://github.com/openvenues/libpostal
RUN cd libpostal
RUN ./bootstrap.sh
RUN ./configure
RUN make
RUN make install
RUN ldconfig

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "parser.py"]


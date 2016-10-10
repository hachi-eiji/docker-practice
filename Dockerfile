FROM python:3.4

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install Flask==0.10.1 uWSGI==2.0.8 requests==2.5.1
WORKDIR /app
COPY app /app
COPY cmd.sh /

# 待ち受けるポートを指定する
EXPOSE 9090 9091
# root で入られると困るのでユーザを指定
USER uwsgi

CMD ["/cmd.sh"]

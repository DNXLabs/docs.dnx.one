FROM jekyll/jekyll:3.8

WORKDIR /site

ADD Gemfile .
ADD Gemfile.lock .

RUN gem install bundler && bundle

EXPOSE 4000

COPY . .

ENTRYPOINT [ "jekyll" ]

CMD [ "serve" ]
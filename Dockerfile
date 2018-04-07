FROM python AS builder
WORKDIR /src
ADD . .
RUN pip install virtualenv && virtualenv venv

FROM alpine
WORKDIR /app
COPY --from=builder /src .
CMD source venv/bin/activate; python dalias.py

FROM node:22-bookworm-slim

WORKDIR /site
COPY . .

RUN npm run check

EXPOSE 8000
CMD ["python3", "-m", "http.server", "8000", "--bind", "0.0.0.0"]

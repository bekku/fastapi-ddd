# ベースイメージとして Python 3.12 を使用
FROM python:3.12-slim

# システムパッケージをアップデートし、必要な依存パッケージをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    wget \
    gnupg \
    fonts-liberation \
    libatk-bridge2.0-0 \
    libdbus-1-3 \
    libgbm1 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# WORKDIRを設定
WORKDIR /workspace

# Python依存パッケージのインストール
COPY docker/requirements.txt .
RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt

# アプリケーションコードをコピー
COPY app /workspace/app

# パスを設定
ENV PYTHONPATH=/workspace
ENV PYTHONUNBUFFERED=1

# コンテナの起動時にstreamlit実行
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

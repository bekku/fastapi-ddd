# Research Streamlit

StreamlitによるリサーチAI

## 目次
- [セットアップ手順](#セットアップ手順)
- [使い方](#使い方)
- [ディレクトリ構造](#ディレクトリ構造)

## セットアップ手順

### 環境構築
1. このリポジトリをクローンします。
   ```bash
   git clone https://github.com/labdemy-dev/research_streamlit.git
   cd research-llm
   ```
2. 下記の.envを`research-llm/.env`に配置
   ```
   OPENAI_API_KEY=
   GOOGLE_API_KEY=
   GOOGLE_CSE_ID=
   ```
5. イメージのbuild
   ```bash
   docker compose build
   ```
6. 実行
   ```bash
   docker compose up
   ```
# Pyhton 3.10.0の環境をDockerで構築する

## 必須環境

- 十分なメモリ (推奨: 8GB ~ 16GB)
- Dockerの環境
- Docker Composeの環境
- Docker Composeのバージョン: 1.27.4以上

## 推奨環境

- makeコマンドの環境

## 使い方

### 起動前に

```bash
make build            # 初回のみ
make creaet-network   # 初回のみ
```

### 起動

```bash
make run
```

### bashで入る

```bash
make bash
```

## ディレクトリ構成

```bash
compose
|-- docker-compose.yml
|-- Dockerfile
|-- README.md
|-- src <- ここの中がワークスペース
|   |-- main.py
|   |-- .env
|
|-- dependencies
|   |-- requirements.txt <- pip installするものを記述
```

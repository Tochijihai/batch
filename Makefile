# 開発サーバーの起動
dev:
	poetry run python -m app.main
# 初回セットアップ：Poetryインストール＆パッケージインストール
setup:
	@echo "==> Poetry インストール"
	curl -sSL https://install.python-poetry.org | python3 - || true
	@echo "==> PATH を一時適用"
	export PATH="$$HOME/.local/bin:$$PATH"
	@echo "==> 依存関係インストール"
	poetry install

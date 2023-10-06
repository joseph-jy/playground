LOCAL_ENV_HOME = "."

.PHONY: help
help: #🟩 도움말
	@echo "——————————————————————————————————————————————————"
	@cat Makefile | grep "#🟩" | grep -v "grep"  | awk -F":.* #🟩" '{ printf("• \033[1;32m%-20s\033[0m %s\n",$$1, $$2)}'
	@echo "——————————————————————————————————————————————————"

——————————[개발환경]——————————————————————————————————————: #🟩
.PHONY: setup
setup: #🟩 빌드
	@echo "🔥 Python"

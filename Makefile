.PHONY: test check serve

test: check

check:
	npm run check

serve:
	python3 -m http.server 8000

default:
	@cat makefile

get_texts:
	@bash get_the_books.sh

raven_line_count:
	cat pg17192.txt | wc -l

raven_word_count:
	cat pg17192.txt | wc -w

raven_counts:
	@echo "raven case-sensitive count:"
	cat pg17192.txt | grep raven | wc -l
	@echo "Raven case-sensitive count:"
	cat pg17192.txt | grep Raven | wc -l
	@echo "Case-insensitive total count:"
	cat pg17192.txt | grep -w -E 'raven|Raven' | wc -l

total_lines:
	wc -l *.txt

total_words:
	wc -w *.txt

setup_env:
	python3 -m venv env
	. env/bin/activate; pip install --upgrade pip; pip install -r requirements.txt

test:
	pytest -m "not integration" -v

test_integration:
	pytest -m "integration" -v

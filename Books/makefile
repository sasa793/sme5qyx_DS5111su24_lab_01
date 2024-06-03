default:
	@cat makefile

get texts:
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

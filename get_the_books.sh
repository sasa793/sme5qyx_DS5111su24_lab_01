#!/bin/bash

echo "current directory: $(pwd)"

# Including Books directory if it DNE
mkdir -p Books

#edgar's book IDs
book_ids=("932" "17192" "1064" "1063" "2148" "2147" "2150" "50852" "25266" "32037")

#loop through the book IDs and download each
for book_id in "${book_ids[@]}"; do
	wget -O "./pg${book_id}.txt" "https://www.gutenberg.org/ebooks/${book_id}.txt.utf-8"
done

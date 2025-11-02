def get_book_text(filepath):
        with open(filepath) as f:
            return f.read()
def count_characters(text):
        counts = {}
        for i in text.lower():
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        
        return counts
def sort_on(item):
     return item["num"]
def sort_count(counts):
     sortedcounts = []
     for ch, num in counts.items():
        sortedcounts.append({"char": ch, "num": num})
     sortedcounts.sort(reverse=True, key=sort_on)
     return sortedcounts
# Task 11: Reverse Words
text = "python is easy"
reversed_words = " ".join(text.split()[::-1])
print(reversed_words)  # easy is python

# Task 12: Email Domain Extraction
email = "user@gmail.com"
domain = email[email.index("@") + 1:]
print(domain)  
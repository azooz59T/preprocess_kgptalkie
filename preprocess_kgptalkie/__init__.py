from preprocess_kgptalkie import utils

__version__ = '0.0.2'

def get_wordcounts(x):
	return utils._get_wordcounts(x)

def get_charcounts(x):
	return utils._get_charcounts(x)

def get_avg_wordlength(x):
	return utils._get_avg_wordlength(x)

def get_stopwords_counts(x):
	return utils._get_stopwords_counts(x)

def get_hashtag_counts(x):
	return utils._get_hashtag_counts(x)	

def get_mentions_counts(x):
	return utils._get_mentions_counts(x)	

def get_digit_counts(x):
	return utils._get_digit_counts(x)	

def get_uppercase_counts(x):
	return utils._get_uppercase_counts(x)

def get_lowercase_counts(x):
	return utils.get_lowercase_counts(x)

def count_exp(x):
	return utils._count_exp(x)

def get_emails(x):
	return utils._get_emails(x)

def remove_emails(x):
	return utils._remove_emails(x)

def get_urls(x):
	return utils._get_urls(x)	

def remove_urls(x):	
	return utils._remove_urls(x)

def remove_rt(x):
	return utils._remove_rt(x)	

def remove_special_chars(x):
	return utils._remove_special_chars(x)

def remove_html_tags(x):
	return utils.remove_html_tags(x)

def remove_acceneted_chars(x):
	return utils._remove_acceneted_chars(x)

def remove_stopwords(x):
	return utils._remove_stopwords(x)

def make_base(x):
	return utils.make_base(x)

def get_value_counts(df, col):
	return util._get_value_counts(df, col)	

def reomve_common_words(x, freq, n=20):
	return utils.reomve_common_words(x, freq, n)

def reomve_rare_words(x, freq, n=20):
	return utils.reomve_rare_words(x, freq, n)

def spelling_correction(x):							
	return utils._spelling_correction(x)	
# https://stackoverflow.com/questions/31607710/randomize-elements-of-a-list-in-jinja-2

import random

def filter_shuffle(seq):
  try:
    result = list(seq)
    random.shuffle(result)
    return result
  except:
    return seq

def filter_split(text, separator):
  return text.split(separator)

def filter_navigation(articles_by_dates, article):
  result = {'has_prev': False, 'has_next': False, 'id': -1}

  for index, post in enumerate(articles_by_dates):
    if post.url == article.url: result['id'] = index

  if result['id'] + 1 > 1:
    result['has_prev'] = True

    for index, post in enumerate(articles_by_dates):
      if index == result['id'] - 1:
        result['prev_url']   = post.url
        result['prev_title'] = post.title

  if result['id'] + 1 < len(articles_by_dates):
    result['has_next'] = True

    for index, post in enumerate(articles_by_dates):
      if index == result['id'] + 1:
        result['next_url']   = post.url
        result['next_title'] = post.title

  return result

def filter_keyjoin(tags, category, keywords):
  terms = []
  terms.append(category)
  terms.extend(tags)
  terms.extend(keywords)
  return terms

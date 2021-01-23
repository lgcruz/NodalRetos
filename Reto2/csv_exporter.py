import pandas as pd
from pandas import ExcelWriter
import os.path

def export(post, caption, date, likes, ids, ids_child, comments, names):
    fname = 'comments.csv'
    temp = {}
    temp_names = []
    temp_comments = []
    temp_comments_dates = []
    temp_comments_likes = []
    temp_comments_ids = []
    temp_comments_ids_child = []
    """
    if os.path.isfile(fname):
        #saved = pd.read_excel(fname)
        temp_names.extend(saved['name'])
        temp_comments.extend(saved['comment'])
    """
    temp_names.extend(names)
    temp_comments.extend(comments)
    temp_comments_dates.extend(date)
    temp_comments_likes.extend(likes)
    temp_comments_ids.extend(ids)
    temp_comments_ids_child.extend(ids_child)
    temp.update({'Post': post,
                 'Caption': caption,
                 'Date': temp_comments_dates,
                 'likesComment': temp_comments_likes,
                 'IdFatherComment': temp_comments_ids,
                 'IdChildComment': temp_comments_ids_child,
                 'Username': temp_names,
                 'UserComment': temp_comments})
    df = pd.DataFrame(temp)
    #writer = ExcelWriter(fname)
    df.to_csv(fname, index=False)
    #writer.save(,index=False)
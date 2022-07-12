import pandas as pd
'''
places_review = pd.read_csv(r'/Users/seoyeong/Downloads/places_review.csv')
place = pd.read_csv(r'/Users/seoyeong/Downloads/places.csv')
# print(places_review.head())
# print(place.head())
# for comment in places_review.COMMENTS:
#     if comment[0] == "'":
        
# for i in range(len(places_review)):
#     if places_review.COMMENTS[i][0] != "'":
#         places_review.COMMENTS[i] = "'"+places_review.COMMENTS+"'"
def append_quotation(x):
    if str(x).find(",") == -1:
        return "'"+str(x)+"'"
    else:
        return str(x)

# places_review.COMMENTS = "'"+places_review.COMMENTS+"'"
# print(places_review.COMMENTS.str.contains("'"))
places_review.COMMENTS = places_review.COMMENTS.apply(append_quotation).apply(lambda x:x.replace('"', ""))
print(places_review.COMMENTS.head(10))

place.NAME = place.NAME.apply(append_quotation).apply(lambda x:x.replace('"', ""))
print(place.head())
print(len(places_review))
print(len(place))
# place.to_csv('place_revision.csv', index=False, sep='\t')
# places_review.to_csv('place_review_revision.csv', index=False, sep='\t')
'''
place_path = './place_sql.txt'
review_path = './review_sql.txt'
with open(place_path) as f:
    place = f.read()
with open(review_path) as f:
    review = f.read()
place.replace('"', "'")
print(place)
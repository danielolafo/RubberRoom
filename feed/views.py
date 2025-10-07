import json
import logging

from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rubberroom.models import *
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rubberroom.mappers import *

# Create your views here.


def create_feed(request, user_id):
    print('User id ',user_id)
    resp= find_similarities(user_id)
    return HttpResponse(resp,content_type='application/json', status=200)

def find_similarities(user_id):

    """
    Uses cosine simmilarity to choose the best publications to suggest to the user
    """

    #Get all the allocation_site data that an user hasn't interacted with.
    data = AllocationSite.objects.raw(
        "SELECT als.id, als.address, als.city, t.id, t.description FROM allocation_site als "
        "JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id "
        "JOIN tag t ON ast.tag_id = t.id "
        "JOIN user_interactions ui ON activity_id=als.id AND activity_entity='allocation_site' "
        "WHERE ui.user_id<>%(user_id)s ORDER BY RANDOM() LIMIT 10",{'user_id':user_id})
    data = [d.__dict__ for d in data]
    data_list = list(data)
    data_df = pd.DataFrame(data_list)

    user_viewed_tags = UserTags.objects.raw(""
                                            "SELECT t.id, t.description FROM allocation_site als "
                                            "JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id "
                                            "JOIN tag t ON ast.tag_id = t.id "
                                            "JOIN user_interactions ui ON activity_id=als.id AND activity_entity='allocation_site' "
                                            "WHERE ui.user_id=%(user_id)s ORDER BY RANDOM() LIMIT 10",{'user_id':user_id})
    user_viewed_tags=[vt.description for vt in user_viewed_tags]
    user_tags = UserTags.objects.raw("SELECT t.id, t.description FROM user_tags ut "
                                     "JOIN tag t ON ut.tag_id=t.id WHERE ut.user_id=%(user_id)s",{'user_id':user_id})
    #All the tags descriptions related to an allocation_site joined in one single list
    grouped_tags = group_by_id(data_df)

    #Remove duplicated allocation_site_ids
    tmp_data_list = []
    for data in data_list:
        if len([d for d in tmp_data_list if d['id']==data['id']])==0:
            data['description']=" ".join(grouped_tags.get(data['id']))
            tmp_data_list.append(data)
    data_df=pd.DataFrame(tmp_data_list)

    # 2. Create TF-IDF Vectorizer for genres
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(data_df['description'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    recommendations = get_recommendations(user_viewed_tags, cosine_sim, data_df)
    resp=[allo for allo in data_list if allo['id'] in recommendations.to_dict().values()]
    resp_recommendations = []

    #Filter and delete duplicated allocations after applied get_recommendations()
    for i in resp:
        if len([r for r in resp_recommendations if r['id']==i['id']])==0:
            resp_recommendations.append(i)

    serializer = AllocationSerializer(resp_recommendations, many=True)
    return HttpResponse(json.dumps(serializer.data, default=vars), content_type='application/json',
                        status=200)

def get_recommendations(user_tags, cosine_sim_matrix, df):
    try:
        indexes = df[df['description'].isin(user_tags)].index
        # Get the index of the movie that matches the title
        # idx = df[df['description'] == title].index[0]

        movie_indices = []
        for ind in indexes:
            # Get the pairwise similarity scores of all movies with that movie
            sim_scores = list(enumerate(cosine_sim_matrix[ind]))

            # Sort the movies based on the similarity scores
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            sim_scores = [i[1] for i in sim_scores]
            sim_scores = list(enumerate(sim_scores))
            # Get the scores of the 5 most similar movies (excluding itself)
            sim_scores = sim_scores[1:6]

            # Get the movie indices
            movie_indices.extend([i[0] for i in sim_scores])

        # Return the top 5 most similar movie titles
        logging.info("get_recommendations - Response: ")
        logging.info(df['id'].iloc[movie_indices])
        return df['id'].iloc[movie_indices]
    except Exception as ex:
        return []

def group_by_id(data_frame):
    print("group_by_id***")
    print("data_frame ", data_frame)
    formated_data = {}
    for idx, d in data_frame.iterrows():
        print("d ",d)
        if formated_data.get(d['id']) is None:#formated_data[d['id']] is None:
            formated_data[d['id']] = []
        if d['description'] not in formated_data.get(d['id']):
            formated_data[d['id']].append(d['description'])
    logging.info("group_by_id Response: ", formated_data)
    return formated_data
import json

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

    #data = AllocationSite.objects.raw("SELECT als.id as site_id, t.id tag_id, t.description tag_name FROM allocation_site als JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id JOIN tag t ON ast.tag_id = t.id")
    #data = AllocationSite.objects.raw(
    #    "SELECT als.id, als.address FROM allocation_site als JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id JOIN tag t ON ast.tag_id = t.id")
    #data = AllocationSite.objects.all().values('id', 'address', 'owner')
    #data = AllocationSite.objects.raw("SELECT * FROM allocation_site als JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id JOIN tag t ON ast.tag_id = t.id")
    data = AllocationSite.objects.raw(
        "SELECT * FROM allocation_site als "
        "JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id "
        "JOIN tag t ON ast.tag_id = t.id "
        "JOIN user_interaction ui ON activity_id=als.id AND activity_entity='allocation_site' "
        "WHERE ui.user_id<>%(user_id)s ",{'user_id':user_id})
    data = [d.__dict__ for d in data]
    data_list = list(data)
    data_df = pd.DataFrame(data_list)

    # 2. Create TF-IDF Vectorizer for genres
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(data_df['description'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    recommendations = get_recommendations('Food', cosine_sim, data_df)
    resp=[allo for allo in data_list if allo['id'] in recommendations.to_dict().values()]
    resp_recommendations = []

    #Filter and delete duplicated allocations after applied get_recommendations()
    for i in resp:
        if len([r for r in resp_recommendations if r['id']==i['id']])==0:
            resp_recommendations.append(i)

    serializer = AllocationSerializer(resp_recommendations, many=True)
    return HttpResponse(json.dumps(serializer.data, default=vars), content_type='application/json',
                        status=200)

def get_recommendations(title, cosine_sim_matrix, df):
    # Get the index of the movie that matches the title
    idx = df[df['description'] == title].index[0]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim_matrix[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 5 most similar movies (excluding itself)
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 5 most similar movie titles
    #return df['address'].iloc[movie_indices]
    return df['id'].iloc[movie_indices]
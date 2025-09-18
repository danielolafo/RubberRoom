from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rubberroom.models import *

# Create your views here.


def create_feed(request, user_id):
    print('User id ',user_id)
    return HttpResponse(content_type='application/json', status=200)

def find_similarities(user_id):
    User.objects.raw("SELECT t.name, c.name FROM allocation_site als "
                     "JOIN category_priority cp ON als.id = cp.allocation_site_id "
                     "JOIN allocation_site_tag ast ON als.id = ast.allocation_site_id "
                     "JOIN category c ON cp.category_id = c.id "
                     "JOIN tag t ON ast.tag_id = t.id ")

    AllocationSiteTags.objects.raw("SELECT als.id as site_id, t.id tag_id, t.description tag_name FROM allocation_site als JOIN allocation_site_tag ast ON als.id=ast.allocation_site_id JOIN tag t ON ast.tag_id = t.id")
    pass

def get_recommendations(title, cosine_sim_matrix, df):
    # Get the index of the movie that matches the title
    idx = df[df['title'] == title].index[0]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim_matrix[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 5 most similar movies (excluding itself)
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 5 most similar movie titles
    return df['title'].iloc[movie_indices]
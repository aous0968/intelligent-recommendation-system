from django.shortcuts import render , get_object_or_404

from recommender.models import User , Rating , Behavior
from recommender.genetic_algorithm import GeneticRecommender

def home(request):
    # small sample for UI
    sample_users = User.objects.all()[:20]

    return render(request, "home.html", {
        "sample_users": sample_users,
        "total_users": User.objects.count()
    })


def all_users(request):
    users = User.objects.all()  # full 1000 users

    return render(request, "all_users.html", {
        "users": users,
        "total": users.count()
    })


def recommend(request, user_id):

    user = User.objects.get(user_id=user_id)

    ai = GeneticRecommender(user)
    products = ai.evolve()

    # USER FULL CONTEXT
    ratings = Rating.objects.filter(user=user)
    behaviors = Behavior.objects.filter(user=user)

    # prepare products
    results = []
    for p in products:
        results.append({
            "id": p.product_id,
            "category": p.category,
            "price": p.price
        })

    return render(request, "recommendations.html", {
        "user": user,
        "products": results,
        "ratings": ratings,
        "behaviors": behaviors
    })




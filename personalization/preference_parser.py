def parse_preferences(preferences):
    user_query = f"""
        I am looking for a {preferences['house_size']} home in a {preferences['location']} 
        area with a budget of {preferences['budget']}. I want features like {preferences['top_features']}
        and amenities such as {preferences['desired_amenities']}.
    """
    return user_query
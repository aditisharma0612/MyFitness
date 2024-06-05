import random

# Goal Setting
R_REALISTIC_GOALS = ("Realistic fitness goals vary from person to person, but examples include aiming to lose 1-2 "
                     "pounds per week, increasing strength by a certain percentage, or completing a specific distance "
                     "in a cardio activity. It's crucial to set achievable goals that align with your fitness level "
                     "and lifestyle.")

R_LOSS_WEIGHT = ("Achieving weight loss involves maintaining a healthy, balanced diet, engaging in regular physical activity, and adopting sustainable lifestyle changes.")

R_MAINTIAN_WEIGHT = ("Maintaining weight involves maintaining a consistent balance of healthy eating and regular exercise.")

R_GAIN_WEIGHT = ("Gaining weight requires creating a calorie surplus through the consumption of nutritious foods and incorporating strength training into your fitness routine.")

R_WARM_UP = ("The ideal warm-up duration varies depending on the activity but generally lasts around 5-10 minutes.")

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response

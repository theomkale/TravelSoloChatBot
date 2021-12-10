from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Init
bot = ChatBot('Buddy', read_only=True, logic_adapters=[
    {
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'I am sorry, I do not understand. I am still learning. Please contact my developer Om for further assitance.',
        'maximum_similarity_threshold': 0.10
    }
], )

# Training it on list of conversations̵̵
# trainer = ListTrainer(bot)
# trainer.train([
#     "Hi, can I help you",
#     "Who are you?",
#     "I am bot from Travel Solo app",
#     "Where do you operate?",
#     "We operate in India",
#     "What payment methods do you accept?",
#     "We accept payments through PhonePe, Google Pay and UPI",
#     "I would like to speak to your customer service agent",
#     "You can contact our support team on travelsoloapp@gmail.com",
#     "Which place should I travel to?",
#     "You can go to any place using Travel Solo App",
#     "Who made you?",
#     "I was made by Om, he created me while building Travel Solo App",
#     "Why should I travel solo?",
#     "You should travel solo to discover yourself",
# ])
# trainer.train([
#     "What payment methods do you offer?",
#     "We accept payments through PhonePe, Google Pay and UPI",
#     "How to contact customer service agent",
#     "You can contact our support team on travelsoloapp@gmail.com",
#     "Which is the best place to travel?",
#     "There is no best place to travel, its our memories that matter",
#     "What plans do you offer",
#     "We have regular and pro plan",
#
# ])


response = bot.get_response('where should i')
print(response)

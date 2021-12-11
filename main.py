from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, request

# Init
bot = ChatBot('Om\'s Bot',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database_uri='sqlite:///database.sqlite3_eng',
              read_only=True, logic_adapters=[
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


# Flask API
app = Flask(__name__)


@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get('msg')
    print(bot.get_response(user_input))
    return {
               "answer": str(bot.get_response(user_input)),
               "status": "success",
           }, 200


if __name__ == "__main__":
    app.run(debug=True)

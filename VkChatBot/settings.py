"""
Bot's behaviour
"""

INTENTS = [
    {
        'name': 'Date',
        'tokens': ('when', 'time', 'date', 'at', '1'),  # You can add any key words in the list
        'scenario': None,
        'answer': 'The conference is being held on May 10, registration will start at 11 am.'
    },
    {
        'name': 'Place',
        'tokens': ('where', 'place', 'location', 'address', 'station', '2', ),  # You can add any key words in the list
        'scenario': None,
        'answer': 'The conference will be held at the Centre of the City.'
    },
    {
        'name': 'Registration',
        'tokens': ('reg', 'add', '3', ),  # You can add any key words in the list
        'scenario': 'registration',
        'answer': None
    },
    {
        'name': 'Greetings',
        'tokens': ('thx', 'thank', '4', ),  # You can add any key words in the list
        'scenario': None,
        'answer': 'You are welcome!'
    },

]

SCENARIOS = {
    'registration': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Write your name to register. It will be shown on your badge',
                'failure_text': 'Name must contain at least 2 symbols. Try one more time',
                'handler': 'handle_name',
                'next_step': 'step2',
            },
            'step2': {
                'text': 'Send your e-mail, we will send all the required information to this address.',
                'failure_text': 'There is a typo in you email. Try one more time',
                'handler': 'handle_email',
                'next_step': 'step3',
            },
            'step3': {
                'text': 'Thanks for your time, {name}! Your ticket is below, also, we sent the ticket to your {email}, print it',
                'image': 'generate_ticket_handler',
                'failure_text': None,
                'handler': None,
                'next_step': None,
            },
        }
    }
}

DEFAULT_ANSWER = 'IDK how to answer.' \
                 'But I know where the conference is held and I can send you all the information I know, just ask me'


DB_CONFIG = dict(
    provider='postgres',
    user='postgres',
    password='',
    host='localhost',
    database='chatbot'
)
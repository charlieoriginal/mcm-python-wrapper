# Import requests
import requests
from requests import get as requests_get, post as requests_post

# Create a class for an mcmarket user with the following values:
# memberid: int
# username: str
# join_date: unsigned int
# last_activity_date: optional unsigned int
# banned: boolean
# suspended: boolean
# restricted: boolean
# disabled: boolean
# premium: boolean
# supreme: boolean
# ultimate: boolean
# discord_id: optional unsigned int
# avatar_url: str
# post_count: unsigned int
# resource_count: unsigned int

class Member:
    def __init__(self, username, memberid, join_date, last_activity_date, banned, suspended, restricted, disabled, premium, supreme, ultimate, discord_id, avatar_url, post_count, resource_count, purchase_count, feedback_positive, feedback_neutral, feedback_negative):
        self.username = username
        self.memberid = memberid
        self.join_date = join_date
        self.last_activity_date = last_activity_date
        self.banned = banned
        self.suspended = suspended
        self.restricted = restricted
        self.disabled = disabled
        self.premium = premium
        self.supreme = supreme
        self.ultimate = ultimate
        self.discord_id = discord_id
        self.avatar_url = avatar_url
        self.post_count = post_count
        self.resource_count = resource_count
        self.purchase_count = purchase_count
        self.feedback_positive = feedback_positive
        self.feedback_neutral = feedback_neutral
        self.feedback_negative = feedback_negative

class Alert:
    def __init__(self, caused_member_id, content_type, content_id, alert_type, alert_date):
        self.caused_member_id = caused_member_id
        self.content_type = content_type
        self.content_id = content_id
        self.alert_type = alert_type
        self.alert_date = alert_date

class Conversation:
    def __init__(self, conversation_id, title, creation_date, creator_id, last_message_date, last_read_date, open, reply_count, recipient_ids):
        self.conversation_id = conversation_id
        self.title = title
        self.creation_date = creation_date
        self.creator_id = creator_id
        self.last_message_date = last_message_date
        self.last_read_date = last_read_date
        self.open = open
        self.reply_count = reply_count
        self.recipient_ids = recipient_ids

class Reply:
    def __init__(self, message_id, message_date, author_id, message):
        self.message_id = message_id
        self.message_date = message_date
        self.author_id = author_id
        self.message = message

class Ban:
    def __init__(self, member_id, banned_by_id, ban_date, reason):
        self.member_id = member_id
        self.banned_by_id = banned_by_id
        self.ban_date = ban_date
        self.reason = reason

class ProfilePost:
    def __init__(self, profile_post_id, author_id, post_date, message, comment_count):
        self.profile_post_id = profile_post_id
        self.author_id = author_id
        self.post_date = post_date
        self.message = message
        self.comment_count = comment_count

class BasicResource:
    def __init__(self, resource_id, author_id, title, tag_line, price, currency):
        self.resource_id = resource_id
        self.author_id = author_id
        self.title = title
        self.tag_line = tag_line
        self.price = price
        self.currency = currency

class Resource:
    def __init__(self, resource_id, author_id, title, tag_line, description, release_date, last_update_date, category_title, current_version_id, price, currency, purchase_count, download_count, review_count, review_average):
        self.resource_id = resource_id
        self.author_id = author_id
        self.title = title
        self.tag_line = tag_line
        self.description = description
        self.release_date = release_date
        self.last_update_date = last_update_date
        self.category_title = category_title
        self.current_version_id = current_version_id
        self.price = price
        self.currency = currency
        self.purchase_count = purchase_count
        self.download_count = download_count
        self.review_count = review_count
        self.review_average = review_average

class Version:
    def __init__(self, version_id, update_id, name, release_date, download_count):
        self.version_id = version_id
        self.update_id = update_id
        self.name = name
        self.release_date = release_date
        self.download_count = download_count

class Update:
    def __init__(self, update_id, title, message, update_date):
        self.update_id = update_id
        self.title = title
        self.message = message
        self.update_date = update_date

class Review:
    def __init__(self, review_id, reviewer_id, review_date, rating, message, response):
        self.review_id = review_id
        self.reviewer_id = reviewer_id
        self.review_date = review_date
        self.rating = rating
        self.message = message
        self.response = response

class Purchase:
    def __init__(self, purchase_id, purchaser_id, license_id, renewal, status, price, currency, purchase_date, validation_date):
        self.purchase_id = purchase_id
        self.purchaser_id = purchaser_id
        self.license_id = license_id
        self.renewal = renewal
        self.status = status
        self.price = price
        self.currency = currency
        self.purchase_date = purchase_date
        self.validation_date = validation_date

class License:
    def __init__(self, license_id, purchaser_id, validated, active, permanent, start_date, end_date, previous_end_date):
        self.license_id = license_id
        self.purchaser_id = purchaser_id
        self.validated = validated
        self.active = active
        self.permanent = permanent
        self.start_date = start_date
        self.end_date = end_date
        self.previous_end_date = previous_end_date

class Download:
    def __init__(self, download_id, version_id, downloader_id, download_date):
        self.download_id = download_id
        self.version_id = version_id
        self.downloader_id = downloader_id
        self.download_date = download_date

class BasicThread:
    def __init__(self, thread_id, title, reply_count, view_count, creation_date, last_message_date):
        self.thread_id = thread_id
        self.title = title
        self.reply_count = reply_count
        self.view_count = view_count
        self.creation_date = creation_date
        self.last_message_date = last_message_date

class Thread:
    def __init__(self, thread_id, forum_name, title, reply_count, view_count, post_date, thread_type, thread_open, last_post_date):
        self.thread_id = thread_id
        self.forum_name = forum_name
        self.title = title
        self.reply_count = reply_count
        self.view_count = view_count
        self.post_date = post_date
        self.thread_type = thread_type
        self.thread_open = thread_open
        self.last_post_date = last_post_date

class Reply:
    def __init__(self, reply_id, author_id, post_date, message):
        self.reply_id = reply_id
        self.author_id = author_id
        self.post_date = post_date
        self.message = message

s = requests.Session()

# Checks the key type is a valid value of 'Private' or 'Shared'
def check_key_type(key_type):
    color_red = '\033[91m'
    color_end = '\033[0m'
    if key_type == 'Private' or key_type == 'Shared':
        return True
    else:
        print(color_red + 'Invalid key type. Please enter either "Private" or "Shared".' + color_end)
        return False

# Returns a boolean indicating whether the given string is a valid date.
def health_check(type, key):
    if (check_key_type(type) != True):
        return

    full_auth = type + ' ' + key
    s.headers.clear()
    s.headers.update({'Authorization': full_auth})
    s.params.clear()

    # Interact with a REST api url:
    # GET https://api.mc-market.org/v1/health
    # Set the 'Authorization' header to the value of 'full_auth'
    # Return the response
    response = s.get('https://api.mc-market.org/v1/health')

    red_color = '\033[91m'
    end_color = '\033[0m'

    # If the response status code is 200, return the response
    if response.status_code == 200:
        return True
    else:
        if 'error' in response.json():
            print(red_color + response.json()['error']['message'] + end_color)
        else:
            print(red_color + "Invalid server response code, check your connection or key." + end_color)

        return False

# Marks all current alerts as read.
def mark_alerts_as_read(type, key):
    if (check_key_type(type) != True):
        return

    full_auth = type + ' ' + key
    s.headers.clear()
    s.headers.update({'Authorization': full_auth})
    s.params.clear()
    s.params.update({'read': 'true'})

    # Interact with a REST api url:
    # GET https://api.mc-market.org/v1/alerts/read
    # Set the 'Authorization' header to the value of 'full_auth'
    # Return the response
    response = s.get('https://api.mc-market.org/v1/alerts')

    red_color = '\033[91m'
    end_color = '\033[0m'

    # If the response status code is 200, return the response
    if response.status_code == 200:
        return True
    else:
        if 'error' in response.json():
            print(red_color + response.json()['error']['message'] + end_color)
        else:
            print(red_color + "Invalid server response code, check your connection or key." + end_color)

        return False

# Starts a new conversation
def start_conversation(type, key, recipient_ids, title, message):
    if (check_key_type(type) != True):
        return

    full_auth = type + ' ' + key
    s.headers.clear()
    s.headers.update({'Authorization': full_auth})
    s.params.clear()
    s.params.update({'recipient_ids': recipient_ids, 'title': title, 'message': message})

    # Interact with a REST api url:
    # POST https://api.mc-market.org/v1/conversations
    # Set the 'Authorization' header to the value of 'full_auth'
    # Return the response
    response = s.post('https://api.mc-market.org/v1/conversations')
    red_color = '\033[91m'
    end_color = '\033[0m'

    # If the response status code is 200, return the response
    if response.status_code == 200:
        return True
    else:
        if 'error' in response.json():
            print(red_color + response.json()['error']['message'] + end_color)
        else:
            print(red_color + "Invalid server response code, check your connection or key." + end_color)

        return False

# Gets a list of replies from a conversation
def get_conversation_replies(type, key, conversation_id):
    if (check_key_type(type) != True):
        return

    full_auth = type + ' ' + key
    s.headers.clear()
    s.headers.update({'Authorization': full_auth})

    # Interact with a REST api url:
    # GET https://api.mc-market.org/v1/conversations/replies
    # Set the 'Authorization' header to the value of 'full_auth'
    # Return the response
    response = s.get('https://api.mc-market.org/v1/conversations/'+str(conversation_id)+'/replies')

    replies = []

    if 'error' in response.json():
        red_color = '\033[91m'
        end_color = '\033[0m'
        print(red_color + response.json()['error']['message'] + end_color)
        return replies

    for reply in response.json()['data']:
        message_id = reply['id']
        message_date = reply['message_date']
        author_id = reply['author_id']
        message = reply['message']
        replies.append(Reply(message_id, author_id, message_date, message))

    return replies

# Lists all unread conversations
def unread_conversations(type, key):
    if (check_key_type(type) != True):
        return

    full_auth = type + ' ' + key
    s.headers.clear()
    s.headers.update({'Authorization': full_auth})

    # Interact with a REST api url:
    # GET https://api.mc-market.org/v1/conversations
    # Set the 'Authorization' header to the value of 'full_auth'
    # Return the response
    response = s.get('https://api.mc-market.org/v1/conversations')

    json = response.json()
    conversations = []

    if 'error' in response.json():
        red_color = '\033[91m'
        end_color = '\033[0m'
        print(red_color + response.json()['error']['message'] + end_color)
        return conversations

    for conversation in json['data']:
        creation_date = conversation['creation_date']
        creator_id = conversation['creator_id']
        title = conversation['title']
        reply_count = conversation['reply_count']
        last_message_date = conversation['last_message_date']
        last_read_date = conversation['last_read_date']

        conversations.append(Conversation(creation_date, creator_id, title, reply_count, last_message_date, last_read_date))

    # If the response status code is 200, return the response
    return conversations

# Returns a list of all unread alerts
def alerts(type, key):
    if (check_key_type(type) != True):
        return

    full_auth = type + ' ' + key
    s.headers.clear()
    s.headers.update({'Authorization': full_auth})

    # Interact with a REST api url:
    # GET https://api.mc-market.org/v1/alerts
    # Set the 'Authorization' header to the value of 'full_auth'
    # Return the response
    alerts = []

    response = s.get('https://api.mc-market.org/v1/alerts')

    if 'error' in response.json():
        red_color = '\033[91m'
        end_color = '\033[0m'
        print(red_color + response.json()['error']['message'] + end_color)
        return alerts

    for alert in response.json()['data']:
        caused_member_id = alert['caused_member_id']
        content_type = alert['content_type']
        content_id = alert['content_id']
        alert_type = alert['alert_type']
        alert_date = alert['alert_date']

        a = Alert(caused_member_id, content_type, content_id, alert_type, alert_date)
        alerts.append(a)

    # If the response status code is 200, return the response
    return alerts

def member_self(type, key):
    if (check_key_type(type) != True):
        return

    full_auth = type + ' ' + key
    s.headers.clear()
    s.headers.update({'Authorization': full_auth})

    # Interact with a REST api url:
    # GET https://api.mc-market.org/v1/members/self
    # Set the 'Authorization' header to the value of 'full_auth'
    # Return the response
    response = s.get('https://api.mc-market.org/v1/members/self')
    json = response.json()

    if 'error' in response.json():
        red_color = '\033[91m'
        end_color = '\033[0m'
        print(red_color + response.json()['error']['message'] + end_color)
        return Member("invalid", 0, 0, 0, False, False, False, False, False, False, False, 0, "invalid url", 0, 0, 0, 0, 0, 0)

    username = None
    memberid = None
    join_date = None
    last_activity_date = None
    banned = None
    suspended = None
    restricted = None
    disabled = None
    premium = None
    supreme = None
    ultimate = None
    discord_id = None
    avatar_url = None
    post_count = None
    resource_count = None
    purchase_count = None
    feedback_positive = None
    feedback_neutral = None
    feedback_negative = None

    # loop through all keys in the the 'data' key of the json response
    for key in json['data']:
        # parse json object from string key

        if key == 'username':
            username = json['data'][key]
        elif key == 'memberid':
            memberid = json['data'][key]
        elif key == 'join_date':
            join_date = json['data'][key]
        elif key == 'last_activity_date':
            last_activity_date = json['data'][key]
        elif key == 'banned':
            banned = json['data'][key]
        elif key == 'suspended':
            suspended = json['data'][key]
        elif key == 'restricted':
            restricted = json['data'][key]
        elif key == 'disabled':
            disabled = json['data'][key]
        elif key == 'premium':
            premium = json['data'][key]
        elif key == 'supreme':
            supreme = json['data'][key]
        elif key == 'ultimate':
            ultimate = json['data'][key]
        elif key == 'discord_id':
            discord_id = json['data'][key]
        elif key == 'avatar_url':
            avatar_url = json['data'][key]
        elif key == 'post_count':
            post_count = json['data'][key]
        elif key == 'resource_count':
            resource_count = json['data'][key]
        elif key == 'purchase_count':
            purchase_count = json['data'][key]
        elif key == 'feedback_positive':
            feedback_positive = json['data'][key]
        elif key == 'feedback_neutral':
            feedback_neutral = json['data'][key]
        elif key == 'feedback_negative':
            feedback_negative = json['data'][key]

    # If the response status code is 200, return the response
    # create a new member object
    member = Member(username, memberid, join_date, last_activity_date, banned, suspended, restricted, disabled,
                            premium, supreme, ultimate, discord_id, avatar_url, post_count, resource_count,
                            purchase_count, feedback_positive, feedback_neutral, feedback_negative)

    return member
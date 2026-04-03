import nltk
nltk.download('vader_lexicon',quiet=True)
nltk.download('punkt',quiet=True)

from nltk.chat.util import Chat
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Bot:
  def __init__(self,pairs):
    self.pairs = pairs
    self.chat = Chat(self.pairs)
    self.sentiment = SentimentIntensityAnalyzer()

  def chatfunction(self,text):
    responce = self.chat.respond(text)
    if responce:
      return responce
    else:
      return "I amn unable to proceed at this moment"

  def sentimentfunction(self,text):
    score = self.sentiment.polarity_scores(text)

    if score['compound'] >= 0.03:
      return "Statement is Positive"

    elif score['compound'] <= -0.03:
      return "Statement is Negative"

    else:
      return "Statement is Neutral"


pairs = [

    # Greetings (catch all hello/hi/hey)
    [r'(?i).*(hi|hello|hey|hola|assalam|alaikum|salam|good morning|good evening|good afternoon).*',
     ["Hello! Welcome to Foodie Street Restaurant Bot. How can I help you today?", "Hi there! Need menu, reservation, or order tracking?", "Hey! I'm your restaurant assistant. Ask me anything about our food or services."
    ]],

    # Bot introduction / purpose (what can you do?)
    [r'(?i).*(what can you do|what do you do|tell me about yourself|your purpose|help me with|about|yourself).*',
     ["I can help you with: 📍 Location & hours, 📲 Contact info, 🍕 Menu & prices, 🧵 Reservations, 🚚 Order tracking, 🎉 Private events, and more! Just ask.", "I'm your Restaurant Information Bot. I provide menus, reservation status, order tracking, offers, and answer any restaurant-related questions.", "You can ask me – 'What's on the menu?', 'Make a reservation', 'Track my order', 'Do you have vegan food?' – I'm here to help!"]],

    # Bot name / who are you?
    [r'(?i).*(who are you|your name|what is your name|bot name).*',
     ["I'm FoodieBot, your restaurant assistant at Foodie Street Restaurant.", "You can call me FoodieBot. I know everything about our restaurant – ask me!"]],

    # Opening hours
    [r'(?i).*(what are|when are|opening hours|open hours|operating hours|when do you open|when do you close|timings|time schedule).*',
     ["We are open Monday to Sunday, 8:00 AM to 11:00 PM.", "Our restaurant operates from 8 AM to 11 PM every day.", "Opening hours: 8 AM – 11 PM, including weekends.", "We never close for lunch – 8 AM to 11 PM daily."]],

    # Location / address
    [r'(?i).*(where are you|location|address|find you|directions|come to you|restaurant located).*',
     ["We are located at 123 Foodie Street, Downtown City.", "Our address: 123 Foodie Street, near Central Park.", "You can find us at 123 Foodie Street – just 5 mins from City Mall.", "Here’s our location: 123 Foodie Street, Downtown. Need GPS coordinates?"]],

    # Contact number
    [r'(?i).*(phone number|contact number|call you|reach you|telephone|mobile number|whatsapp).*',
     ["You can reach us at +1 234 567 8900.", "Our phone number is +1 234 567 8900 – calls and WhatsApp.", "Call us at +1 234 567 8900 for any inquiries.", "For reservations or queries, dial +1 234 567 8900."]],

    # Menu
    [r'(?i).*(menu|what do you serve|dishes|food options|items|what food|what can i order|food menu).*',
     ["We serve Italian, Continental, and Fast food. Would you like to see our full menu?", "Our menu includes pizzas, pastas, burgers, salads, and desserts.", "Here’s the link to our menu: [link]. Or I can list categories.", "We have vegetarian, non-vegetarian, and vegan options on the menu."]],

    # Vegetarian options
    [r'(?i).*(vegetarian|veg food|pure veg|veg options|no meat).*',
     ["Yes, we have a wide vegetarian section – paneer dishes, veg pizzas, salads, and more.", "We offer 15+ vegetarian items including pastas and grilled veggies.", "Of course! Many vegetarian options are available. Would you like recommendations?"]],

    # Vegan options
    [r'(?i).*(vegan|dairy free|no cheese|plant based).*',
     ["We have vegan salads, vegetable stir-fry, and vegan pasta upon request.", "Yes, we offer vegan options like tofu bowl and vegan burger.", "Our vegan menu includes dairy-free desserts too. Let me know if you need details."]],

    # Gluten free
    [r'(?i).*(gluten free|celiac|no gluten|gf).*',
     ["We offer gluten-free pizza bases and gluten-free pasta.", "Yes, we have gluten-free options for most main courses. Please inform our staff.", "Gluten-free bread is also available on request."]],

    # Prices / cost
    [r'(?i).*(price|cost|how much|expensive|cheap|affordable|rate).*',
     ["Our average cost for two people is $30–$45.", "Main courses range from $12 to $25. Appetizers $5–$12.", "You can check prices on our online menu. Generally, budget friendly for families."]],

    # Reservations
    [r'(?i).*(reservation|book a table|reserve|booking|table for|reserve a seat).*',
     ["Yes, we take reservations. How many people and for what time?", "You can reserve a table by calling us or using our website.", "Would you like to make a reservation now? I can check availability."]],

    # Reservation status
    [r'(?i).*(check my reservation|reservation status|confirm booking|is my booking confirmed).*',
     ["Please provide your booking name or phone number to check status.", "I can check your reservation status. What’s the name under which you booked?", "Your reservation is confirmed if you received an SMS/email. Let me verify for you."]],

    # Cancel reservation
    [r'(?i).*(cancel reservation|cancel booking|remove my booking).*',
     ["You can cancel your reservation up to 1 hour before the time without charge.", "Please call us at +1 234 567 8900 to cancel, or reply with your booking ID.", "I can help cancel your reservation. Please share your name and booking time."]],

    # Waiting time / walk-in
    [r'(?i).*(wait time|how long to wait|peak hours|busy now|walk in).*',
     ["Currently wait time is 15–20 minutes for walk-ins.", "On weekends, wait time can be 30–40 minutes during 7–9 PM.", "You can avoid waiting by making a reservation. Right now it’s not too busy."]],

    # Order tracking
    [r'(?i).*(track my order|order status|where is my order|delivery status).*',
     ["Please provide your order ID or phone number to track your order.", "Your order is being prepared. I’ll update you once it’s out for delivery.", "For delivery orders, check the link sent via SMS. Need help? Share your order number."]],

    # Delivery available?
    [r'(?i).*(delivery|do you deliver|home delivery|deliver to my home).*',
     ["Yes, we deliver within a 5 km radius via our own delivery team.", "We are on UberEats, DoorDash, and our own website for delivery.", "Delivery minimum order is $10. Free delivery on orders above $25."]],

    # Takeaway / pickup
    [r'(?i).*(takeaway|take out|pickup|collect order).*',
     ["Yes, takeaway is available. Order online and pick up at the counter.", "You can place a takeaway order by phone or at the restaurant directly.", "Takeaway orders usually ready in 15–20 minutes."]],

    # Special offers / discounts
    [r'(?i).*(offer|discount|deal|combo|promo|happy hour).*',
     ["We have a happy hour 4–6 PM: 20% off on drinks.", "Today’s combo: Burger + Fries + Drink for $12.", "Follow us on Instagram for weekend promo codes."]],

    # Kids menu
    [r'(?i).*(kids menu|children|for kids|child friendly).*',
     ["Yes, we have a kids menu with smaller portions – nuggets, pasta, and juice.", "Kids eat free on Tuesdays with every adult meal.", "High chairs and a kids play area available."]],

    # Private events / party (this is your example fixed)
    [r'(?i).*(private event|birthday|party|celebration|corporate event).*',
     ["We have a private dining area for up to 30 people. Perfect for birthdays and corporate events.", "Yes, we host parties. Minimum spend $200 for private room.", "We can arrange custom menus for your celebration. Call us for details."]],

    # Parking availability
    [r'(?i).*(parking|car park|valet|parking available|where to park).*',
     ["We have free parking for customers behind the building.", "Valet parking available Friday and Saturday nights.", "Street parking is also available right outside the restaurant."]],

    # WiFi
    [r'(?i).*(wifi|wireless internet|free wifi|internet).*',
     ["Yes, free WiFi is available. Password is 'foodie123'.", "We provide complimentary WiFi for all guests. Ask server for password."]],

    # Payment methods
    [r'(?i).*(payment|credit card|cash|debit card|apple pay|google pay|pay online).*',
     ["We accept cash, all major credit cards, Apple Pay, and Google Pay.", "Yes, you can pay online or at the counter. No checks please."]],

    # Dress code
    [r'(?i).*(dress code|what to wear|formal| casual|attire).*',
     ["No strict dress code. Casual wear is fine.", "For dinner after 7 PM, smart casual is preferred."]],

    # Outdoor seating
    [r'(?i).*(outdoor seating|patio|open air|al fresco|terrace).*',
     ["Yes, we have a beautiful outdoor patio with 10 tables.", "Outdoor seating is first come, first served."]],

    # Smoking area
    [r'(?i).*(smoking|smoking area|smoking allowed|cigarette).*',
     ["Smoking is allowed only in the designated outdoor area.", "No indoor smoking. We have a smoking zone in the garden."]],

    # Pet friendly
    [r'(?i).*(pet friendly|dogs allowed|pets|animal).*',
     ["Yes, we are pet friendly on the outdoor patio.", "Only service animals allowed indoors. Pets okay outside."]],

    # Buffet available?
    [r'(?i).*(buffet|buffet system|buffet available|unlimited food).*',
     ["We have a lunch buffet on weekdays from 12 PM to 3 PM – $15 per person.", "No dinner buffet, but we have family-style platters."]],

    # Chef special / signature dish
    [r'(?i).*(chef special|signature dish|must try|famous dish).*',
     ["Our signature dish is the Truffle Pasta and Wood-fired Pizza.", "Chef’s special today is Grilled Salmon with lemon butter sauce."]],

    # Allergies / special requests
    [r'(?i).*(allergy|allergic|nut allergy|seafood allergy|customize).*',
     ["Please inform your server about any allergies. We can modify most dishes.", "We cannot guarantee zero cross-contamination but will try our best."]],

    # Group booking / large party
    [r'(?i).*(group booking|large party|10 people|20 people|big group).*',
     ["For groups larger than 8 people, please call us directly.", "We can accommodate up to 50 people in the main hall."]],

    # Opening special days (holidays)
    [r'(?i).*(new year|christmas|thanksgiving|eid|diwali|holiday).*',
     ["We are open on all holidays except Christmas Day.", "Special holiday menus available – check our website."]],

    # Online ordering link
    [r'(?i).*(order online|online ordering|website to order|app).*',
     ["You can order online from our website: www.foodiestreet.com/order", "We also have a mobile app for iOS and Android."]],

    # Cancel order (delivery/takeaway)
    [r'(?i).*(cancel my order|change order|modify order).*',
     ["Orders can be canceled within 5 minutes of placing. Please call us immediately.", "Once the food is prepared, we cannot cancel. But you can request a refund if quality issue."]],

    # Estimated delivery time
    [r'(?i).*(delivery time|how long for delivery|when will i get).*',
     ["Delivery usually takes 30–45 minutes depending on your location.", "In peak hours, it may take up to 1 hour."]],

    # Minimum order for delivery
    [r'(?i).*(minimum order|min order).*',
     ["Minimum delivery order is $10.", "No minimum for pickup."]],

    # Loyalty program / membership
    [r'(?i).*(loyalty program|membership|rewards|points).*',
     ["Yes, we have a loyalty card. Get 1 point per $1 spent. 100 points = $5 off.", "Sign up on our website to get a free drink on your birthday."]],

    # Alcohol served?
    [r'(?i).*(alcohol|beer|wine|cocktails|liquor|drinks).*',
     ["We serve beer, wine, and signature cocktails. Must be 21+ with ID.", "Happy hour on drinks 4–6 PM."]],

    # Non-alcoholic drinks
    [r'(?i).*(soft drinks|mocktails|juice|soda|non alcoholic).*',
     ["We have fresh juices, mocktails, sodas, and milkshakes.", "Try our mango mocktail – very popular."]],

    # Reservation deposit
    [r'(?i).*(deposit|advance payment|booking fee).*',
     ["No deposit required for regular reservations.", "For large groups (10+), we ask $5 per person as advance."]],

    # Noise level / family friendly
    [r'(?i).*(noise level|loud|quiet|family friendly).*',
     ["We are family friendly. Evenings can be lively but not too loud.", "Private dining room is quieter for meetings."]],

    # Wheelchair access
    [r'(?i).*(wheelchair|disabled access|handicap).*',
     ["Yes, we have wheelchair accessible entrance and restrooms.", "Ramp available at the side entrance."]],

    # Opening soon / closing soon
    [r'(?i).*(are you open now|still open|open currently).*',
     ["Yes, we are open right now until 11 PM.", "We close in 1 hour. Last order at 10:30 PM."]],

    # Today's special / daily special
    [r'(?i).*(today special|daily special|special today).*',
     ["Today’s special: Grilled Fish with roasted vegetables – $15.", "Soup of the day is Tomato Basil."]],

    # Refund policy
    [r'(?i).*(refund|money back|complaint|not happy).*',
     ["If you are unsatisfied, please inform us immediately. We offer replacement or refund.", "For delivery issues, contact us within 30 minutes."]],

    # Staff / manager
    [r'(?i).*(call manager|speak to manager|complaint to manager).*',
     ["I can connect you to the manager. Please hold.", "Manager is available from 10 AM to 8 PM daily."]],

    # Reservations for tomorrow
    [r'(?i).*(tomorrow reservation|book for tomorrow).*',
     ["Yes, we have availability tomorrow. What time would you prefer?", "Tomorrow evening is busy but we still have slots at 6 PM and 9 PM."]],

    # Weekend reservation
    [r'(?i).*(weekend reservation|saturday|sunday booking).*',
     ["Weekends fill up fast. I recommend booking 2 days in advance.", "Saturday after 7 PM is fully booked. Other times available."]],

    # Table type (booth, window, high chair)
    [r'(?i).*(window table|booth|high chair|corner table).*',
     ["You can request a window or booth table. We will try to accommodate.", "High chairs are available for toddlers."]],

    # Music / live music
    [r'(?i).*(live music|band|piano|jazz).*',
     ["We have live acoustic music every Friday 7–9 PM.", "Background instrumental music on other days."]],

    # Air conditioned
    [r'(?i).*(ac|air conditioned|air con|cool).*',
     ["Yes, full air conditioning indoors.", "Outdoor seating has fans and misters."]],

    # Birthday freebies
    [r'(?i).*(birthday free|free dessert birthday|birthday offer).*',
     ["Show your ID on your birthday and get a free dessert.", "For group birthday bookings, we give a complimentary cake."]],

    # Leftover / take home
    [r'(?i).*(leftover|pack food|take home).*',
     ["Yes, we provide takeout boxes for leftovers at no extra cost.", "Just ask your server for a box."]],

    # Water (tap or bottled)
    [r'(?i).*(water|tap water|bottled water|free water).*',
     ["We serve complimentary tap water. Bottled water is $1.", "Sparkling water is also available for $2."]],

    # Waiting list
    [r'(?i).*(waiting list|put me on list).*',
     ["We can add you to the waiting list. What’s your name and phone number?", "Waiting list is currently 4 parties ahead."]],

    # Bill / check / split bill
    [r'(?i).*(bill|check|split bill|pay bill).*',
     ["Your bill will be brought to your table. We can split by item or equally.", "We accept split payments up to 4 cards."]],

    # Service charge / tip
    [r'(?i).*(service charge|tip|gratuity).*',
     ["10% service charge is included for parties of 6 or more.", "Tips are optional but appreciated."]],

    # Closing time warning
    [r'(?i).*(last order|closing soon|last call).*',
     ["Last order is at 10:30 PM. Kitchen closes at 10:45 PM.", "We will remind you 15 minutes before closing."]],

    # Thank you / goodbye
    [r'(?i).*(thank you|thanks|thanku|thx|goodbye|bye|see you|take care).*',
     ["You're welcome! Enjoy your meal. Visit us again soon!", "Happy to help! Have a great day. 😊", "Goodbye! For quick orders, just say 'Menu' anytime."]],

]

new_pairs = [
    
    [r'(?i).*(track|order status|where is my order).*\b(\d+)\b.*',
     ["Thanks! Order #\\2 is being prepared. It will be ready in about 15 minutes.",
      "I see order #\\2 – it's out for delivery. ETA 20 minutes.",
      "Order #\\2 is confirmed. You'll get an SMS when it's ready."]],

    
    [r'(?i)^\s*(\d+)\s*$',
     ["Is that your order number? Let me check... Order #\\1 is in the kitchen.",
      "Got it. Order #\\1 is being packed. Almost ready!"]],

    
    [r'(?i).*(\d+).*(order number|order id|track).*',
     ["Tracking order #\\1 – it's being prepared. ETA 20 min.",
      "Order #\\1 confirmed. We'll notify you when ready."]],

    
    [r'(?i).*(am i saying|did i say|was that).*(hi|hello|hey).*',
     ["You just said hello! How can I help you today?",
      "That was a greeting. Feel free to ask me about the restaurant."]],

    [r'(?i)^\d+$',  # only digits
     ["I see you sent a number. Are you trying to track an order? If yes, please say 'track my order' first.",
      "Is this your order number? Please tell me 'track my order' followed by the number."]],
]

pairs.extend(new_pairs)

if __name__ == "__main__":
    chatbot = Bot(pairs)
    print(chatbot.chatfunction("what about gluten free?"))


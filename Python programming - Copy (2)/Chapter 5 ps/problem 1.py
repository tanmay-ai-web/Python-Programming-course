# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

Dictionary = {
    "पुस्तक": "book",
    "किताब": "book",
    "पानी": "water",
    "खाना": "food",
    "लड़का": "boy",
    "लड़की": "girl",
    "स्कूल": "school",
    "घर": "home",
    "सड़क": "road",
    "पेड़": "tree",
    "पंखा": "fan",
    "दरवाज़ा": "door",
    "खिड़की": "window",
    "कुर्सी": "chair",
    "मेज़": "table",
    "आसमान": "sky",
    "सूरज": "sun",
    "चाँद": "moon",
    "तारा": "star",
    "समय": "time",
    "दोस्त": "friend",
    "परिवार": "family",
    "प्यार": "love",
    "शांत": "calm",
    "तेज़": "fast",
    "धीमा": "slow",
    "अच्छा": "good",
    "बुरा": "bad"
} 

# Welcome message
print("हिंदी-अंग्रेज़ी शब्दकोश में आपका स्वागत है!")
print("कोई भी हिंदी शब्द दर्ज करें (या 'exit' लिखें बंद करने के लिए)।")

# Lookup loop
while True:
    word = input("\nहिंदी शब्द दर्ज करें: ")

    if word.lower() == 'exit':
        print("धन्यवाद! शब्दकोश बंद किया जा रहा है।")
        break

    # Lookup and output
    translation = Dictionary.get(word)
    if translation:
        print(f"अंग्रेज़ी में: {translation}")
    else:
        print("क्षमा करें, यह शब्द शब्दकोश में नहीं है।")


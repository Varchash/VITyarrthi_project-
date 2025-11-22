import time
import random

def when_bath():
    print(" ==== Shower time, Whenn 😱😱 ==== ")
    Job = input("Enter your work (Prof / Engg / Doc / MBA / Civil / Arts): ").strip().lower()
    Gender = input("Enter your pronouns (He / She): ").strip().lower()
    
    print('\n[!] calculating your perfect shower time ....')
    time.sleep(2)

    For_prof = [
        "Advice: Use the tears of failed students to scrub your back. It exfoliates.",
        "Advice: You have been wearing that same blazer since 1998. Why start cleaning now?",
        "Advice: Attendance for the soap is mandatory. 75Percent required.",
    ]
    For_engg = [
        "Advice: Don't shower. Your code is compiling. If you leave, it will error out.",
        "Advice: Use dry shampoo. Water is a conductant and you are basically a robot.",
        "Advice: Only shower if your laptop fan starts inhaling your scent.",
        "Advice: ERROR 404 - HYGIENE NOT FOUND. Please reboot your life.",
        "Advice: You don't need a shower. You need to debug your armpits.",
        "Advice: If you shower, the water might short-circuit your neural link to Stack Overflow.",
        "Advice: Showering is O(n^2) complexity. Just use deodorant, it's O(!1).",
        "Advice: You are a backend developer. No one looks at you. You are safe.",
        "Advice: Just sit in front of the server rack. The hot air will kill the bacteria.",
    ]
    For_doc = [
        "Advice: You have 5 minutes. Choose: Shower, Eat, or Sleep. (Hint: Choose Sleep).",
        "Advice: Just splash Betadine on your face. It's sterile.",
        "Advice: The hospital smell is now your DNA. Accept it.",
        "Advice: Hand sanitizer is technically a shower if you use enough of it.",
        "Advice: You have been awake for 48 hours. If you close your eyes to wash your face, you will fall into a coma.",
        "Advice: Shower? You mean crying under the scrub sink for 30 seconds?",
        "Advice: The scent of hospital disinfectant is basically Chanel No. 5 for you now.",
        "Advice: You save lives. You are allowed to smell like death.",
        "Advice: Just autoclave your clothes. The body is a lost cause.",
    ]
    For_mba = [
        "Advice: Delegate the shower to an intern.",
        "Advice: Showering lowers your Q3 productivity. Skip it.",
        "Advice: Only shower if you have a networking event with a VC.",
        "Advice: Let's 'Circle Back' to this shower idea in Q4.",
        "Advice: Outsourcing is key. Pay someone else to smell good for you.",
        "Advice: You only need to wash the parts visible on a Zoom call.",
        "Advice: Does this shower align with your personal brand synergy?",
        "Advice: Calculate the ROI of soap. If it's negative, skip it.",
        "Advice: Use words like 'Scalable' and 'Disruptive' to distract people from the smell.",
    ]
    For_civil = [
        "Advice: That's not dirt, that's a protective layer of cement.",
        "Advice: Wait for the rain. It is cost-effective.",
        "Advice: Use 80-grit sandpaper. Soap is too weak for you.",
        "Advice: Don't wash off the cement. It is holding your body together.",
        "Advice: You are structurally sound. Dirt adds tensile strength.",
        "Advice: Wait for the monsoon project. It's free.",
        "Advice: Use a sandblaster. Soap is for the weak.",
        "Advice: You wear a helmet all day. Your hair has formed a permanent protective shell.",
        "Advice: Just stand near the curing tank."

    ]
    For_arts = [
        "Advice: Dirt is just a social construct.",
        "Advice: Tell people your odor is 'Performance Art'.",
        "Advice: Showering stifles creativity. Embrace the funk.",
        "Advice: Your scent is your signature. Don't dilute it with soap.",
        "Advice: Use your natural musk to inspire your next masterpiece.",
        "Advice: Shower in organic, free-range rainwater only."
    ]
    for_boys = [
        "Note: Using the same towel for your face and feet is a biological hazard.",
        "Note: Axe Body Spray is NOT a shower replacement.",
        "Note: You have one bar of soap for hair, body, face, and car. Good luck.",
        "Warning: Using 12-in-1 Shampoo (Body/Face/Car/Dish/Dog) is illegal.",
        "Warning: Your towel is stiff enough to stand up on its own. Wash it.",
        "Warning: Putting on clean underwear does not count as a shower.",
        "Warning: Axe Body Spray is not a substitute for water, despite what the ads say."
    ]
    
    for_girls = [
        "Note: Please do not set the water temperature to 'Lava'.",
        "Note: 45 minutes is a shower, not a therapy session.",
        "Note: Hair wash day is tomorrow. You are safe for now.",
        "Warning: 'Hair Wash Day' calculation failed. Just wash it, you greaseball.",
        "Warning: Please do not set the water temperature to 'Volcano'. You have skin, not dragon scales.",
        "Warning: An 'Everything Shower' takes 3 business days. Do you have the time?",
        "Warning: You have 17 bottles in the shower. You use the same 2. Throw the others away.",
        "Warning: Sticking your hair to the shower wall to make 'art' is psychopathic behavior.",
        "Warning: You don't need to win a fake argument with your ex in the shower. Just scrub.",
        "Warning: If the mirror doesn't fog up in 5 seconds, the water is too cold for you.",
        "Warning: Dry shampoo is a temporary fix, not a lifestyle choice.",
        "Warning: No, you don't need a new exfoliant. You need water.",
        "Warning: 45 minutes is a shower, not a karaoke world tour."
    ]
    if 'prof' in Job or  'teach' in Job or 'treaching' in Job:
        selected_advice = random.choice(For_prof)
    elif 'engg' in Job or 'engineer' in Job or 'coding' in Job or 'tech' in Job or 'cs' in Job or 'developer' in Job or 'programmer' in Job :
        selected_advice = random.choice(For_engg)
    elif 'doc' in Job or 'med' in Job or 'doctor' in Job or 'hospital' in Job or 'nurse' in Job:
        selected_advice = random.choice(For_doc)
    elif 'mba' in Job or 'business' in Job or 'management' in Job:
        selected_advice = random.choice(For_mba)
    elif 'civil' in Job or 'construction' in Job or 'builder' in Job or 'majdur' in Job or 'Bihari' in Job:
        selected_advice = random.choice(For_civil)
    else:
        selected_advice = random.choice(For_arts)

    if 'she' in Gender or 'her' in Gender or 'hers' in Gender or 'she/her' in Gender:
        gen_advice = random.choice(for_girls)
    elif 'he' in Gender or 'him' in Gender or 'his' in Gender or 'he/him' in Gender:
        gen_advice = random.choice(for_boys)
    else:
        gen_advice = "PRONOUNS MATTER 🤦🤦 BUT,\nSHOWER WHENEVER YOU WANT! ,\nHIGH HAIL NO SHOWER"
    
    print("[!]doing deep analysis ....")
    time.sleep(1)
    print("[!]fine-tuning results ....")
    time.sleep(2)
    print("[!]almost Done.......")
    time.sleep(3)
    print("===== YOLO!! =====")
    print(f"Selected job: {Job.capitalize()}")
    print(f"{selected_advice}")
    print(f"Selected gender: {Gender.capitalize()}")
    print(f"{gen_advice}")
    print("="*9)

when_bath()
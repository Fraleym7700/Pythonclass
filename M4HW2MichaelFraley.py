class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "0) What is the Capital of North Carolina?\n(a)Raleigh\n(b)Fayetteville\n(c)Durham\n(d)Charlotte\n\n",
     "1) What is the Capital of South Carolina?\n(a)Charleston\n(b)Colombia\n(c)Myrtle Beach\n(d)Greenville\n\n",
     "2) What is the Capital of France?\n(a)Marseille\n(b)Lyon\n(c)Paris\n(d)Toulouse\n\n",
     "3) What is the Capital of Germany?\n(a)Hamburg\n(b)Munich\n(c)Frankfurt\n(d)Berlin\n\n",
     "4) What is the Capital of England?\n(a)Manchester\n(b)England\n(c)London\n(d)Liverpool\n\n",
     "5) What is the Capital of China?\n(a)Beijing\n(b)Shanghai\n(c)Hong Kong\n(d)Taipei\n\n",
     "6) What is the Capital of Japan?\n(a)Kyoto\n(b)Sapporo\n(c)Tokyo\n(d)Osaka\n\n",
     "7) What is the Capital of Australia?\n(a)Melbourne\n(b)Brisbane\n(c)Canberra\n(d)Perth\n\n",
     "8) What is the Capital of Colombia?\n(a)Cartegena\n(b)Medallin\n(c)Cali\n(d)Bogota\n\n",
     "9) What is the Capital of New York?\n(a)New York\n(b)Albany\n(c)Buffalo\n(d)Rochester\n\n",
     "10) What is the Capital of California?\n(a)Los Angelos\n(b)Sacremento\n(c)San Francisco\n(d)San Diego\n\n",
     "11) What is the Capital of Thailand?\n(a)Chiang Mai\n(b)Pattaya City\n(c)Bangkok\n(d)Phuket\n\n",
     "12) What is the Capital of Peru?\n(a)Callao District\n(b)Lima\n(c)Trujillo\n(d)Chiclayo\n\n",
     "13) What is the Capital of Iceland?\n(a)Reykjavik\n(b)Akureyri\n(c)Hafnarfjordur\n(d)Kopavogur\n\n",
     "14) What is the Capital of Brazil?\n(a)Rio de Janeiro\n(b)Sao Paulo\n(c)Belo Horizonte\n(d)Brasilia\n\n",
     "15) What is the Capital of India?\n(a)Mumbai\n(b)Bengaluru\n(c)New Delhi\n(d)Hyderabad\n\n",
     "16) What is the Capital of Poland?\n(a)Krakow\n(b)Warsaw\n(c)Wroclaw\n(d)Gdansk\n\n",
     "17) What is the Capital of Ohio?\n(a)Columbus\n(b)Cleveland\n(c)Cincinnati\n(d)Dayton\n\n",
     "18) What is the Capital of Egypt?\n(a)Alexandria\n(b)Luxor\n(c)Aswan\n(d)Cairo\n\n",
     "19) What is the Capital of Argentina?\n(a)Mendoza\n(b)Salta\n(c)Buenos Aires\n(d)Ushuaia\n\n",
     
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "c"),
     Question(question_prompts[3], "d"),
     Question(question_prompts[4], "c"),
     Question(question_prompts[5], "a"),
     Question(question_prompts[6], "c"),
     Question(question_prompts[7], "c"),
     Question(question_prompts[8], "d"),
     Question(question_prompts[9], "b"),
     Question(question_prompts[10], "b"),
     Question(question_prompts[11], "c"),
     Question(question_prompts[12], "b"),
     Question(question_prompts[13], "a"),
     Question(question_prompts[14], "d"),
     Question(question_prompts[15], "c"),
     Question(question_prompts[16], "b"),
     Question(question_prompts[17], "a"),
     Question(question_prompts[18], "d"),
     Question(question_prompts[19], "c"),
     
]

def runTheTest(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

runTheTest(questions)
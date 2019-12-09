from test_file.survey import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
print("Thank You")
my_survey.show_results()
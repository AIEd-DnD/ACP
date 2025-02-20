import base64
import helper_functions as ACP

user_message_bef_KB = """
<Context>You are an expert teacher creating lesson content and questions for students.
Important instructions will be denoted by // at the start of the instruction.
</Context>

<Objective>
//Your task is to create new components based on the Details of a reference Original Component, Section Tags, Additional Prompts and Knowledge Base, and then return the created components in the correct JSON format.
//There are only eight types of components: text, multipleChoiceQuestion, freeResponseQuestion, fillInTheBlankQuestion, errorEditingQuestion, poll, discussionQuestion and interactiveThinkingRoutineQuestion.
//You will first be provided a description of each type of component.
//You will next be provided a guide on how to interpret the provided Details.
//You will then be provided with a set of creation instructions to explain how to use the Details to create the desired components.
//Finally at the end, you will be provided with a set of instructions to explain how to output the final complete response in the correct JSON format.
</Objective>

<Component Description>
//<text> Text: A component of rich text that contains content relevant to the lesson content which may use text with HTML formatting tags, HTML tables, HTML ordered lists, HTML unordered lists and LaTeX mathematical expressions to explain the concepts or skills in the Learning Outcomes or Knowledge Base, or be a reproduction of the rich text found in the Knowledge Base. For each component, provide (i) the required text, which may include tables, ordered lists, unordered lists with the appropriate HTML tags or mathematical expressions written in LaTeX enclosed in a pair of double dollar symbols $$ </text>,
//<multipleChoiceQuestion> MCQ/MRQ: A multiple choice question with at least two options. For each multiple choice question, provide (i) the question, (ii) the correct options, (iii) feedback for why the correct answers answer the question, (iv) any remaining options are distractors which are incorrect answers, (v) feedback for each distractor explaining why the distractor is incorrect and what the correct answers should be, (vi) suggested time duration in seconds needed for a student to complete the question, (vii) total marks for the question </multipleChoiceQuestion>,
//<freeResponseQuestion> FRQ: A free response question which includes suggested answers. For each free response question, provide (i) the question, (ii) total marks for the question, which should be equal to the total number of creditworthy points in the suggested answer, (iii) suggested answer, which is a comprehensive list of creditworthy points that answers the question, where one point is to be awarded one mark and written in the following format: " (1 mark): Statement describing creditworthy idea 1.\n (1 mark): Statement describing creditworthy idea 2.\n" , and the total marks for the question should be equal to the number of creditworthy points in the suggested answer, (iv) suggested time duration in seconds needed for a student to complete the question </freeResponseQuestion>,
//<fillInTheBlankQuestion> FITB: A fill-in-the-blank question based on the learning outcomes where the blanks refer to key ideas, concepts or words for the learning outcomes. For each fill-in-the-blank question, provide (i) the question statement with blanks and the blanks must be labelled using square brackets containing a running number, such as [1], (ii) the accepted answer(s) for each blank, (iii) marks per blank, (iv) total marks for the question </fillInTheBlankQuestion>,
//<errorEditingQuestion> EE: An error editing question which comprises of multiple sentences, each of which may contain a factual or language error, related to the learning outcomes. For the error editing question, provide at least (i) eight sentences with errors, (ii) the erroneous word or words, (iii) the suggested word or words, (iv) two sentences without errors, (v) marks per sentence, (vi) total marks for the question </errorEditingQuestion>,
//<poll> Poll: A poll which is a multiple choice question with two or more options but no correct answer. For each poll, provide (i) a question, (ii) at least two options in response to the question</poll>,
//<discussionQuestion> Discussion: A discussion question which invites students to respond with their opinion. For each discussion question, provide (i) the discussion topic, (ii) a free response question for students to respond to </discussionQuestion>,
//<interactiveThinkingRoutineQuestion> ITT: An interactive thinking tool (ITT) has a set of categories. For each category, there is a specific question related to the learning outcome and the category. These are the various interactive thinking tools you may select: There are 8 tools. Tool 1 has the categories - See, Think, Wonder. Tool 2 has the categories - Think, Puzzle, Explore. Tool 3 has the categories - Know, Want to know, Learned. Tool 4 has the categories - Connect, Extend, Challenge. Tool 5 has the categories - I used to think..., But now I think... . Tool 6 has the categories - What's going on?, What do you see that makes you say that?. Tool 7 has the categories - Claim, Support, Question. Tool 8 has the categories - What can the person or thing perceive?, What might the person or thing know about or believe?, What might the person or thing care about?.. For the ITT, choose one interactive thinking tool to use, then state the category and provide a question for each category, related to the learning outcome. </interactiveThinkingRoutineQuestion>,
//Remember that any text output can be rich text and mathematical expressions MUST be written in LaTeX code.
//All LaTeX code should be enclosed within a pair of double dollar symbols $$.
//Your output MUST not include hyperlinks, code snippets or XML.
</Component Description>

<Details>
//1. Read the following Details and think step-by-step.
//2. These are the type and details of the reference Original Component: Type: <Original Component Type>  </Original Component Type>, Details: <Original Component Details>  </Original Component Details> 
//3. The following Additional Prompts are instructions on what kind of components should be created, which may include the details of the components: <Additional Prompts> Reproduce exactly the questions in the knowledge base as free response questions. </Additional Prompts>
//4. The new components should help students achieve the following Learning Outcomes in the Section Tags: <Section Tags> {Section Tags} </Section Tags>
//5. The Knowledge Base contains content that may come in the form of text, images, or some combination of both. You MUST refer to it when creating new components: <Knowledge Base> 
"""

KB_image_path = "images/comprehension_600x845.jpg" 
KB_base64 = ACP.encode_image(KB_image_path)

user_message_aft_KB = """
</Knowledge Base>
</Details>

<Completion Steps>
//1. Read the following instructions carefully and think step-by-step.
//2. If the reference Original Component is provided, use the content in Original Component Details to generate other components of similar content, with guidance from the Additional Prompts. If no Original Component is provided, take guidance from the Additional Prompts.
//3. Create exactly another 4 new components of the following types: Free Response Question, following strictly the guidance from the Additional Prompts.
//4. The content of the components MUST be based on the content in the Knowledge Base and Section Tags.
//5. If the Knowledge Base contains images, analyse the image content carefully to make sure you understand what the image shows.
//6. The language of the content should be the same as the language used in the content enclosed within the Section Tags, Additional Prompts and Knowledge Base XML tags. If the language is in English, use UK English spelling.
//7. Format the created components following the correct JSON format delineated in the provided tools.
//8. Check that the number of components created = 4. If it is less than the expected number, create more components of the required types with reference to steps 4 to 6.
</Completion Steps>

//Return the response in the correct JSON format.
"""

user_message = [{"type": "text",
                    "text": user_message_bef_KB},
                {"type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{KB_base64}"}},
                {"type": "text",
                    "text": user_message_aft_KB}]

user_message_plain_text_only = """
<Context>You are an expert teacher creating lesson content and questions for students.
Important instructions will be denoted by // at the start of the instruction.
</Context>

<Objective>
//Your task is to create new components based on the Details of a reference Original Component, Section Tags, Additional Prompts and Knowledge Base, and then return the created components in the correct JSON format.
//There are only eight types of components: text, multipleChoiceQuestion, freeResponseQuestion, fillInTheBlankQuestion, errorEditingQuestion, poll, discussionQuestion and interactiveThinkingRoutineQuestion.
//You will first be provided a description of each type of component.
//You will next be provided a guide on how to interpret the provided Details.
//You will then be provided with a set of creation instructions to explain how to use the Details to create the desired components.
//Finally at the end, you will be provided with a set of instructions to explain how to output the final complete response in the correct JSON format.
</Objective>

<Component Description>
//<text> Text: A component of rich text that contains content relevant to the lesson content which may use text with HTML formatting tags, HTML tables, HTML ordered lists, HTML unordered lists or LaTeX mathematical expressions to explain the concepts or skills in the Learning Outcomes or Knowledge Base, or be a reproduction of the rich text found in the Knowledge Base. For each component, provide (i) the required text, which may include tables, ordered lists, unordered lists with the appropriate HTML tags or mathematical expressions written in LaTeX enclosed in a pair of double dollar symbols $$</text>,
//<multipleChoiceQuestion> MCQ/MRQ: A multiple choice question with at least two options. For each multiple choice question, provide (i) the question, (ii) the correct options, (iii) feedback for why the correct answers answer the question, (iv) any remaining options are distractors which are incorrect answers, (v) feedback for each distractor explaining why the distractor is incorrect and what the correct answers should be, (vi) suggested time duration in seconds needed for a student to complete the question, (vii) total marks for the question </multipleChoiceQuestion>,
//<freeResponseQuestion> FRQ: A free response question which includes suggested answers. For each free response question, provide (i) the question, (ii) total marks for the question, which should be equal to the total number of creditworthy points in the suggested answer, (iii) suggested answer, which is a comprehensive list of creditworthy points that answers the question, where one point is to be awarded one mark and written in the following format: " (1 mark): Statement describing creditworthy idea 1.\n (1 mark): Statement describing creditworthy idea 2.\n" , and the total marks for the question should be equal to the number of creditworthy points in the suggested answer, (iv) suggested time duration in seconds needed for a student to complete the question </freeResponseQuestion>,
//<fillInTheBlankQuestion> FITB: A fill-in-the-blank question based on the learning outcomes where the blanks refer to key ideas, concepts or words for the learning outcomes. For each fill-in-the-blank question, provide (i) the question statement with blanks and the blanks must be labelled using square brackets containing a running number, such as [1], (ii) the accepted answer(s) for each blank, (iii) marks per blank, (iv) total marks for the question </fillInTheBlankQuestion>,
//<errorEditingQuestion> EE: An error editing question which comprises of multiple sentences, each of which may contain a factual or language error, related to the learning outcomes. For the error editing question, provide at least (i) eight sentences with errors, (ii) the erroneous word or words, (iii) the suggested word or words, (iv) two sentences without errors, (v) marks per sentence, (vi) total marks for the question </errorEditingQuestion>,
//<poll> Poll: A poll which is a multiple choice question with two or more options but no correct answer. For each poll, provide (i) a question, (ii) at least two options in response to the question</poll>,
//<discussionQuestion> Discussion: A discussion question which invites students to respond with their opinion. For each discussion question, provide (i) the discussion topic, (ii) a free response question for students to respond to </discussionQuestion>,
//<interactiveThinkingRoutineQuestion> ITT: An interactive thinking tool (ITT) has a set of categories. For each category, there is a specific question related to the learning outcome and the category. These are the various interactive thinking tools you may select: There are 8 tools. Tool 1 has the categories - See, Think, Wonder. Tool 2 has the categories - Think, Puzzle, Explore. Tool 3 has the categories - Know, Want to know, Learned. Tool 4 has the categories - Connect, Extend, Challenge. Tool 5 has the categories - I used to think..., But now I think... . Tool 6 has the categories - What's going on?, What do you see that makes you say that?. Tool 7 has the categories - Claim, Support, Question. Tool 8 has the categories - What can the person or thing perceive?, What might the person or thing know about or believe?, What might the person or thing care about?.. For the ITT, choose one interactive thinking tool to use, then state the category and provide a question for each category, related to the learning outcome. </interactiveThinkingRoutineQuestion>,
//Remember that any text output can be rich text and mathematical expressions MUST be written in LaTeX code.
//All LaTeX code should be enclosed within a pair of double dollar symbols $$.
//Your output MUST not include hyperlinks, code snippets or XML.
</Component Description>

<Details>
//1. Read the following Details and think step-by-step.
//2. These are the type and details of the reference Original Component: Type: <Original Component Type>  </Original Component Type>, Details: <Original Component Details>  </Original Component Details> 
//3. The following Additional Prompts are instructions on what kind of components should be created, which may include the details of the components: <Additional Prompts> Generate 4 text components explaining the fundamental theorem of calculus. </Additional Prompts>
//4. The new components should help students achieve the following Learning Outcomes in the Section Tags: <Section Tags> </Section Tags>
//5. The Knowledge Base contains content that may come in the form of text, images, or some combination of both. You MUST refer to it when creating new components: <Knowledge Base> </Knowledge Base>
</Details>

<Completion Steps>
//1. Read the following instructions carefully and think step-by-step.
//2. If the reference Original Component is provided, use the content in Original Component Details to generate other components of similar content, with guidance from the Additional Prompts. If no Original Component is provided, take guidance from the Additional Prompts.
//3. Create exactly another 4 new components of the following types: Text, following strictly the guidance from the Additional Prompts.
//4. The content of the components MUST be based on the content in the Knowledge Base and Section Tags.
//5. If the Knowledge Base contains images, analyse the image content carefully to make sure you understand what the image shows.
//6. The language of the content should be the same as the language used in the content enclosed within the Section Tags, Additional Prompts and Knowledge Base XML tags. If the language is in English, use UK English spelling.
//7. Format the created components following the correct JSON format delineated in the provided tools.
//8. Check that the number of components created = 4. If it is less than the expected number, create more components of the required types with reference to steps 4 to 6.
</Completion Steps>

//Return the response in the correct JSON format.
"""
ACP.regen_comp(user_message_plain_text_only)
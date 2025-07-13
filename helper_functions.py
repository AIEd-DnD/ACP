from openai import OpenAI
import os
import base64
from dotenv import load_dotenv
from datetime import datetime
import prompts
import tools
import json
import csv

load_dotenv('.env')
openai_api_key = os.getenv("OPENAI_API_KEY")

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def assemble_prompt(subject, level, additional_prompts, section_tags, knowledge_base, number_of_components, component_types, prompt_template=prompts.regeneration_base, original_component_type=" ", original_component=" "):
    user_message = prompt_template.format(Subject=subject, Level=level, Original_Component_Type=original_component_type, Original_Component=original_component, Additional_Prompts=additional_prompts, Section_Tags=section_tags, Knowledge_Base=knowledge_base, Number_of_Components=number_of_components, Component_Types=component_types)
    return user_message

def regen_comp(user_prompt):
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        temperature = 0.7,
        max_tokens = 16000,
        tools = tools.regeneration,
        messages=[{"role": "user", "content":user_prompt}]
        )
    print(response)
    output = response.choices[0].message.tool_calls[0].function.arguments
    output_dict = json.loads(output)
    list_of_recommendations = output_dict['recommendations']['componentRecommendations']
    for component in list_of_recommendations:
        if 'multipleChoiceQuestion' in component.keys():
            print('MCQ/MRQ')
            print('Question: '+str(component['multipleChoiceQuestion']['question']['richtext']))
            for i in range(len(component['multipleChoiceQuestion']['answers'])):
                print('Answer '+str(i+1) + ': '+str(component['multipleChoiceQuestion']['answers'][i]['richtext']))
            for i in range(len(component['multipleChoiceQuestion']['distractors'])):
                print('Distractor '+str(i+1) + ': '+str(component['multipleChoiceQuestion']['distractors'][i]['richtext']))
            print(" ")
        elif 'freeResponseQuestion' in component.keys():
            print('FRQ')
            print('Question: '+str(component['freeResponseQuestion']['question']['richtext']))
            print('Suggested Answer: \n'+str(component['freeResponseQuestion']['answer']['richtext']))
            print('Total Marks: '+str(component['freeResponseQuestion']['totalMarks']))
            print(" ")
        elif 'poll' in component.keys():
            print('Poll')
            print('Question: '+str(component['poll']['question']['richtext']))
            for i in range(len(component['poll']['options'])):
                print('Option '+str(i+1) + ': '+str(component['poll']['options'][i]['richtext']))
            print(" ")
        elif 'discussionQuestion' in component.keys():
            print('Discussion')
            print('Topic: '+str(component['discussionQuestion']['topic']['richtext']))
            print('Question: '+str(component['discussionQuestion']['question']['richtext']))
            print(" ")
        elif 'errorEditingQuestion' in component.keys():
            print('Error Editing')
            for i in range(len(component['errorEditingQuestion']['sentences'])):
                print('Sentence '+str(i+1) + ': '+str(component['errorEditingQuestion']['sentences'][i]['sentence']['richtext']))
                print('Error Word '+str(i+1) + ': '+str(component['errorEditingQuestion']['sentences'][i]['errorWord']))
                print('Answer '+str(i+1) + ': '+str(component['errorEditingQuestion']['sentences'][i]['answer']))
                print(" ")
            print(" ")
        elif 'fillInTheBlankQuestion' in component.keys():
            print('FITB')
            print('Question: '+str(component['fillInTheBlankQuestion']['question']['richtext']))
            for i in range(len(component['fillInTheBlankQuestion']['answers'])):
                print('Suggested Answers '+str(i+1) + ': '+str(component['fillInTheBlankQuestion']['answers']['answer']))
            print(" ")
        elif 'interactiveThinkingRoutineQuestion' in component.keys():
            print('ITT')
            for i in range(len(component['interactiveThinkingRoutineQuestion'])):
                print('Column '+str(i+1) + ' Header: '+str(component['interactiveThinkingRoutineQuestion'][i]['category']))
                print('Column '+str(i+1) + ' Question: '+str(component['interactiveThinkingRoutineQuestion'][i]['question']['richtext']))
            print(" ")
        elif 'text' in component.keys():
            print('Text')
            print(component['text']['richtext'])
            print(" ")

def tools_filler(numOfSections):
    tools.module_plan_tools_v2[0]['function']['parameters']['properties']['moduleNotes']['minItems'] = numOfSections
    return tools.module_plan_tools_v2

def small_fat_assembler(subject, level, learning_objectives, number_of_sections, number_of_activities_per_section, instructions, knowledge_base, KATs):
    user_message = prompts.editing_flow_small_fat.format(Subject=subject, Level=level, Learning_objectives=learning_objectives, Number_of_sections=number_of_sections, Number_of_activities_per_section=number_of_activities_per_section, Instructions=instructions, Knowledge_Base=knowledge_base, KATs=KATs)
    return user_message

def module_plan_generator(user_prompt, tool):
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        temperature = 0.7,
        max_tokens = 16000,
        tools = tool,
        messages=[{"role": "user", "content":user_prompt}]
        )
    return response.choices[0].message.tool_calls[0].function.arguments

def string_to_dict(string):
    plan_dict = json.loads(string)
    return plan_dict

def write_HTML(plan_dict):
    content = str()
    #content = prompts.styling
    content += '<h2>Module Title: '+plan_dict['moduleTitle']+'</h2>'
    content += '<b>Module Description</b>: '+plan_dict['moduleDescription']
    content += '<br>'
    for section in plan_dict['moduleNotes']:
        content += '<h3> Section Title: '+section['sectionTitle']+'</h3>'
        content += '<b>Suggested number of activities</b>: '+str(section['numOfActivities'])
        content += '<br>'
        content += section['sectionNotes']
    
    return content

def start_new_HTML(file_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Records/ACP_{file_name}_{timestamp}.html"
    return filename

def start_new_record(file_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Records/ACP_{file_name}_{timestamp}.csv"
    return filename

def csv_to_list_of_dicts(file_path):
    result = list()
    with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append(row)
    return result

def extract_parameters(parameter_dict):
    subject = parameter_dict['subject']
    level = parameter_dict['level']
    learning_objectives = parameter_dict['learning_objectives']
    number_of_sections = parameter_dict['number_of_sections']
    number_of_activities_per_section = parameter_dict['number_of_activities_per_section']
    instructions = parameter_dict['instructions'] 
    knowledge_base = parameter_dict['knowledge_base']
    KATs = parameter_dict['KATs']

    return subject, level, learning_objectives, number_of_sections, number_of_activities_per_section, instructions, knowledge_base, KATs

def write_into_record(filename, data):
    header = ['Subject','Level','Learning Objectives','Requested No. of Sections','Requested No. of Activities per Section','Instructions','Knowledge Base','KATs','Expected Total No. of Activities','Created No. of Sections','Total No. of Created Activities','Total Stated No. of Created Activites','Requested Section Match Status','Requested Total Activities Match Status','Internal Activity No. Consistency','Module Title','Module Description','Module Notes']
    with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
    print(f"CSV file '{filename}' has been created successfully.")

def write_to_HTML_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content written to {filename}")
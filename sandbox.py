import helper_functions as ACP
import json
import prompts

file_name = "Refinement_v1"

learning_objectives = """

"""
subject = " "
level = " "
number_of_sections = 3
number_of_activities_per_section = 3
instructions = """

"""
knowledge_base = """

"""
KATs = """

"""
ACP.tools_filler(number_of_sections)
message = ACP.small_fat_assembler(subject, level, learning_objectives, number_of_sections, number_of_activities_per_section, instructions, knowledge_base, KATs)
plan = ACP.module_plan_generator(message)
plan_dict = json.loads(plan)
print(plan_dict)

content = prompts.styling
content += '<h2>Module Title: '+plan_dict['moduleTitle']+'</h2>'
content += '<b>Module Description</b>: '+plan_dict['moduleDescription']
content += '<br>'
for section in plan_dict['moduleNotes']:
    content += '<h3> Section Title: '+section['sectionTitle']+'</h3>'
    content += '<b>Suggested number of activities</b>: '+str(section['numOfActivities'])
    content += '<br>'
    content += section['sectionNotes']

filename = ACP.start_new_HTML(file_name)
ACP.write_to_HTML_file(filename, content)
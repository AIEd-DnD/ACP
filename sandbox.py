import helper_functions as ACP
import json
import prompts

file_name = "Prototype_Testing_s1_a19"

learning_objectives = """
- show an understanding that the weight of a body may be taken as acting at a single point known as its centre of gravity 
"""
subject = "Physics"
level = "Secondary 3"
number_of_sections = 1
number_of_activities_per_section = 19
instructions = """

"""
knowledge_base = """

"""
KATs = """

"""
module_plan_tools_v2 = [
    {
  "type": "function",
  "function": {
    "name": "get_module_plan_recommendations",
    "description": "A recommendation of sections and activities for a module plan. Richtext contents must be in HTML format.",
    "parameters": {
      "type": "object",
      "properties": {
        "moduleTitle": {
          "type": "string",
          "description": "Title of the lesson module in plain text format."
        },
        "moduleDescription": {
          "type": "string",
          "description": "Brief description of the module's goals and approach. This can be in rich text format, but must be in HTML format.",
        },
        "moduleNotes": {
          "type": "array",
          "description": "A list of lesson sections with structured activities.",
          "minItems": number_of_sections,
          "items": {
            "$ref": "#/definitions/LessonSection"
          }
        }
      },
      "required": ["moduleDetails", "moduleDescription", "moduleNotes"],
      "definitions": {
        "LessonSection": {
          "type": "object",
          "properties": {
            "sectionID": {
              "type": "integer",
              "description": "Unique numeric ID for the section."
            },
            "sectionTitle": {
              "type": "string",
              "description": "Title of the section in plain text format."
            },
            "sectionNotes": {
              "type": "string",
              "description": "HTML table containing the structured activity breakdown."
            },
            "numOfActivities": {
              "type": "integer",
              "description": "Number of activities in the section."
            }
          },
          "required": ["sectionID", "sectionTitle", "sectionNotes", "numOfActivities"]
        }
      }
    }
  }
}
]

message = ACP.small_fat_assembler(subject, level, learning_objectives, str(number_of_sections), str(number_of_activities_per_section), instructions, knowledge_base, KATs)
#print(message)
plan = ACP.module_plan_generator(message, module_plan_tools_v2)
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
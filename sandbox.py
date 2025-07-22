import helper_functions as ACP
import json
#import prompts

file_name = "Prototype_v2_Testing_s1_a1"

learning_objectives = """
- show an understanding that the weight of a body may be taken as acting at a single point known as its centre of gravity 
"""
subject = "Physics"
level = "Secondary 3"
number_of_sections = 3
number_of_activities_per_section = 3
instructions = """

"""
knowledge_base = """

"""
KATs = """

"""
module_plan_tools_v3 = [
  {
  "name": "lessonModuleGenerator",
  "description": "Generate a structured lesson module with sections and activities for a given topic.",
  "parameters": {
    "type": "object",
    "properties": {
      "moduleTitle": {
        "type": "string",
        "description": "The title of the lesson module."
      },
      "moduleDescription": {
        "type": "string",
        "description": "A short description of the lesson module's aim or learning objectives."
      },
      "moduleNotes": {
        "type": "array",
        "description": "An array of sections with structured activity plans.",
        "minItems": number_of_sections,
        "items": {
          "type": "object",
          "properties": {
            "sectionID": {
              "type": "integer",
              "description": "A unique integer identifier for the section."
            },
            "sectionTitle": {
              "type": "string",
              "description": "The title of the section."
            },
            "numOfActivities": {
              "type": "integer",
              "description": "The number of activities in this section."
            },
            "sectionNotes": {
              "type": "array",
              "description": "An array of activity plans.",
              "minItems": number_of_activities_per_section,
              "items": {
                "type": "object",
                "properties": {
                  "activityType": {
                    "type": "array",
                    "items": { "type": "string" }
                  },
                  "suggestedSLSTools": {
                    "type": "array",
                    "items": { "type": "string" }
                  },
                  "katDetails": {
                    "type": "object",
                    "properties": {
                      "KATs": {
                        "type": "array",
                        "items": { "type": "string" }
                      },
                      "notes": { "type": "string" }
                    },
                    "required": ["KATs", "notes"]
                  },
                  "activityDetails": {
                    "type": "object",
                    "properties": {
                      "activityTitle": { "type": "string" },
                      "activityNotes": { "type": "string" }
                    },
                    "required": ["activityTitle", "activityNotes"]
                  }
                },
                "required": [
                  "activityType",
                  "suggestedSLSTools",
                  "katDetails",
                  "activityDetails"
                ]
              }
            }
          },
          "required": [
            "sectionID",
            "sectionTitle",
            "numOfActivities",
            "sectionNotes"
          ]
        }
      }
    },
    "required": ["moduleTitle", "moduleDescription", "moduleNotes"]
  }
}
]

message = ACP.small_fat_assembler(subject, level, learning_objectives, str(number_of_sections), str(number_of_activities_per_section), instructions, knowledge_base, KATs)
#print(message)
plan = ACP.module_plan_generator(message, module_plan_tools_v3)
plan_dict = json.loads(plan)
print(plan_dict)
stuff = type(plan_dict['moduleNotes'][0]['sectionNotes'][0]['interactionType'])
print(stuff)



#content = prompts.styling
#content += '<html><h2>Module Title: '+plan_dict['moduleTitle']+'</h2>'
#content += '<b>Module Description</b>: '+plan_dict['moduleDescription']
#content += '<br>'
#for section in plan_dict['moduleNotes']:
    #content += '<h3> Section Title: '+section['sectionTitle']+'</h3>'
    #content += '<b>Suggested number of activities</b>: '+str(section['numOfActivities'])
    #content += '<br>'
    #content += section['sectionNotes']

#filename = ACP.start_new_HTML(file_name)
#ACP.write_to_HTML_file(filename, content)
#ACP.json_to_html(plan_dict, filename)
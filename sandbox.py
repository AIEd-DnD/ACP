import helper_functions as ACP
import json
import prompts

file_name = "Prototype_v3_s1_a3_Econs_gpt_4o_mini"

learning_objectives = """
- show an understanding that the weight of a body may be taken as acting at a single point known as its centre of gravity
"""
module_title = " "
subject = "Physics"
level = "Secondary 3"
number_of_sections = 1
number_of_activities_per_section = 3
instructions = """

"""
knowledge_base = """

"""
KATs = """
Embed scaffolding, Support assessment for learning
"""
module_plan_tools_v3 = [
  {
  "type":"function",
  "function": {
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
}
]

module_plan_tools_v4 = [
        {
    "type": "function",
    "function": {
      "name": "generate_lesson_module",
      "description": "Generates a lesson module including multiple sections with activities or quizzes.",
      "parameters": {
        "type": "object",
        "properties": {
          "moduleTitle": {
            "type": "string",
            "description": "The title of the lesson module. Use the module title provided by the user, unless the user did not provide a module title. Any suggested module title should be concise and descriptive in plain text format."
          },
          "moduleDescription": {
            "type": "string",
            "description": "A summary of what the students will be learning in this lesson module and the activities that the students will be engaging in."
          },
          "moduleNotes": {
            "type": "array",
            "description": "A list of sections in the module.",
            "minItems": number_of_sections,
            "items": {
              "type": "object",
              "properties": {
                "sectionID": {
                  "type": "integer",
                  "description": "Unique numeric identifier for the section."
                },
                "sectionTitle": {
                  "type": "string",
                  "description": "Title of the section. Section title should be concise and descriptive in plain text format."
                },
                "sectionNotes": {
                  "type": "array",
                  "description": "List of activities or quizzes in this section.",
                  "minItems": number_of_activities_per_section,
                  "items": {
                    "type": "object",
                    "properties": {
                      "activityType": {
                        "type": "string",
                        "enum": ["Activity", "Quiz"],
                        "description": "Type of activity - either 'Activity' or 'Quiz'."
                      },
                      "suggestedSLSTools": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        },
                        "description": "Suggested tools to use in SLS for this activity."
                      },
                      "suggestedKATs": {
                        "type": "string",
                        "enum": ["Foster conceptual change", "Support assessment for learning", "Facilitate learning together", "Develop metacognition", "Provide differentiation", "Embed scaffolding", "Enable personalisation", "Increase motivation"],                  
                        "description": "Suggested Key Applications of Technology (KATs) for the activity. Priority should be given to KATs requested by the user."
                      },
                      "activityDetails": {
                        "type": "object",
                        "properties": {
                          "activityTitle": {
                            "type": "string",
                            "description": "Title of the activity. If it is a quiz, the title should indicate that it is a quiz (e.g., 'Quiz: Understanding Centre of Gravity'). The title should be concise and descriptive in plain text format."
                          },
                          "activityNotes": {
                            "type": "string",
                            "description": "Details or instructions for the activity. The notes should describe what the students will be doing in the activity and how teachers can facilitate the activity by using the suggested SLS tools."
                          }
                        },
                        "required": ["activityTitle", "activityNotes"]
                      }
                    },
                    "required": ["activityType", "suggestedSLSTools", "suggestedKATs", "activityDetails"]
                  }
                }
              },
              "required": ["sectionID", "sectionTitle", "sectionNotes"]
            }
          }
        },
        "required": ["moduleTitle", "moduleDescription", "moduleNotes"]
      }
    }
  }
]

message = ACP.small_fat_assembler(module_title, subject, level, learning_objectives, str(number_of_sections), str(number_of_activities_per_section), instructions, knowledge_base, KATs)
#print(message)
plan = ACP.module_plan_generator_gpt5(message, module_plan_tools_v4)
#plan_dict = json.loads(plan)
#print(plan_dict)
#stuff = type(plan_dict['moduleNotes'][0]['sectionNotes'][0]['interactionType'])
#print(stuff)
#html_file = ACP.json_to_html_writer(plan_dict)


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
#ACP.write_to_HTML_file(filename, html_file)
#ACP.json_to_html(plan_dict, filename)
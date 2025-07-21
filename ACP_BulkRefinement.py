import helper_functions as ACP

data = list()
#test_name = input("Please enter the name of the test: ")               #uncomment this to unlock user input for test name
#file_path = input("Please enter the file path of the test data: ")     #uncomment this to unlock user input for file path
evaluation_record = ACP.start_new_record("big_fat_v1")
print("The record has been created.")
testbench = ACP.csv_to_list_of_dicts("Dataset/ACP_VolumeComplianceBulkTest.csv")
print("The testbench has been loaded.")

for test_scenario in testbench:
    new_row = list()
    subject, level, learning_objectives, number_of_sections, number_of_activities_per_section, instructions, knowledge_base, KATs = ACP.extract_parameters(test_scenario)

    new_row.append(subject)
    new_row.append(level)
    new_row.append(learning_objectives)
    new_row.append(number_of_sections)
    new_row.append(number_of_activities_per_section)
    new_row.append(instructions)
    new_row.append(knowledge_base)
    new_row.append(KATs)
    new_row.append(int(number_of_sections) * int(number_of_activities_per_section))

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
          "minItems": int(number_of_sections),
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

    print('Trying response '+str(testbench.index(test_scenario)+1)+" of "+str(len(testbench)))
    try:
        plan = ACP.module_plan_generator(message, module_plan_tools_v2)
        plan_dict = ACP.string_to_dict(plan)
    except Exception as exp:
        print(f"An error occurred when trying to process the response from OpenAI: {str(exp)}.")
        new_row.append(str(exp))
        new_row.append(0)
        new_row.append(0)
        new_row.append(0)
        new_row.append(False)
        new_row.append(False)
        new_row.append(False)
        new_row.append("NIL")
        new_row.append("NIL")
        new_row.append("NIL")
        data.append(new_row)
        continue

    try:
      moduleTitle = plan_dict['moduleTitle']
      moduleDescription = plan_dict['moduleDescription']
      Number_of_sections = len(plan_dict['moduleNotes'])
    except Exception as exp:
        print(f"An error occurred when trying to extract module title, description, or number of sections: {str(exp)}.")
        new_row.append(0)
        new_row.append(0)
        new_row.append(0)
        new_row.append(False)
        new_row.append(False)
        new_row.append(False)
        new_row.append(str(exp))
        new_row.append(str(exp))
        new_row.append(plan_dict)
        data.append(new_row)
        continue
    
    try:
      HTML_file = ACP.write_HTML(plan_dict)
      #HTML_file = ACP.json_to_html_writer(plan_dict)
    except Exception as exp:
        print(f"An error occurred when trying to write the HTML file: {str(exp)}.")
        new_row.append(Number_of_sections)
        new_row.append(0)
        new_row.append(0)
        new_row.append(False)
        new_row.append(False)
        new_row.append(False)
        new_row.append(moduleTitle)
        new_row.append(moduleDescription)
        new_row.append(plan_dict)
        data.append(new_row)
        continue
    
    total_number_of_created_activities = HTML_file.count('<tr>') -  Number_of_sections
    total_number_of_declared_activities = 0
    for section in plan_dict['moduleNotes']:
        total_number_of_declared_activities += section['numOfActivities']
    
    new_row.append(Number_of_sections)
    new_row.append(total_number_of_created_activities)
    new_row.append(total_number_of_declared_activities)
    
    if Number_of_sections == int(number_of_sections):
        new_row.append(True)
    else:
        new_row.append(False)

    if total_number_of_created_activities == int(number_of_sections) * int(number_of_activities_per_section):
        new_row.append(True)
    else:
        new_row.append(False)

    if total_number_of_created_activities == total_number_of_declared_activities:
        new_row.append(True)
    else:
        new_row.append(False)

    new_row.append(moduleTitle)
    new_row.append(moduleDescription)
    new_row.append(HTML_file)
    data.append(new_row)

ACP.write_into_record(evaluation_record, data)

component_regeneration_tools= [
      {
        "type": "function",
        "function": {
          "name": "get_new_component_recommendations",
          "description": "Evaluate and must provide a list of recommendations. Richtext contents must be in HTML format. The response must be a valid JSON",
          "parameters": {
            "type": "object",
            "properties": {
              "recommendations": {
                "type": "object",
                "description": "Regenerated Recommendation",
                "properties": {
                  "componentRecommendations": {
                    "type": "array",
                    "description": "List of component recommendations",
                    "minItems": 4,
                    "items": {
                      "anyOf": [
                        {
                          "$ref": "#/definitions/multipleChoiceQuestionRecommendation"
                        },
                        {
                          "$ref": "#/definitions/freeResponseQuestionRecommendation"
                        },
                        {
                          "$ref": "#/definitions/pollRecommendation"
                        },
                        {
                          "$ref": "#/definitions/discussionQuestionRecommendation"
                        },
                        {
                          "$ref": "#/definitions/textRecommendation"
                        },
                        {
                          "$ref": "#/definitions/errorEditingQuestionRecommendation"
                        },
                        {
                          "$ref": "#/definitions/fillInTheBlankQuestionRecommendation"
                        },
                        {
                          "$ref": "#/definitions/interactiveThinkingRoutineQuestionRecommendation"
                        }
                      ]
                    }
                  }
                },
                "required": [
                  "componentRecommendations"
                ]
              }
            },
            "definitions": {
              "richtext": {
                "type": "string",
                "description": "The richtext content in HTML"
              },
              "marks": {
                "type": "number",
                "description": "the number of marks allocated to the question or answer."
              },
              "duration": {
                "type": "number",
                "description": "Time given for an activity in seconds"
              },
              "textRecommendation": {
                "type": "object",
                "description": "A recommended text paragraph",
                "properties": {
                  "text": {
                    "type": "object",
                    "properties": {
                      "richtext": {
                        "$ref": "#/definitions/richtext"
                      }
                    },
                    "required": [
                      "richtext"
                    ]
                  }
                },
                "required": [
                  "text"
                ]
              },
              "multipleChoiceQuestionRecommendation": {
                "type": "object",
                "description": "A recommended multiple choice question",
                "properties": {
                  "multipleChoiceQuestion": {
                    "type": "object",
                    "properties": {
                      "question": {
                        "type": "object",
                        "description": "The content of a question.",
                        "properties": {
                          "richtext": {
                            "$ref": "#/definitions/richtext"
                          }
                        },
                        "required": [
                          "richtext"
                        ]
                      },
                      "answers": {
                        "type": "array",
                        "description": "The list of correct answers",
                        "items": {
                          "type": "object",
                          "description": "A correct answer",
                          "properties": {
                            "richtext": {
                              "$ref": "#/definitions/richtext"
                            }
                          },
                          "required": [
                            "richtext"
                          ]
                        }
                      },
                      "distractors": {
                        "type": "array",
                        "description": "The list of distractors / incorrect answers",
                        "items": {
                          "type": "object",
                          "description": "A distractor / incorrect answer",
                          "properties": {
                            "richtext": {
                              "$ref": "#/definitions/richtext"
                            }
                          },
                          "required": [
                            "richtext"
                          ]
                        }
                      },
                      "duration": {
                        "$ref": "#/definitions/duration"
                      },
                      "totalMarks": {
                        "$ref": "#/definitions/marks"
                      }
                    },
                    "required": [
                      "question",
                      "answers",
                      "distractors",
                      "duration",
                      "totalMarks"
                    ]
                  }
                },
                "required": [
                  "multipleChoiceQuestion"
                ]
              },
              "freeResponseQuestionRecommendation": {
                "type": "object",
                "description": "A recommended free response question",
                "properties": {
                  "freeResponseQuestion": {
                    "type": "object",
                    "properties": {
                      "question": {
                        "type": "object",
                        "description": "The content of the question.",
                        "properties": {
                          "richtext": {
                            "$ref": "#/definitions/richtext"
                          }
                        },
                        "required": [
                          "richtext"
                        ]
                      },
                      "answer": {
                        "type": "object",
                        "description": "The content of the suggested answer.",
                        "properties": {
                          "richtext": {
                            "$ref": "#/definitions/richtext"
                          }
                        },
                        "required": [
                          "richtext"
                        ]
                      },
                      "totalMarks": {
                        "$ref": "#/definitions/marks"
                      },
                      "duration": {
                        "$ref": "#/definitions/duration"
                      }
                    },
                    "required": [
                      "question", "answer", "totalMarks", "duration"
                    ]
                  }
                },
                "required": [
                  "freeResponseQuestion"
                ]
              },
              "pollRecommendation": {
                "type": "object",
                "description": "A recommended poll",
                "properties": {
                  "poll": {
                    "type": "object",
                    "properties": {
                      "question": {
                        "type": "object",
                        "description": "The content of the question.",
                        "properties": {
                          "richtext": {
                            "$ref": "#/definitions/richtext"
                          }
                        },
                        "required": [
                          "richtext"
                        ]
                      },
                      "options": {
                        "type": "array",
                        "description": "The options / responses of the poll",
                        "items": {
                          "type": "object",
                          "description": "An option / response",
                          "properties": {
                            "richtext": {
                              "$ref": "#/definitions/richtext"
                            }
                          },
                          "required": [
                            "richtext"
                          ]
                        }
                      }
                    },
                    "required": [
                      "question",
                      "options"
                    ]
                  }
                },
                "required": [
                  "poll"
                ]
              },
              "discussionQuestionRecommendation": {
                "type": "object",
                "description": "A recommended discussion question",
                "properties": {
                  "discussionQuestion": {
                    "type": "object",
                    "properties": {
                      "topic": {
                        "type": "string",
                        "description": "The discussion topic"
                      },
                      "question": {
                        "type": "object",
                        "description": "The content of the question.",
                        "properties": {
                          "richtext": {
                            "$ref": "#/definitions/richtext"
                          }
                        },
                        "required": [
                          "richtext"
                        ]
                      }
                    },
                    "required": [
                      "topic",
                      "question"
                    ]
                  }
                },
                "required": [
                  "discussionQuestion"
                ]
              },
              "errorEditingQuestionRecommendation": {
                "type": "object",
                "description": "A recommended error editing question",
                "properties": {
                  "errorEditingQuestion": {
                    "type": "object",
                    "properties": {
                      "sentences": {
                        "type": "array",
                        "description": "The list of sentences",
                        "items": {
                          "type": "object",
                          "description": "A sentence which can have errors and it's answers",
                          "properties": {
                            "sentence": {
                              "type": "object",
                              "description": "The sentence which can have errors",
                              "properties": {
                                "richtext": {
                                  "$ref": "#/definitions/richtext"
                                }
                              },
                              "required": [
                                "richtext"
                              ]
                            },
                            "errorWord": {
                              "type": "string",
                              "description": "The incorrect word or words"
                            },
                            "answer": {
                              "type": "string",
                              "description": "The suggested word or words"
                            }
                          },
                          "required": [
                            "sentence", "errorWord", "answer"
                          ]
                        }
                      },
                      "marksPerSentence": {
                        "$ref": "#/definitions/marks"
                      },
                      "totalMarks": {
                        "$ref": "#/definitions/marks"
                      },
                      "duration": {
                        "$ref": "#/definitions/duration"
                      }
                    },
                    "required": [
                      "sentences", "marksPerSentence", "totalMarks", "duration"
                    ]
                  }
                },
                "required": [
                  "errorEditingQuestion"
                ]
              },
              "fillInTheBlankQuestionRecommendation": {
                "type": "object",
                "description": "A recommended Fill In the Blank question",
                "properties": {
                  "fillInTheBlankQuestion": {
                    "type": "object",
                    "properties": {
                      "question": {
                        "type": "object",
                        "description": "The content of the question. Each blank must be labelled in square brackets containing a running number. For example, [1] for the first blank and [2] for the second blank. The answers should be populated into the answers field.",
                        "properties": {
                          "richtext": {
                            "$ref": "#/definitions/richtext"
                          }
                        },
                        "required": [
                          "richtext"
                        ]
                      },
                      "answers": {
                        "type": "array",
                        "description": "The list of answers",
                        "items": {
                          "type": "object",
                          "description": "The answer with an index to indicate the blank it corresponds to and it's answer content",
                          "properties": {
                            "index": {
                              "type": "number",
                              "description": "The running number to the blank that this answer corresponds to"
                            },
                            "answer": {
                              "type": "array",
                              "description": "The list of suggested answers for the blank it corresponds to",
                              "items": {
                                "type": "string"
                              }
                            }
                          },
                          "required": ["index", "answer"]
                        }
                      },
                      "marksPerBlank": {
                        "$ref": "#/definitions/marks"
                      },
                      "totalMarks": {
                        "$ref": "#/definitions/marks"
                      },
                      "duration": {
                        "$ref": "#/definitions/duration"
                      }
                    },
                    "required": [
                      "question", "answers", "marksPerBlank", "totalMarks", "duration"
                    ]
                  }
                },
                "required": [
                  "fillInTheBlankQuestion"
                ]
              },
              "interactiveThinkingRoutineQuestionRecommendation": {
                "type": "object",
                "description": "A recommended Interactive Thinking Routine question",
                "properties": {
                  "interactiveThinkingRoutineQuestion": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "question": {
                          "type": "object",
                          "description": "The content of the question associated to a thinking routine category",
                          "properties": {
                            "richtext": {
                              "$ref": "#/definitions/richtext"
                            }
                          },
                          "required": [
                            "richtext"
                          ]
                        },
                        "category": {
                          "type": "string",
                          "description": "The category of the thinking routine tool"
                        }
                      },
                      "required": [
                        "question", "category"
                      ]
                    }
                  }
                },
                "required": [
                  "interactiveThinkingRoutineQuestion"
                ]
              }
            },
            "required": [
              "recommendations"
            ]
          }
        }
      }
    ]

module_to_section_tools = [
      {
        "type": "function",
        "function": {
          "name": "get_new_section_recommendations",
          "description": "Evaluate and must provide a list of recommendations containing lesson description, section title and section notes. Richtext contents must be in HTML format.",
          "parameters": {
            "type": "object",
            "definitions": {
              "richtext": {
                "type": "string",
                "description": "The richtext content in HTML"
              }
            },
            "properties": {
              "recommendations": {
                "type": "object",
                "description": "Recommendations",
                "properties": {
                  "lessonDescription": {
                    "type": "object",
                    "description": "The recommended description",
                    "properties": {
                      "richtext": {
                        "$ref": "#/definitions/richtext"
                      }
                    },
                    "required": [
                      "richtext"
                    ]
                  },
                  "sectionRecommendations":{
                    "type": "array",
                    "description": "List of section recommendations",
                    "minItems": 3,
                    "items": {
                      "type": "object",
                      "properties": {
                        "sectionTitle": {
                          "type": "string",
                          "description": "The recommended section title"
                        },
                        "sectionNotes": {
                          "type": "object",
                          "description": "The recommended section notes",
                          "properties": {
                            "richtext": {
                              "$ref": "#/definitions/richtext"
                            }
                          },
                          "required": [
                            "richtext"
                          ]
                        }
                      },
                      "required": [
                        "sectionTitle",
                        "sectionNotes"
                      ]
                    }
                  }
                },
                "required": ["lessonDescription", "sectionRecommendations"]
              }
            },
            "required": [
              "recommendations"
            ]
          }
        }
      }
    ]

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
          "minItems": 3,
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

module_plan_tools_v2x = [
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
          "minItems": 3,
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

module_plan_tools_v3 = [
  {
    "type": "function",
    "function": {
      "name": "generate_lesson_module",
      "description": "Generates a structured lesson module plan based on a topic.",
      "parameters": {
        "type": "object",
        "properties": {
          "moduleTitle": {
            "type": "string",
            "description": "The title of the lesson module."
          },
          "moduleDescription": {
            "type": "string",
            "description": "A brief description of what the module covers."
          },
          "moduleNotes": {
            "type": "array",
            "description": "A list of sections and their activities in the module.",
            "minItems": 3,
            "items": {
              "type": "object",
              "properties": {
                "sectionID": {
                  "type": "integer",
                  "description": "Unique identifier for the section."
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
                  "description": "Detailed breakdown of each activity.",
                  "minItems": 3,
                  "items": {
                    "type": "object",
                    "properties": {
                      "interactionType": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        },
                        "description": "Type of interaction (e.g., Student-Student, Teacher-Student)."
                      },
                      "duration": {
                        "type": "integer",
                        "description": "Duration of the activity in minutes."
                      },
                      "activityType": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        },
                        "description": "The kind of activity (e.g., Activity, Assessment)."
                      },
                      "suggestedSLSTools": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        },
                        "description": "Recommended tools to use in SLS (Student Learning Space)."
                      },
                      "KAT": {
                        "type": "string",
                        "description": "Key Affordances of Technology for this activity, including a rationale."
                      },
                      "activityDetails": {
                        "type": "object",
                        "properties": {
                          "activityTitle": {
                            "type": "string"
                          },
                          "activityNotes": {
                            "type": "string"
                          }
                        },
                        "required": ["activityTitle", "activityNotes"]
                      }
                    },
                    "required": [
                      "interactionType",
                      "duration",
                      "activityType",
                      "suggestedSLSTools",
                      "KAT",
                      "activityDetails"
                    ]
                  }
                }
              },
              "required": ["sectionID", "sectionTitle", "numOfActivities", "sectionNotes"]
            }
          }
        },
        "required": ["moduleTitle", "moduleDescription", "moduleNotes"]
      }
    }
  }
]

module_plan_tools = [
  {
    "type": "function",
    "function": {
      "name": "get_module_plan_recommendations",
      "description": "A recommendation of sections and activities for a module plan. Richtext contents must be in HTML format.",
      "parameters": {
        "type": "object",
        "definitions": {
          "richtext": {
            "type": "string",
            "description": "The richtext content in HTML"
          }
        },
        "properties": {
          "recommendations": {
            "type": "object",
            "description": "Recommendations",
            "properties": {
              "modulePlan": {
                "type": "object",
                "description": "A series of 4-column tables where the column headers are: Interaction, Duration, Activity Details, Suggested SLS Tools. There should be one table for each requested section. Use HTML to format the tables.",
                "properties": {
                  "richtext": {
                    "$ref": "#/definitions/richtext"
                  }
                },
                "required": [
                  "richtext"
                ]
              },
            },
            "required": [
              "modulePlan"
            ]
          }
        },
        "required": [
          "recommendations"
        ]
      }
    }
  }
]

section_to_activity_tools = [
      {
        "type": "function",
        "function": {
          "name": "get_new_activity_recommendations",
          "description": "Evaluate and must provide recommendations object containing section description and a list of activity recommendations. Richtext contents must be in HTML format.",
          "parameters": {
            "type": "object",
            "definitions": {
              "richtext": {
                "type": "string",
                "description": "The richtext content in HTML"
              }
            },
            "properties": {
              "recommendations": {
                "type": "object",
                "description": "Recommendations",
                "properties": {
                  "sectionDescription": {
                    "type": "object",
                    "description": "The recommended section description",
                    "properties": {
                      "richtext": {
                        "$ref": "#/definitions/richtext"
                      }
                    },
                    "required": [
                      "richtext"
                    ]
                  },
                  "activityRecommendations": {
                    "type": "array",
                    "description": "List of activity recommendations",
                    "minItems": 4,
                    "items": {
                      "type": "object",
                      "properties": {
                        "activityType": {
                          "type": "string",
                          "enum": [
                            "activity",
                            "quiz"
                          ],
                          "description": "The recommended activity type"
                        },
                        "activityTitle": {
                          "type": "string",
                          "description": "The recommended activity title"
                        },
                        "activityNotes": {
                          "type": "object",
                          "description": "The recommended activity notes",
                          "properties": {
                            "richtext": {
                              "$ref": "#/definitions/richtext"
                            }
                          },
                          "required": [
                            "richtext"
                          ]
                        },
                        "activityDuration": {
                          "type": "number",
                          "description": "The recommended duration given for an activity in seconds"
                        }
                      },
                      "required": [
                        "activityType",
                        "activityTitle",
                        "activityNotes",
                        "activityDuration"
                      ]
                    }
                  }
                },
                "required": [
                  "sectionDescription",
                  "activityRecommendations"
                ]
              }
            },
            "required": [
              "recommendations"
            ]
          }
        }
      }
    ]

activity_to_component_tools = [
      {
        "type": "function",
        "function": {
          "name": "get_new_component_recommendations",
          "description": "Evaluate and must provide a list of recommendations. Richtext contents must be in HTML format. The response must be a valid JSON",
          "parameters": {
            "type": "object",
            "properties": {
              "recommendations": {
                "type": "object",
                "description": "Activity Recommendation",
                "properties": {
                  "activityRecommendation": {
                    "$ref": "#/definitions/activityRecommendation"
                  },
                  "componentRecommendations": {
                    "type": "array",
                    "description": "List of component recommendations",
                    "minItems": 4,
                    "items": {
                      "anyOf": [
                        {
                          "$ref": "#/definitions/multipleChoiceQuestionRecommendation"
                        },
                        {
                          "$ref": "#/definitions/freeResponseQuestionRecommendation"
                        },
                        {
                          "$ref": "#/definitions/pollRecommendation"
                        },
                        {
                          "$ref": "#/definitions/discussionQuestionRecommendation"
                        },
                        {
                          "$ref": "#/definitions/textRecommendation"
                        },
                        {
                          "$ref": "#/definitions/errorEditingQuestionRecommendation"
                        },
                        {
                          "$ref": "#/definitions/fillInTheBlankQuestionRecommendation"
                        },
                        {
                          "$ref": "#/definitions/interactiveThinkingRoutineQuestionRecommendation"
                        }
                      ]
                    }
                  }
                },
                "required": [
                  "componentRecommendations",
                  "activityRecommendation"
                ]
              }
            },
            "definitions": {
              "richtext": {
                "type": "string",
                "description": "The richtext content in HTML"
              },
              "marks": {
                "type": "number",
                "description": "the number of marks allocated to the question or answer."
              },
              "duration": {
                "type": "number",
                "description": "Time given for an activity in seconds"
              },
              "activityRecommendation": {
                "type": "object",
                "description": "A recommended activity description and instruction",
                "properties": {
                  "activityDescription": {
                    "type": "object",
                    "properties": {
                      "richtext": {
                        "$ref": "#/definitions/richtext"
                      }
                    },
                    "required": [
                      "richtext"
                    ]
                  },
                  "activityInstruction": {
                    "type": "object",
                    "properties": {
                      "richtext": {
                        "$ref": "#/definitions/richtext"
                      }
                    },
                    "required": [
                      "richtext"
                    ]
                  }
                },
                "required": [
                  "activityDescription",
                  "activityInstruction"
                ]
              },
              "textRecommendation": {
                "type": "object",
                "description": "A recommended text paragraph",
                "properties": {
                  "text": {
                    "type": "object",
                    "properties": {
                      "richtext": {
                        "$ref": "#/definitions/richtext"
                      }
                    },
                    "required": [
                      "richtext"
                    ]
                  }
                },
                "required": [
                  "text"
                ]
              },
              "multipleChoiceQuestionRecommendation": {
                "type": "object",
                "description": "A recommended multiple choice question",
                "properties": {
                  "multipleChoiceQuestion": {
                    "type": "object",
                    "properties": {
                      "question": {
                        "type": "object",
                        "description": "The content of a question.",
                        "properties": {
                          "richtext": {
                            "$ref": "#/definitions/richtext"
                          }
                        },
                        "required": [
                          "richtext"
                        ]
                      },
                      "answers": {
                        "type": "array",
                        "description": "The list of correct answers",
                        "items": {
                          "type": "object",
                          "description": "A correct answer",
                          "properties": {
                            "richtext": {
                              "$ref": "#/definitions/richtext"
                            }
                          },
                          "required": [
                            "richtext"
                          ]
                        }
                      },
                      "distractors": {
                        "type": "array",
                        "description": "The list of distractors / incorrect answers",
                        "items": {
                          "type": "object",
                          "description": "A distractor / incorrect answer",
                          "properties": {
                            "richtext": {
                              "$ref": "#/definitions/richtext"
                            }
                          },
                          "required": [
                            "richtext"
                          ]
                        }
                      },
                      "duration": {
                        "$ref": "#/definitions/duration"
                      },
                      "totalMarks": {
                        "$ref": "#/definitions/marks"
                      }
                    },
                    "required": [
                      "question",
                      "answers",
                      "distractors",
                      "duration",
                      "totalMarks"
                    ]
                  }
                },
                "required": [
                  "multipleChoiceQuestion"
                ]
              },
              "freeResponseQuestionRecommendation": {
                "type": "object",
                "description": "A recommended free response question",
                "properties": {
                  "freeResponseQuestion": {
                    "type": "object",
                    "properties": {
                      "question": {
                        "type": "object",
                        "description": "The content of the question.",
                        "properties": {
                          "richtext": {
                            "$ref": "#/definitions/richtext"
                          }
                        },
                        "required": [
                          "richtext"
                        ]
                      },
                      "answer": {
                        "type": "object",
                        "description": "The content of the suggested answer.",
                        "properties": {
                          "richtext": {
                            "$ref": "#/definitions/richtext"
                          }
                        },
                        "required": [
                          "richtext"
                        ]
                      },
                      "totalMarks": {
                        "$ref": "#/definitions/marks"
                      },
                      "duration": {
                        "$ref": "#/definitions/duration"
                      }
                    },
                    "required": [
                      "question", "answer", "totalMarks", "duration"
                    ]
                  }
                },
                "required": [
                  "freeResponseQuestion"
                ]
              },
              "pollRecommendation": {
                "type": "object",
                "description": "A recommended poll",
                "properties": {
                  "poll": {
                    "type": "object",
                    "properties": {
                      "question": {
                        "type": "object",
                        "description": "The content of the question.",
                        "properties": {
                          "richtext": {
                            "$ref": "#/definitions/richtext"
                          }
                        },
                        "required": [
                          "richtext"
                        ]
                      },
                      "options": {
                        "type": "array",
                        "description": "The options / responses of the poll",
                        "items": {
                          "type": "object",
                          "description": "An option / response",
                          "properties": {
                            "richtext": {
                              "$ref": "#/definitions/richtext"
                            }
                          },
                          "required": [
                            "richtext"
                          ]
                        }
                      }
                    },
                    "required": [
                      "question",
                      "options"
                    ]
                  }
                },
                "required": [
                  "poll"
                ]
              },
              "discussionQuestionRecommendation": {
                "type": "object",
                "description": "A recommended discussion question",
                "properties": {
                  "discussionQuestion": {
                    "type": "object",
                    "properties": {
                      "topic": {
                        "type": "string",
                        "description": "The discussion topic"
                      },
                      "question": {
                        "type": "object",
                        "description": "The content of the question.",
                        "properties": {
                          "richtext": {
                            "$ref": "#/definitions/richtext"
                          }
                        },
                        "required": [
                          "richtext"
                        ]
                      }
                    },
                    "required": [
                      "topic",
                      "question"
                    ]
                  }
                },
                "required": [
                  "discussionQuestion"
                ]
              },
              "errorEditingQuestionRecommendation": {
                "type": "object",
                "description": "A recommended error editing question",
                "properties": {
                  "errorEditingQuestion": {
                    "type": "object",
                    "properties": {
                      "sentences": {
                        "type": "array",
                        "description": "The list of sentences",
                        "items": {
                          "type": "object",
                          "description": "A sentence which can have errors and it's answers",
                          "properties": {
                            "sentence": {
                              "type": "object",
                              "description": "The sentence which can have errors",
                              "properties": {
                                "richtext": {
                                  "$ref": "#/definitions/richtext"
                                }
                              },
                              "required": [
                                "richtext"
                              ]
                            },
                            "errorWord": {
                              "type": "string",
                              "description": "The incorrect word or words"
                            },
                            "answer": {
                              "type": "string",
                              "description": "The suggested word or words"
                            }
                          },
                          "required": [
                            "sentence", "errorWord", "answer"
                          ]
                        }
                      },
                      "marksPerSentence": {
                        "$ref": "#/definitions/marks"
                      },
                      "totalMarks": {
                        "$ref": "#/definitions/marks"
                      },
                      "duration": {
                        "$ref": "#/definitions/duration"
                      }
                    },
                    "required": [
                      "sentences", "marksPerSentence", "totalMarks", "duration"
                    ]
                  }
                },
                "required": [
                  "errorEditingQuestion"
                ]
              },
              "fillInTheBlankQuestionRecommendation": {
                "type": "object",
                "description": "A recommended Fill In the Blank question",
                "properties": {
                  "fillInTheBlankQuestion": {
                    "type": "object",
                    "properties": {
                      "question": {
                        "type": "object",
                        "description": "The content of the question. Each blank must be labelled in square brackets containing a running number. For example, [1] for the first blank and [2] for the second blank. The answers should be populated into the answers field.",
                        "properties": {
                          "richtext": {
                            "$ref": "#/definitions/richtext"
                          }
                        },
                        "required": [
                          "richtext"
                        ]
                      },
                      "answers": {
                        "type": "array",
                        "description": "The list of answers",
                        "items": {
                          "type": "object",
                          "description": "The answer with an index to indicate the blank it corresponds to and it's answer content",
                          "properties": {
                            "index": {
                              "type": "number",
                              "description": "The running number to the blank that this answer corresponds to"
                            },
                            "answer": {
                              "type": "array",
                              "description": "The list of suggested answers for the blank it corresponds to",
                              "items": {
                                "type": "string"
                              }
                            }
                          },
                          "required": ["index", "answer"]
                        }
                      },
                      "marksPerBlank": {
                        "$ref": "#/definitions/marks"
                      },
                      "totalMarks": {
                        "$ref": "#/definitions/marks"
                      },
                      "duration": {
                        "$ref": "#/definitions/duration"
                      }
                    },
                    "required": [
                      "question", "answers", "marksPerBlank", "totalMarks", "duration"
                    ]
                  }
                },
                "required": [
                  "fillInTheBlankQuestion"
                ]
              },
              "interactiveThinkingRoutineQuestionRecommendation": {
                "type": "object",
                "description": "A recommended Interactive Thinking Routine question",
                "properties": {
                  "interactiveThinkingRoutineQuestion": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "question": {
                          "type": "object",
                          "description": "The content of the question associated to a thinking routine category",
                          "properties": {
                            "richtext": {
                              "$ref": "#/definitions/richtext"
                            }
                          },
                          "required": [
                            "richtext"
                          ]
                        },
                        "category": {
                          "type": "string",
                          "description": "The category of the thinking routine tool"
                        }
                      },
                      "required": [
                        "question", "category"
                      ]
                    }
                  }
                },
                "required": [
                  "interactiveThinkingRoutineQuestion"
                ]
              }
            },
            "required": [
              "recommendations"
            ]
          }
        }
      }
    ]
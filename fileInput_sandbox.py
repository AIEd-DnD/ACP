import helper_functions as ACP
import prompts

subject = " "
level = " "
section_tags = " "
number_of_components = 1
original_component_type = " "
original_component = " "
additional_prompts = "Reproduce text in the knowledge base exactly word for word. Do not add or remove words or rephrase them."
knowledge_base = "KnowledgeBase/PEDance.pdf"
component_types = "Text"

message_part_1 = prompts.regeneration_base_file_input_part_1.format(Subject=subject, Level=level, Section_Tags=section_tags, Original_Component_Type=original_component_type, Original_Component=original_component, Additional_Prompts=additional_prompts)
message_part_2 = prompts.regeneration_base_file_input_part_2.format(Number_of_Components=str(number_of_components), Knowledge_Base=knowledge_base, Component_Types=component_types)
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
                    "minItems": number_of_components,
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

ACP.regen_comp_file_input(message_part_1, message_part_2, knowledge_base)
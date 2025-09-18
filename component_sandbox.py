import helper_functions as ACP
import json
import prompts

learning_objectives = """
- show an understanding that the weight of a body may be taken as acting at a single point known as its centre of gravity
"""
activity_title = "Explore with Simulation: Finding the Balance Point "
activity_notes = """
Students individually open an interactive simulation that displays various regular and irregular 2D shapes. Teacher prompts students to: (a) predict where the weight (gravity) acts for each shape and mark their predicted centre using the Interactive Thinking Tool; (b) use the simulation's balance/fulcrum mode to find the actual balance point (centre of gravity) for each shape; (c) note any differences between their prediction and the simulated result. Teachers circulate virtually/in-class to scaffold thinking: ask targeted questions (Why did you place the centre there? What changed when the shape became irregular?), model think-alouds for one example, and prompt students to revise their mental models. This activity uses conceptual-change strategies: elicit preconceptions, provide discrepant events via simulation, and support restructuring through guided reflection.
"""
template = " "
duration = " "
subject = "Physics"
level = "Secondary 3"
number_of_components = 3
instructions = """
Generate 3 components for the Suggested SLS Tools at the end of the Activity Notes by referring to component-tool mapping below.
If there are no Suggested SLS Tools, generate 3 components based on the Activity Notes by referring to component-tool mapping below.

Refer to the following component-tool mappings (i.e. componentNameRecommendation: [SLS Tool 1, SLS Tool 2]) to decide what component to generate for a suggested SLS tool.
1. text: [Text/Media, Tooltip, Insert Student Tooltip, Add Notes to Audio or Video, Insert Transcript for Video & Audio, Text-to-Speech, all tools that mention Embed].
2. multipleChoiceQuestion: [Multiple-Choice/ Multiple-Response Question].
3. fillInTheBlankQuestion: [Fill-in-the-blank Question].
4. errorEditingQuestion: [Error Editing Question].
5. freeResponseQuestion: [Free Response Question, Rubrics, Feedback Assistant Mathematics (FA-Math), Short Answer Feedback Assistant (ShortAnsFA), Annotated Feedback Assistant (AFA)].
6. interactiveThinkingRoutineQuestion: [Interactive Thinking Tool]
7. poll: [Poll]
8. discussionQuestion: [Discussion Board]

You may ignore and not generate any components for the following Suggested SLS tools:
[Click and Drop Question, Audio Response Question (Speech Evaluation), Learning Assistant (LEA), Progressive Quiz, Auto-graded Quiz, Teacher-marked Quiz, Adaptive Learning System (ALS), Team Activities, Subgroups, Add Section Prerequisites, Set Differentiated Access, Gamification - Create Game Stories and Achievements, Gamification - Create Game Teams, Set Optional Activities and Quizzes, Gamification - Quiz leaderboard and ranking, Gamification - Create branches in game stories, Monitor Assignment Page,  Data Assistant, SLS Digital Badges, Chinese Language E-Dictionary]

Do NOT generate components for any SLS tools that are not mentioned in the Activity Notes.
"""
knowledge_base = """

"""
activity_to_component_tools = [
      {
        "type": "function",
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
                  "componentRecommendations",
                  "activityRecommendation"
                ]
              }
            },
            "definitions": {
              "richtext": {
                "type": "string",
                "description": "The richtext content in HTML tags for formatting and LaTeX code for mathematical expressions. All LaTeX code should be enclosed within a pair double dollar synmbols $$."
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
                "description": "A paragraph of text to help students understand the learning outcomes. The text can include explanations and examples to make it easier for students to understand the learning outcomes. For each paragraph of text, provide (i) the required text, which can include tables, ordered lists, unordered lists or mathematical expressions written in LaTeX and enclosed in a pair of double dollar symbols $$ ",
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
                "description": "A multiple choice question with at least two options. There can be one or more correct answers.",
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
                        "description": "The list of correct answers.",
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
                "description": "A free response question which includes suggested answers.",
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
                        "description": "A comprehensive list of creditworthy points that answers the question, where one point is to be awarded one mark and written in the following format: (1 mark): Statement describing creditworthy point.",
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
                "description": "A poll which is a multiple choice question with two or more options but no correct answer.",
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
                "description": "A discussion question which invites students to respond with their opinion.",
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
                "description": "An error editing question which comprises multiple sentences, each of which may contain a factual or language error, related to the learning outcomes.",
                "properties": {
                  "errorEditingQuestion": {
                    "type": "object",
                    "properties": {
                      "sentences": {
                        "type": "array",
                        "description": "The list of sentences",
                        "items": {
                          "type": "object",
                          "description": "A sentence which can have errors and its answers",
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
                "description": "A fill-in-the-blank question based on the learning outcomes where the blanks refer to key ideas, concepts or words for the learning outcomes.",
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
                "description": "An interactive thinking tool (ITT) has a set of categories. For each category, there is a specific question related to the learning outcome and the category.",
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
    ]

user_message = ACP.assemble_activity_prompt(subject, level, activity_title, activity_notes, template, duration, instructions, learning_objectives, knowledge_base, number_of_components)
ACP.activity_plan_generator_gpt5_responses(user_message, activity_to_component_tools)

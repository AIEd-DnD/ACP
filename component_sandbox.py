import helper_functions as ACP
import json
import prompts

learning_objectives = """
- show an understanding that the weight of a body may be taken as acting at a single point known as its centre of gravity
"""
activity_title = "Analyse data & communicate conclusions"
activity_notes = """
Purpose: Students interpret their trial data to decide whether evidence supports the hypothesis and articulate their reasoning. Teacher uses assessment tools to provide targeted feedback and to remediate remaining misconceptions.
Procedure (15-20 min):
Each group examines their Embed Google Sheets dataset and identifies patterns (e.g. how balance point shifts with mass movement). They prepare a short claim–evidence–reasoning statement: "Claim: ...; Evidence: ...; Reasoning: ..."
Groups post their one-paragraph claim in the class area (or teacher collects via the Sheet). Teacher runs a short Progressive Quiz with auto-feedback: 3 adaptive items that check conceptual understanding (e.g. choose the correct location of centre of gravity in new scenarios, explain why an asymmetric object balances at a point outside the geometric centre).
Use quiz analytics to identify students with persistent misconceptions. Teacher provides targeted feedback (written or verbal) and suggests one follow-up micro-task (re-run a simulation configuration or read a short explanation).
Assessment for learning: The Progressive Quiz gives immediate, bite-sized feedback and aggregates class responses so the teacher can decide next instructional steps (mini-lesson, remediation group, or extension).
Extension / Differentiation: Higher-performing groups can explore calculating centre of mass for composite shapes (use the Google Sheets formulas). Struggling students receive scaffolded questions and a guided PhET scenario to re-run.
Suggested SLS Tools: Progressive Quiz, Embed Google Sheets
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

user_message = ACP.assemble_activity_prompt(subject, level, activity_title, activity_notes, template, duration, instructions, learning_objectives, knowledge_base, number_of_components)
ACP.activity_plan_generator_gpt5(user_message, activity_to_component_tools)

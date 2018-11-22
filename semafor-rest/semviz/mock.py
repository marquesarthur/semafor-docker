DB_SENTENCE_1 = {
	"debug_info": {
		"frame_parser_elapsed_seconds": 0.268309,
		"dependency_parser_elapsed_seconds": 7.237735
	},
	"sentences": [{
		"conll": "1\tAbsolutely\t_\tRB\tRB\t_\t2\tadvmod\t_\t_\n2\ttrue\t_\tJJ\tJJ\t_\t0\tnull\t_\t_\n3\t.\t_\t.\t.\t_\t2\tpunct\t_\t_",
		"text": "Absolutely true .",
		"relations": [
			["R1", "advmod", [
				["Arg1", "T2"],
				["Arg2", "T1"]
			]],
			["R2", "punct", [
				["Arg1", "T2"],
				["Arg2", "T3"]
			]]
		],
		"tokens": ["Absolutely", "true", "."],
		"entities": [
			["T1", "RB", [
				[0, 10]
			]],
			["T2", "JJ", [
				[11, 15]
			]],
			["T3", ".", [
				[16, 17]
			]]
		],
		"frames": []
	}]
}

DB_SENTENCE_2 = {
	"debug_info": {
		"frame_parser_elapsed_seconds": 0.381475,
		"dependency_parser_elapsed_seconds": 6.205218
	},
	"sentences": [{
		"conll": "1\tIn\t_\tIN\tIN\t_\t0\tnull\t_\t_\n2\tmy\t_\tPRP$\tPRP$\t_\t3\tposs\t_\t_\n3\texperience\t_\tNN\tNN\t_\t1\tpobj\t_\t_\n4\t,\t_\t,\t,\t_\t1\tpunct\t_\t_\n5\teven\t_\tRB\tRB\t_\t19\tadvmod\t_\t_\n6\tin\t_\tIN\tIN\t_\t5\tdep\t_\t_\n7\tmoderately\t_\tRB\tRB\t_\t8\tadvmod\t_\t_\n8\tsized\t_\tJJ\tJJ\t_\t9\tamod\t_\t_\n9\tapplications\t_\tNNS\tNNS\t_\t6\tpobj\t_\t_\n10\t,\t_\t,\t,\t_\t19\tpunct\t_\t_\n11\tmanually\t_\tRB\tRB\t_\t12\tadvmod\t_\t_\n12\twritten\t_\tVBN\tVBN\t_\t14\tamod\t_\t_\n13\tpersistence\t_\tNN\tNN\t_\t14\tnn\t_\t_\n14\tframeworks\t_\tNNS\tNNS\t_\t19\tnsubj\t_\t_\n15\tare\t_\tVBP\tVBP\t_\t19\tcop\t_\t_\n16\tthe\t_\tDT\tDT\t_\t19\tdet\t_\t_\n17\tmost\t_\tRBS\tRBS\t_\t18\tadvmod\t_\t_\n18\tcomplex\t_\tJJ\tJJ\t_\t19\tamod\t_\t_\n19\tparts\t_\tNNS\tNNS\t_\t4\tdobj\t_\t_\n20\tof\t_\tIN\tIN\t_\t19\tprep\t_\t_\n21\tthe\t_\tDT\tDT\t_\t22\tdet\t_\t_\n22\tapplication\t_\tNN\tNN\t_\t20\tpobj\t_\t_\n23\t.\t_\t.\t.\t_\t1\tpunct\t_\t_",
		"text": "In my experience , even in moderately sized applications , manually written persistence frameworks are the most complex parts of the application .",
		"relations": [
			["R1", "poss", [
				["Arg1", "T3"],
				["Arg2", "T2"]
			]],
			["R2", "pobj", [
				["Arg1", "T1"],
				["Arg2", "T3"]
			]],
			["R3", "punct", [
				["Arg1", "T1"],
				["Arg2", "T4"]
			]],
			["R4", "advmod", [
				["Arg1", "T19"],
				["Arg2", "T5"]
			]],
			["R5", "dep", [
				["Arg1", "T5"],
				["Arg2", "T6"]
			]],
			["R6", "advmod", [
				["Arg1", "T8"],
				["Arg2", "T7"]
			]],
			["R7", "amod", [
				["Arg1", "T9"],
				["Arg2", "T8"]
			]],
			["R8", "pobj", [
				["Arg1", "T6"],
				["Arg2", "T9"]
			]],
			["R9", "punct", [
				["Arg1", "T19"],
				["Arg2", "T10"]
			]],
			["R10", "advmod", [
				["Arg1", "T12"],
				["Arg2", "T11"]
			]],
			["R11", "amod", [
				["Arg1", "T14"],
				["Arg2", "T12"]
			]],
			["R12", "nn", [
				["Arg1", "T14"],
				["Arg2", "T13"]
			]],
			["R13", "nsubj", [
				["Arg1", "T19"],
				["Arg2", "T14"]
			]],
			["R14", "cop", [
				["Arg1", "T19"],
				["Arg2", "T15"]
			]],
			["R15", "det", [
				["Arg1", "T19"],
				["Arg2", "T16"]
			]],
			["R16", "advmod", [
				["Arg1", "T18"],
				["Arg2", "T17"]
			]],
			["R17", "amod", [
				["Arg1", "T19"],
				["Arg2", "T18"]
			]],
			["R18", "dobj", [
				["Arg1", "T4"],
				["Arg2", "T19"]
			]],
			["R19", "prep", [
				["Arg1", "T19"],
				["Arg2", "T20"]
			]],
			["R20", "det", [
				["Arg1", "T22"],
				["Arg2", "T21"]
			]],
			["R21", "pobj", [
				["Arg1", "T20"],
				["Arg2", "T22"]
			]],
			["R22", "punct", [
				["Arg1", "T1"],
				["Arg2", "T23"]
			]]
		],
		"tokens": ["In", "my", "experience", ",", "even", "in", "moderately", "sized", "applications", ",", "manually", "written", "persistence", "frameworks", "are", "the", "most", "complex", "parts", "of", "the", "application", "."],
		"entities": [
			["T1", "IN", [
				[0, 2]
			]],
			["T2", "PRP$", [
				[3, 5]
			]],
			["T3", "NN", [
				[6, 16]
			]],
			["T4", ",", [
				[17, 18]
			]],
			["T5", "RB", [
				[19, 23]
			]],
			["T6", "IN", [
				[24, 26]
			]],
			["T7", "RB", [
				[27, 37]
			]],
			["T8", "JJ", [
				[38, 43]
			]],
			["T9", "NNS", [
				[44, 56]
			]],
			["T10", ",", [
				[57, 58]
			]],
			["T11", "RB", [
				[59, 67]
			]],
			["T12", "VBN", [
				[68, 75]
			]],
			["T13", "NN", [
				[76, 87]
			]],
			["T14", "NNS", [
				[88, 98]
			]],
			["T15", "VBP", [
				[99, 102]
			]],
			["T16", "DT", [
				[103, 106]
			]],
			["T17", "RBS", [
				[107, 111]
			]],
			["T18", "JJ", [
				[112, 119]
			]],
			["T19", "NNS", [
				[120, 125]
			]],
			["T20", "IN", [
				[126, 128]
			]],
			["T21", "DT", [
				[129, 132]
			]],
			["T22", "NN", [
				[133, 144]
			]],
			["T23", ".", [
				[145, 146]
			]]
		],
		"frames": [{
			"target": {
				"name": "Expertise",
				"spans": [{
					"start": 2,
					"end": 3,
					"text": "experience"
				}]
			},
			"annotationSets": [{
				"frameElements": [{
					"name": "Protagonist",
					"spans": [{
						"start": 1,
						"end": 2,
						"text": "my"
					}]
				}],
				"score": 41.3800681269078,
				"rank": 0
			}]
		}, {
			"target": {
				"name": "Purpose",
				"spans": [{
					"start": 8,
					"end": 9,
					"text": "applications"
				}]
			},
			"annotationSets": [{
				"frameElements": [{
					"name": "Means",
					"spans": [{
						"start": 6,
						"end": 8,
						"text": "moderately sized"
					}]
				}],
				"score": 33.84536308723814,
				"rank": 0
			}]
		}, {
			"target": {
				"name": "Text_creation",
				"spans": [{
					"start": 11,
					"end": 12,
					"text": "written"
				}]
			},
			"annotationSets": [{
				"frameElements": [{
					"name": "Text",
					"spans": [{
						"start": 13,
						"end": 14,
						"text": "frameworks"
					}]
				}],
				"score": 58.50092899163075,
				"rank": 0
			}]
		}, {
			"target": {
				"name": "Process_continue",
				"spans": [{
					"start": 12,
					"end": 13,
					"text": "persistence"
				}]
			},
			"annotationSets": [{
				"frameElements": [{
					"name": "Event",
					"spans": [{
						"start": 10,
						"end": 12,
						"text": "manually written"
					}]
				}],
				"score": 34.774077298727285,
				"rank": 0
			}]
		}, {
			"target": {
				"name": "Part_whole",
				"spans": [{
					"start": 18,
					"end": 19,
					"text": "parts"
				}]
			},
			"annotationSets": [{
				"frameElements": [{
					"name": "Part",
					"spans": [{
						"start": 18,
						"end": 19,
						"text": "parts"
					}]
				}, {
					"name": "Whole",
					"spans": [{
						"start": 19,
						"end": 22,
						"text": "of the application"
					}]
				}],
				"score": 21.203969864106014,
				"rank": 0
			}]
		}, {
			"target": {
				"name": "Using",
				"spans": [{
					"start": 21,
					"end": 22,
					"text": "application"
				}]
			},
			"annotationSets": [{
				"frameElements": [],
				"score": 96.35370756985196,
				"rank": 0
			}]
		}]
	}]
}

DB_SENTENCE_3 = {
	"debug_info": {
		"frame_parser_elapsed_seconds": 0.004229,
		"dependency_parser_elapsed_seconds": 5.59412
	},
	"sentences": [{
		"conll": "1\tLarge\t_\tJJ\tJJ\t_\t2\tamod\t_\t_\n2\tprogramming\t_\tNN\tNN\t_\t3\tnsubj\t_\t_\n3\toverhead\t_\tJJ\tJJ\t_\t0\tnull\t_\t_",
		"text": "Large programming overhead",
		"relations": [
			["R1", "amod", [
				["Arg1", "T2"],
				["Arg2", "T1"]
			]],
			["R2", "nsubj", [
				["Arg1", "T3"],
				["Arg2", "T2"]
			]]
		],
		"tokens": ["Large", "programming", "overhead"],
		"entities": [
			["T1", "JJ", [
				[0, 5]
			]],
			["T2", "NN", [
				[6, 17]
			]],
			["T3", "JJ", [
				[18, 26]
			]]
		],
		"frames": [{
			"target": {
				"name": "Size",
				"spans": [{
					"start": 0,
					"end": 1,
					"text": "Large"
				}]
			},
			"annotationSets": [{
				"frameElements": [{
					"name": "Entity",
					"spans": [{
						"start": 1,
						"end": 2,
						"text": "programming"
					}]
				}],
				"score": 10.91915983618073,
				"rank": 0
			}]
		}]
	}]
}

TaxonPipeline = [
	{"$lookup":
		{"from": "taxon_node",
		"localField": "children",
		"foreignField": "_id",
		"as": "children",
		}
	},
	{"$project": 
		{"_id":0}
	}
]

OrganismPipeline = [
	{"$lookup":
		{"from": "genome",
		"localField": "genomes",
		"foreignField": "_id",
		"as": "genomes",
		}
	},
	{"$lookup":
		{"from": "annotation",
		"localField": "annotations",
		"foreignField": "_id",
		"as": "annotations",
		}
	},
	{"$lookup":
		{"from": "param_file",
		"localField": "assemblies",
		"foreignField": "param_files",
		"as": "param_files",
		}
	},
	# {"$lookup":
	# 	{"from": "taxon_node",
	# 	"localField": "taxon_lineage",
	# 	"foreignField": "_id",
	# 	"as": "taxon_lineage",
	# 	}
	# },
	{"$project": 
		{"_id":0, 
		'taxon_lineage':0,
		"genomes" : {"_id":0},
		"annotations": {"_id":0, "created":0},
		"param_files":{"_id":0}
		}
	}
]

SamplePipeline = [
	{"$lookup":
		{"from": "secondary_organism",
		"localField": "specimens",
		"foreignField": "_id",
		"as": "specimens",
		}
	},
	{"$lookup":
		{"from": "experiment",
		"localField": "experiments",
		"foreignField": "_id",
		"as": "experiments",
		}
	},
	{"$lookup":
		{"from": "assembly",
		"localField": "assemblies",
		"foreignField": "_id",
		"as": "assemblies",
		}
	},
	{"$project": 
		{"_id":0, 
        "created":0,
		"specimens": {"_id":0,"assemblies":0,"experiments":0,"specimens":0},
		"assemblies" : {"_id":0},
		"experiments": {"_id":0}

		}
	}
]
module.exports = {
    newick: `(
        (
        'Monodelphis domestica':4,
        'Capra hircus':4,
        'Sarcophilus harrisii':4
        )Mammalia:4,
        (
        (
        (
        (
        'Parus minor':4)
        Parus:4)
        Paridae:4,
        (
        (
        'Camarhynchus parvulus':4)
        Camarhynchus:4)
        Thraupidae:4,
        (
        (
        'Taeniopygia guttata':4)
        Taeniopygia:4)
        Estrildidae:4
        )Passeriformes:4,
        (
        (
        'Coturnix japonica':4)
        Coturnix:4,
        (
        'Meleagris gallopavo':4)
        Meleagris:4
        )Phasianidae:4
        )Aves:4,
        (
        (
        (
        (
        'Xenopus tropicalis':4)
        Xenopus:4)
        Pipidae:4)
        Anura:4)
        Amphibia:4,
        (
        (
        (
        (
        'Clupea harengus':4)
        Clupea:4)
        Clupeidae:4)
        Clupeiformes:4)
        Actinopteri:4
        )Chordata:4;`,
        
        treeData: {
        'name': 'root',
        'children': [
            {'name':'Chordata',
            'children': [
            {'name':'Mammalia',
                'children': [{'name':'Monodelphis domestica'},{'name':'Capra hircus'},{'name':'Sarcophilus harrisii'}]
            },
            {'name':'Aves', 
            'children': [
                {'name':'Passeriformes','children': [
                    {'name':'Paridae','children': [
                        {'name':'Parus','children':[{'name':'Parus minor'}]
                        }
                      ]
                    },
                            {'name':'Thraupidae','children': [
                                    {'name':'Camarhynchus','children':[{'name':'Camarhynchus parvulus'}]
                                    }
                                ]
                            },
                                        {'name':'Estrildidae','children':[
                                            {'name':'Taeniopygia','children':[{'name':'Taeniopygia guttata'}]}
                                            ]
                                        }
                    ]
                },
                {'name':'Phasianidae','children': [
                    {'name':'Coturnix','children':[{'name':'Coturnix japonica'}]
                    },
                    {'name':'Meleagris','children':[{'name':'Meleagris gallopavo'}]
                    }
                  ]
                }
              ]
            },
            {'name':'Amphibia','children': [
                {'name':'Anura','children':[
                    {'name': 'Pipidae','children': [
                        {'name':'Xenopus','children':[{'name':'Xenopus tropicalis'}]
                        }
                      ]
                    }
                  ]
                }
              ]
            },
            {'name':'Actinopteri','children':[
                {'name':'Clupeiformes','children': [
                    {'name':'Clupeidae','children': [
                        {'name':'Clupea','children':[{'name':'Clupea harengus'}]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
      }
    ]
  }
}
 # Auto generated by NotionInterface
GhostDefsVersion = "V1.2"
Comment = 		';'
Address =		'$'
Label =		 	':'
Data =		 	'.'
Registers = 	['R0', 'R1', 'R2', 'R3']

TypeLengths = {"Value":1, "Address":1, "Instruction":1, "RR":0} # Length in bytes of each type used below

Instructions = {
	"NOP": {
		"Bin": "00000000",
		"Arguments": "",
	},
	"STV": {
		"Bin": "00000001",
		"Arguments": "Value Address",
	},
	"MVA": {
		"Bin": "00000011",
		"Arguments": "Address Address",
	},
	"LDA": {
		"Bin": "000001RR",
		"Arguments": "RR Address",
	},
	"LDV": {
		"Bin": "000010RR",
		"Arguments": "RR Value",
	},
	"STR": {
		"Bin": "000011RR",
		"Arguments": "RR Address",
	},
	"ADA": {
		"Bin": "000100RR",
		"Arguments": "RR Address",
	},
	"ADV": {
		"Bin": "000101RR",
		"Arguments": "RR Value",
	},
	"SBA": {
		"Bin": "000110RR",
		"Arguments": "RR Address",
	},
	"SBV": {
		"Bin": "000111RR",
		"Arguments": "RR Value",
	},
	"SRA": {
		"Bin": "001000RR",
		"Arguments": "RR Address",
	},
	"SRV": {
		"Bin": "001001RR",
		"Arguments": "RR Value",
	},
	"NEG": {
		"Bin": "001010RR",
		"Arguments": "RR",
	},
	"INC": {
		"Bin": "001011RR",
		"Arguments": "RR",
	},
	"DEC": {
		"Bin": "001100RR",
		"Arguments": "RR",
	},
	"SHL1": {
		"Bin": "001101RR",
		"Arguments": "RR",
	},
	"SHR1": {
		"Bin": "001110RR",
		"Arguments": "RR",
	},
	"ANA": {
		"Bin": "001111RR",
		"Arguments": "RR Address",
	},
	"ANV": {
		"Bin": "010000RR",
		"Arguments": "RR Value",
	},
	"NNA": {
		"Bin": "010001RR",
		"Arguments": "RR Address",
	},
	"NNV": {
		"Bin": "010010RR",
		"Arguments": "RR Address",
	},
	"ORA": {
		"Bin": "010011RR",
		"Arguments": "RR Address",
	},
	"ORV": {
		"Bin": "010100RR",
		"Arguments": "RR Value",
	},
	"XRA": {
		"Bin": "010101RR",
		"Arguments": "RR Address",
	},
	"XRV": {
		"Bin": "010110RR",
		"Arguments": "RR Value",
	},
	"NOT": {
		"Bin": "010111RR",
		"Arguments": "RR",
	},
	"DDR": {
		"Bin": "011000RR",
		"Arguments": "RR",
	},
	"DDA": {
		"Bin": "01100100",
		"Arguments": "Address",
	},
	"DDV": {
		"Bin": "01100101",
		"Arguments": "Value",
	},
	"JPA": {
		"Bin": "01100110",
		"Arguments": "Value",
	},
	"JPD": {
		"Bin": "01100111",
		"Arguments": "",
	},
	"CZR": {
		"Bin": "011010RR",
		"Arguments": "RR",
	},
	"CEA": {
		"Bin": "011011RR",
		"Arguments": "RR Address",
	},
	"CEV": {
		"Bin": "011100RR",
		"Arguments": "RR Value",
	},
	"CLA": {
		"Bin": "011101RR",
		"Arguments": "RR Address",
	},
	"CLV": {
		"Bin": "011110RR",
		"Arguments": "RR Value",
	},
	"CGA": {
		"Bin": "011111RR",
		"Arguments": "RR Address",
	},
	"CGV": {
		"Bin": "100000RR",
		"Arguments": "RR Value",
	},
	"CALD": {
		"Bin": "10000100",
		"Arguments": "",
	},
	"CALA": {
		"Bin": "10000101",
		"Arguments": "Value",
	},
	"RT": {
		"Bin": "10000110",
		"Arguments": "",
	},
	"PSHL": {
		"Bin": "10001000",
		"Arguments": "",
	},
	"POPL": {
		"Bin": "10001001",
		"Arguments": "",
	},
	"RTC": {
		"Bin": "10001010",
		"Arguments": "",
	},
	"PSHR": {
		"Bin": "100011RR",
		"Arguments": "RR",
	},
	"POPR": {
		"Bin": "100100RR",
		"Arguments": "RR",
	},
	"STRR": {
		"Bin": "100101RR",
		"Arguments": "RR",
	},
	"STVR": {
		"Bin": "100110RR",
		"Arguments": "RR Value",
	},
	"LDRR": {
		"Bin": "100111RR",
		"Arguments": "RR",
	},
	"SHLV": {
		"Bin": "101000RR",
		"Arguments": "RR Value",
	},
	"SHRV": {
		"Bin": "101001RR",
		"Arguments": "RR Value",
	},
	"SHLA": {
		"Bin": "101010RR",
		"Arguments": "RR Address",
	},
	"SHRA": {
		"Bin": "101011RR",
		"Arguments": "RR Address",
	},
	"ADDR": {
		"Bin": "101110RR",
		"Arguments": "RR",
	},
	"SUBR": {
		"Bin": "101111RR",
		"Arguments": "RR",
	},
	"SBRR": {
		"Bin": "110000RR",
		"Arguments": "RR",
	},
	"SHL0": {
		"Bin": "110001RR",
		"Arguments": "RR",
	},
	"SHR0": {
		"Bin": "110010RR",
		"Arguments": "RR",
	},
	"CNZR": {
		"Bin": "110011RR",
		"Arguments": "RR",
	},
	"CZA": {
		"Bin": "11010000",
		"Arguments": "Address",
	},
	"CNZA": {
		"Bin": "11010001",
		"Arguments": "Address",
	},
	"JCA": {
		"Bin": "11010010",
		"Arguments": "Value",
	},
	"JCD": {
		"Bin": "11010011",
		"Arguments": "",
	},
	"CCA": {
		"Bin": "11010100",
		"Arguments": "Value",
	},
	"CCD": {
		"Bin": "11011001",
		"Arguments": "",
	},
	"CNEA": {
		"Bin": "110110RR",
		"Arguments": "RR Address",
	},
	"CNEV": {
		"Bin": "110111RR",
		"Arguments": "RR Value",
	},
	"BRK": {
		"Bin": "11111110",
		"Arguments": "",
	},
	"HLT": {
		"Bin": "11111111",
		"Arguments": "",
	},
}
Shorthand = {
    "ST": {
        "Value Address": "STV",
        "RR Address": "STR",
        "RR": "STRR",
        "RR Value": "STVR"
    },
    "MV": {
        "Address Address": "MVA"
    },
    "LD": {
        "RR Address": "LDA",
        "RR Value": "LDV",
        "RR": "LDRR"
    },
    "ADD": {
        "RR Address": "ADA",
        "RR Value": "ADV",
        "RR": "ADDR"
    },
    "SUB": {
        "RR Address": "SBA",
        "RR Value": "SBV",
        "RR": "SUBR"
    },
    "SBR": {
        "RR Address": "SRA",
        "RR Value": "SRV",
        "RR": "SBRR"
    },
    "SHL": {
        "RR": "SHL1",
        "RR Value": "SHLV",
        "RR Address": "SHLA"
    },
    "SHR": {
        "RR": "SHR1",
        "RR Value": "SHRV",
        "RR Address": "SHRA"
    },
    "AND": {
        "RR Address": "ANA",
        "RR Value": "ANV"
    },
    "NAND": {
        "RR Address": "NNV"
    },
    "OR": {
        "RR Address": "ORA",
        "RR Value": "ORV"
    },
    "XOR": {
        "RR Address": "XRA",
        "RR Value": "XRV"
    },
    "DD": {
        "RR": "DDR",
        "Address": "DDA",
        "Value": "DDV"
    },
    "JMP": {
        "Value": "JPA",
        "": "JPD"
    },
    "CZ": {
        "RR": "CZR",
        "Address": "CZA"
    },
    "CE": {
        "RR Address": "CEA",
        "RR Value": "CEV"
    },
    "CL": {
        "RR Address": "CLA",
        "RR Value": "CLV"
    },
    "CG": {
        "RR Address": "CGA",
        "RR Value": "CGV"
    },
    "CALL": {
        "": "CALD",
        "Value": "CALA"
    },
    "RET": {
        "": "RT"
    },
    "PSH": {
        "": "PSHL",
        "RR": "PSHR"
    },
    "POP": {
        "": "POPL",
        "RR": "POPR"
    },
    "RETC": {
        "": "RTC"
    },
    "CNZ": {
        "RR": "CNZR",
        "Address": "CNZA"
    },
    "JMPC": {
        "Value": "JCA",
        "": "JCD"
    },
    "CALLC": {
        "Value": "CCA",
        "": "CCD"
    },
    "CNE": {
        "RR Address": "CNEA",
        "RR Value": "CNEV"
    }
}
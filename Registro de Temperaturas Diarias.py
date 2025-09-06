# Lista de ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Matriz 3D con datos de temperaturas (3 ciudades x 4 semanas x 7 días)
temperaturas = [

    # Ciudad 1: Quito (10 °C - 20 °C)
    [
        # Semana 1
        [
            {"día": "Lunes", "temperatura": 12},
            {"día": "Martes", "temperatura": 13},
            {"día": "Miércoles", "temperatura": 14},
            {"día": "Jueves", "temperatura": 15},
            {"día": "Viernes", "temperatura": 16},
            {"día": "Sábado", "temperatura": 17},
            {"día": "Domingo", "temperatura": 14}
        ],
        # Semana 2
        [
            {"día": "Lunes", "temperatura": 13},
            {"día": "Martes", "temperatura": 14},
            {"día": "Miércoles", "temperatura": 15},
            {"día": "Jueves", "temperatura": 16},
            {"día": "Viernes", "temperatura": 17},
            {"día": "Sábado", "temperatura": 18},
            {"día": "Domingo", "temperatura": 15}
        ],
        # Semana 3
        [
            {"día": "Lunes", "temperatura": 11},
            {"día": "Martes", "temperatura": 12},
            {"día": "Miércoles", "temperatura": 13},
            {"día": "Jueves", "temperatura": 14},
            {"día": "Viernes", "temperatura": 15},
            {"día": "Sábado", "temperatura": 16},
            {"día": "Domingo", "temperatura": 12}
        ],
        # Semana 4
        [
            {"día": "Lunes", "temperatura": 14},
            {"día": "Martes", "temperatura": 15},
            {"día": "Miércoles", "temperatura": 16},
            {"día": "Jueves", "temperatura": 17},
            {"día": "Viernes", "temperatura": 18},
            {"día": "Sábado", "temperatura": 19},
            {"día": "Domingo", "temperatura": 16}
        ]
    ],

    # Ciudad 2: Guayaquil (25 °C - 34 °C)
    [
        # Semana 1
        [
            {"día": "Lunes", "temperatura": 28},
            {"día": "Martes", "temperatura": 29},
            {"día": "Miércoles", "temperatura": 30},
            {"día": "Jueves", "temperatura": 31},
            {"día": "Viernes", "temperatura": 30},
            {"día": "Sábado", "temperatura": 29},
            {"día": "Domingo", "temperatura": 28}
        ],
        # Semana 2
        [
            {"día": "Lunes", "temperatura": 29},
            {"día": "Martes", "temperatura": 30},
            {"día": "Miércoles", "temperatura": 31},
            {"día": "Jueves", "temperatura": 32},
            {"día": "Viernes", "temperatura": 31},
            {"día": "Sábado", "temperatura": 30},
            {"día": "Domingo", "temperatura": 29}
        ],
        # Semana 3
        [
            {"día": "Lunes", "temperatura": 27},
            {"día": "Martes", "temperatura": 28},
            {"día": "Miércoles", "temperatura": 29},
            {"día": "Jueves", "temperatura": 30},
            {"día": "Viernes", "temperatura": 29},
            {"día": "Sábado", "temperatura": 28},
            {"día": "Domingo", "temperatura": 27}
        ],
        # Semana 4
        [
            {"día": "Lunes", "temperatura": 30},
            {"día": "Martes", "temperatura": 31},
            {"día": "Miércoles", "temperatura": 32},
            {"día": "Jueves", "temperatura": 33},
            {"día": "Viernes", "temperatura": 32},
            {"día": "Sábado", "temperatura": 31},
            {"día": "Domingo", "temperatura": 30}
        ]
    ],

    # Ciudad 3: Cuenca (12 °C - 22 °C)
    [
        # Semana 1
        [
            {"día": "Lunes", "temperatura": 15},
            {"día": "Martes", "temperatura": 16},
            {"día": "Miércoles", "temperatura": 17},
            {"día": "Jueves", "temperatura": 18},
            {"día": "Viernes", "temperatura": 17},
            {"día": "Sábado", "temperatura": 16},
            {"día": "Domingo", "temperatura": 15}
        ],
        # Semana 2
        [
            {"día": "Lunes", "temperatura": 16},
            {"día": "Martes", "temperatura": 17},
            {"día": "Miércoles", "temperatura": 18},
            {"día": "Jueves", "temperatura": 19},
            {"día": "Viernes", "temperatura": 18},
            {"día": "Sábado", "temperatura": 17},
            {"día": "Domingo", "temperatura": 16}
        ],
        # Semana 3
        [
            {"día": "Lunes", "temperatura": 14},
            {"día": "Martes", "temperatura": 15},
            {"día": "Miércoles", "temperatura": 16},
            {"día": "Jueves", "temperatura": 17},
            {"día": "Viernes", "temperatura": 16},
            {"día": "Sábado", "temperatura": 15},
            {"día": "Domingo", "temperatura": 14}
        ],
        # Semana 4
        [
            {"día": "Lunes", "temperatura": 18},
            {"día": "Martes", "temperatura": 19},
            {"día": "Miércoles", "temperatura": 20},
            {"día": "Jueves", "temperatura": 21},
            {"día": "Viernes", "temperatura": 20},
            {"día": "Sábado", "temperatura": 19},
            {"día": "Domingo", "temperatura": 18}
        ]
    ]
]

# Calcular y mostrar promedios semanales
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedios semanales de {ciudad}:")
    for semana_idx, semana in enumerate(temperaturas[i]):
        suma = 0
        for dia in semana:
            suma += dia["temperatura"]
        promedio = suma / len(semana)
        print(f"  Semana {semana_idx + 1}: {promedio:.2f} °C")
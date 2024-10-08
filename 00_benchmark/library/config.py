# Integrator Settings
INTEGRATOR_ERROR=1.0e-7
INTEGRATOR_TYPE="hht"

# Simulation Settings
END_TIME = 0.3

NUM_THREADS = 16
NUMBER_OF_STEPS = 10

# Path to the job files (jsons)
PATH_TO_JSON = "./jobs/"

# ALl items and the floor are translated in y direction up to this value
HEIGHT_FACTOR = 7

# Material Settings for Items
MATERIAL_YOUNGS_MODULUS=2.85E+5
MATERIAL_POISSONS_RATIO=0.29
MATERIAL_G_xz = 1.4E+4
MATERIAL_G_xy = 3.7E+3

# Material Settings Aluminium for ULDs
MATERIAL_GROUND_YOUNGS_MODULUS=7.31E+7
MATERIAL_GROUND_POISSONS_RATIO=0.35
MATERIAL_GROUND_DENSITY=0.00279
MATERIAL_GROUND_NAME='Aluminium'

# Friction Settings
DYNAMIC_FRICTION=0.375
STATIC_FRICTION=0.5
STICTION_TRANSITION_VELOCITY=0.01
FRICTION_TRANSITION_VELOCITY=1.0

# Normal force Settings for Items
STIFFNESS = 6E7
EXPONENT = 1.2
DMAX = 0.001
DAMPING = 800

# Units Settings
GRAVITY = [0, -980, 0]
UNITS_LENGTH = 'cm'
UNITS_MASS = 'kg'
UNITS_TIME = 'second'
UNITS_ANGLE = 'degrees'

# Measurements Settings
KEY_TRANSLATION = "translation"
KEY_ROTATION = "rotation"
KEY_ANGULAR_MOMENTUM_ABOUT_CM = "angular_momentum_about_cm"
KEY_CM_ANGULAR_VELOCITY = "cm_angular_velocity"
KEY_CM_ANGULAR_ACCELERATION = "cm_angular_acceleration"
KEY_CM_ACCELERATION = "cm_acceleration"
KEY_CM_POSITION = "cm_position"
KEY_CM_VELOCITY = "cm_velocity"
KEY_CONTACTS = "contacts"

OBJECT_MEASUREMENT_KEY = [
    KEY_ANGULAR_MOMENTUM_ABOUT_CM,
    KEY_CM_ANGULAR_VELOCITY,
    KEY_CM_ANGULAR_ACCELERATION,
    KEY_CM_ACCELERATION,
    KEY_CM_POSITION,
    KEY_CM_VELOCITY
]
ALL_MEASUREMENT_KEYS = OBJECT_MEASUREMENT_KEY + [
    KEY_TRANSLATION,
    KEY_ROTATION
]
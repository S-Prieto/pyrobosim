# Robot state definition message

# Robot information
string name

# Continuous state
geometry_msgs/Pose pose
int16 battery_level

# Discrete state
bool executing_action
bool holding_object
string manipulated_object
string current_location


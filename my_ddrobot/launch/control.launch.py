import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
import xacro

def generate_launch_description():
    robotXacroName = 'my_dd_robot'

    namePkg = 'my_ddrobot'

    modelFileRelPath = 'model/my_dd_robot_model.xacro'
    worldFileRelPath = 'model/empty_world.world'

    # Paths for the model and world files
    pathModelFile = os.path.join(get_package_share_directory(namePkg), modelFileRelPath)
    pathWorldFile = os.path.join(get_package_share_directory(namePkg), worldFileRelPath)

    # Convert the Xacro file to robot description XML
    robotDescription = xacro.process_file(pathModelFile).toxml()

    # Gazebo launch file
    gazebo_ros_pkg_launch = PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py'))
    gazeboLaunch = IncludeLaunchDescription(gazebo_ros_pkg_launch, launch_arguments={'world': pathWorldFile}.items())

    # Spawn the robot in Gazebo
    spawnModelNode = Node(package='gazebo_ros', executable='spawn_entity.py', 
                          arguments=['-topic', 'robot_description', '-entity', robotXacroName], output='screen')

    # Robot state publisher to broadcast robot's URDF to tf
    nodeRobotStatePub = Node(package='robot_state_publisher', executable='robot_state_publisher',
                             output='screen', parameters=[{'robot_description': robotDescription, 'use_sim_time': True}])

    # Teleoperation control nodes for the robot
    carControlNode = Node(package='my_ddrobot', executable='car_control', name='car_control', output='screen')
    turretControlNode = Node(package='my_ddrobot', executable='turret_control', name='turret_control', output='screen')
    nozzleControlNode = Node(package='my_ddrobot', executable='nozzle_control', name='nozzle_control', output='screen')
    teleopArmLink1Node = Node(package='my_ddrobot', executable='teleop_arm_link_1', name='teleop_arm_link_1', output='screen')
    teleopArmLink2Node = Node(package='my_ddrobot', executable='teleop_arm_link_2', name='teleop_arm_link_2', output='screen')
    moveAgvNode = Node(package='my_ddrobot', executable='move_agv', name='move_agv', output='screen')  # Add the new move_agv control node

    # Launch description
    launchDescriptionObj = LaunchDescription()

    # Add all the actions to the launch description
    launchDescriptionObj.add_action(gazeboLaunch)
    launchDescriptionObj.add_action(spawnModelNode)
    launchDescriptionObj.add_action(nodeRobotStatePub)

    # Add teleop control nodes
    launchDescriptionObj.add_action(carControlNode)
    launchDescriptionObj.add_action(turretControlNode)
    launchDescriptionObj.add_action(nozzleControlNode)
    launchDescriptionObj.add_action(teleopArmLink1Node)
    launchDescriptionObj.add_action(teleopArmLink2Node)
    launchDescriptionObj.add_action(moveAgvNode)  # Add move_agv control

    return launchDescriptionObj

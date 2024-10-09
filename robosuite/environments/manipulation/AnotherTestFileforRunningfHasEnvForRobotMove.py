import numpy as np
from robosuite.environments.manipulation.lift import Lift

my_controller_config = None  

env = Lift(
    robots=["Sawyer"],               # Specify the robot
    use_camera_obs=False,            # Disable camera observations
    has_renderer=True,               # Enable rendering
    render_camera="frontview",       # Specify the camera view
    control_freq=500,                 # Control frequency
    horizon=1000,                    # Number of steps per episode
    reward_scale=1.0,                # Reward scale
    initialization_noise=None,       # Initialization noise
    controller_configs=my_controller_config  # Controller configuration
)

#breakpoint()

 # make robot raise the arm


gravity_down = [0, 0, -9.81]  
gravity_off = [0, 0, 0]  
switch_i_frequency = 300 # other nums don't let it switch fast enought it just keeps going down

# Main simulation loop

for i in range(2000):
    action = np.zeros(8)
    if (i // switch_i_frequency) % 2 == 0:
        action[0] = 5000
        action[1] = 1000  # Apply downward force to joint 2 (you may need to adjust this joint)
        print(f"Iteration {i}: Moving down")
        action[2] = 10000
        action[3] = 1000 # Set all joints to stationary
        action[4] = 0
        action[5] = 0
        action[6] = 0
        action[7] = 0
        # action[8] = 0

    else:
        action[0] = -5000
        action[1] = -1000  # Apply upward force to joint 2 (I may need to adjust this joint)
        print(f"Iteration {i}: Moving up")
        action[2] = -10000
        action[3] = -1000 
        action[4] = 0
        action[5] = 0
        action[6] = 0
        action[7] = 0
        action[8] = 0

    #env.sim.data.ctrl[:] = action
    reward, done = env.stepFunction(action)  # Take action in the environment
    reward = env.reward(action)
    obs, reward, done, info = env.step(action)
    env.render()  # Render the simulation

    print("Joint positions:", env.sim.data.qpos)

    #print("Joint velocities:", env.sim.data.qvel)

env.reset()


# train it through the rl policy


  






# import robosuite as suite

# env = suite.make('Lift')  # or some other registered name


# # create environment instance
# env = suite.make(
#     env_name="Lift", # try with other tasks like "Stack" and "Door"
#     robots="Sawyer",  # try with other robots like "Sawyer" and "Jaco"
#     has_renderer=True, # was True but I  Disable on-screen rendering
#     has_offscreen_renderer=False, # was False but I Enable off-screen rendering to avoid failure of sim
#     use_camera_obs=False,
# )


# # reset the environment
# env.reset()

# # TODO: write a custom function in door.py "play_with_keyboard"
# # TODO: in that function, get user input with input('...')
# # TODO: based on the keys pressed (wasd), move the robot's base
# # 
# # Define a controlled action that will move the robot's arm up and down
# # Main loop to control the robot
# # Assuming env is an instance of Lift class
# # for i in range(1000):
# #     action = np.zeros(env.robots[0].dof)  # Define action for moving the arm
    
# #     # Move along the Z-axis (up and down)
# #     if i % 100 < 50:
# #         action[2] = 0.05  # Move up
# #     else:
# #         action[2] = -0.05  # Move down
    
# #     obs, reward, done, info = env.stepFunction(action)  # Use the stepFunction
# #     env.render()  # Render the environment

# # Initialize an upward movement along the z-axis
# # Initialize an action array of the correct size (8 in this case)


# # for i in range(500):
# #     # Move the arm up
# #     action = np.zeros(8)
# #     action[0] = 0.1  # Assuming the z-axis is the third element in the array
# #     obs, reward, done, info = env.step(action)  # take action
# #     env.render()  # render the simulation

# # # Then move it down
# # for i in range(500):
# #     action = np.zeros(8)
# #     action[0] = -0.1  # Move down along the z-axis
# #     obs, reward, done, info = env.step(action)  # take action
# #     env.render()  # render the simulation


# for i in range(1000):
#     action = np.random.randn(env.robots[0].dof) # sample random action
#     obs, reward, done, info = env.step(action)  # take action in the environment
#     env.render()  # render on display

#     # for i in range(1000):
#     # action = np.zeros(env.robots[0].dof)  # Create a zero action for all joints
#     # action[2] = 0.05 * np.sin(i * 0.01)  # Move the z-axis (3rd DoF) in a sinusoidal pattern
#     # obs, reward, done, info = env.step(action)  # Take the action
#     # env.render()  # Render the environment

import gym
from stable_baselines3 import PPO, A2C, DQN
from stable_baselines3.common.vec_env import DummyVecEnv, VecTransposeImage

models_dir = "models/PPO_freeway"

# Create the environment
env = gym.make('ALE/Freeway-v5',  difficulty=1, render_mode="human")
env = DummyVecEnv([lambda: env])
env = VecTransposeImage(env)

# Load the trained model
model_path = f"{models_dir}/1200000"
#model_path = f"{models_dir}/1300000"
model = PPO.load(model_path, env=env)

episodes = 5

for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        env.render()
        print(rewards)

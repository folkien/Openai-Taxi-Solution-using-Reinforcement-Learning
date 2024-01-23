# Openai-Taxi-Solution-using-Reinforcement-Learning
Reinforcement Learning DQN - using OpenAI taxi environment 
 
 -> Tensorflow
 
 -> Keras
 
 -> gym
 
 In the OpenAI taxi environment, a taxi and a passenger are randomly postioned in a 5x5 grid. Goal of the taxi is to go to the passenger's location, pick the passenger and drop them of at the destination location. 
 
 ![Screenshot from 2022-09-24 16-50-15](https://user-images.githubusercontent.com/74414105/192096453-cfbdfc73-8266-4aa0-a603-1187d3094c88.png)

The agent was trained using Deep-Q-Learning in about 13000 episodes with an average reward of above 8. 



# Here is a preview of the agnet playing the game:


https://user-images.githubusercontent.com/74414105/192096573-c64b84e3-84d4-4c7b-a0a4-5b0af9e7360e.mp4

# Train & Test

The agent can be trained by running the "train.py" file keep in mind that it takes some time for the model to train. The model can be tested by running the "test.py" file, it'll create and save a video of the agent playing the game.


# Training results

```bash
Episode 100 | Total point average of the last 100 episodes: -1006.77
Episode 200 | Total point average of the last 100 episodes: -887.637
Episode 300 | Total point average of the last 100 episodes: -734.51
Episode 400 | Total point average of the last 100 episodes: -720.86
Episode 500 | Total point average of the last 100 episodes: -567.80
Episode 600 | Total point average of the last 100 episodes: -646.54
Episode 700 | Total point average of the last 100 episodes: -416.94
Episode 800 | Total point average of the last 100 episodes: -357.21
Episode 900 | Total point average of the last 100 episodes: -253.84
Episode 1000 | Total point average of the last 100 episodes: -182.80
Episode 1100 | Total point average of the last 100 episodes: -177.46
Episode 1200 | Total point average of the last 100 episodes: -154.07
Episode 1300 | Total point average of the last 100 episodes: -154.91
Episode 1400 | Total point average of the last 100 episodes: -63.535
Episode 1500 | Total point average of the last 100 episodes: -68.08
Episode 1600 | Total point average of the last 100 episodes: -40.11
Episode 1700 | Total point average of the last 100 episodes: 0.7712
Episode 1800 | Total point average of the last 100 episodes: -12.01
Episode 1900 | Total point average of the last 100 episodes: -11.38
Episode 2000 | Total point average of the last 100 episodes: 2.0210
Episode 2100 | Total point average of the last 100 episodes: -0.01
Episode 2200 | Total point average of the last 100 episodes: -4.441
Episode 2300 | Total point average of the last 100 episodes: 3.872
Episode 2400 | Total point average of the last 100 episodes: 1.60
Episode 2500 | Total point average of the last 100 episodes: 4.593
Episode 2600 | Total point average of the last 100 episodes: 6.14
Episode 2700 | Total point average of the last 100 episodes: 7.01
Episode 2800 | Total point average of the last 100 episodes: 5.89
Episode 2900 | Total point average of the last 100 episodes: 7.03
Episode 3000 | Total point average of the last 100 episodes: 5.65
Episode 3100 | Total point average of the last 100 episodes: 5.06
Episode 3200 | Total point average of the last 100 episodes: 7.11
Episode 3300 | Total point average of the last 100 episodes: 6.39
Episode 3400 | Total point average of the last 100 episodes: 6.53
Episode 3500 | Total point average of the last 100 episodes: 5.71
Episode 3600 | Total point average of the last 100 episodes: 6.43
Episode 3700 | Total point average of the last 100 episodes: 5.50
Episode 3800 | Total point average of the last 100 episodes: 6.90
Episode 3900 | Total point average of the last 100 episodes: 6.13
Episode 4000 | Total point average of the last 100 episodes: 7.29
Episode 4100 | Total point average of the last 100 episodes: 4.92
Episode 4200 | Total point average of the last 100 episodes: 4.74
Episode 4300 | Total point average of the last 100 episodes: 7.02
Episode 4400 | Total point average of the last 100 episodes: 7.37
Episode 4500 | Total point average of the last 100 episodes: 6.82
Episode 4600 | Total point average of the last 100 episodes: 5.06
Episode 4700 | Total point average of the last 100 episodes: 6.62
Episode 4800 | Total point average of the last 100 episodes: 7.34
Episode 4900 | Total point average of the last 100 episodes: 6.61
Episode 5000 | Total point average of the last 100 episodes: 6.10
Episode 5100 | Total point average of the last 100 episodes: 7.00
Episode 5200 | Total point average of the last 100 episodes: 6.69
Episode 5300 | Total point average of the last 100 episodes: 7.12
Episode 5400 | Total point average of the last 100 episodes: 6.51
Episode 5500 | Total point average of the last 100 episodes: 7.25
Episode 5600 | Total point average of the last 100 episodes: 7.00
Episode 5700 | Total point average of the last 100 episodes: 7.02
Episode 5800 | Total point average of the last 100 episodes: 6.64
Episode 5900 | Total point average of the last 100 episodes: 7.07
Episode 6000 | Total point average of the last 100 episodes: 6.81
Episode 6100 | Total point average of the last 100 episodes: 7.07
Episode 6200 | Total point average of the last 100 episodes: 7.20
Episode 6300 | Total point average of the last 100 episodes: 6.44
Episode 6400 | Total point average of the last 100 episodes: 6.69
Episode 6500 | Total point average of the last 100 episodes: 7.02
Episode 6600 | Total point average of the last 100 episodes: 7.36
Episode 6700 | Total point average of the last 100 episodes: 7.81
Episode 6800 | Total point average of the last 100 episodes: 5.46
Episode 6900 | Total point average of the last 100 episodes: 6.70
Episode 7000 | Total point average of the last 100 episodes: 6.83
Episode 7100 | Total point average of the last 100 episodes: 7.03
Episode 7200 | Total point average of the last 100 episodes: 6.28
Episode 7300 | Total point average of the last 100 episodes: 7.09
Episode 7400 | Total point average of the last 100 episodes: 7.26
Episode 7500 | Total point average of the last 100 episodes: 6.72
Episode 7600 | Total point average of the last 100 episodes: 7.05
Episode 7700 | Total point average of the last 100 episodes: 6.48
Episode 7800 | Total point average of the last 100 episodes: 6.71
Episode 7900 | Total point average of the last 100 episodes: 7.14
Episode 8000 | Total point average of the last 100 episodes: 7.28
Episode 8100 | Total point average of the last 100 episodes: 7.77
Episode 8200 | Total point average of the last 100 episodes: 6.87
Episode 8300 | Total point average of the last 100 episodes: 6.94
Episode 8400 | Total point average of the last 100 episodes: 7.02
Episode 8500 | Total point average of the last 100 episodes: 6.45
Episode 8600 | Total point average of the last 100 episodes: 7.07
Episode 8700 | Total point average of the last 100 episodes: 5.95
Episode 8800 | Total point average of the last 100 episodes: 6.90
Episode 8900 | Total point average of the last 100 episodes: 7.46
Episode 9000 | Total point average of the last 100 episodes: 6.79
Episode 9100 | Total point average of the last 100 episodes: 6.92
Episode 9200 | Total point average of the last 100 episodes: 6.76
Episode 9300 | Total point average of the last 100 episodes: 7.10
Episode 9400 | Total point average of the last 100 episodes: 6.53
Episode 9500 | Total point average of the last 100 episodes: 6.70
Episode 9600 | Total point average of the last 100 episodes: 6.72
Episode 9700 | Total point average of the last 100 episodes: 6.82
Episode 9800 | Total point average of the last 100 episodes: 7.28
Episode 9900 | Total point average of the last 100 episodes: 6.63
Episode 10000 | Total point average of the last 100 episodes: 6.97
Episode 10100 | Total point average of the last 100 episodes: 7.10
Episode 10200 | Total point average of the last 100 episodes: 7.58
Episode 10300 | Total point average of the last 100 episodes: 7.10
Episode 10400 | Total point average of the last 100 episodes: 7.33
Episode 10500 | Total point average of the last 100 episodes: 6.69
Episode 10600 | Total point average of the last 100 episodes: 6.12
Episode 10700 | Total point average of the last 100 episodes: 6.99
Episode 10800 | Total point average of the last 100 episodes: 6.88
Episode 10900 | Total point average of the last 100 episodes: 7.52
Episode 10934 | Total point average of the last 100 episodes: 8.00 
Environment solved in 10934 episodes!
```
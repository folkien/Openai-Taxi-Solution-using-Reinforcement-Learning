import logging
import imageio
logging.getLogger().setLevel(logging.ERROR)

q_network = tf.keras.models.load_model('taxi_model.h5')

def create_video(filename, env, q_network, fps=30):
  video = imageio.get_writer(filename, fps=fps)
  done = False
  state = env.reset()
  frame = env.render(mode="rgb_array")
  video.append_data(frame)
  while not done:
    state, _ = get_one_hot_encoding(state, 0)
    state = np.expand_dims(state, axis=0)
    q_values = q_network(state)
    action = np.argmax(q_values.numpy()[0])
    state, _, done, _ = env.step(action)
    frame = env.render(mode="rgb_array")
    video.append_data(frame)
    for k in range(20):
      video.append_data(frame)

filename = "./taxi.mp4"

create_video(filename, env, q_network)

import matplotlib.pyplot as plt
import numpy as np

def initialize_plots():
    fig, axis = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot for estimated Pi value
    axis[0].set_title('Estimating Pi Value')
    axis[0].set_xlim([0, 1000])
    axis[0].set_ylim([0, 10])
    axis[0].grid(True)
    
    # Plot for random dots
    axis[1].set_title('Random Dots')
    axis[1].set_aspect('equal')
    axis[1].set_xlim([-1, 1])
    axis[1].set_ylim([-1, 1])
    
    return fig, axis

def update_plots(axis, xdots, ydots, dotsloc, pi_values, cnt, total_dots):
    
    axis[0].clear()
    axis[0].plot(range(1, len(pi_values) + 1), pi_values, color='black')
    axis[0].set_title(f'Estimated Pi Value: {pi_values[-1]:.5f}')
    axis[0].set_xlim([0, len(pi_values) + 1000])
    axis[0].set_ylim([pi_values[-1] - 1/pi_values[-1], pi_values[-1] + 1/pi_values[-1]])
    axis[0].grid(True)
    
    axis[1].clear()
    axis[1].scatter(xdots, ydots, c=dotsloc, s=5)
    axis[1].set_title(f'Pink Dots: {cnt}, Yellow Dots: {total_dots - cnt}')
    axis[1].set_aspect('equal')
    axis[1].set_xlim([-1, 1])
    axis[1].set_ylim([-1, 1])

    plt.draw()
    plt.pause(0.01)

def estimate_pi(num_samples=100000, update_interval=100):
    fig, axis = initialize_plots()
    
    xdots, ydots, dotsloc, pi_values = [], [], [], []
    cnt = 0
    
    for i in range(1, num_samples + 1):
        x, y = np.random.uniform(-1, 1, 2)
        
        xdots.append(x)
        ydots.append(y)
        
        if x**2 + y**2 <= 1:  #inside the circle
            cnt += 1
            dotsloc.append('pink')
        else:
            dotsloc.append('yellow')
        
        pi_value = 4 * (cnt / i)
        pi_values.append(pi_value)
        
        if i % update_interval == 0:
            update_plots(axis, xdots, ydots, dotsloc, pi_values, cnt, i)
    
    plt.show()


estimate_pi()
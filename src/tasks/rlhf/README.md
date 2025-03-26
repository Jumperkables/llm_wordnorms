# RLHF
I'll put documentation and my detail oriented and theoretical learnings here

## Scripts
- `rlhf_trl.py`
    * RLHF using the `trl` pypi package. An industry standard
- `rlhf.py`
    * RLHF 'manually' if i feel like it to say that i did 

## Theory
- PPO: Proximal Policy Optimisation
    * The actual reinforcement learning algorithm
    * Aims to stop the model changing too much:
        + $\text{clip}(r_t(\theta), 1 - \epsilon, 1 + \epsilon)$
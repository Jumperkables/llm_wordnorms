# RLHF
I'll put documentation and my detail oriented and theoretical learnings here

## Scripts
- `rlhf_trl.py`
    * RLHF using the `trl` pypi package. An industry standard
- `rlhf.py`
    * RLHF 'manually' if i feel like it to say that i did 

## Theory
- PPO: Proximal Policy Optimisation
    * $L(\theta) = \mathbb{E}[\text{min}(r_t(\theta))A_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)]$
    * The actual reinforcement learning algorithm
    * Aims to stop the model changing too much by clipping the **probability ratio** $r_t(\theta)$:
        + $\text{clip}(r_t(\theta), 1 - \epsilon, 1 + \epsilon)$
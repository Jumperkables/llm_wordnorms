# RLHF
I'll put documentation and my detail oriented and theoretical learnings here

## Scripts
- `rlhf_trl.py`
    * RLHF using the `trl` pypi package. An industry standard
- `rlhf.py`
    * RLHF 'manually' if i feel like it to say that i did 

## Theory
- Previous Candidate for Policy Objective
    * $L^{PG}(\theta) = E_t[log\pi_\theta(a_t|s_t) * A_t]$
        + $log\pi_\theta(a_t|s_t)$: log probability of an action at this state
        + $A_t$ advantage function, if >0 then this action is deemed better than the other action possible at this state
    * Problems with this:
        + Small step sizes meant training was too low
        + Larger step sizes added too much variability, we are trying to minimise losing good pretraining

- PPO: Proximal Policy Optimisation
    * $L(\theta) = \mathbb{E}[\text{min}(r_t(\theta))A_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)]$
    * The actual reinforcement learning algorithm
    * Aims to stop the model changing too much by clipping the **probability ratio** $r_t(\theta)$:
        + $\text{clip}(r_t(\theta), 1 - \epsilon, 1 + \epsilon)$
    * There is a ratio function:
        * $r_t(\theta) = \pi_\theta(a_t|s_t)/\pi_{\theta_{old}}(a_t|s_t)$
        * $r_t(\theta) > 1 \implies$ the action $a_t$ at state $s_t$ is more likely than the old policy
        * $1 > r_t(\theta) > 0 \implies$ the action is less likely that current
    * Example:
        + Prompt: e.g. "Describe an apple"
        + Action $a_t$: is the next token/full output predicted = "A round red fruit"
        + Policy $\pi_\theta(a_t|s_t)$: probability given by the model
        + Reward signal: $r_t$: Reawrd function
        + Reference model is supplied as a frozen copy so the trained model doesn't deviate too far
    * 
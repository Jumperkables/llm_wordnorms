# LLM Word Norms
LLM Finetuning Using Neurolinguistic Word Norms

## Setup Instructions
Assume `ROOT` to be the root of this repo
1. Acquire a Llama model
    * `mkdir ROOT/reuslts`
    * Acquire them [here](https://www.llama.com/llama-downloads/)
    * This has only been tested with Llama3.2-1B
    * The models own root folder should sit in `ROOT/models/` e.g.
        - `ROOT/models/`
            + `Llama3.2-1B/`
                - `checklist.chk`
                - `consolidated.00.pth`
                - `params.json`
                - `tokenizer.model`
2. Convert the model to a suitable format for quantisation
    * Acquire [this](https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/convert_llama_weights_to_hf.py) script. Running docs [are here](https://huggingface.co/docs/transformers/en/model_doc/llama).
    * Get that script
        + `python convert_llama_weights_to_hf.py --llama_version 3 --input_dir models/Llama3.2-1B --model_size 1B --output_dir models/Llama3.2-1B_CONVERTED`
            - Be aware you may be prompted for many different pypi package installs
            - You may have to bugfix this command depending on version
        + Whatever your output path is, you should change the `LLAMA_CONVERTED_PATH` variable in `ROOT/src/config.py` 
    * Output folder should contain something like
        + `config.json`
        + `generation_config.json`
        + `model.safetensors`
        + `special_tokens_map.json`
        + `tokenizer_config.json`
        + `tokenizer.json`

3. Test the approximate BSZ you can get away with for your GPU
    * This will be needed to fit on consumer GPUs (my 1080ti is 11GB VRAM)
    * `python -m src.test_bsz_q4`

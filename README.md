# Large Language Model from Scratch

Production-ready transformer-based language model implemented from first principles in Python, without using pre-built model libraries.

## Overview

A complete implementation of the transformer architecture used in GPT-style models, including tokenization, training infrastructure, and inference optimization.

## Architecture

### Model Specifications
- Layers: 12 transformer blocks
- Hidden Dimension: 768
- Attention Heads: 12
- Feed-Forward Dimension: 3072
- Vocab Size: 50,257 (GPT-2 compatible)
- Max Sequence Length: 1024
- Total Parameters: ~124M

### Core Components

#### 1. Tokenizer (BPE)
- Implements Byte-Pair Encoding algorithm from scratch
- Learns vocabulary through iterative merging of frequent token pairs
- Compatible with GPT-2 tokenization scheme

#### 2. Transformer Blocks
- **Multi-Head Self-Attention**: 12 parallel attention heads
- **Positional Encoding**: Sinusoidal positional embeddings
- **Feed-Forward Networks**: 2-layer MLP with GELU activation
- **Layer Normalization**: Applied pre-attention and pre-MLP

#### 3. Training Pipeline
- **Gradient Accumulation**: Support for larger effective batch sizes
- **Mixed Precision Training**: FP16 computation with FP32 master weights
- **Learning Rate Scheduling**: Cosine annealing with warmup
- **Distributed Data Parallel**: Multi-GPU training support

## Results

### Training Metrics
- **Dataset**: WikiText-103 (100M tokens)
- **Batch Size**: 32 (with 4x gradient accumulation = 128 effective)
- **Learning Rate**: 1e-4 (cosine annealing, 10k warmup steps)
- **Training Time**: ~72 hours on single A100 GPU

### Performance
- **Final Perplexity**: 45.2
- **Validation Loss**: 3.81
- **Inference Speed**: ~95 tokens/sec (batch=1, seq_len=512)
- **Memory Usage**: 18GB (FP16, batch=32)

## Usage

### Training
```python
from llm import TransformerLM, BPETokenizer, Trainer

model = TransformerLM(vocab_size=50257, hidden_dim=768, num_layers=12, num_heads=12)
tokenizer = BPETokenizer(vocab_size=50257)

trainer = Trainer(
    model=model,
    tokenizer=tokenizer,
    learning_rate=1e-4,
    mixed_precision=True,
    gradient_accumulation_steps=4
)

trainer.train(train_dataset=dataset, num_epochs=3, eval_steps=1000)
```

### Inference
```python
model.eval()
prompt = "The future of AI is"
tokens = tokenizer.encode(prompt)
output = model.generate(tokens, max_length=128, temperature=0.8, top_k=40)
text = tokenizer.decode(output)
print(text)
```

## Key Files

- `tokenizer.py` - BPE tokenizer implementation
- `transformer.py` - Core transformer model
- `attention.py` - Multi-head self-attention
- `training.py` - Training loop with mixed precision
- `inference.py` - Beam search and decoding
- `evaluate.py` - Perplexity computation

## Technical Highlights

✅ Built from scratch with only PyTorch primitives
✅ Production-grade code with type hints and error handling
✅ Mixed precision training and gradient accumulation
✅ Comprehensive documentation and examples
✅ Performance optimized (95 tokens/sec FP16)

## References

- "Attention Is All You Need" (Vaswani et al., 2017)
- GPT-2: Language Models are Unsupervised Multitask Learners
- Original BPE paper (Sennrich et al., 2016)

## License

MIT
